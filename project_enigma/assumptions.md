# Assumptions

## Overview

The provided specification was incomplete and some behaviors were only discoverable through the supplied test cases. The following assumptions were made while implementing the decoder.

## Hidden Rules Identified

1. Letters `a` to `z` represent values from 1 to 26.

   - `a = 1`
   - `b = 2`
   -  ...
   - `z = 26`

2. The first decoded value in a package represents the number of measurements that follow.

3. Values greater than 26 may be represented using multiple characters and must be combined according to the patterns observed in the examples.

4. The underscore character (`_`) is treated as a zero-value measurement.

5. Consecutive underscores represent multiple zero values.

6. Spaces are treated as separators and do not contribute to the numeric value.

7. When insufficient measurement values exist for a declared count, decoding stops and only fully decoded results are returned.

8. Special encoding patterns were inferred from the provided examples when the written requirements were ambiguous.

## Edge Case Handling

- Empty strings return an empty list.
- Standalone underscores return zero values.
- Invalid or incomplete measurement groups terminate processing safely.
- Spaces between zero-value markers are ignored during decoding.

## Limitations

The official encoding specification is incomplete. Some behaviors were derived from the supplied test cases and may require confirmation before being used in a production environment.
