# The Interrogation — clarifications.md
## Clarification Questions for the Client (Acme Metrics Corp)

Hello,

Welcome back! While you were away, I built the decoder and got all 17 test cases passing. However, I had to make several assumptions to fill in the gaps in the specification. I'd like to confirm these with you before we move to production.

---

### Question 1: Does z-encoding apply to VALUES as well as counts?

Your note only mentions that "numbers higher than 26 are encoded with multiple characters." It is clear this applies to the COUNT field. However, the test cases show it also applies to individual measured values inside a package.

**Example:** `dz_a_aazzaaa` → [28, 53, 1]
The value `53` can only be decoded if `zza` (inside the values section) is treated as a z-encoded number = 26+26+1 = 53.

**My assumption:** Yes, values use z-encoding too.
**Please confirm:** Is this always the case, or can values ever be plain single characters only?

---

### Question 2: What does the underscore `_` mean — and is it an official part of the format?

The client's note makes no mention of `_` at all, yet it appears in many test cases. I reverse-engineered the following rules:

- `_` as a standalone value = 0
- `_` as a z-encoding terminator (e.g. `z_`) = adds 0 to the sum (so `z_` = 26)
- `_` at the start of a package = empty package (sum = 0)

**Please confirm:** Is `_` an officially supported character in the encoding format, or is it a "corrupt/missing" data marker? Should it always mean 0?

---

### Question 3: The behavior of `_` at the start of a package seems inconsistent — can you clarify?

This is the most confusing part of the test cases. Consider:

| Input | Expected Output | Observation |
|-------|----------------|-------------|
| `__` | `[0]` | Only ONE zero returned, second `_` is ignored |
| `_ _` | `[0, 0]` | TWO zeros returned when separated by a space |
| `_ad` | `[0]` | `ad` after the `_` is completely discarded |
| `aab___` | `[1, 0, 0]` | Here `__` produces TWO zeros (they are values inside a `b=2` count package) |

**The contradiction:** `__` alone produces `[0]`, but `__` after `aab` produces `[0, 0]`. The meaning of `__` changes depending on context.

**My assumption:** When `_` starts a package, it signals "empty package = 0" AND discards all remaining characters until the next space. This is why `__` = `[0]` (second `_` discarded) but `_ _` = `[0, 0]` (space saves the second one).

**My proposed production rule:** A leading `_` in a space-separated token = one zero package, rest of token discarded. Is this correct, or should `__` always mean `[0, 0]`?

---

### Question 4: What should happen with completely unknown/invalid characters?

The test cases only show letters `a–z`, underscores `_`, and spaces. What should the function do if it encounters something else (e.g. numbers, punctuation, uppercase letters)?

**My proposed production rule:** Ignore/skip unknown characters. Please confirm.

---

### Question 5: Is there a maximum package count or value size?

The current test cases go up to values like 53. In production, could counts or values be extremely large (e.g. thousands of z's)? The current implementation handles any size, but confirming this helps with performance planning.

---

### Question 6: Can a package have count = 0 explicitly (not via `_`)?

For example, if the input is just `a` with no values following — count = 1 but no value characters exist. My current implementation returns `0` for this (the loop breaks early). Is that the intended behavior?

---

Thank you for your time. Once these are confirmed, I can update the specification document and finalize the production-ready version.

Best regards,
Renad
