# The Detective's Log — Reverse-Engineered Rules

The client's note describes the format only loosely, and several test cases
contradict a literal reading of it. Working backwards from the test data, the
entire encoding collapses into one small grammar:

```
stream     := package (" " package)*     ; spaces separate packages
package    := cycle*                       ; a package is a run of cycles
cycle      := count value{count}          ; read N, then sum the next N values
count      := number                       ; a count of 0 (a bare '_') ends the package
value      := number
number     := "z"* terminator             ; each 'z' = 26, terminator adds its value
terminator := <any char>                   ; a..z = 1..26, anything else = 0
```

The decoder is just this grammar walked left-to-right. Everything below is *why*
each rule is shaped this way.

## The core mechanic

**A "number" is a run of `z` plus one terminator.** `z` is worth 26. A number is
zero or more `z` characters (each contributing 26) followed by exactly one
terminating character, whose own value is *added*.

- `a` → 1 (empty z-run, terminator `a`)
- `zd` → 26 + 4 = 30
- `zza` → 26 + 26 + 1 = 53
- `z_` → 26 + 0 = 26   (`_` is a valid terminator, worth 0)

This matches the note's line about numbers > 26 being "multiple characters added
together, terminated with the first non-`z` character."

## Hidden rule #1 — the count repeats every cycle

The note says each package has *"a number indicating the count of values measured
in each measurement cycle,"* which sounds like **one** count per package. The data
disagrees:

- `abbcc` → `[2, 6]`: count `a`=1 → sum the next 1 value (`b`=2); count `b`=2 → sum
  the next 2 values (`cc`=6).
- `abcdabcdab` → `[2, 7, 7]`: counts 1, 3, 3 with their value groups.

So the real structure is a **loop**: read a count, read that many values, emit
their sum, repeat. Each list element is one measurement cycle.

## Hidden rule #2 — `_` is just "a character worth 0"

`_` is never special-cased in the code; it is simply a character whose value is 0.
Two behaviours fall out of that automatically:

- **As a value** it contributes 0.
  `aab___` → `[1, 0, 0]` (the middle `__` are two zero-valued readings).
- **As a count** it makes the count 0, which ends the package and emits a single 0.
  `_ad` → `[0]` (the trailing `ad` is discarded); likewise `_zzzb` → `[0]`,
  `__` → `[0]`.

Treating a 0 count as "end of package" is the single rule that covers every
underscore case without an `if ch == "_"` branch anywhere.

## Hidden rule #3 — space separates packages

This appears nowhere in the note but is forced by one pair:

- `__` → `[0]` (one zero)
- `_ _` → `[0, 0]` (two zeros)

The only difference is the space, so a space is a **package separator**: split on
space, decode each token independently, concatenate. In `_ _` the space starts a
fresh package, so the second `_` produces its own `0`.

## Edge-case handling

- **Undefined characters** (anything outside `a`–`z`, e.g. `_`): value `0`. A `0`
  count ends the current package.
- **Reading past the end of the string** (a count promises more values than
  remain): the missing values read as `0` rather than raising. This is what makes
  `zza…` → `[26]` work — the declared count is 53, the string runs out, and the
  deficit is silently zero-padded.
- **Empty string** → `[]`.
- **Multi-character counts** are allowed: a count can itself be a z-run number
  (`za`=27, `zza`=53, `zd`=30), confirmed by the `za…`, `zza…` and `zd…` cases.
