1. Executive Summary
This document identifies ambiguities in the measurement encoding protocol identified during the development of decoder.py. These areas require clarification to ensure the system remains stable as the data input grows in complexity.

2. Technical Ambiguities
The "Termination" Boundary: Currently, a count of 0 terminates the entire parsing sequence. We must clarify if a 0 should only terminate the current cycle or the entire package.

Token Delimiters: While _ and   are handled, the behavior of other non-alphabetical characters (e.g., numbers or punctuation) is undefined. Should these be treated as errors, or ignored?

Trailing z Values: The protocol is clear on zza, but should a final z at the end of a string be treated as an error (because it is not followed by a non-z character) or as an implicit 26?



3. Contradictory Scenarios (Production Proposals)
Scenario 1: Leading/Trailing Underscores
Conflict: In _, it is a cycle of 0. In __, it returns 0.
Proposed Production Standard: Every underscore must explicitly represent a 0 value, regardless of position.

Scenario 2: Space Delimiters
Conflict: Spaces are treated as noise in _ _.
Proposed Production Standard: Spaces should be strictly defined as "structural whitespace" that cannot appear inside a multi-character number (e.g., z z should be invalid, not 52).

Scenario 3: Truncated Packages
Conflict: aab___ returns a partial cycle.
Proposed Production Standard: Implement a "Strict Mode" for production that raises a ValidationError if the total count of values provided does not match the sum of cycle counts defined in the header.


4. Future-Proofing Questions
Alphabet Limits: Should we extend the schema to support uppercase letters (A=27, B=28...)?

Data Integrity: Does the client require a checksum or parity bit at the end of each measurement cycle to detect data corruption?

Performance Scaling: If processing multi-gigabyte measurement strings, should we shift to a generator-based parsing approach (yield) to minimize memory footprint?