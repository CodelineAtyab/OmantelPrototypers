# The Interrogation — Clarification Questions for the Client

Now that the lead engineer is back from the retreat, these are the questions I
would put to them before treating the decoder as production-ready. The current
implementation reproduces every supplied example, but the behaviour on several
items is *inferred*, not *specified* — and a few cases look mutually
inconsistent.

## 1. The meaning of the count

The note says the package starts with "a number indicating the count of values
measured in **each** measurement cycle." That implies one count per package, but
the tests (`abbcc` → `[2, 6]`) only work if a fresh count is read at the start of
every cycle.

- **Q:** Confirm the format is a repeating `count, values…` loop, not a single
  leading count.

## 2. The role of the underscore `_`

`_` currently means `0` as a value but ends the package when it lands where a
count was expected:

- `aab___` → `[1, 0, 0]`  (`_` as values = zeros)
- `_ad` → `[0]`           (`_` as a count discards the rest, dropping `ad`)

- **Q:** Is `_` a deliberate "null / no measurement" sentinel? And is dropping
  everything after a `_`-in-count-position intended, or should the parser emit `0`
  and continue? `_ad` → `[0]` versus a plausible `[0, 4]` is the exact fork.

## 3. Space as a separator (undocumented)

Nothing in the note mentions spaces, but the only difference between
`__` → `[0]` and `_ _` → `[0, 0]` is a space, so I treat it as a package
separator.

- **Q:** Confirm spaces separate independent packages. How should leading/trailing
  spaces, multiple consecutive spaces, or a space mid-number behave? None are in
  the test set, so the current behaviour is a guess.

## 4. Numbers greater than 26

Large numbers are additive z-runs: `zz` = 52, `zza` = 53, `zd` = 30.

- **Q:** Confirm the encoding is purely additive, not positional/base-26. Is there
  a maximum legal value, and what should a trailing `z` with no terminator
  (a string ending in `z`) produce?

## 5. Truncated / under-length packages

`zza…` declares a count of 53 but the string is shorter, and the test expects
`[26]`. I silently treat the missing values as `0`.

- **Q:** Is zero-padding a truncated package desired, or should an input that
  promises more values than it provides be rejected as malformed? In a live feed,
  silent padding can mask corrupted packets.

## 6. Character set

Only `a`–`z`, `_` and space appear in the tests; everything non-alphabetic is
valued `0`.

- **Q:** What is the full legal alphabet? How should uppercase letters, digits or
  other punctuation be handled — coerce to `0`, ignore, or raise?

## Cases that look contradictory, and proposed production behaviour

| Cases | Tension | Proposed rule |
|-------|---------|---------------|
| `__` → `[0]` vs `_ _` → `[0, 0]` | Identical but for a space | Make the space-as-separator rule explicit and documented, not inferred. |
| `_ad` → `[0]` vs `aab___` → `[1, 0, 0]` | `_` sometimes stops parsing, sometimes is a plain `0` | Define `_` formally as "null measurement" with one consistent rule for value vs. count position. |
| `zza…` → `[26]` (count 53, short input) | Declared length exceeds actual | Decide explicitly between "zero-pad" (current) and "reject malformed". |

For a real data feed I would recommend: an explicit documented grammar; a strict
mode that rejects truncated or out-of-alphabet packages instead of silently
emitting zeros; and a single unambiguous definition of `_`. The decoder reproduces
every supplied example today, but the items above should be confirmed before it
processes live measurements.
