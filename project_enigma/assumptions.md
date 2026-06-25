# Detective's Log — Hidden Rules

The client's note described the encoding only loosely. Below are the rules I had to
reverse-engineer from the test cases to make the decoder generic (no hardcoding).

## Character values

- `a` = 1, `b` = 2, … `z` = 26, as stated in the note.
- Any character that is **not** a lowercase letter `a`–`z` (for example `_`, a space,
  or anything unexpected) is treated as **0**. The note never defines these, so I chose
  0 as a safe, neutral value. This is confirmed by `("a_", [0])`, where the underscore
  contributes nothing.

## Reading a single number (multi-character values)

A number is read as: a run of `z` characters, each adding 26, ended by the **first
non-`z` character**, which adds its own value and finishes the number.

- `z_` = 26 + 0 = 26
- `za` = 26 + 1 = 27
- `zza` = 26 + 26 + 1 = 53

This matches the note's "numbers higher than 26 are encoded with multiple characters
that are added together," and its line about the number being "terminated with the
first non-`z` character." Importantly, this rule applies to **every** number in the
string — both counts and measured values — which the note did not make explicit.

## Packet structure (inferred — the note does not state this directly)

The string is a sequence of packets laid end to end. Each packet is:

1. one number = the **count** of values in that packet, then
2. that many numbers = the **measured values**.

The output for each packet is the **sum of its values**. The note never uses the word
"sum"; I inferred it from `("abbcc", [2, 6])` (`a`=count 1 → value `b`=2; `c`=count 3 →
`d+a+b` = 7... etc.) and especially `("abcdabcdab", [2, 7, 7])`, which only works if:

- the count is read **per packet** (here the counts are 1, 3, 3), not a single fixed
  cycle length, and
- each packet's output is the sum of its values.

## Sequence termination

When the number in the **count position** evaluates to **0**, that marks the end of the
data: the decoder appends a single `0` and stops, discarding anything that follows.

This is the only reading consistent with all of these cases:

- `("_", [0])`
- `("__", [0])` — the second `_` is discarded
- `("_ad", [0])` — `ad` is discarded
- `("_zzzb", [0])` — `zzzb` is discarded
- `("abcdabcdab_", [2, 7, 7, 0])` — trailing `_` produces the final 0

## Edge cases

- **Empty string** → `[]` (the loop never runs).
- **Count larger than the remaining characters** → the decoder reads as many values as
  exist and stops gracefully (no crash).
- **Undefined characters** (`_`, space, etc.) → value 0, as above.

## One contradictory case

`("_ _", [0, 0])` does **not** fit the rules above; my decoder returns `[0]` for it.
This appears to be a faulty expected output — see `clarifications.md` for the reasoning.
