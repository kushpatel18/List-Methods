import math as m
from enum import Enum

def len_list(l):

    return  len(l)


def append_list(l):

    n=int(input("\nEnter the element to be inserted at last: "))
    l.append(n)

    print("Updated List: ",l)


def F3(l,len):

    print("\nFirst 3 elements of list are: ")
    if(len<3):
        print("Invalid Request! Inadequate Length")
    else:
        print(l[0:3])
        # for i in range(0,3):
        #     print(l[i])

def L3(l,len):

    print("\nLast 3 elements of list are: ")
    if(len<3):
        print("Invalid Request! Inadequate Length")
    else:
        print(l[len-3:len])
        # for i in range (len-3,len):
        #     print(l[i])

def M3(l,len):

    print("\nMiddle 3 elements of list are: ")
    if(len<5):
        print("Invalid Request! Inadequate Length")
    else:
        mid=m.floor(len/2)
        print(l[mid-1:mid+2])
        # for i in range(mid-1,mid+2):
        #     print(l[i])

def Reverse(l):

    rev_lst=l[::-1]
    print("\nReversed List is:\n",rev_lst)

def Trimmed_List(l,len):

    print("\nTrimmed List:")
    if(len<2):
        print([])       #Empty String
    else:
        print(l[1:len-1])

def is_Present(l,target):

    if(target in l):
        print(f"\nFirst Occurrence of element {target} in the list is at index {l.index(target)} ")
    else:
        print(f"\nElement {target} is not present in the list")

def Count_Occur(l,multiple):

    if(multiple in l):
        print(f"\nElement {multiple} occurs a total of {l.count(multiple)} time(s) in the list")
    else:
        print(f"\nElement {multiple} does not occur even once in the list")

def Sort(l,n):

    class Order(Enum):
        ASC=0
        DESC=1

    if(n==Order.ASC.value):
        l.sort()
        print("\nList in Ascending order: ",l)
    elif(n==Order.DESC.value):
        l.sort()
        l.reverse()
        print("\nList in Descending Order: ",l)
    else:
        print("Invalid Input! Choose correct Sorting Order ")


def MIN_MAX(l,n):

    class Min_Max(Enum):
        MIN=0
        MAX=1

    if(n==Min_Max.MIN.value):
        print("\nElement with Minimum Value: ",min(l))
    elif(n==Min_Max.MAX.value):
        print("\nElement with Maximum Value: ",max(l))
    else:
        print("Invalid Input! Try Again with Correct Input")

def SUM_AVG(l,len,a):

    class Sum_Avg(Enum):
        SUM=0
        AVG=1

    if(a==Sum_Avg.SUM.value):
        print("\nSum of all elements of the list: ",sum(l))
    elif(a==Sum_Avg.AVG.value):
        print("\nAverage of all elements of the list: ",sum(l)/len)
    else:
        print("Invalid Input! Try Again with Correct Input")

def Make_Unique(l):

    l2=set(l)
    l3=list(l2)

    print("\nList with non-duplicate values are: ",l3)

def Sort_Criteria(n,crit):

    size=int(input("\nEnter the no. of elements of list of strings: "))
    list2=[]

    for i in range(0,size):
        str=input("Enter string element: ")
        list2.append(str    )

    class Order(Enum):
        ASC=0
        DESC=1

    class Criteria(Enum):
        LEN=0
        CHAR_COUNT=1
        VOWEL_COUNT=2

    if(crit==Criteria.LEN.value):

        print("\nList Sorted by Length of Element")

        def Length(list2):
            return  len(list2)

        if(n==Order.ASC.value):
            list2.sort(key=Length)
            print("List in Ascending order: ",list2)
        elif(n==Order.DESC.value):
            list2.sort( reverse=True ,key=Length)
            print("List in Descending Order: ",list2)
        else:
            print("Invalid Input! Choose Correct Sorting Order")

    elif(crit==Criteria.CHAR_COUNT.value):

        print("\nList Sorted by Character Count")
        char=input("Enter a character to determine a specific sort order: ")

        def Count_char(ele):
            return ele.count(char)

        if(n==Order.ASC.value):
            list2.sort(key=Count_char)
            print("List in Ascending order: ",list2)
        elif(n==Order.DESC.value):
            list2.sort(reverse=True,key=Count_char)
            print("List in Descending Order: ",list2)
        else:
            print("Invalid Input! Choose Correct Sorting Order")

    elif(crit==Criteria.VOWEL_COUNT.value):

        print("\nList Sorted By Vowel Count")
        def Vowel_Count(ele):
            total=0
            for vowel in "aeiou":
                total+=ele.count(vowel)
            return total

        if(n==Order.ASC.value):
            list2.sort(key=Vowel_Count)
            print("List in Ascending order: ",list2)
        elif(n==Order.DESC.value):
            list2.sort(reverse=True, key=Vowel_Count)
            print("List in Descending Order: ",list2)
        else:
            print("Invalid Input! Choose Correct Sorting Order")

    else:

        print("\nInvalid Input! No other criterias available")

def Search(l,len,val):

    if val in l:
        print(f"\nElement {val} is present  at index {l.index(val)} in the list")
    else:
        print(f"\nElement {val} is not present in the list")

def Split_Lists(l,len):

    print("\nSplitting A List Into Two Sublists")
    mid=m.floor(len/2)
    list2,list3=[],[]

    for i in range(0,mid+1):
        list2.append(l[i])

    for j in range(mid+1,len):
        list3.append(l[j])

    print("First Sublist: ",list2)
    print("Second Sublist: ",list3)

def Merge_Lists(l1):

    size=int(input("\nEnter the no. of elements of second list: "))
    l2=[]

    for i in range(0,size):
        str=input("Enter string element: ")
        l2.append(str)

    print("\nMerging Two Lists")
    l3=l1.copy()
    l3.extend(l2)

    print("Merged List: ",l3)


def Remove_element(l,len,val,remove_ele):

    class Remove(Enum):
        FIRST_OCCUR=0
        ALL_OCCUR=1
        DUPLICATE=2

    if val in l:
        if( remove_ele==Remove.FIRST_OCCUR.value):
            l.remove(val)
            print("\nUpdated List: ",l)
        elif( remove_ele==Remove.ALL_OCCUR.value):
            while(l.count(val)!=0):
                l.remove(val)
            print("\nUpdated List: ",l)
        elif(remove_ele==Remove.DUPLICATE.value):
            while(l.count(val)!=1):
                l.remove(val)
            print("\nUpdated List: ",l)
        else:
            print("\nInvalid Input! Specify choice of the no. of occurrences you want to remove ")

    else:
        print(f"\nElement {val} is not present in the list")



def Insert_Element(l,len,choice,ele):

    class Insert_Element(Enum):
        RANDOM=0
        SORTED=1

    if(choice==Insert_Element.RANDOM.value):
        index=int(input("\nEnter the index position where you want to insert the element: "))
        if(index<len | index>(-len)):
            l.insert(index,ele)
            print("Updated List: ",l)
        else:
            print("IndexError! Index Out of Range")

    elif(choice==Insert_Element.SORTED.value):

        class Order(Enum):
            ASC=0
            DESC=1

        print("\n---------------------------------------------------------------------------------------------------------")
        print("Choice Values for Sorting Order:")
        print("\tAscending Order  : 0")
        print("\tDescending Order : 1")
        print("---------------------------------------------------------------------------------------------------------")

        order=int(input("\nEnter a value to determine sort order: "))

        if(order==Order.ASC.value):
            l.insert(-1,ele)
            l.sort()
            print("Updated List in Ascending Order: ",l)

        elif(order==Order.DESC.value):
            l.insert(-1,ele)
            l.sort()
            l.reverse()
            print("Updated List in Descending Order: ",l)

        else:
            print("Invalid Input! Choose Sort Order carefully")

    else:
        print("\nInvalid Input! Try Again")



def Pop_Element(l,len,choice):

    class Pop_index(Enum):
        LAST_INDEX=0
        RANDOM=1

    if(choice==Pop_index.LAST_INDEX.value):
        print(f"\nPopped element from the list: {l.pop()}")
        print("Updated List:",l)

    elif(choice==Pop_index.RANDOM.value):
        index=int(input("\nEnter the index postion from where the element is to be removed: "))
        if(index<len | index>= (-len)):
            print(f"Popped element from the list: {l.pop(index)}")
            print("Updated List:",l)
        else:
            print("Invalid Input! Index Bound Out of Range")

    else:
        print("\nInvalid Input! Try Again with an Available Choice")
