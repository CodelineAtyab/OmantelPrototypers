# The Interrogation — `clarifications.md`

The current implementation passes all provided test cases, but several rules
were inferred from a single example each, and a few cases look contradictory.
Below are the questions I'd put to the original engineer, grouped by risk.

## A. Contradictions in the existing test cases

1. **Does a `0` count terminate the whole package, or just emit a zero and
   continue?**
   - `("_ad", [0])` and `("__", [0])` imply that a `0` count **stops** decoding
     entirely — the trailing `ad` / `_` are discarded.
   - But `("aab___", [1, 0, 0])` shows decoding *continuing* through underscores
     when they sit in a **value** position (the `b`=2 count consumes `__`),
     before a final `0` count closes it out.
   - I resolved this as "**`0` in the count position terminates**; `0` in a value
     position is just a zero." Is that the intended distinction, or should a
     malformed/zero count instead be skipped, or raise an error?

2. **Is a space a package separator, or a value?**
   - `("_ _", [0, 0])` only works if space splits the stream into two packages.
     Yet the note never mentions spaces or multiple packages in one string.
   - Confirm: can a single input legitimately contain **multiple packages**
     separated by spaces? Are other separators (newline, comma) also valid?
     Should leading/trailing/double spaces produce empty packages?

3. **What is the count actually counting — characters or numbers?**
   - With single-letter values these are indistinguishable, but case 3 proves it
     counts **numbers** (so `zza` counts as *one* item worth 53, not three).
   - Please confirm the count is "number of measured *values* in the cycle,"
     each value being a full z-accumulated number.

## B. Underspecified behaviour (inferred from one example)

4. **Undefined characters.** I map `_`, space, and anything outside `a–z` to
   `0`. Is `0` the correct sentinel, or should unknown bytes be rejected as
   corrupt data? Are there other meaningful symbols (digits, uppercase) the
   real feed can contain?

5. **A `z`-run with no terminator** (e.g. a value ending in `...zz`). The note
   says a number ends at "the first non-`z` character," but gives no rule when
   the stream ends first. I currently take the accumulated `26 × n`. Should a
   dangling `z`-run instead be an error, or be ignored?

6. **Count larger than the remaining numbers.** If a cycle declares a count of
   5 but only 2 numbers remain, I sum the 2 available and stop. Should this
   instead be flagged as a truncated/invalid package?

7. **Is there an upper bound on a value or a count?** z-accumulation makes both
   unbounded (`zzzz...` keeps adding 26). Real measurement hardware presumably
   has a max range — should we validate against it?

## C. Production-hardening questions

8. **Error strategy.** For a production decoder, do you want lenient behaviour
   (best-effort decode, as now) or strict validation that raises on anything
   that doesn't match the grammar? Lenient decoding can silently mask corrupt
   telemetry.

9. **Empty vs. zero.** `("", [])` returns an empty list while `("_", [0])`
   returns `[0]`. Is "no measurements" (`[]`) semantically different from "one
   measurement of zero" (`[0]`) downstream? This matters for averaging/billing.

10. **Round-trip / encoder.** Is there a matching *encoder*, and must
    `decode(encode(x)) == x`? If so, the ambiguous cases above (zero counts,
    spaces) need a single canonical encoding so the round-trip is stable.

11. **Character set & encoding.** Is the input guaranteed ASCII lowercase, or
    could it arrive as Unicode / different case / a byte stream? Confirm so we
    can validate input at the boundary.

## Recommended production defaults (pending answers)

Until the above are confirmed, I'd propose treating a malformed package
(unterminated `z`-run, count exceeding available numbers, unexpected symbol) as
a **validation error** surfaced to the caller rather than silently coerced — so
corrupt telemetry is caught, not averaged into the metrics.
