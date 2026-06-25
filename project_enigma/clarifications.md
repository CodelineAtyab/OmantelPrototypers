# Interrogation: Clarification Questions

## Overview

After reviewing the client note and the test cases, I found several areas where the encoding rules are unclear or incomplete. These are the clarification questions I would ask the client before using this decoder in a production environment.

## Questions About Measurement Cycles

1. Should every measurement cycle start with a count value?

2. Should the count tell the decoder how many following measurement values to read?

3. Should the output contain the sum of each cycle, or should it contain the individual decoded values?

4. Are count values encoded using the same rules as normal measurement values?

5. What should happen if the count says to read more values than are available before the string ends?

Recommended production behavior: incomplete cycles should raise a clear validation error or be handled using a documented rule, rather than being silently accepted.

## Questions About Letter Encoding

6. Can we confirm that `a` through `z` always represent values 1 through 26?

7. Are uppercase letters allowed, or should the decoder only accept lowercase letters?

8. If uppercase letters are provided, should they be converted to lowercase or treated as invalid characters?

Recommended production behavior: the accepted character set should be clearly defined. For example, only lowercase `a-z` should be valid unless uppercase support is explicitly required.

## Questions About `z` Sequences

9. Should `z` always represent 26?

10. When a value starts with `z`, should the decoder continue adding 26 for every following `z`?

11. Should the first non-`z` character after a `z` sequence terminate the encoded number?

12. Should examples like the following be considered correct?

* `za` = 27
* `zd` = 30
* `zza` = 53

13. What should happen if a `z` sequence reaches the end of the string without a terminating character?

Recommended production behavior: the `z` sequence rule should be clearly documented. A standalone `z` should either be accepted as 26 or rejected as incomplete, depending on the intended format.

## Questions About Invalid Characters

14. Should invalid characters such as `_`, spaces, numbers, or symbols be accepted?

15. Should `_` always decode to 0?

16. Should invalid characters behave differently depending on whether they appear as a count or as a measurement value?

17. If an invalid character appears where a measurement value is expected, should it count as one value with a value of 0?

18. If an invalid character appears where a count is expected, should the whole segment be treated as corrupted?

Recommended production behavior: invalid characters should either always raise a validation error or always be handled using one consistent rule.

## Questions About Spaces

19. Should spaces be treated as separators?

20. Should a string containing only spaces return `[0]`, or should it return `[]`?

21. Should spaces inside an encoded string be ignored, treated as invalid values, or used to split the input into separate segments?

Recommended production behavior: spaces should be clearly defined as either separators or invalid characters.

## Ambiguous or Contradictory Test Case Behavior

Some test cases suggest that invalid characters behave differently depending on their position.

For example:

* `a_` returns `[0]`, which suggests `_` can act as a measurement value worth 0.
* `_ad` returns `[0]`, which suggests that if `_` appears where a count is expected, the full segment is corrupted.
* `_ _` returns `[0, 0]`, which suggests spaces can separate corrupted segments.
* `""` returns `[]`, but a string with spaces may return `[0]`, meaning empty input and whitespace input are treated differently.

These behaviors are possible to implement, but they should be confirmed because they are not fully explained in the client note.

## Proposed Production Rules

For a production version of this decoder, I would suggest the following clear rules:

1. Each cycle starts with an encoded count.
2. The count determines how many following measurement values to read.
3. The output for each cycle is the sum of those measurement values.
4. Valid letters are lowercase `a-z`, where `a = 1` and `z = 26`.
5. Numbers greater than 26 are encoded using `z` sequences.
6. Invalid characters should either be rejected with a clear error or consistently decoded as 0.
7. Spaces should either be officially supported as separators or rejected.
8. Incomplete cycles should not be silently accepted unless the client confirms that partial decoding is allowed.

## Final Clarification Needed

Before deployment, I would ask the client to confirm whether this decoder should be forgiving and return partial results, or strict and raise errors when the input does not fully match the expected format.
