# The Detective's Log: Reverse-Engineered Encodings

Through systematic breakdown of the input/output mappings against the initial brief, several implicit, "hidden rules" were uncovered that deviate from standard serialization formats:

### 1. Count Presentation Rule
The original requirement notes that a "number" dictates the measurement count. The test suite reveals that this count is **not** an ASCII digit (`1`, `2`, `3`), but is instead encoded using the exact same alphabetical variable-length format as the measurements themselves (`a` = 1, `b` = 2, etc.).

### 2. Inner-Cycle Metric Aggregation
When a cycle indicates a count higher than 1 (e.g., `b` = 2 or `c` = 3), the decoded output does not append distinct elements to the final list. Instead, the parser absorbs the assigned number of parameters and **sums them together** to generate one single metric block integer per cycle (e.g., `"abbcc"` uses a count of 2 to read two individual `c` values, outputting $3 + 3 = 6$).

### 3. Early Packet Termination and Abort Command (`_`)
* The underscore (`_`) mathematically processes as `0`.
* If a packet packet-stream starts with `0` (or encounters a count evaluating to `0`), it acts as an **abort condition**. The parser logs a `0` value for that sequence and halts the loop execution for the remainder of that packet substring, effectively ignoring trailing unparsed buffer garbage (e.g., `"_zzzb"` $\rightarrow$ `[0]`).

### 4. Spacing Delimiters
Spaces within strings act as hard package stream packet frame boundaries. Input streams containing `" "` are isolated into individual strings and parsed through independent state cycles, appending tracking elements linearly (e.g., `"_ _"` $\rightarrow$ `[0, 0]`).