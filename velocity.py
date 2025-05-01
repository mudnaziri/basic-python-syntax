
while True:
 print("__Welcome to the Velocity Calculator__")
 print("1.if you know value of velocity: ")
 print("2.if you know value of distance: ")
 print("3.if you know value of time: ")
 print("4.Exit program")
 choice = input("Enter your choice: ")
 if choice == "1":
    d = int(input("Enter value of distance in KM: "))
    t = int(input("Enter value of time in sec: "))
    if t == 0:
       print("can't divide with zero!!")
    else:
       v = d / t
       print(v)
 if choice =="2":
    v = int(input("Enter value of velocity in M/S: "))
    t = int(input("Enter value of time in sec: "))
    d = v * t
    print(d)
 if choice == "3":
    d = int(input("Enter value of distance in KM: "))
    v = int(input("Enter value of velocity in M/S: "))
    t = d / v
    print(t)
 if choice == "4":
    print("Exiting program. Goodbye!")
 break

while True:
 print("__Welcome to the Velocity Calculator__")
 print("1.if you know value of velocity: ")
 print("2.if you know value of distance: ")
 print("3.if you know value of time: ")
 print("4.Exit program")
 choice = input("Enter your choice: ")
 if choice == "1":
    d = int(input("Enter value of distance in KM: "))
    t = int(input("Enter value of time in sec: "))
    if t == 0:
       print("can't divide with zero!!")
    else:
       v = d / t
       print(v)
 if choice =="2":
    v = int(input("Enter value of velocity in M/S: "))
    t = int(input("Enter value of time in sec: "))
    d = v * t
    print(d)
 if choice == "3":
    d = int(input("Enter value of distance in KM: "))
    v = int(input("Enter value of velocity in M/S: "))
    t = d / v
    print(t)
 if choice == "4":
    print("Exiting program. Goodbye!")
 break

while True:
   print('__Welcome to the current Calculator__')
   print('1.if you know value of current: ')
   print('2.if you know value of charge: ')
   print('3.if you know value of time: ')
   print('4.Exit program')
   choice = input('Enter your choice: ')
   if choice == "1":
      q = int(input('Enter value of charge in coulomb: '))
      t = int(input('Enter value of time in sec: '))
      if t == 0:
         print("can't divide with zero!!")
      else:
         i = q / t
         print(i)
      if choice =="2":
         i = int(input("Enter value of current in ampere: "))
         t = int(input("Enter value of time in sec: "))
         q = i * t  
         print(q)
      if choice =="3":
         q= int(input("Enter value of charge in coulomb: "))
         i = int(input("Enter value of current in ampere: "))   
         t = q / i
         print(t)
      if choice == "4":
          print("Exiting program. Goodbye!")
          break
          


    

