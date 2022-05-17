def principal():
    print("Welcome to SSN Validator!")

    ex = False
    while ex != True:
        print("")
        first = input("Give me the first three numbers (XXX): ")
        second = input("Give me the next two numbers (XX): ")
        third = input("Give me the last four numbers (XXXX): ")

        print(f"{first}-{second}-{third}")
        print("")

        if checkAll(first, second, third):
            print("It's a valid number.")
        else:
            print("It's not a valid number.")
        print("")
        opt = input("Do you want to try with another number combination? (y/n) ")
        if opt == "y":
            ex = False
        else:
            ex = True

def checkAll(first, second, third):
    checkFirst(first)
    checkSecond(second)
    checkThird(third)

def checkFirst(numbers):
    if len(numbers) == 3:
        if checkAreNumbers(numbers):
            if numbers != "000" and numbers != "666" and numbers < "900":
                return True
            else:
                print("1. This combination can't be neither 000, nor 666 nor can't be between 900-999")
                return False
        else:
            print("1. Only type numbers!")
            return False
    else:
        print("1. Make sure this combination has THREE numbers.")
        return False

def checkSecond(numbers):
    if len(numbers) == 2:
        if checkAreNumbers(numbers):
            if numbers != "00":
                return True
            else:
                print("2. This combination can't be 00")
                return False
        else:
            print("2. Only type numbers!")
            return False
    else:
        print("2. Make sure this combination has TWO numbers.")
        return False

def checkThird(numbers):

    if len(numbers) == 4:
        if checkAreNumbers(numbers):
            if numbers != "0000":
                return True
            else:
                print("3. This combination can't be 0000")
                return False
        else:
            print("3. Only type numbers!")
            return False
    else:
        print("3. Make sure this combination has FOUR numbers.")
        return False

def checkAreNumbers(numbers):
    try:
        for letter in numbers:
            int(letter)
        return True
    except:
        return False

principal()