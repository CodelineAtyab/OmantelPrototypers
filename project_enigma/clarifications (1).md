# Clarifications (clarifications.md)

## Questions for Client

1. What is the exact rule for grouping characters into numbers?
2. How should repeated characters like 'aa' be handled?
3. What defines sequence termination exactly?
4. How should underscores be interpreted?
5. Should small segments after '_' be ignored always?
6. What is the rule behind large sequence compression?

## Observations
- Some outputs contradict simple addition.
- Patterns like 'aazzaaa' and 'za...azaaa' require special interpretation.

## Suggestions
- Provide formal grammar
- Define underscore behavior clearly
- Add more test cases with explanation

## Conclusion
Clearer specifications will improve consistency and maintainability.
