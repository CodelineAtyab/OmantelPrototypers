# Clarification Questions for Acme Metrics Corp

## 1. What exactly does `_` mean?
Our assumption: `_` = 0. As a header it terminates immediately.
As a value it contributes 0. Please confirm.

## 2. What about characters outside `a-z` and `_`?
Our assumption: treat them as 0. Should they raise an error instead?

## 3. What if a header promises more values than exist in the string?
Our assumption: sum what is available, no error raised.
Should this be treated as malformed input?

## 4. Can multiple consecutive spaces appear?
Our assumption: each space creates a new segment boundary.
Double spaces would create an empty segment contributing nothing.

## 5. Is there a maximum number size?
Our assumption: unlimited `z` chaining is valid.
Is there a practical upper limit?