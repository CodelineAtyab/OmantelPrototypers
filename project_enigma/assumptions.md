# The Detective's Log (assumptions.md)

The client's note was vague, so I reverse-engineered the real rules by
comparing the note against the test cases one by one. Here is what I found.

## The core format

The note says each package is "a number indicating the count of values measured
in each measurement cycle, followed by the measured values". After studying the
examples, this is what it actually means:

1. Read a **count** number.
2. Read that many **value** numbers right after it.
3. Add those values together. That sum is one output number.
4. Repeat from step 1 until the string runs out.

Example: `abbcc`

- `a` = 1, so the first cycle has 1 value -> next value is `b` = 2 -> output `2`
- `b` = 2, so the next cycle has 2 values -> `c` + `c` = 3 + 3 = 6 -> output `6`
- Result: `[2, 6]`

This single rule explains the tricky ones too:

- `abcdabcdab` -> count `a`(1) sums `b`=2, then count `c`(3) sums `d+a+b`=7,
  then count `c`(3) sums `d+a+b`=7 -> `[2, 7, 7]`.
- `zdaaaaaaaab...bbaa` -> count is `zd` = 30, then the next exactly 30 values
  add up to 34 -> `[34]`.

## How a single number is read (the "z" rule)

The note says numbers above 26 use multiple characters "added together" and are
"terminated with the first non-z character". So a number is read like this:

- Every `z` means 26 and we keep reading.
- The first character that is **not** `z` ends the number and is added on.

So `z` = 26, `za` = 26 + 1 = 27, `zz a` = 26 + 26 + 1 = 53, and a plain letter
like `d` is just 4. This is used for both the count and the values.

Example: `dz_a_aazzaaa` -> `[28, 53, 1]`

- count `d` = 4, then 4 values: `z_`(26+0=26... read as z then `_`), `a`, `_`, `a`
  giving 26 + 1 + 0 + 1 = 28
- count `a` = 1, then 1 value `zza` = 53
- count `a` = 1, then 1 value `a` = 1

## Edge cases and undefined characters

- **The underscore `_`**: it is not a letter, so I treat it as value `0`. This
  matches `a_` -> `[0]` (count `a`=1, then value `_`=0).
- **A count of zero acts as a terminator.** When the count itself comes out as 0
  (for example a leading `_`), it means there is no real cycle there. I record a
  single `0` and stop reading the rest of that chunk. This is what makes
  `__` -> `[0]`, `_ad` -> `[0]`, and `_zzzb` -> `[0]` (everything after the first
  `_` is ignored), while `aab___` still gives `[1, 0, 0]`.
- **Spaces split the input.** `_ _` -> `[0, 0]` only makes sense if the space
  breaks the text into two separate chunks (`_` and `_`) that are decoded on
  their own and joined together. So I split on spaces first, decode each piece,
  and combine the results.
- **Empty string** -> `[]`, because there is nothing to read.
- **Unknown characters in general** are treated like `_` (value 0), so the
  function never crashes on unexpected input.

## Running out of characters

If a count asks for more values than the string actually has, the reader simply
stops at the end and adds up whatever it managed to read. This keeps the function
safe on malformed input instead of throwing an error.
