def decode_measurements(encoded_string: str) -> list[int]:
    results: list[int] = []
    for segment in encoded_string.split(" "):
        _decode_segment(segment, results)
    return results


def _char_value(ch: str) -> int:
    if ch == '_':
        return 0
    if 'a' <= ch <= 'z':
        return ord(ch) - ord('a') + 1
    return 0


def _read_encoded_number(s: str, pos: int) -> tuple[int, int]:
    if pos >= len(s):
        return 0, pos
    if s[pos] != 'z':
        return _char_value(s[pos]), pos + 1
    total = 0
    while pos < len(s) and s[pos] == 'z':
        total += 26
        pos += 1
    if pos < len(s):
        total += _char_value(s[pos])
        pos += 1
    return total, pos


def _decode_segment(s: str, results: list[int]) -> None:
    pos = 0
    length = len(s)
    while pos < length:
        if s[pos] == '_':
            results.append(0)
            return
        count, pos = _read_encoded_number(s, pos)
        cycle_sum = 0
        for _ in range(count):
            if pos >= length:
                break
            value, pos = _read_encoded_number(s, pos)
            cycle_sum += value
        results.append(cycle_sum)


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

    for encoded, expected in test_cases:
        result = decode_measurements(encoded)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: decode_measurements({encoded!r}) = {result} (expected {expected})")
        