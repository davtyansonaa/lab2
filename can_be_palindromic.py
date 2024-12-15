def can_be(str1):
  can_be=0
  map={i:str1.count(i) for i in str1}
  for count in map.values():
    if count%2!=0:
      can_be+=1
      if can_be>1:
        return False
  return True
print(can_be(text))
