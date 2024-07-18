# countConstruct
# from dynamic programming video YT
# https://www.youtube.com/watch?v=oBt53YbR9Kk&t=11470s
# Timestamp: 02:38:58

# this program prints total number of ways target can be created 
# using wordBank

def countConstructNoDP(target, wordBank):

    if target == '':
        return 1
    ans = 0
    for currWord in wordBank:
        if(target.startswith(currWord)):
            remainingTarget = target[len(currWord):]
            res = countConstructNoDP(remainingTarget, wordBank)
            ans += res
    return ans

# suppose if we had to count or add the value at each stage, like 1+1+1+1 at each level, then
# init ans = 1, and then see the o/p 
# for countConstructNoDP('abcdef', ['ab', 'cd', 'ef', 'def', 'abcd']) we get 6, which
# basically counts number of hops

print(countConstructNoDP('abcdef', ['ab', 'cd', 'cde', 'ef', 'def', 'abcd', 'f']))


def countConstructDP(target, wordBank, memo = None):

    if memo is None:
        memo = {}

    if target in memo:
        return memo[target]
    if target == '':
        return 1
    ans = 0
    for currWord in wordBank:
        if(target.startswith(currWord)):
            remainingTarget = target[len(currWord):]
            res = countConstructDP(remainingTarget, wordBank, memo)
            memo[target] = res
            ans += res
    return ans


print(countConstructDP('eeeeeeeeeeeeeee', ['e', 'eee', 'eeeee', 'eeeeee', 'eeeeeeeee']))