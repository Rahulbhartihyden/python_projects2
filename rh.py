import random
cpu_num=random.randint(1,100)
player_num=int(input("Enter the numbers between 1-100: "))

while player_num != cpu_num:
    if cpu_num > player_num:
         print("Too High!")
         break
    else:
        print("Too low")
        
        player_num=int(input("Enter the number between 1-100:"))
        
else:
    print("Well Done!!")
   
  
