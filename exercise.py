#1
'''
START
    SET gtst = "Day 7"
END
'''

gtst = "Day 7"


#2
'''
START
    SET gtst = "Day 7"
    DISPLAY "Hello Today is our " + gtst + " course"
END
'''
gtst = "Day 7"

print(f"Hello Today is our {gtst} course")


#3
'''
START
    SET numbers = [0, 2, 4]

    DISPLAY "The 1st Even number is: ", numbers[0]
    DISPLAY "The 2nd Even number is: ", numbers[1]
    DISPLAY "The 3rd Even number is: ", numbers[2]
END
'''
numbers = [0, 2, 4]

print(f"The 1st Even number is: {numbers[0]}")
print(f"The 2nd Even number is: {numbers[1]}")
print(f"The 3rd Even number is: {numbers[2]}")

#4
'''
START
    CREATE dictionary fruits
        apple = 10
        banana = 15
        pineapple = 20
END
'''
fruits = {
    "apple": 10,
    "banana": 15,
    "pineapple": 20
}

#5
'''
START
    CREATE dictionary fruits
        apple = 10
        banana = 15
        pineapple = 20

    SET choice = "apple"

    DISPLAY "The value of ", choice,
            " is: ", fruits[choice], " birr"
END
'''
fruits = {
    "apple": 10,
    "banana": 15,
    "pineapple": 20
}

choice = "apple"

print(f"The value of {choice} is: {fruits[choice]} birr")