#def decode_measurements(encoded_string: str) -> list[int]:
"""This function decodes an encoded string into a list of integers.
  RULE 1: A generic logic should be implemented without handling edge cases using if statements for specific inputs.
  RULE 2: The generic logic should handle all inputs and generate the expected outputs.

  Args:
      encoded_string (str): The encoded string to decode.

  Returns:
      list[int]: The list of decoded integers.
  """
 # pass # Remove this pass and place your logic here to decode the string into a list of integers based on the specified encoding rules.
def decode_measurements(encoded: str) -> list[int]:
    results = []
    
    # Split by whitespace to handle separated packages like "_ _"
    packages = encoded.split()
    
    for pkg in packages:
        i = 0
        while i < len(pkg):
            count = 0
            
            # 1. Parse the count for the current measurement cycle
            while i < len(pkg):
                char = pkg[i]
                i += 1
                if char == 'z':
                    count += 26
                elif char == '_':
                    count += 0
                    break
                else:
                    count += ord(char) - ord('a') + 1
                    break
            
            # If the parsed count is 0, append 0 and terminate this package entirely
            if count == 0:
                results.append(0)
                break
                
            # 2. Parse the values based on the 'count' of effective characters
            val_sum = 0
            eff_count = 0
            
            while i < len(pkg) and eff_count < count:
                char = pkg[i]
                i += 1
                if char == 'z':
                    val_sum += 26
                    # 'z' adds to the sum but does NOT count as an effective character
                elif char == '_':
                    val_sum += 0
                    eff_count += 1
                else:
                    val_sum += ord(char) - ord('a') + 1
                    eff_count += 1
            
            results.append(val_sum)
            
    return results
 # return []  # Placeholder return statement; replace with actual decoding logic.


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
