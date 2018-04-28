class Solution(object):
	def mostCommonWord(self, paragraph, banned):
		"""
		:type paragraph: str
		:type banned: List[str]
		:rtype: str
		"""
		banned_set = set(banned)
		from collections import Counter
		cnt = Counter(re.sub(r"[!?',;.]", "", paragraph).lower().split())
		best, word = 0, ""
		for w in cnt:
			if w not in banned_set and cnt[w] > best:
				word, best = w, cnt[w]
		return word
