"""It's an infinite dice roller"""
import random
while True:
  a=input("")
  if a=="":
      b=random.randint(1,6)
  print("⚪"*b)
  print(b)