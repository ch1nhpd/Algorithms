'''
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns 3 possible results:

-1: The number I picked is lower than your guess (i.e. pick < num).
1: The number I picked is higher than your guess (i.e. pick > num).
0: The number I picked is equal to your guess (i.e. pick == num).
Return the number that I picked.
    testcase:
        n = 2126753390
        pick = 1702766719
'''

def guess(x):
    if x == 1702766719:
        return 0
    elif x > 1702766719:
        return -1
    else:
        return 1

def guessNumber(n) -> int:
    min = 0
    max = n
    while True:
        g = (min+max+1)//2
        x = guess(g)
        if x == 0:
            return g
        elif x == -1:
            max = g
        else:
            min = g

print(guessNumber(2126753390))
print(-2147483648//-1)