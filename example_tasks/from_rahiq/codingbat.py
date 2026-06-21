 #Warmup 1 ## 1
def sleep_in(weekday, vacation):
  if not weekday or vacation:
    return True
  else:
    return False
 
  ## 2
def monkey_trouble(a_smile, b_smile):
  if a_smile and b_smile:
    return True
  if not a_smile and not b_smile:
    return True
  return False

  ## 3
  def sum_double(a, b):
  sum = a + b
  
  if a == b:
    sum = sum * 2
  return sum

 ## 4
 def diff21(n):
  if n <= 21:
    return 21 - n
  else:
    return (n - 21) * 2
  
  ## 5
  def parrot_trouble(talking, hour):
  return (talking and (hour < 7 or hour > 20))
  

  ## 6
  def makes10(a, b):
  return (a == 10 or b == 10 or a+b == 10)

 ## 7
 def near_hundred(n):
  return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))

 ## 8
 def pos_neg(a, b, negative):
  if negative:
    return (a < 0 and b < 0)
  else:
    return ((a < 0 and b > 0) or (a > 0 and b < 0))
  
 ## 9
 def not_string(str):
  if len(str) >= 3 and str[:3] == "not":
    return str
  return "not " + str
  
 ## 10
 def missing_char(str, n):
  front = str[:n]   # up to but not including n
  back = str[n+1:]  # n+1 through end of string
  return front + back

 ## 11
 def front_back(str):
  if len(str) <= 1:
    return str
  
  mid = str[1:len(str)-1]  # can be written as str[1:-1]
  
  # last + mid + first
  return str[len(str)-1] + mid + str[0]

 ## 12
 def front3(str):
  # Figure the end of the front
  front_end = 3
  if len(str) < front_end:
    front_end = len(str)
  front = str[:front_end]
  return front + front + front

#Warmup 2 ##1
def string_times(str, n):
  result = ""
  for i in range(n):  # range(n) is [0, 1, 2, .... n-1]
    result = result + str  # could use += here
  return result

 ##2
 def front_times(str, n):
  front_len = 3
  if front_len > len(str):
    front_len = len(str)
  front = str[:front_len]
  
  result = ""
  for i in range(n):
    result = result + front
  return result

 ##3
 def string_bits(str):
  result = ""
  # Many ways to do this. This uses the standard loop of i on every char,
  # and inside the loop skips the odd index values.
  for i in range(len(str)):
    if i % 2 == 0:
      result = result + str[i]
  return result

 ##4
 def string_splosion(str):
  result = ""
  for i in range(len(str)):
    result = result + str[:i+1]
  return result

 ##5
 def last2(str):
  if len(str) < 2:
    return 0
  last2 = str[len(str)-2:]
  count = 0

  for i in range(len(str)-2):
    sub = str[i:i+2]
    if sub == last2:
      count = count + 1

  return count

 ##6
 def array_count9(nums):
  count = 0
  # Standard loop to look at each value
  for num in nums:
    if num == 9:
      count = count + 1

  return count

 ##7
 def array_front9(nums):
  end = len(nums)
  if end > 4:
    end = 4
  
  for i in range(end):  # loop over index [0, 1, 2, 3]
    if nums[i] == 9:
      return True
  return False

 
 ##8
 def array123(nums):
  # Note: iterate with length-2, so can use i+1 and i+2 in the loop
  for i in range(len(nums)-2):
    if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
      return True
  return False

##9
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



 
  

