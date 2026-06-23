#Warmup-1 > sleep_in
def sleep_in(weekday, vacation):
  if not weekday or vacation:
    return True
  else:
    return False
#Warmup-1 > monkey_trouble
def monkey_trouble(a_smile, b_smile):
  if a_smile and b_smile:
    return True
  elif not a_smile and not b_smile:
    return True
  elif not a_smile or not b_smile:
    return False
  else:
    return False
 
#Warmup-1 > sum_double
def sum_double(a, b):
  if a != b:
    return a + b
  else:
    return (a+b)*2
#Warmup-1 > diff21
def diff21(n):
  if n > 21:
    return 2 * abs(21 - n)
  else:
   return 21 - n
#Warmup-1 > parrot_trouble
def parrot_trouble(talking, hour):
  if talking == True and (hour < 7 or hour > 20):
    return True
  else:
    return False
#Warmup-1 > makes10
def makes10(a, b):
  if a  == 10 or b == 10:
    return True
  elif (a + b) == 10:
    return True
  else:
    return False
#Warmup-1 > near_hundred
def near_hundred(n):
  return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))
 
#Warmup-1 > pos_neg
def pos_neg(a, b, negative):
  if negative:
    return (a < 0 and b < 0)
  else:
    return ((a < 0 and b > 0) or (a > 0 and b < 0))
#Warmup-1 > not_string
def not_string(str):
  if len(str) >= 3 and str[:3] == "not":
    return str
  return "not " + str
 
#Warmup-1 > missing_char
def missing_char(str, n):
  front = str[:n]  
  back = str[n+1:]
  return front + back
 
#Warmup-1 > front_back
def front_back(str):
  if len(str) <= 1:
    return str
  mid = str[1:len(str)-1]  # can be written as str[1:-1]
  # last + mid + first
  return str[len(str)-1] + mid + str[0]
 
#Warmup-1 > front3
def front3(str):
  # Figure the end of the front
  front_end = 3
  if len(str) < front_end:
    front_end = len(str)
  front = str[:front_end]
  return front + front + front
 
#------------------------------------------------------------------------------------------------------------
 
#Warmup-2 > string_times
def string_times(str, n):
  if n == 1 :
    return str
  else:
    return str * n
#Warmup-2 > front_times
def front_times(str, n):
  if len(str) < 3 or len(str) >= 3:
    return str[:3] * n
 
 
#Warmup-2 > string_bits
def string_bits(str):
  result = ""
  for i in range(len(str)):
    if i % 2 == 0:
      result = result + str[i]
  return result
 
#Warmup-2 > string_splosion
def string_splosion(str):
  result = ""
  for i in range(len(str)):
    result = result + str[:i+1]
  return result
 
#Warmup-2 > last2
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
 
#Warmup-2 > array_count9
def array_count9(nums):
  count = 0
  for i in nums:
    if i == 9:
      count = count + 1
  return count
 
#Warmup-2 > array_front9
def array_front9(nums):
  # First figure the end for the loop
  end = len(nums)
  if end > 4:
    end = 4
  for i in range(end):  # loop over index [0, 1, 2, 3]
    if nums[i] == 9:
      return True
  return False
 
#Warmup-2 > array123
def array123(nums):
  # Note: iterate with length-2, so can use i+1 and i+2 in the loop
  for i in range(len(nums)-2):
    if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
      return True
  return False
 
#Warmup-2 > string_match
def string_match(a, b):
  # Figure which string is shorter.
  shorter = min(len(a), len(b))
  count = 0
  # Loop i over every substring starting spot.
  # Use length-1 here, so can use char str[i+1] in the loop
  for i in range(shorter-1):
    a_sub = a[i:i+2]
    b_sub = b[i:i+2]
    if a_sub == b_sub:
      count = count + 1
 
  return count
 
