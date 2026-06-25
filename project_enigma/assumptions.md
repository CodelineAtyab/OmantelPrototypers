Detective's Log — Hidden Rules

Core Encoding Model

The string encodes a sequence of measurement groups. Each group is:

[count_number] [value_number × count]


count_number — how many value-numbers follow in this group.
The count value-numbers are each decoded and summed to produce one integer in the output list.


Number Encoding

A number is read character by character from a stream:


'z' → add 26 to an accumulator; continue reading (multi-char sequence).
Any non-'z' character → add its alphabetical value (a=1 … y=25, z=26) and stop.
'_' → contributes 0 and terminates accumulation.


This is consistent with the spec note: "terminated with the first non-z character following a sequence of multiple characters." A single non-z character is both the sole contribution and the terminator.

The _ (Underscore) Character

_ behaves differently depending on its position:

As a value (inside a group being summed)

_ = 0. It terminates any preceding z-accumulation and adds nothing. Example: z_ = 26 + 0 = 26.

As a count (first number of a new group)

_ = 0, so count = 0. Special rule: when count is 0, the decoder emits a 0-measurement immediately and abandons the rest of the current segment. This is the only way count = 0 is reachable (no other character encodes 0).

This rule explains:


"_" → [0] — count=0, emit 0, nothing left.
"__" → [0] — count=0, emit 0, second _ is abandoned.
"_ad" → [0] — count=0, emit 0, "ad" abandoned.
"_zzzb" → [0] — count=0, emit 0, "zzzb" abandoned.


Space as a Segment Separator

A space character splits the string into independent segments. Each segment is decoded as a self-contained stream; results are concatenated.


"_ _" → ["_", "_"] → [0] + [0] = [0, 0]
"" → [] (no segments, no output)


Implied Rules Not Stated in the Spec

RuleEvidenceValues within a group are summed (not listed individually)"aa" → [1], not [1, 1]_ in count position aborts the segment"__" → [0], not [0, 0]Space is a segment delimiter"_ _" → [0, 0]If count exceeds remaining chars, missing values default to 0"a_" (count=1, one _ value=0) → [0]Empty string → empty list"" → []