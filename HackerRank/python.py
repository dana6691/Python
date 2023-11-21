#%%
# Simple Array Sum
are = [1 ,2, 3, 4, 10, 11]
def simpleArraySum(ar):
    ar_sum =0 
    for i in range(len(ar)):
        ar_sum = ar_sum + ar[i]
    return ar_sum

#%%
# Compare the Triplets
def compareTriplets(a, b):
    bob =0
    alice =0
    for i in range(len(a)):
        if a[i] > b[i]:
            alice +=1
        elif a[i] < b[i]:
            bob +=1
    return alice,bob
compareTriplets([17, 28, 30],[99,16,8])
# %%
# Diagonal Difference
def diagonalDifference(arr):
    arr_sum =0
    arr_sum2 =0
    n = len(arr)
    for i ,j in zip(range(n),range(1,n+1)):
        arr_sum += arr[i][i]
        arr_sum2 += arr[i][-j]
    return abs(arr_sum2-arr_sum)
x = [[11,2,4],
[4, 5, 6],
[10, 8 ,-12]]
diagonalDifference(x)
# %%
# Proportion of Plus Minus Zeros
def plusMinus(arr):
    pos =0
    neg =0
    zero =0
    for i in range(len(arr)):
        sum = len(arr)
        if arr[i] > 0:
            pos +=1
        elif arr[i] < 0:  
            neg +=1  
        else: zero +=1
    print(pos/sum)
    print(neg/sum)
    print(zero/sum)

arr = [-4, 3, -9, 0 ,4 ,1]
plusMinus(arr)
# %%
# Proportion of Plus Minus Zeros (2)
def plusMinus(arr):
    print(len([x for x in arr if x > 0])/len(arr))
    print(len([x for x in arr if x < 0])/len(arr))
    print(len([x for x in arr if x == 0])/len(arr))                                      
arr = [-4, 3, -9, 0 ,4 ,1]
plusMinus(arr)
# %%
n = int(input().strip())
arr = [1 if int(temp)>0 else -1 if int(temp)<0 else 0 for temp in input().strip().split(' ') ]
print("{0:.6f}".format(arr.count(1)/n))
print("{0:.6f}".format(arr.count(-1)/n))
print("{0:.6f}".format(arr.count(0)/n))
# %%
# Staircase
# n = 6
     #
    ##
   ###
  ####
 #####
######
# plus on print to not having any space between two
def staircase(n):
    for i in range(n):
        print(" "*(len(range(n))-i-1)+ "#"*(i+1))
    
staircase(5)
# %%
# Remove Mini-Max and Sum
def miniMaxSum(arr):
    maxx=0
    minn=0
    for i in range(len(arr)):
        if arr[i] < max(arr):
            maxx = maxx + arr[i]
        if arr[i] > min(arr):
            minn = minn + arr[i]
        if max(arr) == min(arr):
            maxx = (len(arr)-1)*arr[0]
            minn = (len(arr)-1)*arr[0]
    print(maxx,minn)
arr = [1,2,3,4,5]
miniMaxSum(arr)
# %%
# Remove Mini-Max and Sum (2)
def miniMaxSum(arr):
    maxx = sum([i for i in arr]) - min(arr)
    mini = sum([i for i in arr]) - max(arr)
    print(maxx,minn)
arr = [1,2,3,4,5]
miniMaxSum(arr)
# %%
# B-day cake; count max number
def birthdayCakeCandles(candles):
    return candles.count(max(candles))
birthdayCakeCandles([3,2,1,3])
# %%
#Time conversion
def timeConversion(s):
    if s[8:10] == "AM" and s[0:2] != "12":
        return s[0:8]
    elif s[8:10] == "AM" and s[0:2] == "12":
        return "00" + s[2:8]
    elif s[8:10] == "PM" and s[0:2] == "12":
        return "12" + s[2:8]
    elif s[8:10] == "PM" and s[0:2] != "12":
        return str(int(s[0:2])+12) + s[2:8]

timeConversion("07:05:45PM")
# %%
#Time conversion
def timeConversion(s):
    if s[8:10] == "AM" and s[0:2] != "12":
        return s[0:8]
    elif s[8:10] == "AM" and s[0:2] == "12":
        return "00" + s[2:8]
    elif s[8:10] == "PM" and s[0:2] == "12":
        return "12" + s[2:8]
    elif s[8:10] == "PM" and s[0:2] != "12":
        return str(int(s[0:2])+12) + s[2:8]

timeConversion("07:05:45PM")
# %%
def findStrings(w, queries):
    for i in range(len(w)):
       print(w[i])
    
findStrings(["a", "aa", "aab", "ab", "b"] )
# %%
5-2 = 3
5-1 = 4
0-2 = 8
0-1 = 9


#%%
list = [75,67,40,33]
for i in range(len(list)):
    if list[i]%10 = 3 or list[i]%10 = 8:
        return list + 2
    if list[i]%10 = 4 or list[i]%10 = 9:
        return list + 1
    print(list[i]%10)
# %%
def gradingStudents(grades):
    for i in range(len(grades)):
        if grades[i] >= 40 and grades[i]%10== 3:
            return grades[i] + 2
list = [75,67,40,33]
gradingStudents(list)
# %%
# round up grade, if difference is less than 3
# no round up if grade < 40
def gradingStudents(grades):
    for i in range(len(grades)):
        if grades[i] >= 40 and grades[i]%10 in [3,8]:
            print(grades[i]+2)
        elif grades[i] >= 40 and grades[i]%10 in [4,9]:
            print(grades[i]+1)
        elif grades[i] < 33:
            pass
        else:
            print(grades[i])
list = [4,73,67,38,33]
gradingStudents(list)
# %%
def gradingStudents(grades):
    for i in range(len(grades)):
        if grades[i] >= 38 and grades[i]%10 in [3,8]:
            print(grades[i]+2)
        elif grades[i] >= 38 and grades[i]%10 in [4,9]:
            print(grades[i]+1)
        elif grades[i] < 38:
            pass
        else:
            print(grades[i])
list = [4,73,67,38,33]
gradingStudents(list)
# %%
def gradingStudents(grades):
    for i in range(len(grades)):   
        if grades[i] >= 38:
            if grades[i] % 5 == 3:
                print(grades[i]+2)
            elif grades[i] % 5 == 4:
                print(grades[i]+1)
        elif grades[i] < 38:
            pass
        else:
            print(grades[i])
list = [4,73,67,38,33]
gradingStudents(list)
# %%
