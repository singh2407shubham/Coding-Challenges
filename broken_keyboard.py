def brokenKeyboard(string, letters):
  
  avaialable = set()
  for char in letters:
    if char not in avaialable:
      avaialable.add(char)  
  
  string = string.split()
  count = 0

  for word in string:
    present = True
    for char in word:
      if char.lower() not in avaialable and ord(char.lower())>= ord('a') and ord(char.lower())<= ord('z'):
        present = False
        break
    if present: count += 1

  return count


string = "3 + 2 = 5"
letters = []

ans = brokenKeyboard(string, letters)
print(ans)
