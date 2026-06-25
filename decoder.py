def _char_value(ch: str) -> int:
    if ch == '_':
        return 0
    return ord(ch) - ord('a') + 1

def _read_zchain(s: str, pos: int) -> tuple[int, int]:
    total = 0
    while pos < len(s):
        ch = s[pos]
        pos += 1
        total += _char_value(ch)
        if ch != 'z':
            break
    return total, pos

def decode_measurements(encoded_string: str) -> list[int]:
    results: list[int] = []
    for segment in encoded_string.split(' '):
        if not segment:
            continue
        pos = 0
        while pos < len(segment):
            if segment[pos] == '_':
                results.append(0)
                break
            count, pos = _read_zchain(segment, pos)
            measurement = 0
            for _ in range(count):
                if pos >= len(segment):
                    break
                val, pos = _read_zchain(segment, pos)
                measurement += val
            results.append(measurement)
    return results
