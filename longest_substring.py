#Given a string, find the length of the longest substring without repeating characters.

#Examples:

#Given "abcabcbb" , the answer is "abc" , which the length is 3.

#Given "bbbbb" , the answer is "b" , with the length of 1.

#Given "pwwkew" , the answer is "wke" , with the length of 3. Note that the answer must be a substring , "pwke" is a subsequence and not a substring.

def print_substring(arr, new_arr):
    t = len(arr) + 1
    arr_mod = arr[1:t:1]
    i=0
    for letter in arr_mod:
        if arr_mod.index(letter)==i:
            new_arr += letter
        i +=1
    print(new_arr)

arr = 'aabbbbjsbjhdvhjbdhsvbdbsgj'
new_arr = ' '
print_substring(arr, new_arr)
