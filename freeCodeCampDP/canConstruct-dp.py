# canConstruct
# from dynamic programming video YT
# https://www.youtube.com/watch?v=oBt53YbR9Kk&t=11470s
# Timestamp: 02:13:45


# no dynamic programming here. brute force, complexity O(n^m) 
# where n = number of words in words in wordBank
#       m = length of target
def canConstructNoDP(target, wordBank):
    
    if target == '':
        return True
    
    for currWord in wordBank:
        if target.startswith(currWord):
            remainingTarget = target[len(currWord):]
            res = canConstructNoDP(remainingTarget, wordBank)
            if res is True:
                return True
            
    return False

# print(canConstructNoDP('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))



# dynamic programming approach here. brute force, complexity O(n * m^2)
# m^2 because of the string slicing  
# where m = number of words in words in wordBank
def canConstructDP(target, wordBank, memo = None):
    
    if memo is None:
        memo = {}

    if target in memo:
        return memo[target]
    
    if target == '':
        return True
    
    for currWord in wordBank:
        if target.startswith(currWord):
            remainingTarget = target[len(currWord):]
            res = canConstructDP(remainingTarget, wordBank, memo)
            memo[target] = res
            if res is True:
                return True
            
    return False



print(canConstructDP('eeeeeeeeeeeee', ['e', 'eee', 'eeee', 'eeeee', 'eeeeeee']))
