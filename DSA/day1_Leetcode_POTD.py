# LeetCode 20: Valid Parentheses
# Link: https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")": "(", "]": "[", "}": "{"}
        
        for char in s:
            if char in mapping:
                # If stack is not empty and top matches the corresponding opening bracket
                if stack and stack[-1] == mapping[char]:
                    stack.pop()
                else:
                    return False  # Mismatched or unexpected closing bracket
            else:
                # If it's an opening bracket, push it to the stack
                stack.append(char)
                
        # Return True only if the stack is completely empty at the end
        return True if not stack else False


# Driver Code (for running in VS Code)
if __name__ == "__main__":
    sol = Solution()
    
    # Test cases
    test_cases = ["()", "()[]{}", "(]", "([)]", "{[]}"]
    
    for s in test_cases:
        result = sol.isValid(s)
        print(f"Input: '{s}' -> Output: {result}")