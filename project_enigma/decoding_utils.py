def decode_measurements(encoded_string: str) -> list[int]:

    def letter_to_int(character: str) -> int:
        if "a" <= character <= "z":
            return ord(character) - 96
        return 0

    def extract_number(text: str, position: int):
        accumulated = 0
        while position < len(text) and text[position] == "z":
            accumulated += 26
            position += 1
        if position < len(text) and text[position] != "_":
            accumulated += letter_to_int(text[position])
            position += 1
        elif position < len(text) and text[position] == "_":
            position += 1
        return accumulated, position

    def process_segment(segment: str) -> list[int]:
        output = []
        cursor = 0

        while cursor < len(segment):
            how_many, cursor = extract_number(segment, cursor)

            if how_many == 0:
                output.append(0)
                break

            running_sum = 0
            for _ in range(how_many):
                if cursor >= len(segment):
                    break
                next_val, cursor = extract_number(segment, cursor)
                running_sum += next_val

            output.append(running_sum)

        return output

    final_output = []
    for part in encoded_string.split(" "):
        final_output.extend(process_segment(part))

    return final_output


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