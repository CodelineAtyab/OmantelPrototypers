def decode_measurements(encoded_string: str) -> list[int]:
    """
    Decodes measurement packages by alternating between reading a 'count'
    and summing the subsequent 'count' number of measured values.
    """
    def value(ch):

        return ord(ch) - ord("a") + 1 if "a" <= ch <= "z" else 0
    
    """Helper to parse a single number (count or value)."""
    def parse_count(i):

        # Accumulate 'z's
        if encoded_string[i] == "z":

            total = 0

            while i < len(encoded_string) and encoded_string[i] == "z":

                total += 26

                i += 1
            # Add the final character value if it's not a z-terminator
            if i < len(encoded_string) and "a" <= encoded_string[i] <= "z":

                total += value(encoded_string[i])

                i += 1
 
            return total, i
 
        return value(encoded_string[i]), i + 1
 
    def parse_value(i):

        ch = encoded_string[i]
 
        if ch == "_":

            return 0, i + 1
 
        total = value(ch)

        i += 1
 
        if ch != "z":

            while i < len(encoded_string) and encoded_string[i] == "z":

                total += 26

                i += 1
 
        if ch == "z" and i < len(encoded_string) and encoded_string[i] == "_":

            total += 1
 
        return total, i
 
    result = []

    i = 0
 
    while i < len(encoded_string):

        if encoded_string[i] == " ":

            i += 1

            continue
 
        if encoded_string[i] == "_":

            result.append(0)
 
            while i < len(encoded_string) and encoded_string[i] == "_":

                i += 1
 
            if i < len(encoded_string) and encoded_string[i].isalpha():

                break
 
            continue
 
        count, i = parse_count(i)
 
        total = 0

        decoded_values = 0
 
        while decoded_values < count and i < len(encoded_string):

            if encoded_string[i] == " ":

                i += 1

                continue
 
            decoded_value, i = parse_value(i)

            total += decoded_value

            decoded_values += 1
 
        if decoded_values < count:

            break
 
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
