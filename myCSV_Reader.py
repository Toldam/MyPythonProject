csvFile = open("FL_insurance_sample.csv")
arr = []
running = True

def printStartMenu():
    menuFunctions()


def menuFunctions():
    while running:
        print(30 * "-", "MENU", 30 * "-")
        print("1. Print the CSV file")
        print("2. Pull individual values")
        print("3. print inspirational quote")
        print("q. Exit")
        print(67 * "-")

        inp1 = input("Enter your input1: ")

        if inp1 == "1":
            printFile()
        elif inp1 == "2":
            subMenu()
        elif inp1 == "3":
            print("you hit 3")
        elif inp1 == "q":
            print("you hit quit")
            break


def subMenu():
    print(30 * "-", "MENU", 30 * "-")
    print(" 1. policyID\t\t\t\t 2. statecode\t\t\t\t 3. county")
    print(" 4. eq_site_limit\t\t\t 5. hu_site_limit\t\t\t 6. fl_site_limit")
    print(" 7. fr_site_limit\t\t\t 8. tiv_2011\t\t\t\t 9. tiv_2012")
    print("10. eq_site_deductible\t\t11. hu_site_deductible\t\t12. fl_site_deductible")
    print("13. fr_site_deductible\t\t14. point_latitude\t\t\t15. point_longitude")
    print("16. line\t\t\t\t\t17. construction\t\t\t18. point_granularity")
    print()
    print("q. Exit")
    print(67 * "-")

    while running:
        elementCounter = 0
        running2 = True

        inpTemp = input("Enter your input2: ")
        for line in csvFile:
            elementCounter += 1
            words = line.split(',')
            arr.append(words[(int(inpTemp) - 1)])

        while running2:
            subMenu2()
            inp = input("Enter your input3: ")
            if inp == "1":
                print("Number of Elements: ", elementCounter, "\n", arr)
            elif inp == "2":
                print("Number of Elements: ", elementCounter, "\n", sorted(arr))
            elif inp == "3":
                print("Number of Elements: ", elementCounter, "\n", sorted(arr, reverse=True))
            elif inp == "4":
                return
            elif inp == "q" or "Q" or "quit" or "Quit":
                yesOrNo = input("Are you sure Y/N")
                if yesOrNo == "y" or "yes" or "Y" or "Yes":
                    break #return to subMenu
                else:
                    return




def subMenu2():
    print(30 * "-", "MENU", 30 * "-")
    print("1. Do not sort and print")
    print("2. Sort by ascending order")
    print("3. Sort by descending order")
    print("4. return")
    print("q. Exit")
    print(67 * "-")



def printFile():
    for line in csvFile:
        print(line)


printStartMenu()

