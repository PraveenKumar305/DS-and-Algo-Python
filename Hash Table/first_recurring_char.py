#Google Question

# Given an array = [2,5,1,2,3,5,1,2,4]:
# Return 2

# Given an array = [2,1,1,2,3,5,1,2,4]:
# Return 1

# Given an array = [2,3,4,5]:
# Return undefined/None

# naive: O(n^2), SC: O(1)
def first_recurring_char(input):
    for i in range(len(input)):
        for j in range(i-1,0,-1):
            if input[i] == input[j]:
                return input[i]
    return None

#print(first_recurring_char([2, 5, 1, 2, 3, 5, 1, 2, 4]))

# optimized: O(n), SC: O(n) now because of hash_table

def first_recurring_char2(input):
    hash_table = dict()
    for i in input:
        #print(hash_table)
        if i in hash_table != None:
            return i
        else:
            hash_table[i] = i
    #print(hash_table)
    return None

array = [2, 5, 5, 2, 3, 5, 1, 2, 4]
array2 = [2, 1, 1, 2, 3, 5, 1, 2, 4]
array3 = [2, 3, 4, 5]
#print(first_recurring_char(array3))