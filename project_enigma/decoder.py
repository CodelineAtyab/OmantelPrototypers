def decode_measurements(encoded_string: str) -> list[int]:
    """This function decodes an encoded string into a list of integers.
  RULE 1: A generic logic should be implemented without handling edge cases using if statements for specific inputs.
  RULE 2: The generic logic should handle all inputs and generate the expected outputs.

  Args:
      encoded_string (str): The encoded string to decode.

  Returns:
      list[int]: The list of decoded integers.
    """

    results = []

    variables = encoded_string.split(' ')

    for variable in variables:
        i = 0   
        n = len(variable)  

        while i < n:
            if variable[i] == '_':
                results.append(0)
                break 

            count = 0
            while i < n and variable[i] == 'z':
                count = count + 26
                i = i + 1

            if i < n and variable[i] != '_' and 'a' <= variable[i] <= 'z':
                count = count + ord(variable[i]) - ord('a') + 1
                i = i + 1

            total = 0
            for _ in range(count):
                if i >= n:
                    break

                value = 0

                while i < n and variable[i] == 'z':
                    value = value + 26
                    i = i + 1

                if i < n:
                    terminator = variable[i]
                    if terminator == '_':
                        value = value + 0
                    else:
                        value = value+ ord(terminator) - ord('a') + 1
                    i = i + 1

                total = total + value

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

    passed = 0
    for encoded, expected in test_cases:
        result = decode_measurements(encoded)
        status = "PASS" if result == expected else "FAIL"
        if status == "PASS":
            passed += 1
        print(f"{status}: decode_measurements({encoded!r}) = {result} (expected {expected})")

    print(f"\nResult: {passed}/{len(test_cases)} passed")