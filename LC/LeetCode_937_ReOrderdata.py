def solution(logs):
  def customSort(s):
    left, right = s.split(" ", 1)

    if right[0].isalpha():
      return (0, right, left)
    else:
      return (1, None, None)

  return sorted(logs, key=customSort)

print(solution(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]))

'''
The log.split(" ", 1) means to only at most one time, from left to right, upon encountering a white-space character, split the string into two strings and store the two strings in a list.

Then we look at the second string, or the right_side in this case of "8 1 5 1", we can see that the first character of 8, which is from right_side[0] is not an alpha character, with .isalpha() only returning true when a character is any lowercase or uppercase character from "a-z".

For a log like "let1 art can", right_side[0].isalpha() would be applied to the letter 'a' in this case, and would return true.

What we are returning from this function informs the sorted() function how sorted() ought to behave. The return of (0, right_side, left_side) tells sorted() to sort this entire log with a priority of 0, which is lower in value than 1, so any log with a right_side that begins with a letter will come before any log with a right_side that begins with a number.

After ensuring that the logs with letters in the right_side come first, the letter logs are further sorted alpha-numerically by the contents of their entire right side, then if the right_sides still match, they are sorted even further based on the contents of their left_sides, alpha-numerically with the sorted() function.

The second return statement is missing instructions on how to be sorted with only (1,) passed into it, missing the second argument. The logs with digits in their right_side only know that they must come after the letter logs, and they do not sort because they have no rule to sort by in the second argument.

We have to write it as (1, ) because this is a tuple, I think of it as just (1), but we cannot write (1) because Python would think of it as just 1, rather than as a tuple with one element. We are specifying the sorting rules for the sort algorithm by returning tuples.

The logs are then sorted() with the sorting logic provided by sorting_algorithm. The key in sorted() is an optional argument that allows us to attach our own custom function to override the default sorting behaviour.

The built in sorting algorithm is used, which is TimSort in Python, most relevant sorting algorithms including this one provide a worst case run time of O(nlog(n)) and a space of O(n).

'''