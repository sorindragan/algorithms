import numpy as np
import datetime

def linear(arr, to_find):
    for val in arr:
        if val[1] == to_find:
            return val[0] 
    return -1


def binary(arr, to_find):
    midd = int(len(arr) / 2)
    if arr[midd][1] == to_find:
        return arr[midd][0]
    
    if len(arr) == 1:
        return -1
    
    if arr[midd][1] > to_find:
        return binary(arr[:midd], to_find)
    
    if arr[midd][1] < to_find:
        return binary(arr[midd:], to_find)


def main():
    max_int = 10000
    length = 5000
    arr = list(enumerate([np.random.randint(0, max_int) for _ in range(length)]))
    to_find = arr[np.random.randint(0, length)][1]
    # print(arr, to_find)

    # linear
    l0 = datetime.datetime.now()
    index_l = linear(arr, to_find)
    l1 = datetime.datetime.now()

    # arr needs to be sorted
    arr.sort(key=lambda t: t[1])
    # binary
    b0 = datetime.datetime.now()
    index_b = binary(arr, to_find)
    b1 = datetime.datetime.now()
    
    print(f"{to_find} was [liniarly] found at index {index_l} in {(l1-l0).microseconds} microseconds")
    print(f"{to_find} was [binary] found at index {index_b} in {(b1-b0).microseconds} microseconds")
    

if __name__ == '__main__':
    main()
