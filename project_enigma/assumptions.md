# The Detective's Log — `assumptions.md`

The client's note described the format only loosely. Below are the "hidden
rules" I reverse-engineered from the test cases, and the reasoning behind each.

## The core structure (the breakthrough)

The note says: *"a number indicating the count of values measured in each
measurement cycle, followed by the measured values."*

The decisive clue was `("dz_a_aazzaaa", [28, 53, 1])`. No simple prefix of that
string sums to 28, but it falls out cleanly if you read the stream as repeating
**cycles**:

```
[count C][number_1][number_2] ... [number_C]   ->   sum of those C numbers
```

So each cycle reads one **count**, then sums the next **C numbers** to produce
one output value, and repeats until the stream is consumed.

Walking through `dz_a_aazzaaa`:

| Step  | Count    | Numbers read                 | Sum    |
|-------|----------|------------------------------|--------|
| 1     | `d` = 4  | `z_`=26, `a`=1, `_`=0, `a`=1 | **28** |
| 2     | `a` = 1  | `zza` = 26+26+1              | **53** |
| 3     | `a` = 1  | `a` = 1                      | **1**  |

This same model reproduces `("abbcc", [2, 6])` (count 1 → `b`; count 2 → `cc`)
and `("abcdabcdab", [2, 7, 7])` (count 1 → `b`; count 3 → `dab`; count 3 → `dab`).

## Rule 1 — letter values

`a`=1, `b`=2, … `z`=26, exactly as stated.

## Rule 2 — `z` is an accumulator ("a number > 26")

The note: *"Numbers higher than 26 are encoded with multiple characters that are
added together [and] terminated with the first non-'z' character."*

I read this as: a single **number** is a run of zero-or-more `z`s (each worth
26) followed by **one** terminating non-`z` character that adds its own value
and ends the number.

- `a`            → 1
- `zz` + `a`     → 26 + 26 + 1 = 53   (confirmed by case 3)
- `z` + `d`      → 26 + 4 = 30        (the count in case 7 → reads 30 numbers
                                       that sum to 34)

## Rule 3 — the count is itself a number

The count is read with the *same* z-accumulation logic, which is why
`zdaaaa...` (case 7) yields a single value: `z`+`d` = a count of **30**, then
the next 30 letters (26 `a`s + 4 `b`s) are summed → **34**.

## Rule 4 — undefined characters (`_`, spaces, anything non a–z) = 0

Every test case treats `_` as contributing nothing. Examples:
`("a_", [0])` → count `a`=1, next number `_`=0 → value 0. In value position an
underscore is simply a zero (`("aab___", [1, 0, 0])` → count 2 reads `__` = 0).

## Rule 5 — a count of 0 terminates the package (emitting one `0`)

This was the subtlest rule, forced by three cases that would otherwise produce
extra output:

- `("_ad", [0])` — if `_`=0 in the count position only paused, `ad` would
  decode to `4` and we'd get `[0, 4]`. It doesn't, so the package **stops**.
- `("__", [0])` and `("_zzzb", [0])` — same: the leading `_` (count 0) emits a
  single `0` and ends decoding; the rest of the string is ignored.

So: when the count evaluates to 0, append one `0` and terminate the current
package. (Counts coming from letters are always ≥ 1, so this never fires
mid-stream for "real" data.)

## Rule 6 — space separates independent packages

`("_ _", [0, 0])` is the only case with a space, and it cannot come from a
single package (the leading `_` would stop after the first `0`). It only works
if the space splits the input into two packages `"_"` and `"_"`, each decoding
to `[0]`, concatenated. So a space is a hard package boundary.

## Rule 7 — empty / exhausted input

- `("", [])` — empty input yields an empty list.
- If a cycle's count asks for more numbers than remain, we sum what's left and
  stop (the loop ends naturally when the stream is exhausted).

## Summary of the decision table

| Situation                                  | Behaviour                          |
|--------------------------------------------|------------------------------------|
| `a`–`y` in number position                 | adds 1–25, ends the number         |
| `z` in number position                     | adds 26, continues the run         |
| `_` / space / undefined in number position | adds 0, ends the number            |
| count evaluates to `0`                     | emit one `0`, terminate package    |
| space between packages                     | start a fresh package, concatenate |
| empty string                               | `[]`                               |
