def decode_measurements(encoded_string: str) -> list[int]:
    """This function decodes an encoded string into a list of integers.

    RULE 1: A generic logic should be implemented without handling edge cases using if statements for specific inputs.
    RULE 2: The generic logic should handle all inputs and generate the expected outputs.
    """

    def read_number(s: str, i: int) -> tuple[int, int]:
        # A number is a sequence of 'z' (each = 26) followed by a terminating char
        total = 0

        # accumulate z's
        while i < len(s) and s[i] == 'z':
            total += 26
            i += 1

        # terminating character
        if i < len(s):
            c = s[i]
            if 'a' <= c <= 'y':
                total += ord(c) - ord('a') + 1
            # if '_' or anything else → treated as 0
            i += 1

        return total, i

    def decode_package(s: str) -> list[int]:
        values: list[int] = []
        i = 0
        n = len(s)

        while i < n:
            count, i = read_number(s, i)

            if count == 0:
                values.append(0)
                break

            total = 0
            for _ in range(count):
                if i >= n:
                    break
                value, i = read_number(s, i)
                total += value

            values.append(total)

        return values

    result: list[int] = []
    for package in encoded_string.split(' '):
        if package == "":
            continue
        result.extend(decode_package(package))

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



