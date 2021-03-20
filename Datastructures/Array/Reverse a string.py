# A string is given. We have to print the reversed string.
# For example, the string is "Hi how are you?"
# The output should be "?ouy era woh iH"

# Metod1 is we can create a new array and append the characters of the original array,
#one by one from the end to the beginning.

def simple_reverse(string):
    my_list = []
    for i in range(len(string)-1, -1, -1): #The for loop runs from the last element to the first element of the original string
        my_list.append(string[i]) #The characters of the original string are added to the new string
    return ''.join(my_list) #The characters of the reversed array are joined to form a string

string = "Hello"
print(simple_reverse(string))
#Since we only have to traverse the string once, the time complexity is O(n)
#But since we are also creating a new array of the same size , the space complexity is also O(n)

# Method2(this method is not that good)
def reverse(string):
    #check input
    if not (string) or len(string) < 2 or not (type(string)):
        return 'hmm thats not good'
    backwards = []
    total_items = len(string) - 1
    for i in range(total_items, -1, -1):
        backwards.append(string[i])
    #print(backwards)
    return ''.join(backwards)


#Apart from these, some built-in functions that can be used to reverse a string are as follows:

string1 = 'abcde'
string2 = reversed(string1)
print(''.join(string2))

list1 = list(string1)
list1.reverse()
print(''.join(list1))

#Both these methods are of O(n) time complexity