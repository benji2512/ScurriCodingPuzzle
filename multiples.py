def multiples_three_and_five(start: int, finish: int):
  """
  Print a range of numbers(end inclusive) and replace multiples of 3 with the word Three, replace multiples of 5 with the word Five
  and replace the multiples of 3 and 5 with the word ThreeFive
  All arguments must be integers.
  :param start: The starting number in the range.
  :param finish: The last number in the range.
  """
  for i in range(start,finish+1): # +1 added to finish variable to include 100 as end range is exclusive
    if i % 3 == 0 and i % 5 == 0:
      print("ThreeFive")
    elif i % 3 == 0:
      print("Three")
    elif i % 5 == 0:
      print("Five")
    else:
      print(i)

if __name__ == "__main__":
  multiples_three_and_five(1,100)
