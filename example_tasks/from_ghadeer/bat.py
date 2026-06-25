#Warmup 1 : 

def sleep_in(weekday, vacation):
  return not weekday or vacation


def diff21(n):
  
    if n <= 21:
        return abs(n - 21)
    else:
        return 2 * abs(n - 21)


def near_hundred(n):
  return abs(n - 100) <= 10 or abs(n - 200) <= 10


def missing_char(str, n):
  return str[:n] + str[n+1:]


def monkey_trouble(a_smile, b_smile):
  
    return a_smile == b_smile



def parrot_trouble(talking, hour):
    return talking and (hour < 7 or hour > 20)


def pos_neg(a, b, negative):
  
    if negative:
        return a < 0 and b < 0
    else:
        return (a < 0 and b > 0) or (a > 0 and b < 0)


def front_back(s):
    if len(s) <= 1:
        return s
    return s[-1] + s[1:-1] + s[0]


def sum_double(a, b):
  
    if a == b:
        return 2 * (a + b)
    else:
        return a + b


def makes10(a, b):
  return a == 10 or b == 10 or (a + b == 10)



def not_string(s):
    if s.startswith("not"):
        return s
    else:
        return "not " + s




def front3(s):
    front = s[:3]
    return front * 3


#Warmup 2: 


def string_times(s, n):
    return s * n


def string_splosion(s):
    result = ""
    for i in range(len(s)):
        result += s[:i+1]
    return result



def array_front9(nums):
   return 9 in nums[:4]


def front_times(s, n):
    front = s[:3]
    return front * n



def last2(str):
    if len(str) < 2:
        return 0
    
    last = str[-2:]
    count = 0
    
    for i in range(len(str) - 2):
        if str[i:i+2] == last:
            count += 1
            
    return count



def array123(nums):
    for i in range(len(nums) - 2):
        if nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3:
            return True
    return False



def string_bits(s):
    return s[::2]


def array_count9(nums):
  return nums.count(9)


def string_match(a, b):
  
    count = 0
    length = min(len(a), len(b))
    
    for i in range(length - 1):
        if a[i:i+2] == b[i:i+2]:
            count += 1
            
    return count


