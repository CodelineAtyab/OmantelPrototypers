def decode_measurements(encoded_string: str) -> list[int]:
  """This function decodes an encoded string into a list of integers.
  RULE 1: A generic logic should be implemented without handling edge cases using if statements for specific inputs.
  RULE 2: The generic logic should handle all inputs and generate the expected outputs.

  Args:
      encoded_string (str): The encoded string to decode.

  Returns:
      list[int]: The list of decoded integers.
  """
  # A "number" is z-accumulated: each 'z' adds 26 and the run continues; the
  # first non-'z' char adds its value (a..z -> 1..26, anything else -> 0) and
  # ends the number. Returns (value, next_position).
  def read_number(s, pos):
    total = 0
    while pos < len(s) and s[pos] == "z":
      total += 26
      pos += 1
    if pos < len(s):
      ch = s[pos]
      total += ord(ch) - ord("a") + 1 if "a" <= ch <= "z" else 0
      pos += 1
    return total, pos

  # Decode one space-free package: read a count, then sum that many numbers.
  def decode_package(s):
    values = []
    pos = 0
    while pos < len(s):
      count, pos = read_number(s, pos)
      if count == 0:            # undefined char in count position -> emit 0, stop
        values.append(0)
        break
      value = 0
      for _ in range(count):
        if pos >= len(s):
          break
        num, pos = read_number(s, pos)
        value += num
      values.append(value)
    return values

  # A space separates independent packages; concatenate their results.
  result = []
  for package in encoded_string.split(" "):
    result.extend(decode_package(package))
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