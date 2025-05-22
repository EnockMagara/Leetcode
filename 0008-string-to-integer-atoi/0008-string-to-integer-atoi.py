class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Define 32-bit integer bounds
        INT_MAX = 2**31 - 1  # 2147483647
        INT_MIN = -2**31     # -2147483648
        
        # Initialize variables
        result = 0
        sign = 1
        i = 0
        
        # Step 1: Skip leading whitespace
        while i < len(s) and s[i] == ' ':
            i += 1
        
        # Step 2: Check for sign
        if i < len(s) and s[i] == '-':
            sign = -1
            i += 1
        elif i < len(s) and s[i] == '+':
            sign = 1
            i += 1
        
        # Step 3: Read digits and build number
        while i < len(s) and s[i].isdigit():
            digit = ord(s[i]) - ord('0')
            
            # Step 4: Check for overflow
            if result > INT_MAX // 10 or (result == INT_MAX // 10 and digit > INT_MAX % 10):
                return INT_MAX if sign == 1 else INT_MIN
            
            result = result * 10 + digit
            i += 1
        
        # Step 5: Apply sign and return
        return sign * result