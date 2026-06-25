# Clarification Questions

## Questions for the Client

1. What is the official meaning of the underscore (`_`) character?

   - Does it always represent a value of zero, or can it have other meanings?

2. How should values greater than 26 be encoded?

   - Should multiple letters always be summed together?
   - Are there any limits on the number of characters used?

3. What is the exact termination rule for multi-character values?

   - The specification mentions termination using the first non-`z` character, but several examples appear open to interpretation.

4. Should spaces always be ignored?

   - Are spaces formatting characters only, or do they carry semantic meaning?

5. How should invalid characters be handled?

   - Should they be ignored, generate an error, or terminate decoding?

6. What should happen if the declared measurement count is larger than the number of available measurements?

7. Are uppercase letters valid input?

8. Are there additional encoding patterns that are not represented in the provided test cases?

## Potential Contradictions

1. Some test cases suggest special handling for certain character sequences that are not explicitly described in the written requirements.

2. The specification for values greater than 26 does not fully explain how multiple-character sequences should be parsed.

3. The behavior of underscores and spaces is demonstrated by examples but is not formally defined.

## Recommendation

Before deploying this decoder in a production environment, a formal specification should be created that clearly defines:

- Encoding rules
- Termination rules
- Error handling
- Treatment of special characters
- Expected behavior for malformed input
