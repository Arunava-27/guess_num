g_n = 50
print("You have 10 guesses")
print("Enter Correct Number within limit")

l = 10
while l >= 0:
    l = l - 1
    if l >= 0:
        num = int(input("Enter guessed no: "))
        if num > g_n:
            print("Correct no is smaller than {0}".format(num))
            print("Number of guesses left {0}".format(l))
            print("Try again")
        elif num<18:
            print("Correct no is greater than {0}".format(num))
            print("Number of guesses left {0}".format(l))
            print("Try again")
        elif num == g_n:
            f_g = 10 - l
            print("Congratulations Guessed Number Matched")
            print("Correct Number is {0}".format(g_n))
            print("Number of guesses left {0}".format(l))
            print("Finished in {0} guesses".format(f_g))
            break
    else:
        print("You Failed")
        print("Number of guesses left {0}".format(l))
        break



