"""
CodingBat Python Solutions
Warm-Up 1 & Warm-Up 2
"""

# ============================================================
# WARM-UP 1
# ============================================================

# sleep_in
def sleep_in(weekday, vacation):
    return (not weekday) or vacation


# monkey_trouble
def monkey_trouble(a_smile, b_smile):
    return a_smile == b_smile


# sum_double
def sum_double(a, b):
    s = a + b
    if a == b:
        return s * 2
    return s


# diff21
def diff21(n):
    if n <= 21:
        return 21 - n
    return (n - 21) * 2


# parrot_trouble
def parrot_trouble(talking, hour):
    return talking and (hour < 7 or hour > 20)


# makes10
def makes10(a, b):
    return a == 10 or b == 10 or a + b == 10


# near_hundred
def near_hundred(n):
    return abs(100 - n) <= 10 or abs(200 - n) <= 10


# pos_neg
def pos_neg(a, b, negative):
    if negative:
        return a < 0 and b < 0
    return (a < 0) != (b < 0)


# not_string
def not_string(str):
    if str[:3] == "not":
        return str
    return "not " + str


# missing_char
def missing_char(str, n):
    return str[:n] + str[n+1:]


# front_back
def front_back(str):
    if len(str) <= 1:
        return str
    return str[-1] + str[1:-1] + str[0]


# front3
def front3(str):
    front = str[:3]
    return front * 3


# ============================================================
# WARM-UP 2
# ============================================================

# string_times
def string_times(str, n):
    return str * n


# front_times
def front_times(str, n):
    front = str[:3]
    return front * n


# string_bits
def string_bits(str):
    return str[::2]


# string_splosion
def string_splosion(str):
    result = ""
    for i in range(len(str) + 1):
        result += str[:i]
    return result


# last2
def last2(str):
    if len(str) < 2:
        return 0
    last = str[-2:]
    count = 0
    for i in range(len(str) - 2):
        if str[i:i+2] == last:
            count += 1
    return count


# array_count9
def array_count9(nums):
    return nums.count(9)


# array_front9
def array_front9(nums):
    return 9 in nums[:4]


# array123
def array123(nums):
    for i in range(len(nums) - 2):
        if nums[i:i+3] == [1, 2, 3]:
            return True
    return False


# string_match
def string_match(a, b):
    count = 0
    for i in range(min(len(a), len(b)) - 1):
        if a[i:i+2] == b[i:i+2]:
            count += 1
    return count


# make_bricks
def make_bricks(small, big, goal):
    use_big = min(goal // 5, big)
    remaining = goal - use_big * 5
    return remaining <= small


# lone_sum
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


# round_sum
def round10(num):
    return round(num / 10) * 10

def round_sum(a, b, c):
    return round10(a) + round10(b) + round10(c)


# close_far
def close_far(a, b, c):
    diff_b = abs(a - b)
    diff_c = abs(a - c)
    if diff_b <= 1 and diff_c > diff_b + 1:
        return True
    if diff_c <= 1 and diff_b > diff_c + 1:
        return True
    return False


# make_chocolate
def make_chocolate(small, big, goal):
    use_big = min(goal // 5, big)
    remaining = goal - use_big * 5
    if remaining <= small:
        return remaining
    return -1
