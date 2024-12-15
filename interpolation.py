def interpolation(num,x):
  n=len(num)
  hi=n-1
  lo=0

  while lo<=hi and num[lo] <= x <= num[hi]:
    pos = int(lo+((x-num[lo])*(hi-lo))/(num[hi]-num[lo]))
    if x==num[pos]:
      return pos
    elif x>num[pos]:
      lo=pos+1
    else:
      hi=pos-1
  return -1


num=[1,3,5,7,10,15,18,21,25]
x=21

print(interpolation(num,x))
