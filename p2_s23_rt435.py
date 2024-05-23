'''I was having formating issues with the epsilon synmbol so I just wrote espilon in place.'''

print('Project 2 for Cs 341\n','Section Number:008\n','Semester:Spring 2023\n','Written by: Richard Tyrrell,rt435\n','Instructor:Marvin Nakayama, marvin@njit.edu')

#stack struct
class Stack:
    def __init__(self):
        self.items = []
        
    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


def pdacheck(string):
    stacky = Stack()  # initialize the stack
    operators = '+-*/'  # set of mathmatic operators
    state = 0  # storing States here so we can compare
    print('\nStarting State = q{}'.format(state))  # Starting State

    for i in string:

        # Check for $ then move to q1
        if i == '$' and state == 0:
            stacky.push('$')
            state = 1
            print('{}, epsilon -> $: Current state = q{}'.format(i, state))

        elif i == '$' and state == 1:
            stacky.push('$')
            state = 2
            print('{}, epsilon -> $: Current state = q{}'.format(i, state))

        # parens must be both L and R so we push it onto the stack for later
        elif i == '(' and state == 2:
            stacky.push('(')
            state = 2
            print('{}, epsilon -> (: Current state = q{}'.format(i, state))

        # check for number in q2 move to q3
        elif i.isdigit() and state == 2:
            state = 3
            print('{}, epsilon -> epsilon: Current state = q{}'.format(i, state))

        # check for dot in q2 move to q4
        elif i == '.' and state == 2:
            state = 4
            print('{}, epsilon -> epsilon: Current state = q{}'.format(i, state))

        # loop in q3 if number
        elif i.isdigit() and state == 3:
            state = 3
            print('{}, epsilon -> epsilon: Current state = q{}'.format(i, state))

        # dot in q3 we move to q5
        elif i == '.' and state == 3:
            state = 5
            print('{}, epsilon -> epsilon: Current state = q{}'.format(i, state))

        # number in q4 move to q5
        elif i.isdigit() and state == 4:
            state = 5
            print('{}, epsilon -> epsilon: Current state = q{}'.format(i, state))

        # loop on number in q5
        elif i.isdigit() and state == 5:
            state = 5
            print('{}, epsilon -> epsilon: Current state = q{}'.format(i, state))

        # If $ at q5 check stack then move to q7
        elif i == '$' and state == 5:
            if stacky.peek() == '$':
                stacky.pop()
                state = 7
            else:
                break
            print('{}, $ -> epsilon: Current state = q{}'.format(i, state))

        # operators at q5 back to q2
        elif i in operators and state == 5:
            state = 2
            print('{}, epsilon -> epsilon: Current state = q{}'.format(i, state))

        # if parenR in q5 check stack for parenL go to q6 if so
        elif i == ')' and state == 5:
            if stacky.peek() == '(':
                stacky.pop()
                state = 6
            else:
                break
            print('{}, ( -> epsilon: Current state = q{}'.format(i, state))

        # loop on q6 for parens
        elif i == ')' and state == 6:
            if stacky.peek() == '(':
                stacky.pop()
                state = 6
            else:
                break
            print('{}, ( -> epsilon: Current state = q{}'.format(i, state))

        # check if it's an operator
        elif i in operators and state == 6:
            state = 2
            print('{}, epsilon -> epsilon: Current state = q{}'.format(i, state))

        # $ in q6 check stack
        elif i == '$' and state == 6:
            if stacky.peek() == '$':
                stacky.pop()
                state = 7
            else:
                break
            print('{}, $ -> epsilon: Current state = q{}'.format(i, state))

        # $ in q7 and $ on top of stack accept it
        elif i == '$' and state == 7:
            if stacky.peek() == '$':
                stacky.pop()
                state = 8 # accepting state
            else:
                break
            print('{}, $ -> epsilon: Current state = q{}'.format(i, state))


        #Anything that fails crashes
        else:
            break

   #Make sure it made it to the accepting state
    if state == 8:
        print(string)
        print("String accepted\n")
    else:
        print(string)
        print("Program crashed at state {}".format(state, i))
        print("String not accepted \n")


#user input to get the program rocking and rolling
def main():
    while True:
        choice = input("Enter a string? (y/n) ")
        if choice.lower() == 'n':
            print("\n",choice)
            break
        elif choice.lower() == 'y':
            string = input("\nEnter string")
            print(" ",string)
            pdacheck(string)
        else:
            print("Enter a string again? (y/n)")

if __name__ == "__main__":
    main()