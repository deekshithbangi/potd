'''
Given a string consisting of lower case English alphabets, the task is to find the number of distinct subsequences of the string
Note: Answer can be very large, so, ouput will be answer modulo 109+7.

Example 1:

Input: 
s = "gfg"
Output: 
7
Explanation: 
The seven distinct subsequences are "", "g", "f", "gf", "fg", "gg" and "gfg" .
Example 2:

Input: 
s = "ggg"
Output: 
4
Explanation: 
The four distinct subsequences are "", "g", "gg", "ggg".
'''
def distinctSubsequences(self, s):
		# code here 
        dp = [0 for i in range(len(s) + 1)] 
        dp[0] = 1 
        i = 1 
        d = dict() 
        while i < len(dp): 
            dp[i] = (dp[i-1] *2) % (10**9 + 7)
            character = s[i-1] 
            
            if character in d:
                dp[i] -= dp[d[character] - 1]
                
            d[character] = i
            i+=1    
        return dp[-1] % (10 ** 9 + 7) 

'''
create a dp with the length(s) + 1 
set dp[0] to 1 
create a dict 
loop through the string 
set the current_value as previous * 2 
if current character is already in dict then subtract the value of dp[ index of character - 1] 
add character into dict with the i as value 

use (10 ** 9 + 7) -- as answer will be too long and as per question
'''