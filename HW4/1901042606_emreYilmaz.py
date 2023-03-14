# ----------------------------------------------------------------------------------------------------- QUESTION 1 ----------------------------------------------------------------------------------------------------- #

def findPath(board, rown, coln, total, string, points):
    if(rown>=len(board) or coln>=len((board[0]))): # If the borders are exceed.
        return total

    move1 = "A" + str(rown+1+1) + "B" + str(coln+1) # Store the next movement
    move2 = "A" + str(rown+1) + "B" + str(coln+1+1) # Store the next movement

    # Initilization
    total1 = -1
    total2 = -1

    if(rown+1<len(board)): # If the next move towards down is valid, make it.
        total1 = findPath(board, rown+1, coln, total+board[rown+1][coln], string, points)

    if(coln+1<len(board[0])): # If the next move towards right is valid, do it
        total2 = findPath(board, rown, coln+1, total+board[rown][coln+1], string, points)
    
    if ((rown+1<len(board)) or (coln+1<len(board[0]))): # If we made 2 valid movement
        
        if(total1>total2): # If recursive call of downside movement is greater than other, add it to result collections.
            if move1 not in string:
                string.insert(0, move1) # Add path
                points.insert(0, board[rown+1][coln]) # Add point
            return total1

        else: # If recursive call of rightside movement is greater than other, add it to result collections.
            if move2 not in string:
                string.insert(0, move2) # Add path
                points.insert(0, board[rown][coln+1]) # Add point
            return total2
    else:
        return total+board[len(board)-1][len(board[0])-1] # If we reach the end, return the total point



# It is helper function to create necessary data and printing. It is not important for you. Look the function above.
def InitiliazerFindPath(table):
    
    points = []
    string = []


    total2 = 0
    move1 = "A" + str(1) + "B" + str(1)
    move2 = "A" + str(len(table)) + "B" + str(len(table[0]))

    result = findPath(table, 0,0, table[0][0], string, points)
    result -= table[len(table)-1][len(table[0])-1]
    string.insert(0, move1)
    points.insert(0, table[0][0])
    string.append(move2)
    points.append(table[len(table)-1][len(table[0])-1])

    
    # Cleaning unnecessary data
    i = 0
    length = len(string)
    while(i<length-1):
        if( not(((int(string[i][1])+1 == int(string[i+1][1])) and( int(string[i][3]) == int(string[i+1][3]))) or( (int(string[i][3])+1 == int(string[i+1][3])) and (int(string[i][1]) == int(string[i+1][1]))))):
            string.pop(i+1)
            points.pop(i+1)
            length = length-1
            i = i-1
        i = i+1



    print("Total score: ", result)
    print("Points accordign to path: ", points)
    print("Path: ", string)


def TestForPart1():
    table1 = [ [25, 30, 25],
            [45, 15, 11],
            [1, 88, 15],
            [9, 4, 23],
        ]

    print("Firstly, it is tested the table in the PDF: ")
    InitiliazerFindPath(table1)


    rowNumber = int(input("\nNow, enter the row and column number, then it will be created a random table.\nEnter row number: "))
    columnNuber = int(input("Enter column number: "))
    table = []
    print("The board is: ")

    # Initiliaze the board
    table = [[0] * columnNuber for _ in range(rowNumber)]

    # Put random numbers to the board
    for i in range (0,rowNumber):
        for j in range(0, columnNuber):
            table[i][j] = random.randrange(100)
            
    # silmeyi unutma bunu
    table[len(table)-1][0] = 30
    # Printing the table
    for i in range (0,rowNumber):
        print(table[i])
    print()
    
    InitiliazerFindPath(table)

# ----------------------------------------------------------------------------------------------------- QUESTION 2 ----------------------------------------------------------------------------------------------------- #

# This partition function is written by help of text book, "Anany Levitin - Introduction to the Design and Analysis of Algorithms" page 159
def LomutoPartition(array, left, right):
    pivot = array[left]
    S = left

    for i in range (left+1, right+1):
        if(array[i]<pivot):
            S = S+1
            temp = array[S]
            array[S] = array[i]
            array[i] = temp
    temp = array[S]
    array[S] = array[left]
    array[left] = temp
    return S

# This partition function is written by help of text book, "Anany Levitin - Introduction to the Design and Analysis of Algorithms" page 160
def QuickSelect(array, targetIndex, left, right):
    if left == right:
        return array[left]

    S = LomutoPartition(array, left, right)
    if S == targetIndex:
        return array[S]
    elif S > targetIndex:    
        return QuickSelect(array, targetIndex, left, S - 1)
    else:
        return QuickSelect(array, targetIndex, S + 1, right)

def TestForQ2():


    print("Enter positive numbers (-1 for exit): ")

    inp = None
    arr = []
    while(inp!=-1):
        inp = int(input("Enter a number to add to array (-1 for exit): "))
        if inp!=-1:
            arr.append(inp)

    middleIndex = int(len(arr)/2)

    result = QuickSelect(arr, middleIndex, 0, len(arr)-1)
    print("Your array is: ", end='')
    for i in range (0, len(arr)):
        print(arr[i], end=' ')
    print()
    print(f"Value of median: {result}")
    print()




    
# ----------------------------------------------------------------------------------------------------- QUESTION 3-A ----------------------------------------------------------------------------------------------------- #
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

# Classic Linked List implementation
class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0
    
    def append(self, data):
        self.count = self.count + 1
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head  # make the new node point to itself
            return
        current = self.head
        while current.next != self.head:  # stop at the last node that points to the head
            current = current.next
        current.next = new_node
        new_node.next = self.head  # make the new node point to the head
        
    
    # It is modified. It gets a node and removes its next node
    def remove(self, node):
        self.count = self.count - 1
        if self.head is None:
            return
        if self.head == node:  # if the node to be removed is the head
            current = self.head
            while current.next != self.head:  # find the last node that points to the head
                current = current.next
            if self.head == self.head.next:  # if there is only one node
                self.head = None
            else:
                current.next = self.head.next
                self.head = self.head.next
            return
        current = self.head
        while current.next != self.head:
            if current.next == node:
                current.next = current.next.next
                return
            current = current.next

       
    # Add numbers to the linked list
    def add_numbers(self, n):
        for i in range(1, n+1):
            self.append(i)

    # Does the task. Finds the survivor. Explaining exists in the report.
    def josephus(self):
        print(self.count)
        iterator = self.head
        while(self.count!=1):
            self.remove(iterator.next)
            iterator= iterator.next



def TestJosephusA():
    size = int(input("Please enter the people number for question 3-a: "))

    liste = LinkedList()
    liste.add_numbers(size)
    liste.josephus()
    print(f"The survivor is index: {liste.head.data}")
    print()

    # ----------------------------------------------------------------------------------------------------- QUESTION 3-B ----------------------------------------------------------------------------------------------------- #
import random

# It is learned from ("Anany Levitin - Introduction to the Design and Analysis of Algorithms"), in the page 154, 155, 156
def Josephus(size):
    if(size==1):
        return 1

    if(size%2==0):
        return 2 * Josephus(int(size/2)) - 1
    
    else:
        return 2 * Josephus(int(size/2)) + 1


def TestJosephusB():
    size = None
    print("Please enter the input for question 3-b")
    size = int(input("Please enter the people number: "))
    result = Josephus(size)
    print(f"The survivor is index: {result}")
    print()











    








def menu():

    while(1):
        print("Which part do you want to test? (1 - 2 - 3.1 - 3.2 are options.)")
        inp = input()

        if inp == "1":
            TestForPart1()
        
        if inp == "2":
            TestForQ2()

        if inp == "3.1":
            TestJosephusA()

        if inp == "3.2":
            TestJosephusB()
        
        else:
            print("Please enter valid input!")

menu()