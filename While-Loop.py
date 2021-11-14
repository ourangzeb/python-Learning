

def eatApples(num_ofapples, on_diet):
    remaining_apple = num_ofapples

    if on_diet == True:
        print("He can eat apples.......")

        while remaining_apple > 0:
            print("eating apple which is " + str(remaining_apple))
            remaining_apple = remaining_apple - 1



    print("Done")
    return


eatApples(5,True)
