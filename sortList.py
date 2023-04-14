import sys, time

List = []
x = True
y = True

def texttime(words):
	for c in words:
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(0.08)
def texttime2(words):
	for c in words:
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(0.01)
def texttime3(words):
	for c in words:
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(0.5)
		
texttime("List sorting\n")

#Def algorithms
def bubble_sortLH(lst):
    for i in range(len(lst)):
        for j in range(len(lst)-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]

def bubble_sortHL(lst):
    for i in range(len(lst)):
        for j in range(len(lst)-1):
            if lst[j] < lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]

def mean(lst):
    if len(lst) == 0:
        return None
    else:
        print(sum(lst) / len(lst))

def total(lst):
    texttime3("...\n")
    print(sum(lst))

def linear(lst, num):
    count = 0
    for i in lst:
        if i == num:
            count += 1
    texttime3("...\n")
    print(count)


#Input list
texttime("How Long is your list?: ")
lenList = int(input())
for i in range(lenList):
    x = 0
    x = i+1
    texttime2(f"Input integer {x}: ")
    preList = int(input())
    List.append(preList)
texttime("List: ")
print(List)



#Bubble/Avg/Total/Linear
def TASK():
    texttime("'BUBBLE', 'AVG', 'TOTAL' or 'LINEAR': ")
    task = input()
    while task == "BUBBLE":
        HLLH = input("High to low 'HL' or low to high 'LH'?: ")
        if HLLH == "LH":
            bubble_sortLH(List)
            texttime3("...\n")
            print(List)
            break
        elif HLLH == "HL":
            bubble_sortHL(List)
            texttime3("...\n")
            print(List)
            break
    while task == "AVG":
        mean(List)
        break
    while task == "TOTAL":
        total(List)
        break
    while task == "LINEAR":
        linearNum = int(input("Enter number: "))
        linear(List, linearNum)
        break
        
    

#Loop
while x:
    time.sleep(0.5)
    texttime("Sort list? 'y' or 'n': ")
    again = input()
    while again == "y":
        if y:
            texttime("\nWhich sort method?\n")
            texttime2("\nBubble sort will put your list in ascending or descending order.")
            time.sleep(0.35)
            texttime2("\nAverage will find the mean average of your list.")
            time.sleep(0.35)
            texttime2("\nTotal will find the sum of your list.")
            time.sleep(0.35)
            texttime2("\nLinear will find how many times a number appears in the list.")
        texttime3("\n...\n")
        TASK()
        y = False
        break
    while again == "n":
        print("Okay, bye!")
        x = False
        break
    
