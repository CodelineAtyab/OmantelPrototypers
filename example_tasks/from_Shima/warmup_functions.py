# Warmup-1: sleep_in
# Return True if it is not a weekday or if we are on vacation.
def sleep_in(weekday, vacation):
    if not weekday or vacation:
        return True
    else:
        return False


# Warmup-1: monkey_trouble
# We are in trouble if both monkeys are smiling or both are not.
def monkey_trouble(a_smile, b_smile):
    if a_smile and b_smile:
        return True
    elif not a_smile and not b_smile:
        return True
    elif not a_smile or not b_smile:
        return False
    else:
        return False


# Warmup-1: sum_double
# Return double the sum if the values are the same.
def sum_double(a, b):
    if a != b:
        return a + b
    else:
        return (a + b) * 2


# Warmup-1: diff21
# Return the absolute difference from 21, doubled if over.
def diff21(n):
    if n > 21:
        return 2 * abs(21 - n)
    else:
        return 21 - n


# Warmup-1: parrot_trouble
# Trouble occurs if the parrot talks before 7 or after 20.
def parrot_trouble(talking, hour):
    if talking and (hour < 7 or hour > 20):
        return True
    else:
        return False


# Warmup-1: makes10
# Return True if either value is 10 or their sum is 10.
def makes10(a, b):
    if a == 10 or b == 10:
        return True
    elif (a + b) == 10:
        return True
    else:
        return False


# Warmup-1: near_hundred
# Return True if the value is within 10 of 100 or 200.
def near_hundred(n):
    return (abs(100 - n) <= 10) or (abs(200 - n) <= 10)


# Warmup-1: pos_neg
# Return True if one is negative and one is positive, unless negative flag is set.
def pos_neg(a, b, negative):
    if negative:
        return (a < 0 and b < 0)
    else:
        return (a < 0 < b) or (b < 0 < a)


# Warmup-1: not_string
# Add 'not ' to the front if the string does not already start with it.
def not_string(text):
    if text.startswith("not"):
        return text
    return "not " + text


# Warmup-1: missing_char
# Remove the character at the given index.
def missing_char(text, n):
    front = text[:n]
    back = text[n + 1:]
    return front + back


# Warmup-1: front_back
# Swap the first and last characters of the string.
def front_back(text):
    if len(text) <= 1:
        return text

    mid = text[1:-1]
    return text[-1] + mid + text[0]


# Warmup-1: front3
# Return 3 copies of the front of the string.
def front3(text):
    front_end = 3
    if len(text) < front_end:
        front_end = len(text)
    front = text[:front_end]
    return front + front + front


# Warmup-2: string_times
# Repeat the string n times.
def string_times(text, n):
    if n == 1:
        return text
    else:
        return text * n


# Warmup-2: front_times
# Repeat the first 3 characters n times.
def front_times(text, n):
    return text[:3] * n


# Warmup-2: string_bits
# Return every other character starting with the first.
def string_bits(text):
    result = ""
    for i in range(len(text)):
        if i % 2 == 0:
            result += text[i]
    return result


# Warmup-2: string_splosion
# Build a string made of prefixes of the input.
def string_splosion(text):
    result = ""
    for i in range(len(text)):
        result += text[: i + 1]
    return result


# Warmup-2: last2
# Count the number of times the last two chars appear elsewhere in the string.
def last2(text):
    if len(text) < 2:
        return 0

    last_two = text[-2:]
    count = 0
    for i in range(len(text) - 2):
        if text[i : i + 2] == last_two:
            count += 1
    return count


# Warmup-2: array_count9
# Count how many 9s appear in the list.
def array_count9(nums):
    count = 0
    for i in nums:
        if i == 9:
            count += 1
    return count


# Warmup-2: array_front9
# Check whether one of the first 4 items is a 9.
def array_front9(nums):
    end = len(nums)
    if end > 4:
        end = 4

    for i in range(end):
        if nums[i] == 9:
            return True
    return False


# Warmup-2: array123
# Check whether the sequence 1, 2, 3 appears in the list.
def array123(nums):
    for i in range(len(nums) - 2):
        if nums[i] == 1 and nums[i + 1] == 2 and nums[i + 2] == 3:
            return True
    return False


# Warmup-2: string_match
# Count matching 2-char substrings in both strings.
def string_match(a, b):
    shorter = min(len(a), len(b))
    count = 0
    for i in range(shorter - 1):
        if a[i : i + 2] == b[i : i + 2]:
            count += 1
    return count
