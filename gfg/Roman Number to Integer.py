'''
Given a string in roman no format (s)  your task is to convert it to an integer . Various symbols and their values are given below.
I 1
V 5
X 10
L 50
C 100
D 500
M 1000

Example 1:

Input:
s = V
Output: 5
Example 2:

Input:
s = III 
Output: 3
Your Task:
Complete the function romanToDecimal() which takes a string as input parameter and returns the equivalent decimal number. 

Expected Time Complexity: O(|S|), |S| = length of string S.
Expected Auxiliary Space: O(1)

Constraints:
1<=roman no range<=3999
'''
class Solution:
    def romanToDecimal(self, s):
        roman = {'I': 1, 'V' : 5, 'X' : 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000} 
        res = 0 
        
        for i in range(len(s)):
            if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]:
                res -= roman[s[i]] 
            else:
                res += roman[s[i]] 
        return res
    
'''
subtract - if current is less than the nextone
add - if current is greater than the nextone 
test-case
CMXCVIII
998
'''
