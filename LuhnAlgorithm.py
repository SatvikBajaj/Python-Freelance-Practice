#Conversion to list and each entry to integer
userList = list(user)
#Exception Handler used to prevent crash , a letter key was entered (non number)
try:
    for i in range(len(userList)):
        userList[i] = int(userList[i])
except: 
    print ("Invalid number ...")

#Step 1 of Luhn Algorithim (Fetch number)
luhn1 = userList 

#Step 2 of Luhn Algorithm (Reverse number)
luhn2 = []
for i in range(len(luhn1)):
    luhn2.append(luhn1[-i-1])
    
#Step 3 of Luhn Algorithm (Double every other number from the right)
luhn3 = []
for i in range(len(luhn2)):
    if i != 0 and (i%2) != 0:
        luhn3.append(2*luhn2[i])
    else:
        luhn3.append(luhn2[i])
        
#Step 4 of Luhn Algorithm (Subract 9 off each entry over 9)
luhn4 = luhn3
for i in range(len(luhn4)):
    if luhn4[i] >= 9:
        luhn4[i] -= 9
        
#Step 5 of Luhn Algorithm (Check if Sum of Number is divisble by ten)
luhn5 = luhn4
luhnSum = 0
luhnCheck = False
for i in range(len(luhn5)):
    luhnSum += luhn5[i]
if luhnSum % 10 == 0:
    luhnCheck = True
else:
    luhnCheck = False
    
#Output Answer
if luhnCheck:
    print ("I hope you didn't enter your real data because it checks out!")
else:
    print ("The number you entered is not a valid credit card number.")
    