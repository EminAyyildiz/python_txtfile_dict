

import sys
from collections import defaultdict


filename = input("Enter the name of the file:")
output_file = open(filename, 'r')
counts_for_word = dict()
#we create the dictionary we will create
for line in output_file :

    words = line.split()

    for word in words:

        if word not in counts_for_word :

            counts_for_word [word] = 1

        else:

            counts_for_word [word] += 1
#Our for loop, where we assign each word separately to the dictionary as a variable and then calculate how many times these words are used in the file.

dict_1 = counts_for_word 
#here I am copying the dictionary I created above to the new dictionary I created with my last name
print(dict_1)

dict_1[","]
