def ternary_search(arr,key):
  l,r=0,len(arr)-1

  while l<=r:
    m1 = l + (r - l) // 3
    m2 = r - (r - l) // 3
    if key>arr[m1] and key<arr[m2]:
      l=m1+1
      r=m2-1
    elif key<arr[m1]:
      r=m1-1
    elif key>arr[m2]:
      l=m2+1
    elif key==arr[m1]:
      return m1
    else:
      return m2
  return -1

nums=[-1,9,11,20,34,67,87]
target=67
print(ternary_search(nums,target))
