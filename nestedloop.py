



def printpyrimid(n):

    for i in range(n):
        j = 0
        for j in range(n-i):
            print(" ",  end = '')

        for j in range(i):
            print("* ",  end = '')

        print("")

    for i in range(n):
        j = 0
        for j in range(i):
            print(" ",  end = '')

        for j in range(n-i):
            print("* ",  end = '')

        print("")


printpyrimid(5)

