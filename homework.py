#8kyu
# Time Complexity- O(1 + 1) => O(1)
# Space Complexity- O(1)

def even_or_odd(number):
    if number % 2 == 0: #O(1)
        return "Even" 
    else:               #O(1)
        return "Odd"
    
even_or_odd(12)

# 8kyu
# Time Complexity-O(1 + 1) => O(1)
# Space Complexity- O(1)

def bool_to_word(boolean):
    
    if boolean == True: #O(1)
        return "Yes"
    
    elif boolean == False: #O(1)
        return 'No'
    
bool_to_word(True)

# 6kyu
# Time Complexity - O(n + 1) + O(n + 1) => O(2n + 2) => O(n)
#Space Complexity - O(n + 1) + O(2) + O(n +1) => O(n)
def solution(s): #O(1)
    list_a = [] #O(n)
    
    if len(s) % 2 != 0: #O(1)
        s += "_"   #O(1)
        
    for char in range(0, len(s), 2): #O(n)
        list_a.append(s[char : char  +2]) #O(1)
    return list_a

solution("asdfg")