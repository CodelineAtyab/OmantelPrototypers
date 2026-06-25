"""
Project Enigma — The Cryptic Measurement Decoder
=================================================

A decoder for Acme Metrics Corp's measurement-package encoding.

The format, reverse-engineered from the test corpus, is a tiny grammar.
Reading it top-down explains every rule in one place:

    stream   := package (" " package)*        ; spaces separate packages
    package  := cycle*                          ; a package is a run of cycles
    cycle    := count value{count}             ; read N, then sum the next N
    count    := number                          ; "0" (a bare '_') ends the package
    value    := number
    number   := "z"* terminator               ; each 'z' = 26, terminator adds its value
    terminator := <any char>                    ; a..z = 1..26, anything else = 0

The whole decoder is just that grammar walked left-to-right by a Cursor.
There are no input-specific branches: '_', spaces and end-of-string all fall
out of the generic rules (an undefined char is simply worth 0).
"""

from __future__ import annotations

Z_UNIT = 26          # value carried by each 'z' in a multi-character number
PACKAGE_SEP = " "    # spaces delimit independent packages


def _char_value(ch: str) -> int:
    """a..z -> 1..26; every other character (incl. '_') -> 0."""
    return ord(ch) - ord("a") + 1 if "a" <= ch <= "z" else 0


class _Cursor:
    """A left-to-right reader over one package, exposing grammar primitives."""

    def __init__(self, text: str) -> None:
        self._text = text
        self._pos = 0

    @property
    def at_end(self) -> bool:
        return self._pos >= len(self._text)

    def _peek(self) -> str | None:
        return None if self.at_end else self._text[self._pos]

    def _take(self) -> str:
        ch = self._text[self._pos]
        self._pos += 1
        return ch

    def read_number(self) -> int:
        """number := 'z'* terminator. Past end-of-string reads as 0."""
        total = 0
        while self._peek() == "z":
            total += Z_UNIT
            self._take()
        if not self.at_end:                 # consume exactly one terminator
            total += _char_value(self._take())
        return total


def _decode_package(text: str) -> list[int]:
    cursor = _Cursor(text)
    measurements: list[int] = []

    while not cursor.at_end:
        count = cursor.read_number()
        if count == 0:                      # a '_' where a count was expected: stop here
            measurements.append(0)
            break
        measurements.append(sum(cursor.read_number() for _ in range(count)))

    return measurements


def decode_measurements(encoded_string: str) -> list[int]:
    """Decode an Acme measurement string into its list of summed measurements."""
    measurements: list[int] = []
    for package in encoded_string.split(PACKAGE_SEP):
        measurements.extend(_decode_package(package))
    return measurements


if __name__ == "__main__":
    test_cases = [
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

    passed = 0
    for encoded, expected in test_cases:
        result = decode_measurements(encoded)
        ok = result == expected
        passed += ok
        print(f"{'PASS' if ok else 'FAIL'}: decode_measurements({encoded!r}) = {result} (expected {expected})")
    print(f"\n{passed}/{len(test_cases)} passed")