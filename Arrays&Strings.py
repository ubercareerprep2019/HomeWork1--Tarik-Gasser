#This function takes two strings and returns true if one string is a permutation of
#the other, false otherwise.
def isStringPermutation(s1, s2):
    #check for if string are not equal in length this results in faster run time in somecases
    if(len(s1) != len(s2)):
        return False
    # sorted() python function used to lexicographical order strings
    # to handle case sensitive strings use python .lower() function
    sortedS1 = sorted(s1.lower())
    sortedS2 = sorted(s2.lower())
    #compared
    if (sortedS1 == sortedS2):
        return True
    else:
        return False
# this answer is great, but one can argue that its O(n^2) because of the if all stattment
    if all(x in sortedS1 for x in sortedS2):
      return True
    else:
      return False
    # this answer runs O(nlogn)
    for i in range(len(sortedS1)):
        if(sortedS1[i] != sortedS2[i]):
            return False

    return True


#even with using dictionaries it wouldnt decrease the time complexity
def pairsThatEqualSum(inputArray,targetSum):
    answer = []
    for i in inputArray:
        if (targetSum-i in inputArray):
            answer.append([i, targetSum-i])
            inputArray.remove(i)
    
    return answer
#worstcase runtime is O(n) or O(n^2) - becasue of if statement in for loop that has a python equivalent to .contains() check

#Method 1 Tests
print(isStringPermutation("Ernest", "nester"))
print(isStringPermutation("dad", "add"))
print(isStringPermutation("dog", "cat"))
print(isStringPermutation("dogg", "dog"))
#Method 2 Tests
nums1 = [1,2,3,4,5,6,7,8,9]
nums2 = [1,2,3,4,5,6,7,8,9]
nums3 = [1,2,3,4,5,6,7,8,9]
nums4 = [9,7,5,3,1]
print(pairsThatEqualSum(nums1,10))
print(pairsThatEqualSum(nums2,0))
print(pairsThatEqualSum(nums3,1))
print(pairsThatEqualSum(nums4,10))