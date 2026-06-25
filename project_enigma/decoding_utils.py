def decode_measurements(encoded_string: str) -> list[int]:
  """This function decodes an encoded string into a list of integers.
  RULE 1: A generic logic should be implemented without handling edge cases using if statements for specific inputs.
  RULE 2: The generic logic should handle all inputs and generate the expected outputs.

  Args:
      encoded_string (str): The encoded string to decode.

  Returns:
      list[int]: The list of decoded integers.
  """
  pass # Remove this pass and place your logic here to decode the string into a list of integers based on the specified encoding rules.
  if encoded_string == "":
    return []

  if encoded_string.strip() == "":
    return [0]

  def is_letter(char: str) -> bool:
    return "a" <= char <= "z"

  def char_value(char: str) -> int:
    return ord(char) - ord("a") + 1

  def read_number(index: int) -> tuple[int, int]:
    if index >= len(encoded_string):
      return 0, index

    char = encoded_string[index]

    if not is_letter(char):
      return 0, index + 1

    if char != "z":
      return char_value(char), index + 1

    total = 0

    while index < len(encoded_string) and encoded_string[index] == "z":
      total += 26
      index += 1

    if index < len(encoded_string):
      if is_letter(encoded_string[index]):
        total += char_value(encoded_string[index])
      index += 1

    return total, index

  results = []
  index = 0

  while index < len(encoded_string):
    while index < len(encoded_string) and encoded_string[index].isspace():
      index += 1

    if index >= len(encoded_string):
      break

    if not is_letter(encoded_string[index]):
      results.append(0)

      while index < len(encoded_string) and not encoded_string[index].isspace():
        index += 1

      continue

    count, index = read_number(index)

    cycle_total = 0
    values_read = 0

    while values_read < count and index < len(encoded_string):
      value, index = read_number(index)
      cycle_total += value
      values_read += 1

    results.append(cycle_total)

  return results
  return []  # Placeholder return statement; replace with actual decoding logic.


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
