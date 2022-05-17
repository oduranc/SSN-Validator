def principal():
    print("Welcome to SSN Validator!")

    print("")

    try:
        first = int(input("Give me the first three numbers (XXX): "))
        second = int(input("Give me the next two numbers (XX): "))
        third = int(input("Give me the last four numbers (XXX): "))
        print(f"{first}-{second}-{third}")

        if checkFirst(first) and checkSecond(second) and checkThird(third):
            print("It's a valid number")
    except:
        print("Your input is not a valid number. Make sure you are just typing numbers.")

def checkFirst(numbers):
    if len(numbers) == 3:
        if numbers != "000" and numbers != "666" and numbers < "900":
            return True
        else:
            print("1. This combination can't be neither 000, nor 666 nor can't be between 900-999")
            return False
    else:
        print("1. Make sure this combination has THREE numbers.")
        return False

def checkSecond(numbers):
    if len(numbers) == 2:
        if numbers != "00":
            return True
        else:
            print("2. This combination can't be 00")
            return False
    else:
        print("2. Make sure this combination has TWO numbers.")
        return False

def checkThird(numbers):
    if len(numbers) == 4:
        if numbers != "0000":
            return True
        else:
            print("3. This combination can't be 0000")
            return False
    else:
        print("3. Make sure this combination has FOUR numbers.")
        return False

principal()