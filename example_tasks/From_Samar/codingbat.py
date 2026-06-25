def sleep_in(weekday, vacation):

    return (not weekday) or vacation
 
def monkey_trouble(a_smile, b_smile):

    return a_smile == b_smile
 
def sum_double(a, b):

    total = a + b

    return total * 2 if a == b else total
 
def diff21(n):

    if n <= 21:

        return 21 - n

    return (n - 21) * 2
 
def parrot_trouble(talking, hour):

    return talking and (hour < 7 or hour > 20)
 
def makes10(a, b):

    return a == 10 or b == 10 or a + b == 10
 
def near_hundred(n):

    return abs(100 - n) <= 10 or abs(200 - n) <= 10
 
def pos_neg(a, b, negative):

    if negative:

        return a < 0 and b < 0

    return (a < 0) != (b < 0)
 
def not_string(str):

    if str[:3] == "not":

        return str

    return "not " + str
 
def missing_char(str, n):

    return str[:n] + str[n + 1:]
 
def front_back(str):

    if len(str) <= 1:

        return str

    return str[-1] + str[1:-1] + str[0]
 
def front3(str):

    front = str[:3]

    return front * 3
 
def string_times(str, n):

    return str * n
 
def front_times(str, n):

    front = str[:3]

    return front * n
 
def count_xx(str):

    count = 0

    for i in range(len(str) - 1):

        if str[i:i + 2] == "xx":

            count += 1

    return count
 
def string_match(a, b):

    shorter = min(len(a), len(b))

    count = 0

    for i in range(shorter - 1):

        if a[i:i + 2] == b[i:i + 2]:

            count += 1

    return count
 
def string_bits(str):

    return str[::2]
 
def string_splosion(str):

    result = ""

    for i in range(len(str) + 1):

        result += str[:i]

    return result
 
def last2(str):

    if len(str) < 2:

        return 0

    last_two = str[-2:]

    count = 0

    for i in range(len(str) - 2):

        if str[i:i + 2] == last_two:

            count += 1

    return count
 
def array_count9(nums):

    return nums.count(9)
 
def array_front9(nums):

    return 9 in nums[:4]
 
def array123(nums):

    for i in range(len(nums) - 2):

        if nums[i:i + 3] == [1, 2, 3]:

            return True

    return False
 
 