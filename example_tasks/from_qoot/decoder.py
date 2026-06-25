def decode_measurements(encoded_string: str) -> list[int]:
    if not encoded_string or len(encoded_string) <= 1:
        return []

    # 1. Skip the first character (the setup header)
    payload = encoded_string[1:]
    
    decoded_values = []
    current_char = None
    current_sum = 0

    # Helper to convert character to its numeric value
    def get_char_value(ch: str) -> int:
        if ch == '_':
            return 0
        if 'a' <= ch <= 'z':
            return ord(ch) - ord('a') + 1
        return 0  # Default fallback for spaces or undefined characters

    # 2. Process the payload to group consecutive identical characters
    for char in payload:
        if char == current_char:
            current_sum += get_char_value(char)
        else:
            # If switching characters, save the previous group's sum
            if current_char is not None:
                decoded_values.append(current_sum)
            
            # Start a new group
            current_char = char
            current_sum = get_char_value(char)
            
    # Append the final group remaining in the loop
    if current_char is not None:
        decoded_values.append(current_sum)

    return decoded_values
