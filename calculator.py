#Simple Calculator
import operator as math
while True:
  print("\n__wellcome to calculator__")
  print("1. Addition ")
  print("2. Subtraction ")
  print("3. Multiplication ")
  print("4. Division ")
  print("5. Exit program ") 

  choice = input("Choose an option: ") 
  if choice == "5":
    print("Exiting program. Goodbye!")
    break
  if choice in ["1", "2", "3", "4"]:
   a = int(input("Enter first number: "))
   b = int(input("Enter second number: "))
  if choice == "1":
    print(math.add(a, b))
  elif choice == "2":
    print(math.sub(a, b))
  elif choice == "3":
    print(math.mul(a,b))
  elif choice == "4":
    print(math.truediv(a,b))
  else:
    print("Invalid choice. Try again.") 

