$$ The function signature only said "decode an encoded string into a list of integers," with no spec for what the encoding actually was. I worked backward from test cases to recover the rules, and it turned out to be a layered scheme:

$$Letter values. a through z map to 1–26 (case-insensitive). Anything outside that range — digits, punctuation, underscores, spaces — has no letter value on its own.
Lead-character-as-counter. The first character of a segment isn't just data — it's an instruction. Its value tells you how many subsequent "numbers" to read and sum into a single output value. So "bcc" (b=2) means "sum the next 2 numbers," giving c+c = 3+3 = 6.
The "z-extension" for numbers above 26. Since a single letter can only encode up to 26, a run of consecutive z characters extends the value: each z in the run contributes 26, and the run is closed off by the next character, whose own value is added on top. So z + z + a = 26 + 26 + 1 = 53. This also means a "number" in this scheme isn't always one character — it can span several, and I had to treat "read one number" as its own sub-routine rather than just indexing one character at a time.

How I handled undefined/edge characters

Underscores and other non a-z characters get a value of 0 — they're valid characters in the encoding, not garbage to filter out. But critically, if a character with value 0 shows up as a lead character (i.e., it's expected to act as a counter), I treat that as a termination signal: the function appends a 0 to the result and stops processing the rest of that segment. I inferred this because test cases showed trailing data after a 0-lead being silently ignored rather than producing an error or partial result.
Zero values inside a chunk being summed (as opposed to in the lead position) behave normally — they just contribute 0 to the sum and processing continues. So there's a meaningful difference between "0 in a counting position" (stop) and "0 in a summed position" (just adds nothing).

How I handled sequence/segment boundaries

Whitespace acts as a hard segment separator. The input can contain multiple space-separated chunks, and each one is decoded completely independently, with its own fresh start (and its own potential 0-lead termination). The results from each chunk get concatenated into one flat list. I confirmed this because a lone "_" decodes to [0], but "_ _" (two space-separated segments) decodes to [0, 0] rather than stopping after the first underscore — so spaces reset the parser, while other non-letter characters (like underscores) do not.

Open question I flagged rather than guessed at
What happens if a run of z characters hits the end of a segment with no terminating character after it (e.g., a token that's just "zz")? I didn't have a test case to pin this down, so I made an assumption (treat it as 26 * count, with nothing added) and noted it explicitly as an assumption rather than silently picking a behavior.
