def longest(str1):
  res = ""
  res_len=0
  if len(str1) < 1:
      return ""
  for i in range(len(str1)):
    #odd nums
    l,r=i,i
    while l>=0 and r<len(str1) and str1[l]==str1[r]:
      if(r-l+1>res_len):
        res=str1[l:r+1]
        res_len=r-l+1
      l-=1
      r+=1
    #even
    l,r=i,i+1
    while l>=0 and r<len(str1) and str1[l]==str1[r]:
      if(r-l+1>res_len):
        res=str1[l:r+1]
        res_len=r-l+1
      l-=1
      r+=1
  return res

text1="annawhohtetheapple"

print(longest(text1))
