def decode_measurements(encoded_string: str) -> list[int]:
    """This function decodes an encoded string into a list of integers."""
    results = []
    i = 0
    n = len(encoded_string)

    def read_value_token():
        nonlocal i
        if i >= n or encoded_string[i] == ' ':
            return None
        c = encoded_string[i]
        if c == '_':
            i += 1
            return 0
        val = 0
        while i < n:
            ch = encoded_string[i]
            if ch == 'z':
                val += 26
                i += 1
            elif ch == '_':
                i += 1
                return val
            elif ch == ' ':
                return val
            else:
                val += ord(ch) - ord('a') + 1
                i += 1
                return val
        return val

    while i < n:
        c = encoded_string[i]

        if c == ' ':
            i += 1
            continue

        if c == '_':
            while i < n and encoded_string[i] != ' ':
                i += 1
            results.append(0)
            continue

        count = 0
        zero_cycle = False
        while i < n:
            ch = encoded_string[i]
            if ch == ' ':
                break
            if ch == '_':
                while i < n and encoded_string[i] != ' ':
                    i += 1
                results.append(0)
                zero_cycle = True
                break
            if ch == 'z':
                count += 26
                i += 1
            else:
                count += ord(ch) - ord('a') + 1
                i += 1
                break

        if zero_cycle:
            continue

        total = 0
        for _ in range(count):
            if i >= n or encoded_string[i] == ' ':
                break
            val = read_value_token()
            if val is None:
                break
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