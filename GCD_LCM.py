# GCD and LCM of two numbers

def GCD(x,y):

  while x%y != 0:
    rem = x%y
    x = y
    y = rem
  return y

def LCM(x,y):
  return x*y / GCD(x,y)
