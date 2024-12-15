def binary_search(arr,x):
  l,r=0,len(arr)-1
  while l<=r:
    mid =(r+l)//2
    if x>arr[mid]:
      l=mid+1
    elif x<arr[mid]:
      r=mid-1
    else:
      return mid
  return -1

array=[1,2,3,4,5,6,7,8]
x=7
print(binary_search(array,x))
