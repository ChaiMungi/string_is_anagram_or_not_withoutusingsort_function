


import sys


def main():
    str1=sys.argv[1]
    str2 =sys.argv[2]
    unique_str = set(sys.argv[1])
    unique_str2 = set(sys.argv[2])
    for chr in unique_str2:
        if str2.count(chr) == str1.count(chr):
	    i=1
        else:
            i=0
            break   

    if i==1:
       print("\nstring is anagram")
    elif i==0:
       print("\nstring is not anagram") 
    


if __name__ == "__main__":
     main()

#if set(str.lower()) == set(str2.lower()):
#    print("The strings are anagrams.")
#else:
#        print("The strings aren't anagrams.")
