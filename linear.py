def linear_search(arr, x):
  for i in range(len(arr)):
    if arr[i]==x:
      return i
    else:
      print("No match Found")

