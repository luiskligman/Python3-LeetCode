# Bucket Sort Problem

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}  # dictionary to store occurances of each number
        freq = [[] for i in range(len(nums) + 1)]  # make an array of len(nums), because a number could
                                                   # occur n times, or all numbers could be unique and they 
                                                   # all fall under index 1

        for n in nums:  # for each number in the given list
            count[n] = 1 + count.get(n, 0)  # in the count map, if it doesnt exist, return 0, 1 + 0 = 1
                                            # therefore, that number will be added to the list with a value
                                            # of 1, if value is already in list, get its value, 
                                            # value + 1 = new count[n] value, basically increasing it by one

        # in count, the key is the number, the value is the number of occurances

        for key, value in count.items():  # grab each key-value pair from the dictionary
            freq[value].append(key)  # in the array we are saying, how many numbers occur one time, two times
                                     # so if 2 occures 3 times, there will be an array at index 2 in the 
                                     # array, if 1 2 3 all occur 4 times, they will all be stored in an 
                                     # array at index 4

        res = []
        for i in range(len(freq) - 1, 0, -1):  # iterate frequencies in reverse order, this way the first
                                               # numbers we encounter are the most frequent
            # go through all numbers that appeared exactly i times                                   
            for n in freq[i]:  
                res.append(n)  # add this number to our result
                if len(res) == k:  # if we collected k number we are done
                    return res
        
