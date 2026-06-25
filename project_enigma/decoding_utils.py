"""
decoding_utils.py

Decodes Acme Metrics Corp's custom "measurement package" string format.

------------------------------------------------------------------------
FORMAT (reverse-engineered from the client's note + the hardcoded tests)
------------------------------------------------------------------------

A package is a sequence of one or more *measurement values*. Each value is
encoded as:

    <count><number_1><number_2>...<number_count>

  - <count> is itself a "number" (see below). It tells you how many
    sub-numbers to read and ADD TOGETHER to produce this measurement value.
  - Each <number_i> is also a "number", parsed with the same rule.

A "number" is parsed as follows (this is the literal rule from the note):
  - Consume zero or more 'z' characters. Each contributes 26.
  - The first character that is NOT 'z' terminates the number. Its
    alphabetic value (a=1, b=2, ..., y=25) is added to the total.
  - 'a'-'y' on their own (with no leading 'z') are simply 1-character
    numbers equal to their own value.
  - '_' (underscore) is treated as a terminator with value 0 (i.e. it acts
    like a letter worth zero). So a lone '_' is the number 0, and 'z_' is
    26 + 0 = 26.

The key subtlety (and the thing the note's wording obscures) is that the
"count" character does NOT mean "read this many raw characters" -- it means
"read this many NUMBERS" (each of which may itself span multiple
characters via the z-run rule). This recursive structure is what makes
several of the harder test cases work, e.g. "dz_a_aazzaaa" -> [28, 53, 1].

Special handling for '_' as a SEGMENT TERMINATOR
--------------------------------------------------
If '_' appears at a position where a new value's <count> was expected to
start, it is NOT read as "the number 0" via the normal number rule.
Instead, it acts as an explicit "stop" marker: a single 0 is appended to
the output and the rest of the segment is discarded/ignored. This was
inferred from cases like "_ad" -> [0] (not [0, 4]) and "__" -> [0] (not
[0, 0]).

Underscore is only special in this "fresh value start" position. When it
shows up *inside* a number (as a terminator after some 'z's, or as a
1-character number on its own within a sum), it just behaves as the value
0, with no stopping behaviour, e.g. "a_" -> [0], "aab___" -> [1, 0, 0].

Multiple segments (space-separated)
------------------------------------
A space character is treated as a delimiter between independent packages.
Each space-separated segment is decoded independently (its own "stop"
behaviour resets), and all resulting values are concatenated into a single
flat list. This was inferred from "_ _" -> [0, 0] (two independent
single-character segments, each producing its own 0) as opposed to a
single segment "_ _" which (without splitting) would stop at the first
character and only yield [0].

Undefined / unspecified behaviour we had to make a judgment call on
---------------------------------------------------------------------
- A number that is an EXACT multiple of 26 (e.g. just "zz" with nothing
  after it) has no terminator character to close it, per the note's own
  description. If this happens at the end of a segment, we currently treat
  the trailing z-run as contributing 26*<zcount> with no terminator value
  (i.e. terminator contributes 0). See assumptions.md / clarifications.md
  for why this is a guess, not a confirmed rule.
- If a header asks for more sub-numbers than there are characters left to
  parse, we stop early and use whatever was successfully parsed. This
  never happens in the given tests, but real-world malformed input will
  hit it.
"""


def _letter_val(ch: str) -> int:
    """a-z -> 1-26, underscore -> 0 (used only for in-number terminators)."""
    if ch == "_":
        return 0
    return ord(ch) - ord("a") + 1


def _parse_number(s: str, i: int) -> tuple[int, int]:
    """
    Parse a single "number" from s starting at index i, following the
    z-run rule: 0+ 'z' characters (each worth 26), terminated by the first
    non-'z' character (worth its own alphabetic value, with '_' == 0).

    Returns (value, new_index).

    If the string ends while still consuming a run of 'z' characters (no
    terminator available), the number is just 26 * zcount (undefined edge
    case per the spec -- see module docstring / assumptions.md).
    """
    n = len(s)
    zcount = 0
    while i < n and s[i] == "z":
        zcount += 1
        i += 1

    if i < n:
        value = 26 * zcount + _letter_val(s[i])
        i += 1
    else:
        value = 26 * zcount

    return value, i


def _decode_segment(s: str) -> list[int]:
    """Decode a single (non-space-containing) encoded segment."""
    out: list[int] = []
    i = 0
    n = len(s)

    while i < n:
        if s[i] == "_":
            # Underscore at the start of a new value = explicit stop marker.
            out.append(0)
            break

        count, i = _parse_number(s, i)

        total = 0
        for _ in range(count):
            if i >= n:
                # Not enough characters left to satisfy the requested
                # count -- stop summing with whatever we have so far.
                break
            value, i = _parse_number(s, i)
            total += value

        out.append(total)

    return out


def decode_measurements(encoded_string: str) -> list[int]:
    """
    Decode an Acme Metrics measurement package string into a list of
    integer measurement values.

    See the module docstring for the full reverse-engineered format spec.
    """
    if encoded_string == "":
        return []

    result: list[int] = []
    for segment in encoded_string.split(" "):
        result.extend(_decode_segment(segment))
    return result


if __name__ == "__main__":
    TEST_CASES = [
        ("aa", [1]),
        ("abbcc", [2, 6]),
        ("dz_a_aazzaaa", [28, 53, 1]),
        ("a_", [0]),
        ("abcdabcdab", [2, 7, 7]),
        ("abcdabcdab_", [2, 7, 7, 0]),
        ("zdaaaaaaaabaaaaaaaabaaaaaaaabbaa", [34]),
        ("zza_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_", [26]),
        ("za_a_a_a_a_a_a_a_a_a_a_a_a_azaaa", [40, 1]),
        ("_", [0]),
        ("_ad", [0]),
        ("a_", [0]),
        ("_zzzb", [0]),
        ("__", [0]),
        ("", []),
        ("_ _", [0, 0]),
        ("aab___", [1, 0, 0]),
    ]

    failures = 0
    for inp, expected in TEST_CASES:
        got = decode_measurements(inp)
        ok = got == expected
        if not ok:
            failures += 1
        print(f"{'OK ' if ok else 'FAIL'} decode_measurements({inp!r}) = {got!r} (expected {expected!r})")

    print()
    if failures:
        print(f"{failures} test(s) FAILED")
        raise SystemExit(1)
    else:
        print("All test cases passed.")
