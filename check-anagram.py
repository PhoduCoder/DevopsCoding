
import sys

def check_anagram(str1, str2):
    list1=[ c for c in str1]
    list2=[ d for d in str2]

    #print (list1, list2)
    if (set(list1)==set(list2)):
        print ("The string {} and {} are anagrams".format(str1, str2))
    else:
        print ("The strings are not anagrams")


if (__name__=="__main__"):
    input=sys.argv[1:]
    string1=input[0]
    string2=input[1]
    check_anagram(string1, string2)
