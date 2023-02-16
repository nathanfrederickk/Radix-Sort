# Radix-Sort
Given data of matches between two teams with their scores, the analyze function can sort the data and take the top 10 matches (according to scores) with radix sort and remove all the duplicates. The analyze function can also find the matches with the target score using a modified binary search. For example the input can be a table of matches and their score:

```
# a roster of 2 characters
roster = 2

# results with 20 matches
results =
[['AAB', 'AAB', 35], ['AAB', 'BBA', 49], ['BAB', 'BAB', 42],
['AAA', 'AAA', 38], ['BAB', 'BAB', 36], ['BAB', 'BAB', 36],
['ABA', 'BBA', 57], ['BBB', 'BBA', 32], ['BBA', 'BBB', 49],
['BBA', 'ABB', 55], ['AAB', 'AAA', 58], ['ABA', 'AAA', 46],
['ABA', 'ABB', 44], ['BBB', 'BAB', 32], ['AAA', 'AAB', 36],
['ABA', 'BBB', 48], ['BBB', 'ABA', 33], ['AAB', 'BBA', 30],
['ABB', 'BBB', 68], ['BAB', 'BBB', 52]]

# looking for a score of 64
score = 64
```

After all the parameter of the function analyze is fulfilled, we can do:
```
# running the function
analyze(results, roster, score)

# the following is returned for [top10matches, searchedmatches]
[[['ABB', 'AAB', 70],
['ABB', 'BBB', 68],
['AAB', 'BBB', 67],
['AAB', 'AAB', 65],
['AAB', 'AAA', 64],
['ABB', 'ABB', 64],
['AAA', 'AAA', 62],
['AAB', 'AAA', 58],
['ABB', 'ABB', 58],
['AAB', 'ABB', 57]],
[['AAB', 'AAA', 64], ['ABB', 'ABB', 64]]]
```
