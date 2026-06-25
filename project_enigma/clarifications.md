# The Interrogation — clarifications.md
Welcome back from the Himalayas! A few questions so the production decoder
behaves correctly on real traffic rather than just the sample set.
## 1. Output semantics: is the per-cycle sum intended?
The tests only pass if each output integer is the sum of the values in a
cycle (e.g. abbcc -> [2, 6] where 6 = c + c). Can you confirm the output
should be cycle sums, and not the raw list of individual values? If individual
values are ever needed, we'd want a separate flag or function.
## 2. The underscore _ — value vs. terminator
We inferred two roles for _:
- as a value, it counts as 0 in the cycle sum;
- as a count, it ends the whole string and emits a single 0.
Is that intentional? Specifically, should _ad really discard the trailing ad
(current behaviour, giving [0]), or should decoding resume after the _? This is
the biggest production risk: silently dropping data.
## 3. Spaces: separator or value?
We treat a space as a separator between independent strings (_ _ -> [0, 0]).
Is that correct, or should a space be an ordinary 0 value within one string?
## 4. Distinguishing 26 from a "continue"
Because z always means "+26 and continue", the only way to encode a value of
exactly 26 is z followed by a zero-terminator such as z_ (= 26). Is z_ the
canonical encoding for 26? And can a trailing z with no terminator legitimately
appear?
## 5. Malformed / truncated cycles
If a cycle declares a count of 5 but the string ends after 2 values, should we
(a) emit the partial sum (current behaviour), (b) emit 0, or (c) raise an error?
## 6. Character set beyond a-z, _, and space
What is the full set of legal characters? Should uppercase, digits, or other
symbols be (a) treated as 0 like _, (b) rejected with an error, or (c) ignored?
## Scenarios that look contradictory in the current test set
- _ad -> [0] (data after _ dropped) vs. aab___ -> [1, 0, 0] (_ as a value kept).
- __ -> [0] vs. _ _ -> [0, 0] (only consistent if space is a separator).
For production we'd recommend making these rules explicit in the spec and,
ideally, rejecting truly malformed input loudly rather than silently producing 0.