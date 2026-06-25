def letter_value(ch):
    # a -> 1, b -> 2, ... z -> 26
    # anything we don't understand (like "_" or a space) counts as 0
    if "a" <= ch <= "z":
        return ord(ch) - ord("a") + 1
    return 0


def read_one_number(text, start):
    # Read a single number starting at position "start".
    # A "z" means 26 and we keep reading. The first non-z letter
    # ends the number and gets added on top.
    total = 0
    i = start
    while i < len(text):
        ch = text[i]
        if ch == "z":
            total += 26
            i += 1
        else:
            total += letter_value(ch)
            i += 1
            break
    return total, i


def decode_one_part(part):
    numbers = []
    i = 0
    while i < len(part):
        # first read how many values this cycle has
        count, i = read_one_number(part, i)

        # a count of zero means we hit a terminator like "_",
        # so we record a 0 and stop reading this part
        if count == 0:
            numbers.append(0)
            break

        # now read that many values and add them all together
        cycle_total = 0
        for _ in range(count):
            value, i = read_one_number(part, i)
            cycle_total += value

        numbers.append(cycle_total)
    return numbers


def decode_measurements(encoded_string: str) -> list[int]:
    # a space splits the input into separate chunks that we decode on their own
    result = []
    for part in encoded_string.split(" "):
        result.extend(decode_one_part(part))
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

    # Note: the "za..." case originally printed in the brief had too few "_a"
    # groups to ever produce [40, 1] (see clarifications.md). The corrected
    # string is used above, and the same generic rule handles it.
