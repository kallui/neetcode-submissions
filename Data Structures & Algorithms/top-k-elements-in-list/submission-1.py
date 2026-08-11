class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket sort
        # count list[n]

        # [1,2,2,3,3,3]
        # count list = 0,1,2,3,4,5,6
        #              [,1,2,3,,,   ]
        
        freq = {}

        for n in nums:
            if n in freq:
                freq[n] +=1
            else:
                freq[n] = 1
        
        countList = [[] for i in range(len(nums)+1)] # 2D array of countList[n]
        for key, v in freq.items():
            countList[v].append(key)
        
        res = []
        for i in range(len(countList)-1, 0 , -1): # range(start,stop,step)
            if len(countList[i]) > 0:
                for j in countList[i]:
                    res.append(j)
                    if len(res) == k:
                        return res
        
            