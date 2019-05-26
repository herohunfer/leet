import collections
import itertools
class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        c = collections.Counter(barcodes)
        codes = sorted(c.items(), key=lambda pair: pair[1])
        code_l = codes.pop()
        buckets = [[code_l[0]] for _ in range(code_l[1])]
        # print(buckets)
        pos = 0
        for code in codes:
            for i in range(code[1]):
                buckets[pos].append(code[0])
                pos = (pos+1) % code_l[1]
        return [i for bucket in buckets for i in bucket]
