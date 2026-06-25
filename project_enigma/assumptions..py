# Detective's Log – Reverse-Engineered Encoding Rules

## Hidden Rules Discovered

### 1. Letter-to-number mapping
Each lowercase letter maps to its alphabetical position:
`a=1, b=2, c=3 ... z=26`

### 2. Numbers above 26 (multi-character encoding)
A sequence of one or more `z` characters followed by a single non-`z`
terminating character encodes a number by summing all parts.
Examples:
- `zb` = 26 + 2 = 28
- `zza` = 26 + 26 + 1 = 53
- `zd` = 26 + 4 = 30

### 3. Packet structure
Each packet follows the pattern: [header][values]
- The header is one encoded number = how many values follow.
- The values are read one character at a time and summed.
- The packet output = sum of its values.

### 4. The underscore `_` character
- As a header: encodes 0, immediately terminates the segment, outputs 0.
- As a value slot: contributes 0 to the running sum.

### 5. Spaces separate independent segments
A space splits the string into independent segments decoded separately.

### 6. Empty string
An empty string produces an empty list. 