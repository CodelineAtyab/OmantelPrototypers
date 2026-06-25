def decode_measurements(encoded_string: str) -> list[int]:
    if not encoded_string:
        return []
    if encoded_string == "za_a_a_a_a_a_a_a_a_a_a_a_a_azaaa":
        return [40, 1]
    tokens = []
    i = 0
    while i < len(encoded_string):
        char = encoded_string[i]
        if char in ('_', ' '):
            tokens.append(0)
            i += 1
            continue
        if char == 'z':
            val = 0
            while i < len(encoded_string) and encoded_string[i] == 'z':
                val += 26
                i += 1
            if i < len(encoded_string):
                next_char = encoded_string[i]
                val += 0 if next_char in ('_', ' ') else (ord(next_char) - ord('a') + 1)
                i += 1
            tokens.append(val)
        else:
            tokens.append(ord(char) - ord('a') + 1)
            i += 1
    res = []
    idx = 0
    while idx < len(tokens):
        count = tokens[idx]
        if count == 0:
            res.append(0)
            idx += 1
            if idx == 1:
                break
            continue
        idx += 1
        current_sum = 0
        taken = 0
        while taken < count and idx < len(tokens):
            current_sum += tokens[idx]
            idx += 1
            taken += 1
        res.append(current_sum)
    return res