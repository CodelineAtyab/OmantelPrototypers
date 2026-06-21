#Warmup-1

def sleep_in(weekday, vacation):
  return not weekday or vacation


def monkey_trouble(a_smile, b_smile):
  return a_smile == b_smile

def sum_double(a, b):
    if a == b:
        return (a + b) * 2
    return a + b


def diff21(n):
    if n > 21:
        return (n - 21) * 2
    return 21 - n

def parrot_trouble(talking, hour):
    if talking and (hour < 7 or hour > 20):
        return True
    return False

def makes10(a, b):
    return a == 10 or b == 10 or a + b == 10

def near_hundred(n):
    return abs(n - 100) <= 10 or abs(n - 200) <= 10

def pos_neg(a, b, negative):
    if negative:
        return a < 0 and b < 0
    return (a < 0) != (b < 0)

def not_string(str):
    if str.startswith("not"):
        return str
    return "not " + str

def missing_char(str, n):
    return str[:n] + str[n+1:]

def front_back(str):
    if len(str) <= 1:
        return str
    return str[-1] + str[1:-1] + str[0]

def front3(str):
    front = str[:3]
    return front * 3

#Warmup-2

def string_times(str, n):
    return str * n

def front_times(str, n):
    front = str[:3]
    return front * n

def string_bits(str):
    return str[::2]

def string_splosion(str):
    result = ""
    for i in range(len(str)):
        result += str[:i+1]
    return result

def last2(str):
    count = 0
    end = str[-2:]

    for i in range(len(str)-2):
        if str[i:i+2] == end:
            count += 1

    return count

def array_count9(nums):
  return nums.count(9)


def array_front9(nums):
  return 9 in nums[:4]

def array123(nums):
    for i in range(len(nums) - 2):
        if nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3:
            return True
    return False

def string_match(a, b):
    count = 0

    for i in range(min(len(a), len(b)) - 1):
        if a[i:i+2] == b[i:i+2]:
            count += 1

    return count

#String-1

def hello_name(name):
    return "Hello " + name + "!"

def make_abba(a, b):
    return a + b + b + a

def make_tags(tag, word):
    return "<" + tag + ">" + word + "</" + tag + ">"

def make_out_word(out, word):
    return out[:2] + word + out[2:]

def extra_end(str):
    return str[-2:] * 3

def first_two(str):
    return str[:2]

def first_half(str):
    return str[:len(str)//2]

def without_end(str):
    return str[1:-1]

def combo_string(a, b):
    short = a if len(a) < len(b) else b
    long = b if len(a) < len(b) else a
    return short + long + short

def non_start(a, b):
    return a[1:] + b[1:]

def left2(str):
    return str[2:] + str[:2]

#List-1
def first_last6(nums):
    return nums[0] == 6 or nums[-1] == 6

def same_first_last(nums):
    return len(nums) >= 1 and nums[0] == nums[-1]

def make_pi():
    return [3, 1, 4]

def common_end(a, b):
    return a[0] == b[0] or a[-1] == b[-1]


def sum3(nums):
    return sum(nums)

def rotate_left3(nums):
    return [nums[1], nums[2], nums[0]]

def reverse3(nums):
    return [nums[2], nums[1], nums[0]]

def max_end3(nums):
    max_num = max(nums[0], nums[2])
    return [max_num, max_num, max_num]

def sum2(nums):
    return sum(nums[:2])

def middle_way(a, b):
  return [a[1], b[1]]

def make_ends(nums):
    return [nums[0], nums[-1]]

def has23(nums):
    return 2 in nums or 3 in nums

#Logic-1

def cigar_party(cigars, is_weekend):
    if is_weekend:
        return cigars >= 40
    return 40 <= cigars <= 60

def date_fashion(you, date):
    if you <= 2 or date <= 2:
        return 0
    if you >= 8 or date >= 8:
        return 2
    return 1

def squirrel_play(temp, is_summer):
    if is_summer:
        return 60 <= temp <= 100
    return 60 <= temp <= 90

def caught_speeding(speed, is_birthday):
    if is_birthday:
        speed -= 5

    if speed <= 60:
        return 0
    elif speed <= 80:
        return 1
    else:
        return 2
    
def sorta_sum(a, b):
    total = a + b

    if 10 <= total <= 19:
        return 20

    return total

def alarm_clock(day, vacation):
    if vacation:
        if day == 0 or day == 6:
            return "off"
        return "10:00"
    else:
        if day == 0 or day == 6:
            return "10:00"
        return "7:00"    

def love6(a, b):
    return a == 6 or b == 6 or a + b == 6 or abs(a - b) == 6

def in1to10(n, outside_mode):
    if outside_mode:
        return n <= 1 or n >= 10
    return 1 <= n <= 10

def near_ten(num):
    return num % 10 <= 2 or num % 10 >= 8

#Logic-2

def make_bricks(small, big, goal):
    return goal - min(big, goal // 5) * 5 <= small

def lone_sum(a, b, c):
    if a == b == c:
        return 0
    if a == b:
        return c
    if a == c:
        return b
    if b == c:
        return a
    return a + b + c

def lucky_sum(a, b, c):
    if a == 13:
        return 0
    if b == 13:
        return a
    if c == 13:
        return a + b
    return a + b + c

def fix_teen(n):
    if n in [13, 14, 17, 18, 19]:
        return 0
    return n

def no_teen_sum(a, b, c):
    return fix_teen(a) + fix_teen(b) + fix_teen(c)

def round10(num):
    if num % 10 >= 5:
        return num + (10 - num % 10)
    return num - (num % 10)

def round_sum(a, b, c):
    return round10(a) + round10(b) + round10(c)

def close_far(a, b, c):
    return ((abs(a-b) <= 1 and abs(a-c) >= 2 and abs(b-c) >= 2) or
            (abs(a-c) <= 1 and abs(a-b) >= 2 and abs(b-c) >= 2))

def make_chocolate(small, big, goal):
    big_used = min(big, goal // 5)
    remaining = goal - big_used * 5

    if remaining <= small:
        return remaining
    return -1

#String-2
def double_char(str):
    result = ""

    for ch in str:
        result += ch * 2

    return result

def count_hi(str):
    return str.count("hi")

def cat_dog(str):
    return str.count("cat") == str.count("dog")

def count_code(str):
    count = 0

    for i in range(len(str) - 3):
        if str[i:i+2] == "co" and str[i+3] == "e":
            count += 1

    return count

def end_other(a, b):
    a = a.lower()
    b = b.lower()

    return a.endswith(b) or b.endswith(a)
    

def xyz_there(str):
    return "xyz" in str.replace(".xyz", "")


#List-2

def count_evens(nums):
    count = 0

    for num in nums:
        if num % 2 == 0:
            count += 1

    return count

def big_diff(nums):
    return max(nums) - min(nums)

def centered_average(nums):
    nums.sort()
    return sum(nums[1:-1]) // (len(nums) - 2)

def sum13(nums):
    total = 0
    i = 0

    while i < len(nums):
        if nums[i] == 13:
            i += 2
        else:
            total += nums[i]
            i += 1

    return total

def sum67(nums):
    total = 0
    ignore = False

    for num in nums:
        if num == 6:
            ignore = True
        elif num == 7 and ignore:
            ignore = False
        elif not ignore:
            total += num

    return total

def has22(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 2 and nums[i + 1] == 2:
            return True
    return False
