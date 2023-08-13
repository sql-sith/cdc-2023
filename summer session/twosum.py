from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target: 
                return [i, j];

def twoSumBetter(nums: List[int], target: int) -> List[int]:

    '''
        General principals:
        1. Work backwards
            - think about understanding the problem but designing the
            last step of the solution, and how to get there.
            - ask: how do i get from here to there?
        2. For this problem, i understand:
            - i have a list of integers
            - it can have duplicates
            - it is not sorted
            - there are some constraints we don't care about, but 
            not trivially small, and the numbers aren't necessarily
            trivially small either
            - my takeaway: there's nothing special about this list
            that i immediately see that i can exploit
        3. For this problem, i want to:
            - well, i don't know anything useful about the list until
            i start to read it. that will give me information.
            - i should remember what i read from the list.
            - the method i use to remember this information should
            transform the information into something that i can use 
            to immediately answer this question.
    '''



    dict = {}
    for idx, n in enumerate(nums):
        difference = target - n
        if difference in dict:
            return [dict[difference], idx]
        else:
            dict[n] = idx
    

if __name__ == "__main__":
    print(twoSum([2,7,11,15,3,6], 10))
    print(twoSumBetter([2,7,11,15,3,16], 19))
