#The Code (decoder.py)

def decode_measurements(encoded_string: str) -> list[int]:
  """This function decodes an encoded string into a list of integers.
  RULE 1: A generic logic should be implemented without handling edge cases using if statements for specific inputs.
  RULE 2: The generic logic should handle all inputs and generate the expected outputs.

  Args:
      encoded_string (str): The encoded string to decode.

  Returns:
      list[int]: The list of decoded integers.
  """
  def char_to_val(c: str) -> int:
      if c == '_':
          return 0
      if 'a' <= c <= 'z':
          return ord(c) - ord('a') + 1
      return 0

  packets = encoded_string.split(' ') if ' ' in encoded_string else [encoded_string]
  results = []

  for packet in packets:
      if not packet:
          continue
          
      i = 0
      n = len(packet)
      
      def parse_next_number(idx: int) -> tuple[int, int]:
          if idx >= n:
              return 0, idx
          val = char_to_val(packet[idx])
          start_char = packet[idx]
          idx += 1
          if start_char == 'z':
              while idx < n and packet[idx] == 'z':
                  val += 26
                  idx += 1
              if idx < n:
                  val += char_to_val(packet[idx])
                  idx += 1
          return val, idx

      while i < n:
          count, i = parse_next_number(i)
          if count == 0:
              results.append(0)
              break
              
          cycle_sum = 0
          values_read = 0
          for _ in range(count):
              if i >= n:
                  break
              val, i = parse_next_number(i)
              cycle_sum += val
              values_read += 1
              
          if values_read > 0 or count > 0:
              results.append(cycle_sum)
              
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


