# allConstruct
# from dynamic programming video YT
# https://www.youtube.com/watch?v=oBt53YbR9Kk&t=11470s
# Timestamp: 05:10:01


# ------------------ i guess this is top down approach ----------------------
ansFin = []
def allConstruct(target, wordBank, currList = []):

    if target == '':
        return True
    
    for currWord in wordBank:
        if(target.startswith(currWord)):
            currList += [currWord]
            remainingTarget = target[len(currWord):]
            res = allConstruct(remainingTarget, wordBank, currList)
            if res == True:
                ansFin.append(currList.copy())
            currList.pop()


allConstruct('abcdef', ['ab', 'cd', 'cde', 'ef', 'def', 'abcd', 'f'])
# allConstruct('purple', ['purp', 'p', 'ur', 'le', 'purpl'])
# allConstruct('happ', ['cat', 'p', 'dog', 'le', 'mouse'])  # this should give [[]] but gives []
print(ansFin)


# ------------ approach in the video ----------------------------------------------
# this gives the o/p, but return early hence only gives one occurance
# not all

ansFin = []
def allConstruct(target, wordBank):
    if target == '':
        return []
    currList = []
    for currWord in wordBank:
        if(target.startswith(currWord)):
            remainingTarget = target[len(currWord):]
            res = allConstruct(remainingTarget, wordBank)

            if res is not None:
                currList += [currWord] + res
                return currList
    print(ansFin)
    ansFin.append(currList)

print('ths gives one occurance only coz of early return')
print(allConstruct('abcdef', ['ab', 'cd', 'cde', 'ef', 'def', 'abcd', 'f']))
# print(ansFin)


#----------------- from gemini and this works -_- --------------------------------------
# without DP
# check the explaination in the chat: https://g.co/gemini/share/479ee118861d


def allConstruct(target, wordBank):
    if target == "":
        return [[]]  # Base case: empty target has one combination (the empty list)
    
    all_combinations = []
    for word in wordBank:
        if target.startswith(word):
            remaining = target[len(word):]
            remaining_combinations = allConstruct(remaining, wordBank)
            for combo in remaining_combinations:
                all_combinations.append([word] + combo)  
            print(all_combinations)

    return all_combinations

result = allConstruct('abcdef', ['ab', 'cd', 'cde', 'ef', 'def', 'abcd', 'f'])
print(result)


# ----------------- gemini solution with DP --------------------------

def allConstruct(target, wordBank, memo=None):
    if memo is None:
        memo = {}  # Initialize memoization dictionary

    if target == "":
        return [[]]  # Base case: empty target has one combination (the empty list)
    
    if target in memo:
        return memo[target]  # Use memoized result if available
    
    all_combinations = []
    for word in wordBank:
        if target.startswith(word):
            remaining = target[len(word):]
            remaining_combinations = allConstruct(remaining, wordBank, memo)
            for combo in remaining_combinations:
                all_combinations.append([word] + combo)  # Add current word to each combination

    memo[target] = all_combinations  # Store result for memoization
    return all_combinations

# result = allConstruct('aaaaaa', ['a', 'aaa', 'aaaa', 'aaaaaa'])
# print(result)
