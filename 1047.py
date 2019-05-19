class Solution:
    def removeDuplicates(self, S: str) -> str:
        pos = 0
        while pos < len(S)-1:
            if S[pos] == S[pos+1]:
                # j = pos+1
                # while j < len(S) and S[pos] == S[j]:
                #     j += 1
                S = S[:pos] + S[pos+2:]
                if pos > 0:
                    pos -= 1
            else:
                pos += 1
        return S
