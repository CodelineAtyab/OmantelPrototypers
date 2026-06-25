def get_char_value(char: str) -> int:
   """Convert a character to its value: a=1 ... z=26. Any other char (like '_') = 0."""
   if "a" <= char <= "z":
       return ord(char) - ord("a") + 1
   return 0

def read_number(encoded_string: str, index: int):
   """Read one full number starting at index.
   'z' means +26 and keep going; the first non-'z' char ends the number and adds its value.
   Returns (value, next_index)."""
   total = 0
   while index < len(encoded_string) and encoded_string[index] == "z":
       total += 26
       index += 1
   if index < len(encoded_string):
       total += get_char_value(encoded_string[index])
       index += 1
   return total, index

def decode_measurements(encoded_string: str) -> list[int]:
   """Main function: a space separates independent strings,
   so we decode each segment on its own and combine the results."""
   results = []
   for segment in encoded_string.split(" "):
       results.extend(decode_segment(segment))
   return results

def decode_segment(encoded_string: str) -> list[int]:
   results = []
   index = 0
   while index < len(encoded_string):
       count, index = read_number(encoded_string, index)
       if count == 0:                 # '_' where a count is expected = terminated/corrupt string
           results.append(0)
           break                      # stop reading this segment
       total = 0
       for _ in range(count):
           if index >= len(encoded_string):
               break
           value, index = read_number(encoded_string, index)
           total += value
       results.append(total)
   return results

if __name__ == "__main__":
   cases = [
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
   for inp, expected in cases:
       got = decode_measurements(inp)
       ok = got == expected
       passed += ok
       print(f"{'PASS' if ok else 'FAIL'}  decode({inp!r}) = {got}   expected {expected}")
   print(f"\n{passed}/{len(cases)} passed")