#https://www.geeksforgeeks.org/maximum-number-formed-from-array-with-k-number-of-adjacent-swaps-allowed/
import sys


# Function to print the
# elements of the array
def print_ele(arr, n):
    for i in range(n):
        print(arr[i], end=" ");

    print();


# Exchange array elements one by
# one from right to left side
# starting from the current position
# and ending at the target position
def swapMax(arr, target_position,
            current_position):
    aux = 0;
    for i in range(current_position, target_position, -1):
        aux = arr[i - 1];
        arr[i - 1] = arr[i];
        arr[i] = aux;

    # Function to return the


# maximum number array
def maximizeArray(arr, length, swaps):
    # Base condition
    if (swaps == 0):
        return;

    # Start from the first index
    for i in range(length):
        max_index = 0;
        max = -(sys.maxsize - 1);

        # Search for the next K elements
        if (swaps + i) > length:
            limit = length
        else:
            limit = swaps + i

        # Find index of the maximum
        # element in next K elements
        for j in range(i, limit + 1):
            if (arr[j] > max):
                max = arr[j];
                max_index = j;

            # Update the value of
        # number of swaps
        swaps -= (max_index - i);

        # Update the array elements by
        # swapping adjacent elements
        swapMax(arr, i, max_index);

        if (swaps == 0):
            break;

        # Driver code


if __name__ == "__main__":
    arr = [1, 2, 6, 8, 9, 4, 9, 9, 9];
    length = len(arr);
    swaps = 7;
    maximizeArray(arr, length, swaps);

    print_ele(arr, length);


