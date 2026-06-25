# The Interrogation — Clarification Questions

Questions I would ask the client to remove the ambiguity in the encoding spec.

## 1. Contradictory test case: `"_ _"`

The expected output `("_ _", [0, 0])` contradicts three other cases:

- `("__", [0])`
- `("_ad", [0])`
- `("_zzzb", [0])`

All four inputs begin with the same `_` in the count position. The other three establish
that a leading `_` (a zero count) **terminates the stream** and produces a single `[0]`,
discarding everything after it. By the same rule, `"_ _"` should also decode to `[0]`,
not `[0, 0]`.

For `"_ _"` to produce `[0, 0]`, parsing would have to continue past the leading `_` —
which would simultaneously break `"__"`, `"_ad"`, and `"_zzzb"`. So one expectation is
wrong, and the parsimonious conclusion is that `("_ _", [0, 0])` is a typo.

**Question:** Should `"_ _"` decode to `[0]` (consistent with the other terminator cases),
or is there a special rule for spaces we are missing?

## 2. Is the count per-packet or a fixed cycle length?

The note says "a number indicating the count of values measured in each measurement
cycle." This could mean one fixed count for the whole string, but the test data
(`"abcdabcdab"` → `[2, 7, 7]`, with counts 1, 3, 3) only works if the count is read
**fresh at the start of every packet**.

**Question:** Confirm that each packet declares its own count, and that counts may differ
between packets.

## 3. How should undefined characters be treated?

The note only defines `a`–`z`. The tests also include `_` and spaces, which we treat as 0.

**Question:** Should every non-`a`–`z` character map to 0, or do specific characters
(`_`, space, digits, punctuation) carry distinct meanings? Should an unexpected character
be an error instead?

## 4. Production behaviour for malformed input

For real-world data beyond the examples:

- A count that asks for more values than remain in the string.
- A trailing `z` with no following character to terminate the number.
- Input containing characters outside the expected set.

**Question:** In production, should malformed input raise an explicit error, be skipped,
or be coerced to 0 (as the decoder currently does)? Error handling strategy should be
defined rather than left implicit.

## 5. Terminator semantics

We treat a zero count as "end of data — emit one final 0 and discard the rest."

**Question:** Is discarding everything after the terminator the intended behaviour, or
should trailing data be validated/reported rather than silently dropped?
