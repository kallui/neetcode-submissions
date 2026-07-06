class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}

        for x in nums:
            if x in dic:
                dic[x] += 1
            else:
                dic[x] = 1
        
        sortedDic = sorted(dic.items(), key=lambda item:item[1], reverse=True)


        return [item[0] for item in sortedDic[:k]]
