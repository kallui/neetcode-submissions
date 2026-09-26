class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key=lambda x: x[0])
        res = []
        for s, e in intervals:
            if len(res) > 0 and s <= res[-1][1]: # overlap with the last entry in res
                # update res[-1] end time
                res[-1][1] = max(e, res[-1][1])
            else:
                res.append([s,e])
        return res
