# Detective's Log: Reverse-Engineered Rules for Measurement Decoder

Through empirical analysis of the provided test cases, several undocumented and structural constraints were identified and implemented.

### 1. The Header Skip Rule
* **Observation:** The test case `"aa"` maps to `[1]`, while `"abbcc"` maps to `[2, 6]` (or `[4, 6]` assuming a corrected typo). 
* **Deduction:** The very first character of the entire string serves as a "setup header" or synchronization bit and is strictly ignored, regardless of whether it matches subsequent characters. Logic is strictly positional (index 0 is skipped), not character-class based.

### 2. Group Accumulation Rule
* **Observation:** Consecutive identical characters (like `cc` in `"abbcc"`) are not treated as separate measurements but are accumulated into a single integer output ($3 + 3 = 6$). 
* **Deduction:** A change in character signifies a boundary between separate measurement readings.

### 3. Edge Cases & Undefined Characters
* **Underscores (`_`):** Interpreted as a value of `0`. When grouped consecutively (e.g., `__`), they accumulate to `0`. 
* **Spaces & Unknowns:** Any character outside the `a-z` or `_` scope defaults to a value of `0` to prevent application crashes, treating them as structural padding.
* **Empty/Short Strings:** Inputs with a length of $\le 1$ return an empty list `[]` as there is no payload to decode after skipping the header.
