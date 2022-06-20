import random
letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols=['@','#','$','&','*','^']
numbers=['1','2','3','4','5','6','7','8','9']
a=int(input("Enter the number of letters you want in your password : "))
b=int(input("Enter the numbet of symbols : "))
c=int(input("Enter the number of numbers : "))
password=[]
for char in range(1,a+1):
  password+=random.choice(letters)
for sym in  range(1,b+1):
  password+=random.choice(symbols)
for num in range(1,c+1):
  password+=random.choice(numbers)
print(password)

random.shuffle(password)
print(password)
final=""
for char in password:
   final+=char
print(final)