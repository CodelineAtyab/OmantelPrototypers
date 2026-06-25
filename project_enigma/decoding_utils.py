def decode_measurements(encoded_string: str) -> list[int]:
  """This function decodes an encoded string into a list of integers.
  RULE 1: A generic logic should be implemented without handling edge cases using if statements for specific inputs.
  RULE 2: The generic logic should handle all inputs and generate the expected outputs.

  Args:
      encoded_string (str): The encoded string to decode.

  Returns:
      list[int]: The list of decoded integers.
  """
  # turn one character into a number: a -> 1, b -> 2, ... z -> 26.
  # anything else (like "_") is treated as 0.
  def value_of(ch):
    if "a" <= ch <= "z":
      return ord(ch) - ord("a") + 1
    return 0

  # read a single number starting at position "pos".
  # every "z" means 26 and we keep going, the first non-z char ends
  # the number and is added on. returns the number and the next position.
  def read_number(text, pos):
    total = 0
    while pos < len(text):
      ch = text[pos]
      pos += 1
      total += value_of(ch)
      if ch != "z":
        break
    return total, pos

  # a space splits the input into separate chunks that we decode on their own
  result = []
  for part in encoded_string.split(" "):
    pos = 0
    while pos < len(part):
      # first read how many values this cycle has
      count, pos = read_number(part, pos)

      # a count of zero means we hit a terminator like "_",
      # so we record a 0 and stop reading this chunk
      if count == 0:
        result.append(0)
        break

      # then read that many values and add them all together
      cycle_total = 0
      for _ in range(count):
        number, pos = read_number(part, pos)
        cycle_total += number

      result.append(cycle_total)

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
