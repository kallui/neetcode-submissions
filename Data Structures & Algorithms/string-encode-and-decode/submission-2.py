class Solution:

    def encode(self, strs: List[str]) -> str:
        r =""
        # strs = ["Hello","World"]
        for x in strs:
            # x = "Hello"
            r += f"{len(x)}#{x}"
        return r
    def decode(self, s: str) -> List[str]:
        r = []
        i = 0

        # s = 5#Hello15#Worldasdasdasd
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            
            length = int(s[i:j]) # inc ase of 2 numbers
            i = j + 1
            j = i + length
            
            r.append(s[i:j])
            i = j 
        return r