def checkSelfDescribing(number):
  number = str(number)
  counts = {}
  for num in number:
    counts[num] = counts.get(num, 0) + 1
  print(counts)

  for pos in range(len(number)):
    if int(number[pos]) > len(number):
      return 0
    if str(pos) in counts:
      if number[pos] != str(counts[str(pos)]):
        return 0
    elif str(pos) not in counts:
      if number[pos] != '0':
        return 0
  return 1

ans = checkSelfDescribing(521001000)
print(ans)
