from math import sqrt

def jump_search(arr, key):
  prev=-1
  n=len(arr)
  m=int(sqrt(n))
  ind=-1
  while ind<(n-1):
    ind=min(prev+m,(n-1))
    if arr[ind]==key:
      return ind
    elif arr[ind]>key:
      break
    else:
      prev=ind

  for i in range(prev,min(ind,n)):
    if arr[i]==key:
      return i
  return -1

nums=[1,3,5,8,45,233,899,1000]
x=45

print(jump_search(nums, x))
