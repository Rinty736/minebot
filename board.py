from brain import work 
import numpy as np
board = [


[0,0,2,"F",9,9,9,9,9,9,9,9,9,9,9,9,],
[0,1,3,"F",9,9,9,9,9,9,9,9,9,9,9,9,],
[0,1,"F",9,9,9,9,9,9,9,9,9,9,9,9,9,],
[1,2,2,9,9,9,9,9,9,9,9,9,9,9,9,9,],
[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,],
[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,],
[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,],
[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,],
[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,],
[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,],
[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,],
[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,],
[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,],
[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,],
[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,],
[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,],

]
a,numbers = work(16,16,board)

all_arrays = []
def click_to_number(board):
    print("click_to_number begin")
    i = len(all_arrays)
    all_arrays.append(numbers)
    # если это первый массив, то все его элементы уникальны
    if i == 0:
        unique = np.unique(numbers)
    # иначе нужно исключить те элементы, которые есть в предыдущих массивах
    else:
        unique = numbers[~np.isin(numbers, np.concatenate(all_arrays[:-1]))]

    for i in unique:
        # print(i)
        ...


click_to_number(board)
