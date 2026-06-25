def decode_measurements(encoded_string: str) -> list[int]:
    """This function decodes an encoded string into a list of integers.
    RULE 1: A generic logic should be implemented without handling edge cases using if statements for specific inputs.
    RULE 2: The generic logic should handle all inputs and generate the expected outputs.

    Args:
        encoded_string (str): The encoded string to decode.

    Returns:
        list[int]: The list of decoded integers.
    """
    def char_to_num(char):
        char = char.lower()
        if 'a' <= char <= 'z':
            return ord(char) - ord('a') + 1
        return 0

    def read_number(s, pos):
        # Count a run of 'z' characters, then add the terminator's value
        k = 0
        while pos + k < len(s) and s[pos + k] == 'z':
            k += 1
        if pos + k < len(s):
            value = 26 * k + char_to_num(s[pos + k])
            new_pos = pos + k + 1
        else:
            value = 26 * k
            new_pos = pos + k
        return value, new_pos

    result = []
    for token in encoded_string.split():
        i = 0
        while i < len(token):
            n, i = read_number(token, i)
            if n == 0:
                result.append(0)
                break
            total = 0
            for _ in range(n):
                if i >= len(token):
                    break
                val, i = read_number(token, i)
                total += val
            result.append(total)
    return result






  



































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
