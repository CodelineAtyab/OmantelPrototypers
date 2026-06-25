def decode_measurements(encoded_string: str) -> list[int]:
    """This function decodes an encoded string into a list of integers.
    RULE 1: A generic logic should be implemented without handling edge cases using if statements for specific inputs.
    RULE 2: The generic logic should handle all inputs and generate the expected outputs.

    Args:
        encoded_string (str): The encoded string to decode.

    Returns:
        list[int]: The list of decoded integers.
    """
    def char_value(c: str) -> int:
        if c == '_':
            return 0
        if 'a' <= c <= 'z':
            return ord(c) - ord('a') + 1
        return 0

    def read_number(seg: str, pos: int) -> tuple[int, int]:
        acc = 0
        while pos < len(seg) and seg[pos] == 'z':
            acc += 26
            pos += 1
        if pos < len(seg):
            acc += char_value(seg[pos])
            pos += 1
        return acc, pos

    results: list[int] = []

    for seg in encoded_string.split(' '):
        pos = 0
        while pos < len(seg):
            count, pos = read_number(seg, pos)
            if count == 0:
                results.append(0)
                break
            total = 0
            for _ in range(count):
                if pos < len(seg):
                    val, pos = read_number(seg, pos)
                    total += val
            results.append(total)

    return results


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
