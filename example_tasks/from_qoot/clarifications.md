# Client Clarifications: Measurement Encoding Specification

Welcome back from your retreat! While implementing the prototype parser, our engineering team identified a few ambiguities and potential contradictions between the initial test suite and expected real-world data patterns. 

To ensure the production system is resilient, we would appreciate your guidance on the following:

### 1. The Consecutive Header Contradiction
* **Scenario:** In the test case `"aa"`, the output is `[1]`, proving the first letter is skipped. However, if the real-life input is `"aabb"`, does the second `a` signify a measurement of `1`, or should the entire initial character *group* be considered a header? 
* **Production Risk:** If an operational measurement naturally starts with the same letter as the header, positional skipping might accidentally slice a legitimate measurement in half.

### 2. Typo Verifications in Legacy Test Cases
* **Scenario:** The test case `"abbcc"` is listed as producing `[2, 6]`. Based on the accumulation rule established by `cc = 6`, `bb` should mathematically yield `4`. 
* **Question:** Is the input string `"abbcc"` missing a character (should be `"abcc"`), or does a double-letter sometimes *not* accumulate? 

### 3. Non-Consecutive Letter Recurrence
* **Scenario:** If a letter appears, changes to another, and returns later in the string (e.g., `"abaca"` -> skipping header -> `"baca"`).
* **Question:** Should this output two separate measurements (`[2, 3, 1]`), or should all matching letters across the entire string stream be aggregated together?

### 4. Explicit Boundary Disambiguation for Underscores (`_`)
* **Scenario:** Currently, `_` evaluates to `0`. 
* **Question:** Is the underscore intended to represent a literal value of zero, or is it meant to act as a visual spacer/delimiter to separate packets of data? (e.g., does `"ab_b"` mean `[2, 0, 2]` or is it a way to force two separate `b` packets instead of accumulating them?)
