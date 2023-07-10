# canSum
# from dynamic programming video YT
# https://www.youtube.com/watch?v=oBt53YbR9Kk&t=11470s
# https://leetcode.com/playground/kNComULY
# Timestamp: 01:09:56
# A slight different approach.

def func(target, numbers, memo = None):
    if(target in memo):
        return memo[target]
    if(target == 0):
        return True
    if(target < 0):
        return False
    res = False
    for currNum in numbers:
        remainingSum = target - currNum
        memo[target] = func(remainingSum, numbers, memo)
        res = res or func(remainingSum, numbers, memo)
    return res
        
        
        
print(func(7,[5,4,3,7]))
print(func(7,[2,4]))
print(func(8,[2,3,5]))
print(func(300,[7,14]))
