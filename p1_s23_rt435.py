print("Project for CS 341\n"
      "Section Number: 008\n"
      "Semester:Spring2023\n"
      "Written by: Richard Tyrrell rt435\n"
      "Instructor: Marvin Nakayama, marvin@njit.edu")

nums="1234567890"
psi="abcdefghijklmnopqrstuvwxyz"
psiNoEDU="abcfghijklmnopqrstvwxyz"
psiNoE="abcdfghijklmnopqrstuv"
#User Input
inputSTD= input("Do you want to input a string? (y/n) ")
while inputSTD== 'y':
    print("y")
    compString=input("Enter your string: ")
    print(compString)
    #Starting State q1
    currentState = "q1"
    print("State", currentState)
    #Loop for characters from input
    for char in compString:
        # state q1
        if currentState == "q1":
            if char in psi:
                currentState = "q3"
            else:
                currentState = "q2"
        #state q2 (Trap State)
        elif currentState == "q2":
            currentState = "q2"
        #state q3
        elif currentState == "q3":
            if char == "@":
                currentState = "q5"
            elif char == ".":
                currentState = "q4"
            elif char in psi or char in nums:
                currentState = "q3"
        #state q4
        elif currentState == "q4":
            if char in nums:
                currentState = "q3"
            elif char == ".":
                currentState = "q2"
            elif char == "@":
                currentState = "q2"
            elif char in psi:
                currentState = "q2"
        #state q5
        elif currentState == "q5":
            if char in nums:
                currentState = "q6"
            else:
                currentState = "q2"
        #state q6
        elif currentState == "q6":
            if char in nums or char in psi:
                currentState = "q6"
            elif char == ".":
                currentState = "q7"
            elif char == "@":
                currentState = "q2"
        #state q7
        elif currentState == "q7":
            if char == "e":
                currentState = "q8"
            elif char == ".":
                currentState = "q2"
            elif char == "@":
                currentState = "q2"
            elif char in psiNoE:
                currentState = "q6"
            elif char in nums:
                currentState = "q2"
        # state q8
        elif currentState == "q8":
            if char == "d" or char =="u":
                currentState = "q8"
            elif char == ".":
                currentState = "q7"
            elif char == "@":
                currentState = "q2"
            elif char == nums or char == psiNoEDU:
                currentState = "q6"
        #Final Output
        print("Character", char)
        print("State", currentState)
    if (currentState == "q8"):
        print("String is accepted")
    else:
        print("String is rejected")
    inputSTD = input("Do you want to input a string? (y/n) ")
print("n")
print("Project for CS 341\n"
      "Section Number: 008\n"
      "Semester:Spring2023\n"
      "Written by: Richard Tyrrell rt435\n"
      "Instructor: Marvin Nakayama, marvin@njit.edu")

nums="1234567890"
psi="abcdefghijklmnopqrstuvwxyz"
psiNoEDU="abcfghijklmnopqrstvwxyz"
psiNoE="abcdfghijklmnopqrstuv"
psiNoD="abcefghijklmopqrstuv"
psiNoU="abcdefghijklmopqrstvwxyz"

#User Input
inputSTD= input("Do you want to input a string? (y/n) ")
while inputSTD== 'y':
    print("y")
    compString=input("Enter your string: ")
    print(compString)
    #Starting State q0
    currentState = "q0"
    print("State", currentState)
    #Loop for characters from input
    for char in compString:
        # state q1
        if currentState == "q0":
            if char in psi:
                currentState = "q3"
            else:
                currentState = "q2"
        #state q2 (Trap State)
        elif currentState == "q2":
            currentState = "q2"
        #state q3
        elif currentState == "q3":
            if char == "@":
                currentState = "q5"
            elif char == ".":
                currentState = "q4"
            elif char in psi or char in nums:
                currentState = "q3"
        #state q4
        elif currentState == "q4":
            if char in nums:
                currentState = "q3"
            elif char == ".":
                currentState = "q2"
            elif char == "@":
                currentState = "q2"
            elif char in psi:
                currentState = "q2"
        #state q5
        elif currentState == "q5":
            if char in nums or psi:
                currentState = "q6"
            else:
                currentState = "q2"
        #state q6
        elif currentState == "q6":
            if char in nums or char in psi:
                currentState = "q6"
            elif char == ".":
                currentState = "q7"
            elif char == "@":
                currentState = "q2"
        #state q7
        elif currentState == "q7":
            if char == "e":
                currentState = "q8"
            elif char == ".":
                currentState = "q2"
            elif char == "@":
                currentState = "q2"
            elif char in psiNoE:
                currentState = "q6"
            elif char in nums:
                currentState = "q2"
        # state q8
        elif currentState == "q8":
            if char in psiNoD or char in psiNoU:
                currentState = "q7"
            elif char == ".":
                currentState = "q7"
            elif char == "@":
                currentState = "q2"
            elif char == nums or char == psiNoEDU:
                currentState = "q6"
        #Final Output
        print("Character", char)
        print("State", currentState)
    if (currentState == "q8"):
        print("String is accepted")
    else:
        print("String is rejected")
    inputSTD = input("Do you want to input a string? (y/n) ")
print("n")
print("Project for CS 341\n"
      "Section Number: 008\n"
      "Semester:Spring2023\n"
      "Written by: Richard Tyrrell rt435\n"
      "Instructor: Marvin Nakayama, marvin@njit.edu")

nums="1234567890"
psi="abcdefghijklmnopqrstuvwxyz"
psiNoEDU="abcfghijklmnopqrstvwxyz"
psiNoE="abcdfghijklmnopqrstuv"
psiNoD="abcefghijklmopqrstuv"
psiNoU="abcdefghijklmopqrstvwxyz"

#User Input
inputSTD= input("Do you want to input a string? (y/n) ")
while inputSTD== 'y':
    print("y")
    compString=input("Enter your string: ")
    print(compString)
    #Starting State q0
    currentState = "q0"
    print("State", currentState)
    #Loop for characters from input
    for char in compString:
        # state q1
        if currentState == "q0":
            if char in psi:
                currentState = "q3"
            else:
                currentState = "q2"
        #state q2 (Trap State)
        elif currentState == "q2":
            currentState = "q2"
        #state q3
        elif currentState == "q3":
            if char == "@":
                currentState = "q5"
            elif char == ".":
                currentState = "q4"
            elif char in psi or char in nums:
                currentState = "q3"
        #state q4
        elif currentState == "q4":
            if char in nums:
                currentState = "q3"
            elif char == ".":
                currentState = "q2"
            elif char == "@":
                currentState = "q2"
            elif char in psi:
                currentState = "q2"
        #state q5
        elif currentState == "q5":
            if char in nums or psi:
                currentState = "q6"
            else:
                currentState = "q2"
        #state q6
        elif currentState == "q6":
            if char in nums or char in psi:
                currentState = "q6"
            elif char == ".":
                currentState = "q7"
            elif char == "@":
                currentState = "q2"
        #state q7
        elif currentState == "q7":
            if char == "e":
                currentState = "q8"
            elif char == ".":
                currentState = "q2"
            elif char == "@":
                currentState = "q2"
            elif char in psiNoE:
                currentState = "q6"
            elif char in nums:
                currentState = "q2"
        # state q8
        elif currentState == "q8":
            if char in psiNoD:
                currentState = "q7"
            if char in  psiNoU:
                currentState="q7"
            elif char == ".":
                currentState = "q7"
            elif char == "@":
                currentState = "q2"
            elif char == nums or char == psiNoEDU:
                currentState = "q6"
        #Final Output
        print("Character", char)
        print("State", currentState)
    if (currentState == "q8"):
        print("String is accepted")
    else:
        print("String is rejected")
    inputSTD = input("Do you want to input a string? (y/n) ")
print("n")
print("Project for CS 341\n"
      "Section Number: 008\n"
      "Semester:Spring2023\n"
      "Written by: Richard Tyrrell rt435\n"
      "Instructor: Marvin Nakayama, marvin@njit.edu")

nums="1234567890"
psi="abcdefghijklmnopqrstuvwxyz"
psiNoEDU="abcfghijklmnopqrstvwxyz"
psiNoE="abcdfghijklmnopqrstuv"
psiNoD="abcefghijklmopqrstuv"
psiNoU="abcdefghijklmopqrstvwxyz"

#User Input
inputSTD= input("Do you want to input a string? (y/n) ")
while inputSTD== 'y':
    print("y")
    compString=input("Enter your string: ")
    print(compString)
    #Starting State q0
    currentState = "q0"
    print("State", currentState)
    #Loop for characters from input
    for char in compString:
        # state q1
        if currentState == "q0":
            if char in psi:
                currentState = "q3"
            else:
                currentState = "q2"
        #state q2 (Trap State)
        elif currentState == "q2":
            currentState = "q2"
        #state q3
        elif currentState == "q3":
            if char == "@":
                currentState = "q5"
            elif char == ".":
                currentState = "q4"
            elif char in psi or char in nums:
                currentState = "q3"
        #state q4
        elif currentState == "q4":
            if char in nums:
                currentState = "q3"
            elif char == ".":
                currentState = "q2"
            elif char == "@":
                currentState = "q2"
            elif char in psi:
                currentState = "q2"
        #state q5
        elif currentState == "q5":
            if char in nums or psi:
                currentState = "q6"
            elif char ==".":
                currentState="q2"
            else:
                currentState = "q2"
        #state q6
        elif currentState == "q6":
            if char in nums or char in psi:
                currentState = "q6"
            elif char == ".":
                currentState = "q7"
            elif char == "@":
                currentState = "q2"
        #state q7
        elif currentState == "q7":
            if char == "e" or "d":
                currentState = "q8"
            elif char == ".":
                currentState = "q2"
            elif char == "@":
                currentState = "q2"
            elif char in psiNoE:
                currentState = "q6"
            elif char in nums:
                currentState = "q2"
        # state q8
        elif currentState == "q8":
            if char in psiNoU:
                currentState="q7"
            elif char == ".":
                currentState = "q7"
            elif char == "@":
                currentState = "q2"
            elif char == nums or char == psiNoEDU:
                currentState = "q6"
        #Final Output
        print("Character", char)
        print("State", currentState)
    if (currentState == "q8"):
        print("String is accepted")
    else:
        print("String is rejected")
    inputSTD = input("Do you want to input a string? (y/n) ")
print("n")
print("Project for CS 341\n"
      "Section Number: 008\n"
      "Semester:Spring2023\n"
      "Written by: Richard Tyrrell rt435\n"
      "Instructor: Marvin Nakayama, marvin@njit.edu")

nums="1234567890"
psi="abcdefghijklmnopqrstuvwxyz"
psiNoEDU="abcfghijklmnopqrstvwxyz"
psiNoE="abcdfghijklmnopqrstuv"
psiNoD="abcefghijklmopqrstuv"
psiNoU="abcdefghijklmopqrstvwxyz"

#User Input
inputSTD= input("Do you want to input a string? (y/n) ")
while inputSTD== 'y':
    print("y")
    compString=input("Enter your string: ")
    print(compString)
    #Starting State q1
    currentState = "q1"
    print("State", currentState)
    #Loop for characters from input
    for char in compString:
        # state q1
        if currentState == "q1":
            if char in psi:
                currentState = "q3"
            else:
                currentState = "q2"
        #state q2 (Trap State)
        elif currentState == "q2":
            currentState = "q2"
        #state q3
        elif currentState == "q3":
            if char == "@":
                currentState = "q5"
            elif char == ".":
                currentState = "q4"
            elif char in psi or char in nums:
                currentState = "q3"
        #state q4
        elif currentState == "q4":
            if char in nums:
                currentState = "q3"
            elif char == ".":
                currentState = "q2"
            elif char == "@":
                currentState = "q2"
            elif char in psi:
                currentState = "q2"
        #state q5
        elif currentState == "q5":
            if char in nums or psi:
                currentState = "q6"
            elif char ==".":
                currentState="q2"
            else:
                currentState = "q2"
        #state q6
        elif currentState == "q6":
            if char in nums or char in psi:
                currentState = "q6"
            elif char == ".":
                currentState = "q7"
            elif char == "@":
                currentState = "q2"
        #state q7
        elif currentState == "q7":
            if char == "e" or "d":
                currentState = "q8"
            elif char == ".":
                currentState = "q2"
            elif char == "@":
                currentState = "q2"
            elif char in psiNoE:
                currentState = "q6"
            elif char in nums:
                currentState = "q2"
        # state q8
        elif currentState == "q8":
            if char in psiNoU:
                currentState="q7"
            elif char == ".":
                currentState = "q7"
            elif char == "@":
                currentState = "q2"
            elif char == nums or char == psiNoEDU:
                currentState = "q6"
        #Final Output
        print("Character", char)
        print("State", currentState)
    if (currentState == "q8"):
        print("String is accepted")
    else:
        print("String is rejected")
    inputSTD = input("Do you want to input a string? (y/n) ")
print("n")
print("Project for CS 341\n"
      "Section Number: 008\n"
      "Semester:Spring2023\n"
      "Written by: Richard Tyrrell rt435\n"
      "Instructor: Marvin Nakayama, marvin@njit.edu")

nums="1234567890"
psi="abcdefghijklmnopqrstuvwxyz"
psiNoEDU="abcfghijklmnopqrstvwxyz"
psiNoE="abcdfghijklmnopqrstuv"
psiNoD="abcefghijklmopqrstuv"
psiNoU="abcdefghijklmopqrstvwxyz"

#User Input
inputSTD= input("Do you want to input a string? (y/n) ")
while inputSTD== 'y':
    print("y")
    compString=input("Enter your string: ")
    print(compString)
    #Starting State q1
    currentState = "q1"
    print("State", currentState)
    #Loop for characters from input
    for char in compString:
        # state q1
        if currentState == "q1":
            if char in psi:
                currentState = "q3"
            else:
                currentState = "q2"
        #state q2 (Trap State)
        elif currentState == "q2":
            currentState = "q2"
        #state q3
        elif currentState == "q3":
            if char == "@":
                currentState = "q5"
            elif char == ".":
                currentState = "q4"
            elif char in psi or char in nums:
                currentState = "q3"
        #state q4
        elif currentState == "q4":
            if char in nums:
                currentState = "q3"
            elif char == ".":
                currentState = "q2"
            elif char == "@":
                currentState = "q2"
            elif char in psi:
                currentState = "q2"
        #state q5
        elif currentState == "q5":
            if char in nums or psi:
                currentState = "q6"
            elif char ==".":
                currentState="q2"
            else:
                currentState = "q2"
        #state q6
        elif currentState == "q6":
            if char in nums or char in psi:
                currentState = "q6"
            elif char == ".":
                currentState = "q7"
            elif char == "@":
                currentState = "q2"
        #state q7
        elif currentState == "q7":
            if char == "e" or "d":
                currentState = "q8"
            elif char == ".":
                currentState = "q2"
            elif char == "@":
                currentState = "q2"
            elif char in psiNoE:
                currentState = "q6"
            elif char in nums:
                currentState = "q2"
        # state q8
        elif currentState == "q8":
            if char in psiNoU:
                currentState="q7"
            elif char == ".":
                currentState = "q7"
            elif char == "@":
                currentState = "q2"
            elif char == nums or char == psiNoEDU:
                currentState = "q6"
        #Final Output
        print("Character", char)
        print("State", currentState)
    if (currentState == "q8"):
        print("String is accepted")
    else:
        print("String is rejected")
    inputSTD = input("Do you want to input a string? (y/n) ")
print("n")
print("Project for CS 341\n"
      "Section Number: 008\n"
      "Semester:Spring2023\n"
      "Written by: Richard Tyrrell rt435\n"
      "Instructor: Marvin Nakayama, marvin@njit.edu")

nums="1234567890"
psi="abcdefghijklmnopqrstuvwxyz"
psiNoEDU="abcfghijklmnopqrstvwxyz"
psiNoE="abcdfghijklmnopqrstuv"
psiNoD="abcefghijklmopqrstuv"
psiNoU="abcdefghijklmopqrstvwxyz"

#User Input
inputSTD= input("Do you want to input a string? (y/n) ")
while inputSTD== 'y':
    print("y")
    compString=input("Enter your string: ")
    print(compString)
    #Starting State q1
    currentState = "q1"
    print("State", currentState)
    #Loop for characters from input
    for char in compString:
        # state q1
        if currentState == "q1":
            if char in psi:
                currentState = "q3"
            else:
                currentState = "q2"
        #state q2 (Trap State)
        elif currentState == "q2":
            currentState = "q2"
        #state q3
        elif currentState == "q3":
            if char == "@":
                currentState = "q5"
            elif char == ".":
                currentState = "q4"
            elif char in psi or char in nums:
                currentState = "q3"
        #state q4
        elif currentState == "q4":
            if char in nums:
                currentState = "q3"
            elif char == ".":
                currentState = "q2"
            elif char == "@":
                currentState = "q2"
            elif char in psi:
                currentState = "q2"
        #state q5
        elif currentState == "q5":
            if char in nums or psi:
                currentState = "q6"
            elif char ==".":
                currentState="q2"
            else:
                currentState = "q2"
        #state q6
        elif currentState == "q6":
            if char in nums or char in psi:
                currentState = "q6"
            elif char == ".":
                currentState = "q7"
            elif char == "@":
                currentState = "q2"
        #state q7
        elif currentState == "q7":
            if char == "e" or "d":
                currentState = "q8"
            elif char == ".":
                currentState = "q2"
            elif char == "@":
                currentState = "q2"
            elif char in psiNoE:
                currentState = "q6"
            elif char in nums:
                currentState = "q2"
        # state q8
        elif currentState == "q8":
            if char in psiNoU:
                currentState="q7"
            elif char == ".":
                currentState = "q7"
            elif char == "@":
                currentState = "q2"
            elif char == nums or char == psiNoEDU:
                currentState = "q6"
        #Final Output
        print("Character", char)
        print("State", currentState)
    if (currentState == "q8"):
        print("String is accepted")
    else:
        print("String is rejected")
    inputSTD = input("Do you want to input a string? (y/n) ")
print("n")
print("Project for CS 341\n"
      "Section Number: 008\n"
      "Semester:Spring2023\n"
      "Written by: Richard Tyrrell rt435\n"
      "Instructor: Marvin Nakayama, marvin@njit.edu")

nums="1234567890"
psi="abcdefghijklmnopqrstuvwxyz"
psiNoEDU="abcfghijklmnopqrstvwxyz"
psiNoE="abcdfghijklmnopqrstuv"
psiNoD="abcefghijklmopqrstuv"
psiNoU="abcdefghijklmopqrstvwxyz"

#User Input
inputSTD= input("Do you want to input a string? (y/n) ")
while inputSTD== 'y':
    print("y")
    compString=input("Enter your string: ")
    print(compString)
    #Starting State q1
    currentState = "q1"
    print("State", currentState)
    #Loop for characters from input
    for char in compString:
        # state q1
        if currentState == "q1":
            if char in psi:
                currentState = "q3"
            else:
                currentState = "q2"
        #state q2 (Trap State)
        elif currentState == "q2":
            currentState = "q2"
        #state q3
        elif currentState == "q3":
            if char == "@":
                currentState = "q5"
            elif char == ".":
                currentState = "q4"
            elif char in psi or char in nums:
                currentState = "q3"
        #state q4
        elif currentState == "q4":
            if char in nums:
                currentState = "q3"
            elif char == ".":
                currentState = "q2"
            elif char == "@":
                currentState = "q2"
            elif char in psi:
                currentState = "q2"
        #state q5
        elif currentState == "q5":
            if char in nums or psi:
                currentState = "q6"
            elif char ==".":
                currentState="q2"
            else:
                currentState = "q2"
        #state q6
        elif currentState == "q6":
            if char in nums or char in psi:
                currentState = "q6"
            elif char == ".":
                currentState = "q7"
            elif char == "@":
                currentState = "q2"
        #state q7
        elif currentState == "q7":
            if char == "e" or "d":
                currentState = "q8"
            elif char == ".":
                currentState = "q2"
            elif char == "@":
                currentState = "q2"
            elif char in psiNoE:
                currentState = "q6"
            elif char in nums:
                currentState = "q2"
        # state q8
        elif currentState == "q8":
            if char in psiNoU:
                currentState="q7"
            elif char == ".":
                currentState = "q7"
            elif char == "@":
                currentState = "q2"
            elif char == nums or char == psiNoEDU:
                currentState = "q6"
        #Final Output
        print("Character", char)
        print("State", currentState)
    if (currentState == "q8"):
        print("String is accepted")
    else:
        print("String is rejected")
    inputSTD = input("Do you want to input a string? (y/n) ")
print("n")
