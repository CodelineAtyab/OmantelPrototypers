# Clarification Questions for Acme Metrics Corp

## Q1 — What does _ mean as a count, exactly?

When _ appears as a group count (value = 0), we emit 0 and discard the rest of the segment.
This means _ad and _zzzb both produce [0], not [0, 4] or [0, 80].

Question: Is this intentional — does a _ count mean "null/empty measurement, ignore remainder of packet"?
Or should the trailing characters be decoded as further groups?

Why it matters: If _ simply means count = 0 (emit 0, continue), then "__" should be [0, 0],
contradicting the test case. The only consistent interpretation is that _ as a count terminates the segment.

---

## Q2 — Is space the only inter-segment separator?

Question:
- Are other whitespace characters (tab, newline) also delimiters?
- Can segments be separated by multiple consecutive spaces?
- Are there any other delimiter characters beyond space?

---

## Q3 — What happens when count exceeds remaining characters?

For a count of 5 but only 2 value-characters remaining, we currently sum what is available and treat missing values as 0.

Question: Should an undersupplied group raise an error, return a partial sum, or silently pad with 0?

---

## Q4 — Are characters outside a-z, _ and space valid?

The spec only defines a-z, _ and space. The current implementation treats any other character as 0.

Question: Should unexpected characters like digits, punctuation or uppercase raise an error or be treated as 0?

---

## Potential Contradiction in the Test Suite

The requirements table lists ("_ad", [0]) and ("_zzzb", [0]), but the Python main block
shows ("ad", [0]) and ("zzzb", [0]) without the leading underscore. These would require different logic.

Request: Please confirm which version is authoritative — the requirements table or the main block.