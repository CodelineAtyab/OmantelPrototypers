# The Detective's Log — assumptions.md
## Project Enigma: Hidden Rules Reverse-Engineered

---

## Rule 1: The COUNT uses z-encoding

The client's note says numbers higher than 26 use "multiple characters that are added together, terminated by the first non-z character."

I discovered this applies to the COUNT field at the start of each package:
- Read all `z` characters, each adding 26 to the running total.
- Stop at the first non-`z` letter, add its value, and that is the final count.

**Examples discovered from test cases:**
- `d` = 4
- `zd` = 26 + 4 = 30 (confirmed by `zdaaaaaaaabaaaaaaaabaaaaaaaabbaa` → [34] with 30 values)
- `zza` = 26 + 26 + 1 = 53

---

## Rule 2: The VALUES also use z-encoding (not stated in the client's note)

The client's note only describes z-encoding for "numbers." I found through the test cases that individual measured values inside a package are also z-encoded — not flat single letters.

**Evidence:** `dz_a_aazzaaa` → [28, 53, 1]
- Count = `d` = 4
- Value 1: `z_` = 26 + 0 = 26 (z followed by `_` as terminator)
- Value 2: `a` = 1
- Value 3: `_` = 0
- Value 4: `a` = 1
- Sum = 28 ✓

And later in the same string: `azzaaa` → count `a`=1, one value `zza` = 26+26+1 = 53 ✓

---

## Rule 3: Underscore `_` means zero in all positions

The client's note does not mention `_` at all. I reverse-engineered its meaning:
- As a standalone value: `_` = 0
- As the terminator of a z-encoded value: adds 0 (e.g. `z_` = 26 + 0 = 26)
- At the start of a package: signals an empty package with sum = 0

---

## Rule 4: A package starting with `_` discards the rest of its space-separated group

This was the trickiest hidden rule. The test cases revealed a contradiction that required careful analysis:

| Input | Expected | Observation |
|-------|----------|-------------|
| `_ad` | `[0]` | `ad` is discarded after `_` |
| `_zzzb` | `[0]` | `zzzb` is discarded after `_` |
| `__` | `[0]` | second `_` is discarded |
| `_ _` | `[0, 0]` | space separates into two valid packages |
| `aab___` | `[1, 0, 0]` | `b__` = count 2, two `_` values = 0+0=0 — NOT the discard rule |

**Conclusion:** The discard rule only applies when `_` is the very first character in a space-separated group. When `_` appears as a value inside a normal package (e.g. after `b` in `aab___`), it is treated normally as a zero value.

**Implementation decision:** Split the full string by spaces first, then apply the discard rule per token.

---

## Rule 5: Spaces separate independent packages

Spaces are not part of any encoding — they are delimiters between separate package groups. This is what allows `_ _` to produce two packages instead of one.

---

## Summary of Encoding Structure

```
[PACKAGE] [PACKAGE] [PACKAGE] ...
  ^space-separated^

Each PACKAGE:
  COUNT (z-encoded) + COUNT × VALUE (each z-encoded)

  OR

  _ (zero package — rest of this space-group is discarded)

z-encoding for a number N:
  floor(N/26) × 'z' + letter_for(N mod 26)   [where a=1...y=25, and z=26 via the next z]
  underscore '_' counts as 0 in any terminator position
```
