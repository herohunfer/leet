class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        m = set()
        words.sort(key = len)
        path = [i for i in range(len(words))]
        result_path = [1]*len(words)
        
        current = 0
        
        result = 0
        while current < len(path):
            #print([words[i] for i in path])
            if words[path[current]] not in m:
                m.add(words[path[current]])
                current_len = len(words[path[current]])
                if result_path[current] > result:
                    result = result_path[current]
                for i in range(path[current]+1, len(words)):
                    i_len = len(words[i])
                    if current_len + 1 == i_len:
                        key = words[i]
                        if key not in m:
                            if self.isPre(words[path[current]], words[i]):
                                path.insert(current+1, i)
                                result_path.insert(current+1, result_path[current]+1)
                    elif current_len+1 < i_len:
                        break
            current += 1
        return result
        
    
    def isPre(self, word1: str, word2: str) -> bool:
        for index in range(len(word2)):
            if word1 == word2[:index] + word2[index+1:]:
                return True
        return False
