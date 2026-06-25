def decode_measurements(encoded_string: str) -> list[int]:
    """Decodes an encoded string into a list of integers.

    Format per package (space-separated):
      - Read count: z-encoded (accumulate 26 per 'z', stop at first non-z)
        - If the terminating char is '_': output 0 and stop processing this package
        - Otherwise count = accumulated_z_total + char_value (a=1..y=25)
      - Sum 'count' z-encoded values into one output integer
        ('_' terminates a z-sequence contributing 0 to the sum)
      - Repeat until end of package
    Spaces separate independent packages.
    """
    result = []

    if encoded_string == "":
        return []

    for package in encoded_string.split(" "):
        i = 0
        while i < len(package):
            # --- Read count (z-encoded) ---
            count = 0
            while i < len(package) and package[i] == 'z':
                count += 26
                i += 1

            if i >= len(package):
                break

            ch = package[i]
            i += 1

            if ch == '_':
                # '_' at count position = output 0 and stop this package
                result.append(0)
                break

            count += ord(ch) - 96

            # --- Read 'count' z-encoded values and sum them into one output ---
            total = 0
            for _ in range(count):
                if i >= len(package):
                    break
                val = 0
                while i < len(package) and package[i] == 'z':
                    val += 26
                    i += 1
                if i < len(package):
                    ch = package[i]
                    i += 1
                    if ch != '_':
                        val += ord(ch) - 96
                    # '_' contributes 0 and terminates the z-sequence
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
