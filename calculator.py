import math

def calculator():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("\t\tCALCULATOR")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    print("\tEnter your choice from : \n")
    print("\tAddition : 1")
    print("\tSubstraction : 2")
    print("\tMultiplication : 3")
    print("\tDivison : 4")
    print("\tvalue of pi : 5")
    print("\tAverage : 6")
    print("\tPercentage : 7")
    print("\tSquare : 8")
    print("\tCube : 9")

    while True:
        input_value = eval(input("\n\tSelect option from 1-9 : "))

        if input_value > 9:
            print("\n\tPlease enter One Number b/w 1-9 ")
        else:
            break
    
    if input_value == 1:
        a = eval(input("\n\tEnter number 1 :"))
        b = eval(input("\tEnter number 2 :"))
        sum = a+b
        print(f"\n\tSum of {a} & {b} is : {sum} ")
    elif input_value == 2:
        c = eval(input("\n\tEnter number 1 :"))
        d = eval(input("\tEnter number 2 :"))
        diff = c-d
        print(f"\n\tSubstraction of {c} & {d} is : {diff}")
    elif input_value == 3:
        e = eval(input("\n\tEnter number 1 :"))
        f = eval(input("\tEnter number 2 :"))
        mul = e*f
        print(f"\n\tMultiplication of {e} & {f} is : {mul}")
    elif input_value == 4:
        g = eval(input("\n\tEnter number 1 :"))
        h = eval(input("\tEnter number 2 :"))
        div = g/h
        print(f"\n\tDivision of {g} & {h} is : {div}")
    elif input_value == 5:
        print("\n\tValue of pi is : ", math.pi)
    elif input_value == 6:
        i = eval(input("\n\tEnter number 1 :"))
        j = eval(input("\tEnter number 2 :"))
        avg = (i+j)/2
        print(f"\n\tAverage of {i} & {j} is : {avg}")  
    elif input_value == 7:
        k = eval(input("\n\tEnter number :"))
        l = eval(input("\tEnter Total number  :"))
        percent = (k/l)*100
        print(f"\n\tPercent of {k} in {l} is : {percent}")
    elif input_value == 9:
        cu = int(input("\n\tEnter a number : "))
        cube = cu*cu*cu
        print(f"\n\tCube of {cu} is : {cube}")

    repeat = input("\n\twanna do it again? (y/n) :").lower()
    if repeat == 'y':
        calculator()
    else :
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("\t\tCome Back SOON!")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
calculator()
