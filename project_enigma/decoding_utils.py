def decode_measurements(encoded_string: str) -> list[int]:
  """This function decodes an encoded string into a list of integers.
  RULE 1: A generic logic should be implemented without handling edge cases using if statements for specific inputs.
  RULE 2: The generic logic should handle all inputs and generate the expected outputs.

  Args:
      encoded_string (str): The encoded string to decode.

  Returns:
      list[int]: The list of decoded integers.
  """
  def read_number(s, i):
    # A number is a run of 'z' (each worth 26, the continuation char) followed
    # by the first non-'z' terminator. a-y -> 1..25, anything else (e.g. '_') -> 0.
    total = 0
    while i < len(s) and s[i] == 'z':
      total += 26
      i += 1
    if i < len(s):
      c = s[i]
      if 'a' <= c <= 'y':
        total += ord(c) - ord('a') + 1
      i += 1
    return total, i

  def decode_package(s):
    values = []
    i = 0
    n = len(s)
    while i < n:
      count, i = read_number(s, i)          # each cycle begins with its own count
      if count == 0:                        # a 0 count ('_' / unknown) emits a
        values.append(0)                    # single 0 and terminates the package
        break
      total = 0
      for _ in range(count):                # read `count` measured values...
        if i >= n:
          break
        v, i = read_number(s, i)
        total += v
      values.append(total)                  # ...and emit their sum as one reading
    return values

  result = []
  for package in encoded_string.split(' '):  # a space separates packages
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