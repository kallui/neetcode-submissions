class Solution:

    def encode(self, strs: List[str]) -> str:
            # "4#leet4#code"
            res = ""

            for s in strs:
                res += f"{len(s)}#{s}"
            print (res)
            return res
    def decode(self, s: str) -> List[str]:
        res = []

        i = 0
        while i < len(s):
            sizeStr = ""
            # 5#Hello5#world
            # 01234567

            # 2#we3#say1#:3#yes10#!@#$%^&*()
            # 
            # get number before #
            while s[i] != '#':
                sizeStr += s[i]
                i +=1
            i += 1 # skip hashtag
            size = int(sizeStr)
            print(size)

            tmp = ""
            for j in range(size):
                tmp += s[i+j]
            print(tmp)
            res.append(tmp)
            i += size


        return res

            
