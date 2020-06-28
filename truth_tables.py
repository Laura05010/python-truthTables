import itertools
import sys


def main_menu():
    print("^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-")
    print("^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-")
    print("^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-")
    print("PYTHON TRUTH TABLE GENERATOR")
    print("^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-")
    print("SELECT ONE OF THE FOLLOWING OPTIONS:")
    print("1. INSTRUCTIONS")
    print("2. CREATE A TRUTH TABLE")
    print("3. EXIT THE PROGRAM")
    choice = input("Please select an option >>> ")
    if choice == "1":
        instructions()
    elif choice == "2":
        truth_table()
    elif choice == "3":
        print("Thanks for using the program! Have a great day :)")
        sys.exit()
    else:
        print("Invalid Option! Please type \"1\", \"2\", or \"3\" ")
        main_menu()


def instructions():
    print("^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-")
    print("WELCOME TO THE PYTHON TRUTH TABLE GENERATOR!")
    print("^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-")
    print("This program was made to evaluate logical statements with up to FIVE INPUTS. (P,Q,R,S,T)\n\
    It will create the corresponding truth tables and do the work for you!\n\
    Just specify the NUMBER OF INPUTS and then \n\
    write a LOGICAL STATEMENT with the corresponding number of inputs.")
    print()
    print("EXAMPLE OF STATEMENTS & HOW TO WRITE THEM :)")
    print("AN IMPLICATION (P implies Q) must be written as: 'not(p and not q)' OR as:'not p or q'")
    print("AN EQUIVALENCE (P is equivalent to Q) must be written as either: p == q ")
    print("Don't Use '' marks!")
    print("P AND Q should be written as 'p and q'")
    print("P AND (Q AND NOT R) should be written as 'p and (q and not r)'")
    print("(P OR (NOT Q)) AND (NOT C) should be written as '(p or (not q) and (not r))' ")
    print()
    print("^-^-^-^-^-^-^-LIMITATIONS OF USE-^-^-^-^-^-^-^-")
    print("1. The program only refers to inputs that have been created. It is limited to FIVE Inputs")
    print("   ONE input represents P.")
    print("   TWO inputs represent P, Q.")
    print("   THREE inputs represent P, Q, R.")
    print("   FOUR inputs represent P, Q, R, S.")
    print("   FIVE inputs represent P, Q, R, S, T.")
    print("2. Make sure to use the correct parentheses (inner statements are evaluated first).")
    print("3. The evaluation of the logical statement will be evaluated in the next available column")
    print("4. Check syntax and brackets if your statement can't be evaluated!")
    print()
    print()
    wait = input("Return to the main Menu? y/n>>> ").lower()
    if wait[0] == "y":
        main_menu()
    elif wait[0] == "n":
        print("Let's create a truth table then!")
        truth_table()
    else:
        print("Invalid input!")
        main_menu()


def truth_table():
    while True:
        try:
            number_inputs = int(input("Please enter the number of inputs that the statement has (1 to 5): "))
            if number_inputs < 1 or number_inputs > 5:
                print("You must input a number between 1 and 5 (inclusive)")
            break
        except ValueError:
            print("You must input a number between 1 and 5 (inclusive)")
            truth_table()

    truths = list(itertools.product([True, False], repeat=number_inputs))
    # making sure to cover it to lower just in case :)
    statement = input("Please input the logical statement e.g ( p and q) and (not r) >>> ").lower()

    if number_inputs == 1:
        print("P            {0}".format(statement))
    elif number_inputs == 2:
        if "".join(statement.split()) == "not(pandnotq)" or "".join(statement.split()) == "notporq":
            print("P    \t\tQ           P ==> Q")
        elif "".join(statement.split()) == "(notporq)and(notqorp)" or\
               "".join(statement.split()) == "not(pandnotq)andnot(qandnotp)":
            print("P    \t\tQ           P <==> Q")
        else:
            print("P    \t\tQ           {0}".format(statement))
    elif number_inputs == 3:
        print("P    \t\tQ   \t\tR           {0}".format(statement))
    elif number_inputs == 4:
        print("P    \t\tQ   \t\t    R\t\t   S           {0}".format(statement))
    else:
        print("P    \t\tQ   \t\tR   \t\t    S\t\t   T           {0}".format(statement))

    print("-"*20*number_inputs)

    for truth in truths:
        position = 0
        if number_inputs == 1:
            p = truth[0] 
        elif number_inputs == 2:
            p, q = truth[0], truth[1]
        elif number_inputs == 3:
            p, q, r = truth[0], truth[1], truth[2]
        elif number_inputs == 4:
            p, q, r, s = truth[0], truth[1], truth[2], truth[3]
        else:
            p, q, r, s, t = truth[0], truth[1], truth[2], truth[3], truth[4]
            position = 0

        #print("-" * 20 * number_inputs)
        while position < number_inputs:
            print(truth[position], end="\t\t")
            position += 1

        try:
            truth = eval(statement)  # evaluates the statement as a python statement
            print(truth)
        except ValueError:
            print("Unable to evaluate. Check statement and try again. ")

    print()

    wait = input("Create another truth table? y/n ").lower()
    if wait[0] == "y":
        truth_table()
    else:
        main_menu()


if __name__ == '__main__':
    main_menu()
