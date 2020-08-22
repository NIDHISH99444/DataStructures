#mice coding explaination
#https://www.youtube.com/watch?v=nyR8K63F2KY&t=211s
def findoptimal(N):

    if (N <= 6):
        return N

    screen = [0] * (N+1)



    for n in range(1, 7):
        screen[n ] = n

    for n in range(7, N + 1):

        screen[n] = max(2 * screen[n - 3],
                            max(3 * screen[n - 4],
                                4 * screen[n - 5]));

    return screen

if __name__ == "__main__":
    N=11
    print("Maximum Number of A's with ", N,
              " keystrokes is ", findoptimal(N))

