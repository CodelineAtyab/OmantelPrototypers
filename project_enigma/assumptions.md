# Detective's Log: Assumptions

* **Every Cycle Has a Count:** Each measurement cycle begins with a number that tells the decoder how many values follow it.
* **Summing values:** The output is not the raw numbers, but the total sum of all values inside that cycle.
* **Letters to Numbers:** 'a' through 'y' match positions 1 to 25. 
* **The 'z' Accumulator:** 'z' accumulates blocks of 26 until a non-z character finishes the number.
* **Zeros:** Underscores (`_`) and spaces (` `) represent 0.