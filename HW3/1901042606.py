# --------------------------------------------------------------  QUESTION 1 ANSWER  --------------------------------------------------------------


# Add vertex to the graph
def addVertex(graph, vertex):
    graph[vertex] = []
    return graph

# Add edge to the graph
def addEdge(graph, source, target):
    graph[source].append(target)
    return graph

# Helper DFS method
def RecursiveDFS(graph, start, visited):
    visited.append(start)

    for vertex in graph[start]:
        if vertex not in visited:
            RecursiveDFS(graph, vertex, visited)

# Main DFS method
def DFS(graph, start):
    visitedNodes = []
    RecursiveDFS(graph, start, visitedNodes)
    return visitedNodes

# Classical BFS algorithm
def breadth_first_search(graph, start_node):

    visited = []
    queue = [start_node]

    while queue:
        node = queue.pop(0)

        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])
            
    return visited

# Updated BFS algorithm. I explained it in the report
def updated_breadth_first_search(graph, answer, start_node):

    visited = []
    queue = []

    queue.append(start_node)

    while queue:
        node = queue.pop(0)

        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])
            
            if node in answer:
                index = answer.index(node)
                for element in graph[node]:
                    if element not in answer:
                        answer.insert(index+1, element)
                        index = index+1

            else:
                answer.insert(0, node)
                index = answer.index(node)
                for element in graph[node]:
                    if element not in answer:
                        answer.insert(index+1, element)
                        index = index+1

    return visited

# Function to create graph
def create_graph():
    graph = {}

    while True:
        print("Enter a vertex (or 'q' to quit):")
        vertex = input()

        if vertex == "q":
            break

        graph = addVertex(graph, vertex)

    while True:
        print("Enter an edge in format (V1 V2), space seperated without paranthesis (or 'q' to quit):")
        edge = input()

        if edge == "q":
            break

        source, target = edge.split()
        graph = addEdge(graph, source, target)

    return graph



def testForDFS():

     # Test a constsructed graph
    graph2 = {}
    graph2 = addVertex(graph2, "CSE102")
    graph2 = addVertex(graph2, "CSE241")
    graph2 = addVertex(graph2, "CSE222")
    graph2 = addVertex(graph2, "CSE321")
    graph2 = addVertex(graph2, "CSE211")
    graph2 = addVertex(graph2, "CSE422")
    graph2 = addVertex(graph2, "CSE333")
    graph2 = addVertex(graph2, "CSE444")
    graph2 = addVertex(graph2, "CSE555")
    graph2 = addVertex(graph2, "CSE99")

    graph2 = addEdge(graph2, "CSE99", "CSE222")
    graph2 = addEdge(graph2, "CSE102", "CSE241")
    graph2 = addEdge(graph2, "CSE241", "CSE222")
    graph2 = addEdge(graph2, "CSE222", "CSE321")
    graph2 = addEdge(graph2, "CSE211", "CSE333")
    graph2 = addEdge(graph2, "CSE333", "CSE444")
    graph2 = addEdge(graph2, "CSE211", "CSE321")
    graph2 = addEdge(graph2, "CSE321", "CSE422")


    visited = DFS(graph2, list(graph2.keys())[0])

    print("Your default graph is: ", graph2)


    for nodes in graph2:
        newVisited = DFS(graph2, nodes)
        #print("new bu -> ", newVisited)

        addList = []

        if newVisited[0] not in visited:
            if(len(newVisited)==1):
                visited.insert(0, newVisited[0])
            target = None
            for item in newVisited:
                if item not in visited:
                    addList.append(item)
                else:
                    target = item
                    index = visited.index(target)
                    for item in addList:
                        visited.insert(index-1, item)
                        index = index+1
                    break
         
    print("Final List of the default input -> ", visited)
    print("\nNow you can create your own graph.", '\n')





    graph = create_graph()
    print(graph)

    visited = DFS(graph, list(graph.keys())[0])




    for nodes in graph:
        newVisited = DFS(graph, nodes)
        #print("new bu -> ", newVisited)

        addList = []

        if newVisited[0] not in visited:
            if(len(newVisited)==1):
                visited.insert(0, newVisited[0])
            target = None
            for item in newVisited:
                if item not in visited:
                    addList.append(item)
                else:
                    target = item
                    index = visited.index(target)
                    for item in addList:
                        visited.insert(index-1, item)
                        index = index+1
                    break
         
    print("Final List -> " ,visited)



def testForBNF():

    # Test a constsructed graph
    graph2 = {}
    graph2 = addVertex(graph2, "CSE102")
    graph2 = addVertex(graph2, "CSE241")
    graph2 = addVertex(graph2, "CSE222")
    graph2 = addVertex(graph2, "CSE321")
    graph2 = addVertex(graph2, "CSE211")
    graph2 = addVertex(graph2, "CSE422")
    graph2 = addVertex(graph2, "CSE333")
    graph2 = addVertex(graph2, "CSE444")
    graph2 = addVertex(graph2, "CSE555")
    graph2 = addVertex(graph2, "CSE99")

    graph2 = addEdge(graph2, "CSE99", "CSE222")
    graph2 = addEdge(graph2, "CSE102", "CSE241")
    graph2 = addEdge(graph2, "CSE241", "CSE222")
    graph2 = addEdge(graph2, "CSE222", "CSE321")
    graph2 = addEdge(graph2, "CSE211", "CSE333")
    graph2 = addEdge(graph2, "CSE333", "CSE444")
    graph2 = addEdge(graph2, "CSE211", "CSE321")
    graph2 = addEdge(graph2, "CSE321", "CSE422")

    print("Your default graph is: ", graph2)

    # Default input test
    answer = breadth_first_search(graph2, list(graph2.keys())[0])

    for nodes in graph2:
        visited = updated_breadth_first_search(graph2, answer, nodes)
    print("Final List of the default input -> ", answer, '\n')
    print("Now you can create your own graph.",'\n')


    # User input test
    graph = create_graph()
    print("Your new graph is: ", graph)

    answer = breadth_first_search(graph, list(graph.keys())[0])

    for nodes in graph:
        visited = updated_breadth_first_search(graph, answer, nodes)
    print("Final List -> ", answer)




# --------------------------------------------------------------  QUESTION 3 ANSWER  --------------------------------------------------------------

# Checks the column to find the num. If it cannot not find, column is OK
def check_column(num, board, column):
    for i in range(9):
        if (board[i][column]) == num:
            return False
    return True

# Checks the row to find the num. If it cannot not find, row is OK
def check_row(num, board, row):
    for i in range(9):
        if (board[row][i]) == num:
            return False
    return True

# Check 3x3 block to find the num. If it cannot find, block is OK
def check_block(num, board, row, column):
    rowBlock = int(row/3) # Find the rowblock that num belongs. ( For example [3,1] index belongs to second row block and first column block)
    columnBlock = int(column/3) # Find the columnblock that num belongs

    for i in range(int(rowBlock*3), int(rowBlock*3+3)):
        for j in range(int(columnBlock*3), int(columnBlock*3+3)):
            if board[i][j] == num:
                return False
    return True

# Check that the number is okay for a cell
def check_num_is_okay(num, board, row, column):
    return check_block(num, board, row, column) and check_column(num, board, column) and check_row(num, board, row)

# Finds the next empty cell
def find_first_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j]==0:
                return i,j

    return -1, -1

# Main sudoku solver function
def solver(board):
    index_i, index_j = find_first_empty(board)

    if(index_i == -1 and index_j == -1):
        return True

    # We will try to put the numbers from 1 to 10
    for i in range(1, 10):
        if check_num_is_okay(i, board, index_i, index_j):
            board[index_i][index_j] = i

            if solver(board) == False: # If next step is false, it means that the number we put is not correct. We make it empty and continue to putting numbers
                 board[index_i][index_j] = 0
                 continue 
            else:
                return True

    # If no number fits the cell, it means that we must step back to correct previous steps. To do that, we return false.
    return False


def sudokuTester():

    board = [[5,3,0,0,7,0,0,0,0],
            [6,0,0,1,9,5,0,0,0],
            [0,9,8,0,0,0,0,6,0],
            [8,0,0,0,6,0,0,0,3],
            [4,0,0,8,0,3,0,0,1],
            [7,0,0,0,2,0,0,0,6],
            [0,6,0,0,0,0,2,8,0],
            [0,0,0,4,1,9,0,0,5],
            [0,0,0,0,8,0,0,7,9]]
    
    board2 = [[2, 5, 0, 0, 3, 0, 9, 0, 1],
            [0, 1, 0, 0, 0, 4, 0, 0, 0],
            [4, 0, 7, 0, 0, 0, 2, 0, 8],
            [0, 0, 5, 2, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 9, 8, 1, 0, 0],
            [0, 4, 0, 0, 0, 3, 0, 0, 0],
            [0, 0, 0, 3, 6, 0, 0, 7, 2],
            [0, 7, 0, 0, 0, 0, 0, 0, 3],
            [9, 0, 3, 0, 0, 0, 6, 0, 4]]

    board3=  [
            [7, 8, 0, 4, 0, 0, 1, 2, 0],
            [6, 0, 0, 0, 7, 5, 0, 0, 9],
            [0, 0, 0, 6, 0, 1, 0, 7, 8],
            [0, 0, 7, 0, 4, 0, 2, 6, 0],
            [0, 0, 1, 0, 5, 0, 9, 3, 0],
            [9, 0, 4, 0, 6, 0, 0, 0, 5],
            [0, 7, 0, 3, 0, 0, 0, 1, 2],
            [1, 2, 0, 0, 0, 7, 4, 0, 0],
            [0, 4, 9, 2, 0, 6, 0, 0, 7]
            ]

    board4 = [
            [0, 0, 5, 3, 0, 0, 0, 0, 0],
            [8, 0, 0, 0, 0, 0, 0, 2, 0],
            [0, 7, 0, 0, 1, 0, 5, 0, 0],
            [4, 0, 0, 0, 0, 5, 3, 0, 0],
            [0, 1, 0, 0, 7, 0, 0, 0, 6],
            [0, 0, 3, 2, 0, 0, 0, 8, 0],
            [0, 6, 0, 5, 0, 0, 0, 0, 9],
            [0, 0, 4, 0, 0, 0, 0, 3, 0],
            [0, 0, 0, 0, 0, 9, 7, 0, 0]
           ]

    # BOARD 1
    if solver(board)==True:
        print("Answer of the first sudoku table: ")
        for i in range(9):
            print(board[i])
    else:
        print("No answer.")
    print("\n")

    # BOARD 2
    if solver(board2)==True:
        print("Answer of the second sudoku table: ")
        for i in range(9):
            print(board2[i])
    else:
        print("No answer.")
    print("\n")

    # BOARD 3
    if solver(board3)==True:
        print("Answer of the third sudoku table: ")
        for i in range(9):
            print(board3[i])
    else:
        print("No answer.")
    print("\n")

    # BOARD 3
    if solver(board4)==True:
        print("Answer of the fourth sudoku table: ")
        for i in range(9):
            print(board4[i])
    else:
        print("No answer.")
    
    print("\n")
    





""" --------------------------------------------------------------  QUESTION 2 ANSWER  --------------------------------------------------------------""" 
""" In this SECOND question, I used Exponentiation by Squaring. Source: https://en.wikipedia.org/wiki/Exponentiation_by_squaring"""

def recursiveExp(X, exp):
    if exp==0:
        return 1

    elif exp%2 == 1:
        return X * recursiveExp(X*X, (exp-1)/2)
    else:
        return recursiveExp(X*X, int((exp)/2))

def testQuestion2():
    print("Enter the base: ")
    base = int(input())
    print("Enter the exponent: ")
    exp = int(input())
    print("The result: ",recursiveExp(base, exp))




def menu():

    while(1):
        print("Which part do you want to test? (1.1 - 1.2 - 2 - 3 are options.)")
        inp = input()

        if inp == "1.1":
            testForDFS()
        
        if inp == "1.2":
            testForBNF()

        if inp == "2":
            testQuestion2()

        if inp == "3":
            sudokuTester()
        
        else:
            print("Please enter valid input!")


menu()