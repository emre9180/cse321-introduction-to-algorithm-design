#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from random import Random
import random

#---------------------------------------------------------------------- Q1 TEST -------------------------------------------------------------------------------

def common_substring(strings):
    if not strings:
        return ""

    # if we have only one string in the array, return it to compare
    if len(strings) == 1:
        return strings[0]

    # split the array into 2 part
    mid = len(strings) // 2
    left_half = strings[:mid]
    right_half = strings[mid:]

    # get the right and left results
    left_result = common_substring(left_half)
    right_result = common_substring(right_half)

    result = ""
    min_len = min(len(left_result), len(right_result))
    i = 0
    while i < min_len:
        if left_result[i] == right_result[i]:
            result += left_result[i]
            i += 1
        else:
            break

    return result



def test_Q1():

    print("Result of the example in the PDF: ")
    strings = ['programmable', 'programming', 'programmer', 'programmatic', 'programmability']
    print(common_substring(strings)) 
    print()
    test_strings = []
    while True:
        string = input("Enter a string (-1 for exit): ")
        if(string == "-1"):
            break
        test_strings.append(string)
    print(test_strings)        
    print(common_substring(test_strings))



#---------------------------------------------------------------------- Q2 TEST -------------------------------------------------------------------------------

def max_difference(arr):
    min_element = arr[0]
    max_element = arr[0]
    min_index = 0
    max_index = 0
    for i in range(1, len(arr)):
        if arr[i] < min_element:
            min_element = arr[i]
            min_index = i
        if arr[i] > max_element:
            max_element = arr[i]
            max_index = i
    return (min_index, max_index)


def array_to_dict(arr):
    return {i: arr[i] for i in range(len(arr))}

def merge_sort(items):
    # Base case: if the list is empty or has only one element, it's already sorted
    if len(items) <= 1:
        return items

    # Split the list into two halves
    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]

    # Recursively sort the two halves
    left = merge_sort(left)
    right = merge_sort(right)

    # Merge the sorted halves back together
    return merge(left, right)

def merge(left, right):
    # Base case: if one of the lists is empty, return the other
    if not left:
        return right
    if not right:
        return left

    # Choose the element with the smaller value from the two lists
    if left[0][1] < right[0][1]:
        return [left[0]] + merge(left[1:], right)
    else:
        return [right[0]] + merge(left, right[1:])


def test_Q2_A():

    array = [10, 11, 10, 9, 8, 7, 9, 11]
    map = array_to_dict(array)
    items = list(map.items())
    result = merge_sort(items)


    print("Result of the example in the PDF: ")
    print(f"Buy on Day {result[0][0]}, Sell on Day {result[len(result)-1][0]}. Your profit is  {result[len(result)-1][1]-result[0][1]}")
    print()


    print("Enter positive numbers (-1 for exit): ")
    inp = None
    arr = []
    while(inp!=-1):
        inp = int(input("Enter a number to add to array (-1 for exit): "))
        if inp!=-1:
            arr.append(inp)
    
    map = array_to_dict(arr)
    items = list(map.items())
    result = merge_sort(items)
    
    print("Your array: ", arr)
    print(f"Buy on Day {result[0][0]}, Sell on Day {result[len(result)-1][0]}. Your profit is  {result[len(result)-1][1]-result[0][1]}")
    print()


def test_Q2_B():

    array = [10, 11, 10, 9, 8, 7, 9, 11]
    result_index1_Question_B,   result_index2_Question_B = max_difference(array)  
    print("Result of the example in the PDF: ")
    print(f"Buy on Day {result_index1_Question_B}, Sell on Day {result_index2_Question_B}. Your profit is  {array[result_index2_Question_B]-array[result_index1_Question_B]}")
    print()

    print("Enter positive numbers (-1 for exit): ")
    inp = None
    arr = []
    while(inp!=-1):
        inp = int(input("Enter a number to add to array (-1 for exit): "))
        if inp!=-1:
            arr.append(inp)
    
    result_index1_Question_B,   result_index2_Question_B = max_difference(arr)
    print("Your array: ", arr)
    print(f"Buy on Day {result_index1_Question_B}, Sell on Day {result_index2_Question_B}. Your profit is  {arr[result_index2_Question_B]-arr[result_index1_Question_B]}")
    print()







#---------------------------------------------------------------------- Q3 TEST -------------------------------------------------------------------------------

def longest_increasing_subarray(array):
    # store the length of the longest increasing sub-array ending at each index
    lengths = [1] * len(array)

    for i in range(1, len(array)):
        # find the longest increasing sub-array ending at the previous index
        longest_ending_at_prev = lengths[i-1]

        # if the current element is greater than the last element in the
        # longest increasing sub-array ending at the previous index,
        # add it to the sub-array
        if array[i] > array[i-1]:
            lengths[i] = longest_ending_at_prev + 1

    # return the maximum length of the longest increasing sub-arrays
    return max(lengths)



def test_Q3():
    
    array = [1, 4, 5, 2, 4, 3, 6, 7, 1, 2, 3, 4, 7]
    print("Array in the PDF: ", array)
    print("Result of the example in the PDF: ")
    length = longest_increasing_subarray(array)
    print(length)
    print()

    print("Enter positive numbers (-1 for exit): ")
    inp = None
    arr = []
    while(inp!=-1):
        inp = int(input("Enter a number to add to array (-1 for exit): "))
        if inp!=-1:
            arr.append(inp)
    
    length = longest_increasing_subarray(arr)
    print(length)
    print()

    




#---------------------------------------------------------------------- Q4 TEST -------------------------------------------------------------------------------


def max_score(arr):
    n = len(arr)
    m = len(arr[0])
    x = 0
    y = 0
    max_score = arr[0][0]
    while x < n-1 or y < m-1:
        if x < n-1 and (y == m-1 or arr[x+1][y] > arr[x][y+1]):
            max_score += arr[x+1][y]
            x += 1
        elif y < m-1:
            max_score += arr[x][y+1]
            y += 1
    return max_score



# Page 289
def calculate_F(n, m, C):
    # initialize F[0, 0] to C[0, 0]
    F = [[0] * (m ) for _ in range(n)]
    F[0][0] = C[0][0]

    # calculate F[0, j] for j from 1 to m
    for j in range(1, m):
        F[0][j] = F[0][j - 1] + C[0][j]

    # calculate F[i, 0] for i from 1 to n
    for i in range(1, n):
        F[i][0] = F[i - 1][0] + C[i][0]

    # calculate F[i, j] for i from 1 to n and j from 1 to m
    for i in range(1, n):
        for j in range(1, m):
            F[i][j] = max(F[i - 1][j], F[i][j - 1]) + C[i][j]

    return F[n-1][m-1]



def TestForPart4_A():
    table1 = [ [25, 30, 25],
            [45, 15, 11],
            [1, 88, 15],
            [9, 4, 23],
        ]

    print("Array in the PDF: ", table1)
    print("Result of the example in the PDF: ")
    res = calculate_F(4, 3, table1)
    print(res)


    rowNumber = int(input("\nNow, enter the row and column number, then it will be created a random table.\nEnter row number: "))
    columnNuber = int(input("Enter column number: "))
    table = []
    print("The board is: ")
    table = [[0] * columnNuber for _ in range(rowNumber)]

    for i in range (0,rowNumber):
        for j in range(0, columnNuber):
            table[i][j] = random.randrange(100)
            
    for i in range (0,rowNumber):
        print(table[i])
    print()
    
    res = calculate_F(rowNumber, columnNuber, table)
    print(res)


def TestForPart4_B():
    table1 = [ [25, 30, 25],
            [45, 15, 11],
            [1, 88, 15],
            [9, 4, 23],
        ]

    print("Firstly, it is tested the table in the PDF: ")
    res1 = max_score(table1)
    print(res1)


    
    rowNumber = int(input("\nNow, enter the row and column number, then it will be created a random table.\nEnter row number: "))
    columnNuber = int(input("Enter column number: "))
    table = []
    print("The board is: ")
    table = [[0] * columnNuber for _ in range(rowNumber)]

    for i in range (0,rowNumber):
        for j in range(0, columnNuber):
            table[i][j] = random.randrange(100)

    for i in range (0,rowNumber):
        print(table[i])
    print()
    
    res = max_score(table)
    print(res)


def menu():

    while(1):
        print("Which part do you want to test? (1 - 2.1 - 2.2 - 3 - 4.1 - 4.2 are options.)")
        inp = input()

        if inp == "1":
            test_Q1()
        
        if inp == "2.1":
            test_Q2_A()

        if inp == "2.2":
            test_Q2_B()

        if inp == "3":
            test_Q3()
        
        if inp == "4.1":
            TestForPart4_A()
        
        if inp == "4.2":
            TestForPart4_B()
        
        else:
            print("Please enter valid input!")

menu()


