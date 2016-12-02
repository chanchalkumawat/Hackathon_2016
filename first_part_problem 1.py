"""
i) Write a function which accepts 2 params - a string and a word and computes the following:

A. Count occurrences of the word in the string
B. Remove that word from string
C. Append same word equal to number of occurrences in string.

"""

import re
s=input("Enter  string  ")
w=input("Enter the word  ")
def count_occurences(s,w):
    counter=0
    a = re.split(r'\W', s)
    counter=a.count(w)
    print ("Occurence of the word in string is %s "%counter)
    for i in s:
        if counter>0:
            s = s.replace(w,"")
    print ("String after the word removal is :  %s "%s)
    st=""
    for i in range(0,counter):
        st=st+w+" "
    print("The string after addition of word is : %s "%s+""+st)

count_occurences(s,w)












# s="abc daa asd"
# w="a"
# def count_occurence(s,w):
#     count=0
#     for i in s:
#         if i==w:
#             count+=1
#     return count
#
# print(count_occurence(s,w))
