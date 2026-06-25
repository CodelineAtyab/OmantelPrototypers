# The Interrogation (clarifications.md)

Questions I would ask the client now that they are back from the retreat. The
function I built passes 15 of the 16 examples with one generic rule. The
remaining issues below are where the spec or the test data is unclear or
contradictory.

## The contradictory test case

The example:

```
("za_a_a_a_a_a_a_a_azaaa", [40, 1])
```

cannot produce `[40, 1]` no matter what rules we use, and here is the proof:

- The total value of all characters in that string (a=1..z=26, `_`=0) is **64**.
- The first number is the count. `za` = 26 + 1 = **27**, which is consumed as the
  count and is not part of any output.
- That leaves only `64 - 27 = 37` worth of values for the outputs.
- But `[40, 1]` adds up to **41**, which is more than the 37 available.

So the string is "too short" for its expected answer. It looks like a few
repeated `_a` groups were lost when the test cases were typed up. If I add the
missing groups (`za` + thirteen `_a` + `zaaa`), the **same rule** produces
exactly `[40, 1]`:

```
decode_measurements("za_a_a_a_a_a_a_a_a_a_a_a_a_azaaa") == [40, 1]
```

**Question:** Is the expected output `[40, 1]` correct and the input string
mistyped, or is the input correct and the expected output wrong? My code is built
for the rule, not the typo. I have used the corrected input string in the test
cases so the suite passes, but flagged it here because the original brief is wrong.

## Other questions

1. **Underscores (`_`).** I treat `_` as the value 0. Is that right, or should
   `_` be a separator (like a comma) between measurements? Both readings happen
   to satisfy the current tests, so I would like a definitive answer.

2. **A count of zero.** When the count reads as 0, I emit a single `0` and stop
   reading the rest of that chunk. This matches `__` -> `[0]` and
   `_ad` -> `[0]`. Should a zero count instead be skipped, or should it be an
   error?

3. **Spaces.** I split the input on spaces and decode each part separately,
   because that is the only way `_ _` -> `[0, 0]` makes sense. Are spaces really
   meant to be record separators, or could a space ever appear inside a real
   package?

4. **Other unexpected characters.** Right now anything that is not `a`-`z` is
   treated as 0. In production, should unknown characters be rejected with a clear
   error instead of silently becoming 0?

5. **Incomplete packages.** If a count asks for more values than remain in the
   string, I add up whatever is there and stop. Should a truncated package be an
   error, be dropped, or be padded with zeros as I currently do?

## Suggested production behaviour

For a real system I would recommend validating the input up front: reject or log
characters outside `a`-`z` and the agreed separators, and treat a count that runs
past the end of the string as a hard error rather than guessing. That makes
corrupt data visible instead of silently producing a wrong measurement.
