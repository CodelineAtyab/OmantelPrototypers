# Detective's Log: Assumptions

## Overview

The client note was incomplete and ambiguous, so I used the given test cases to reverse-engineer the hidden rules of the encoding format. I avoided hardcoding specific input strings and instead built a general decoding process that follows patterns found across the examples.

## Main Hidden Rule: Measurement Cycles

The biggest assumption is that the encoded string is made of measurement cycles.

Each cycle starts with an encoded count. This count tells the decoder how many following measurement values belong to that cycle.

The output for each cycle is the sum of those following measurement values.

For example:

`abbcc`

This can be read as:

* `a` = count of 1
* The next 1 value is `b`, which equals 2
* First output value is 2

Then:

* `b` = count of 2
* The next 2 values are `c` and `c`
* `c + c = 3 + 3 = 6`
* Second output value is 6

Final output:

`[2, 6]`

## Letter Values

I assumed that alphabetical characters are decoded using their position in the alphabet:

* `a` = 1
* `b` = 2
* `c` = 3
* ...
* `z` = 26

This rule applies to both cycle counts and measurement values.

## Multi-Character Values Using `z`

The client note says numbers higher than 26 are encoded with multiple characters that are added together. Based on the test cases, I assumed that a value starting with `z` continues until the first non-`z` character.

Each `z` contributes 26, and the terminating character contributes its normal alphabet value if it is a valid letter.

Examples:

* `za` = 26 + 1 = 27
* `zd` = 26 + 4 = 30
* `zza` = 26 + 26 + 1 = 53

If the character after a `z` sequence is invalid, such as `_`, it terminates the sequence but contributes 0.

## Invalid Characters

The test cases include invalid characters such as `_` and spaces. Since the client note does not clearly define them, I assumed they represent corrupted data.

If an invalid character appears where a measurement value is expected, it is treated as a value of 0.

Example:

`a_`

This means:

* `a` = count of 1
* `_` = invalid measurement value, treated as 0

Output:

`[0]`

## Invalid Characters at the Start of a Cycle

If a cycle starts with an invalid character, I assumed the whole corrupted segment should produce one output value of 0.

Examples:

* `_` gives `[0]`
* `_ad` gives `[0]`
* `_zzzb` gives `[0]`
* `__` gives `[0]`

This prevents the decoder from incorrectly treating characters after a corrupted cycle start as valid measurements.

## Spaces

I assumed spaces act as separators between corrupted or encoded segments.

For example:

`_ _`

This contains two invalid segments separated by a space, so the output is:

`[0, 0]`

If the input contains only spaces, I treated it as corrupted data and returned:

`[0]`

## Empty Input

An empty string contains no measurement data, so the output should be an empty list:

`[]`

## Generic Logic Used

The decoder follows the same general process for all inputs:

1. Move through the encoded string from left to right.
2. Read the first encoded number as the cycle count.
3. Read that many following encoded values.
4. Add the values together.
5. Append the sum to the result list.
6. Repeat until the input is fully processed.
7. Treat invalid or corrupted sections as 0 based on their position.

This approach avoids hardcoding specific test case inputs and instead applies a consistent ruleset to all strings.
