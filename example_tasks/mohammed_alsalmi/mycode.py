def string_splosion(s):
    result = ""
    for i in range(len(s)):
        result = result + s[:i+1]
    return result
def front_times(str, n):
  front_len = 3
  if front_len > len(str):
    front_len = len(str)
  front = str[:front_len]
  
  result = ""
  for i in range(n):
    result = result + front
  return result
def string_bits(str):
  result = ""
  # Many ways to do this. This uses the standard loop of i on every char,
  # and inside the loop skips the odd index values.
  for i in range(len(str)):
    if i % 2 == 0:
      result = result + str[i]
  return result
def last2(str):
  # Screen out too-short string case.
  if len(str) < 2:
    return 0
  
  # last 2 chars, can be written as str[-2:]
  last2 = str[len(str)-2:]
  count = 0
  
  # Check each substring length 2 starting at i
  for i in range(len(str)-2):
    sub = str[i:i+2]
    if sub == last2:
      count = count + 1

  return count

def monkey_trouble(a_smile, b_smile):
  if a_smile and b_smile:
    return True
  if not a_smile and not b_smile:
    return True
  return False
  ## The above can be shortened to:
  ##   return ((a_smile and b_smile) or (not a_smile and not b_smile))
  ## Or this very short version (think about how this is the same as the above)
  ##   return (a_smile == b_smile)