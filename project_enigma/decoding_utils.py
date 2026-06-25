def decode_measurements(encoded_string: str) -> list[int]:
  """This function decodes an encoded string into a list of integers.
  RULE 1: A generic logic should be implemented without handling edge cases using if statements for specific inputs.
  RULE 2: The generic logic should handle all inputs and generate the expected outputs.

  Args:
      encoded_string (str): The encoded string to decode.

  Returns:
      list[int]: The list of decoded integers.
  """
  my_listy = []
  base = "_abcdefghijklmnopqrstuvwxyz"
  i = 0

  while i < len(encoded_string):
        # --- read the COUNT (a full, possibly multi-char number) ---
        pre_count = encoded_string[i]
        d = 1
        while pre_count[-1] == "z":
            pre_count = pre_count + encoded_string[i + d]
            d = d + 1
        i = i + d                    

        count = 0
        for u in range(len(pre_count)):
            count = count + base.index(pre_count[u])
        if count == 0:        
            my_listy.append(0)
            break
 
        total = 0
        for _ in range(count):
            if i >= len(encoded_string):
                break
            value = encoded_string[i]
            d = 1
            while value[-1] == "z":
                value = value + encoded_string[i + d]
                d = d + 1
            i = i + d             
            for u in range(len(value)):
                total = total + base.index(value[u])

        my_listy.append(total)






    
  return my_listy  # Placeholder return statement; replace with actual decoding logic.


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
        #("_ _", [0, 0]), this needs discussion since it does not match the expected logic. contradicts '__','_ad','_zzzb';
        ("aab___", [1, 0, 0]),
    ]

    for encoded, expected in test_cases:
        result = decode_measurements(encoded)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: decode_measurements({encoded!r}) = {result} (expected {expected})")
