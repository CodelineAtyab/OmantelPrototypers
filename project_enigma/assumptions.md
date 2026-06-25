"The Detective's Log — assumptions.md

The client's note describes the basic encoding ("a"–"z" = 1–26, count followed by
values, multi-character numbers above 26) but leaves several behaviors undefined.
Below are the hidden rules I had to reverse-engineer from the test cases to make
everything pass, along with the reasoning behind each one.

1. Multi-character number encoding (stated, but the termination rule needed inference)

The note says numbers above 26 are "encoded with multiple characters that are added
together," terminated by "the first non-'z' character following a sequence of
multiple characters."

In practice this means: a number is read as a run of consecutive 'z' characters
(each contributing 26), followed by exactly one terminating character that is not
'z' (whose own letter value is added in). If the very first character of the number
is already not 'z', the number is just that single character's value — there's no
"sequence" to terminate.

Example: in "dz_a_aazzaaa", the substring "zzaaa" is one number = z(26) + z(26) + a(1) = 53, because two zs started a multi-char run, terminated by the a.

I applied this same multi-character rule to both the count and the values inside
a cycle — the client's note only explicitly discusses values, but several test cases
(e.g. "zza_a_a...") only resolve correctly if the count is allowed to be a
multi-character (z-chained) number too.

2. Underscore (_) = value 0

The client's note never mentions _. Since it's not a–z, I treated it as a
defined "filler" character with value 0, rather than an error or undefined token.
This is the simplest assumption consistent with cases like "a_" → [0] (count=1,
one value follows: _ = 0) and "abcdabcdab_" → [2, 7, 7, 0] (a trailing _ forms
its own zero-count cycle, contributing a final 0).

I extended this fallback to any character outside a–z and _ (e.g. punctuation)
— defaulting to value 0 rather than raising an error, since the spec gives no
indication that unrecognized characters should halt decoding.

3. Space (' ') is a hard delimiter, not just another zero-value character

This was the least obvious rule, and the one that required the most back-and-forth
to pin down. Initially I treated space the same as any other undefined character
(value 0), but two test cases contradict that:


"__" (two underscores, no space) → [0]
"_ _" (underscore, space, underscore) → [0, 0]


If a space were just another zero-value character, both inputs should decode
identically (since _ and a generic "unknown char defaulting to 0" would behave the
same). They don't — so space must be doing something structurally different from
underscore.

Assumption: the input string is first split on literal spaces into independent
segments ("chunks"). Each chunk is decoded completely independently, and the results
are concatenated in order. The space character itself contributes nothing to the
output — it's purely a separator, like a delimiter between two unrelated measurement
packages that happened to be sent in the same string.

This makes "_ _" decode as two separate one-character chunks ("_" and "_"),
each independently producing [0], concatenated to [0, 0] — matching the expected
output.

4. A count of exactly 0 terminates the current chunk

Within a chunk, once a cycle's count resolves to 0, I treat that as a
"stop" signal: the cycle contributes a single 0 to the output, and any remaining
characters in that chunk are discarded rather than being read as a new cycle.

This was inferred from a trio of cases that only make sense together:


"_ad" → [0] (not [0, 4], even though "ad" is itself a perfectly valid
cycle — count=1, value=4)
"_zzzb" → [0] (not [0, 0], even though "zzzb" is a perfectly valid cycle)
"__" → [0] (the trailing "_" is not read as a second cycle)


In each case, the first cycle's count is 0 (from the leading _), and everything
after it within the same chunk is dropped. I generalized this to: a count of 0 is
not just "zero values to read" — it's an explicit end-of-data marker for that chunk.

Contrast this with "aab___" → [1, 0, 0], where the trailing _ is also a
0-count cycle — but since it's the last character in the chunk anyway, there's
nothing left to discard, so the rule doesn't change the outcome there.

Summary of inferred (non-stated) rules

RuleStated in client note?Inferred fromMulti-char (z-chain) numbers apply to count, not just valuesPartially"zza_a_...", "za_a_...azaaa"_ = value 0No"a_", "_"Unrecognized chars default to value 0No(extrapolated from _)Space splits the string into independent chunksNo"_ _" vs "__"Count = 0 terminates the chunk, discarding remaining charsNo"_ad", "_zzzb", "__"

These are documented as assumptions, not certainties — see clarifications.md
for the questions I'd raise with the client about whether this is the intended
behavior or an artifact of how the test data was generated."