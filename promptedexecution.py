def printPuzzleList(list):
    print("_____________________________________")
    for a in list:
        print("| ", end = "")
        for b in a:
            print((b) + " | ", end = "")
        print()
        print("|___|___|___|___|___|___|___|___|___|")
def printMatrix(mat):
    print("_____________________________________")
    for a in mat:
        print("| ", end = "")
        for b in a:
            print((b), "| ", end = "")
        print()
        print("|___|___|___|___|___|___|___|___|___|")
def numDifferences(mat1, mat2):#9x9's only
    count = 0
    for i in range(0,9):
        for j in range (0,9):
            if mat1[i][j] != mat2[i][j]:
                count += 1
    return count
def getBoxNumber(a, b): #a = row, b = column
    if a < 3:
        if b < 3:
            return 0
        elif b < 6:
            return 1
        else:
            return 2
    elif a < 6:
        if b < 3:
            return 3
        elif b < 6:
            return 4
        else:
            return 5
    else:
        if b < 3:
            return 6
        elif b < 6:
            return 7
        else:
            return 8
def getMissingRowCol(arr):
    whole = [1,2,3,4,5,6,7,8,9]
    for a in arr:
        if a != 0:
            whole.remove(a)
    return whole
def getColumn(mat, num):
    return_arr = []
    for a in mat:
        return_arr.append(a[num])
    return return_arr
def setDesiredBox(mat):
    box_arr = []
    for i in range(0,9,3): #getting boxes from matrix
        for j in range(0,9,3):
            box = []
            for l in range(0,3):
                for k in range(0,3):
                    box.append(mat[i+k][j + l])
            box_arr.append(box)
    desiredboxarr = []
    for a in box_arr:
        desiredboxarr.append(getMissingRowCol(a))
    return desiredboxarr
def checkAndAdd(array1, array2): #checks if elements from array1 are in array2, and adds them to array2 if they are not
    return_arr = array2
    for a in array1:
        isIn = False
        storeVal = 0
        for b in array2:
            if b == a:
                isIn = True
        if isIn == False:
            return_arr.append(a)

def checkAllColumns(col, des_col, value):
    unique = True
    for a in des_col: #loops through arrays of desired_by_col
        if des_col.index(a) != col: #skips desired column we're checking against
            for b in a:     #looping through each individual arary of desired values
                if value == b: #if our value is present
                    unique = False
    return unique

def find_blank(mat):
    x = 0
    index = [-1,-1]
    for a in mat:
        y = 0
        for b in a:
            if b == 0:
                index = [x,y]
                return index
            y+= 1
        x+= 1
    return index
def check_unused(mat,row,col, num):
    clear_r = num not in row
    clear_c = num not in getColumn(mat,col)
    #clear_b = num not in

#Loop that actually works
def backtrackWhile(mat, des_row, des_col, des_box):
    cloneMat = mat.copy() #Doesn't actually work 'cause python hates copying lists
    attempted = [] #holds tested values
    for i in range (0,9):
        attempted.append([])
        for j in range(0,9):
            attempted[i].append([])
    given = [] #matrix that tracks which values are the base of the puzzle
    for i in range(0,9):
        given.append([])
        for j in range(0,9):
            if cloneMat[i][j] != 0:
                given[i].append(True)
            else:
                given[i].append(False)
    fixPrev = False #Bool to determine if the loop should go forward or backwards
    i = 0
    while i < 9:
        j = 0
        while j < 9:
            boxNum = getBoxNumber(i,j)

            if cloneMat[i][j] != 0:
                if fixPrev == True and (not given[i][j]): #not attempted[i][j]:
                    des_row[i].append(cloneMat[i][j])
                    des_col[j].append(cloneMat[i][j])
                    des_box[boxNum].append(cloneMat[i][j])
                    cloneMat[i][j] = 0
                    fixPrev = False

                    #clear attempts of everything below
                    for a in range(i,9):
                        if a == i:
                            for b in range(j+1,9):
                                while attempted[a][b]:
                                    c = attempted[a][b].pop(0)
                                    #print("removing",c,"from attempted[%2d][%2d]"%(a,b))
                        else:
                            for b in range(0,9):
                                while attempted[a][b]:
                                    c = attempted[a][b].pop(0)
                                    #print("removing",c,"from attempted[%2d][%2d]"%(a,b))
            if cloneMat[i][j] == 0:
                found = False
                for a in des_row[i]:
                    for b in des_col[j]:
                        for c in des_box[boxNum]:
                            if a == b and a == c:
                                hasBeenTested = False
                                for k in attempted[i][j]:
                                    if a == k:
                                        hasBeenTested = True
                                if hasBeenTested == False:
                                    cloneMat[i][j] = a
                                    des_row[i].remove(a)
                                    des_col[j].remove(a)
                                    des_box[boxNum].remove(a)
                                    attempted[i][j].append(a)
                                    #print("Trying ", a)
                                    found = True
                            if found:
                                break
                        if found:
                            break
                    if found:
                        break

            #At this point if there are no values present, the current solution is invalid.
            #Or, if fixPrev == True, then the current value is a given and should be skipped over.
            #Either way, backtrack.

            if cloneMat[i][j] == 0 or fixPrev == True:
                #print("Backtracking...")
                fixPrev = True
                if j == 0:
                    if i != 0:
                        i -= 1
                        j = 7
                        #print("New i:", i,"New j:",j)
                    else:
                        #print("no solution")
                        return -1
                else:
                    j -= 2 #Accounts for the += 1 in line below
            j += 1
        i += 1
    return cloneMat

raw = input("Enter puzzle. Rows deliminated by spaces: ")
#test case: 000107460 078000502 000000810 056073000 702608309 000540780 084000000 507000630 029806000
puzzlelist = raw.split(" ")
printPuzzleList(puzzlelist)

matrix = [] #holds puzzle, 0s represent missing digit

#Converting strings to ints, storing in matrix
for a in puzzlelist:
    toInts = []
    for b in a:
        toInts.append(int(b))
    matrix.append(toInts)

#2d arrays storing missing values in matrix
desired_by_row = []
desired_by_col = []
desired_by_box = []

#determining values and storing in correct 2d arrays
for a in matrix:
    desired_by_row.append(getMissingRowCol(a))
for i in range(0,9):
    desired_by_col.append(getMissingRowCol(getColumn(matrix, i)))
desired_by_box = setDesiredBox(matrix)
#print (desired_by_box)

bt_test = backtrackWhile(matrix, desired_by_row, desired_by_col, desired_by_box)
printMatrix(bt_test)
print()

# Easy Puzzles and solutions

    #1   090802750 000003164 300000009 014000000 200000300 530100000 000010020 980040000 020050007
    #
    #2   030020040 060000900 000000050 890003000 106048003 000001480 301007600 009000000 000010524
    #
    #3   000000200 710900580 009200460 008607040 004050010 001400002 020000097 900000800 000806000
    #
    #4   734100000 090207350 100009000 000403010 000095002 000800004 402080600 000700040 650000000
    #
    #5   703020050 040090001 000000004 000602000 001005000 000400102 000907030 302058060 008060017
    #
    #6   103060000 500702900 080000240 390500060 060000054 000400300 000079580 000050400 070000032
    #
    #7   000360000 036070050 008005009 080000340 007500000 042097000 000040090 700001203 195080000
    #
    #8   000340000 006008054 050690020 003700000 000206008 100000000 890000017 600509000 024030000
    #
    #9   020100035 090570040 004090060 100080009 000000000 036000000 200000000 380209001 009306070
    #
    #10  000706023 600001500 000050407 000002006 020607001 080900050 400100900 050029000 000000300
    #

# Medium Puzzles and solutions
    #1   080060000 003800579 000500000 209000030 000600010 000047600 018070000 000400800 000000029
    #
    #2   002000040 130000000 000020007 800100000 200000059 000009004 004001090 320000000 700504003
    #
    #3   090010020 560020000 000300000 003900000 000400567 200000013 008600001 000000032 000000450
    #
    #4   060090000 100300008 300002000 000080010 004005080 630070500 050030060 000000007 900050403
    #
    #5   001000090 000009000 020003057 000960000 003082000 004007008 970000000 060000800 000500160
    #
    #6   000602004 908000002 000000300 000900070 005000010 000324000 100000020 650070000 040008700
    #
    #7   080000094 005207006 300000000 193000400 000005800 060030000 024000003 000061080 000000000
    #
    #8   300000650 400320000 000008900 006005100 008000000 000274000 000100003 050007000 000902006
    #
    #9   000060000 805700060 020001700 042000000 010800000 000050040 009010000 004000806 000903050
    #
    #10  000000084 050009001 800005000 307000000 060800000 008000042 021000005 403000020 000090600
    #

# Hard Puzzles and solutions
    #1   000050810 040000000 080000000 000070000 100300070 920408300 000000100 208000904 070609000
    #
    #2   790000200 080002004 060490000 000600000 020000041 000005002 005000008 900000010 400300090
    #
    #3   125400000 000008040 000000100 000005360 200000000 000073800 080307009 004000000 059000018
    #
    #4   005060049 000023000 080007000 050800002 700000030 090004000 900000650 000000004 040590300
    #
    #5   000008000 000040057 003006040 602000000 400500030 070010005 001080060 000000809 700000400
    #
    #6   600700009 008040000 500000026 000007530 002100090 900000040 000908000 007350000 001000080
    #
    #7   008902000 041076000 200004730 002090603 000007400 000580000 000720010 010008200 000000567
    #
    #8   700085000 000001004 000300200 800017000 000000409 000060080 020000093 080009001 000400002
    #
    #9   200000000 000030400 000010793 700006030 003000670 510008000 000007500 000003061 460500000
    #
    #10  810000004 000040008 004005700 180900000 009070000 000000100 000090200 090700060 000803501
    #
#
