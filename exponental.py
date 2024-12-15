def binary(arr, key, low, high):
  while low<=high:
    mid = (low+high)//2
    if arr[mid]==key:
      return mid
    elif arr[mid]>key:
      high=mid-1
    else:
      low=mid+1
  return -1

def exponental(arr,key):
  index = 1

  if arr[0]==key:
    return 0
  n=len(arr)
  while index<n and arr[index]<key:
    index*=2

  return binary(arr, key, int(index/2), index)


arr=[1,2,5,8,10,34,67,89,112,432,521,553,678]
key=521
print(exponental(arr, key))
