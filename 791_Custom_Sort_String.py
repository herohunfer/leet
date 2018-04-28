S and T are strings composed of lowercase letters. In S, no letter occurs more than once.
S was sorted in some custom order previously. We want to permute the characters of T so that they match the order that S was sorted. More specifically, if x occurs before y in S, then x should occur before y in the returned string.
Return any permutation of T (as a string) that satisfies this property.

Example :
Input:
S = "cba"
T = "abcd"
Output: "cbad"
Explanation:
"a", "b", "c" appear in S, so the order of "a", "b", "c" should be "c", "b", and "a".
Since "d" does not appear in S, it can be at any position in T. "dcba", "cdba", "cbda" are also valid outputs.

Note:
S has length at most 26, and no character is repeated in S.
T has length at most 200.
S and T consist of lowercase letters only.

class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        res = ""
        m = [0]*26
        for c in T:
            m[ord(c) - ord('a')] += 1
        for c in S:
            res += c*m[ord(c) - ord('a')]
            m[ord(c) - ord('a')] = 0
        for c in range(26):
            res += (chr(ord('a')+c))*m[c]
        return res

# better solution with sorted
class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        # intialize array to last order
        d = [26]*26
        for i,v in enumerate(S):
            d[ord(v) - ord('a')] = i

        return ''.join(sorted(T, key=lambda i: d[ord(i)- ord('a')]))

# interesting solution found. notice we dont care about other character order, so can use find and dir[]
# in c++
class Solution {
  public:
    string customSortString(string S, string T) {
        sort(T.begin(), T.end(),
             [&](char a, char b) { return S.find(a) < S.find(b); });
        return T;
    }
};
The second Edition. It is easier to understand.

class Solution {
  public:
    string customSortString(string S, string T) {
        unordered_map<char, int> dir;
        for (int i = 0; i < S.size(); i++) {
            dir[S[i]] = i + 1;
        }
        sort(T.begin(), T.end(),
             [&](char a, char b) { return dir[a] < dir[b]; });
        return T;
    }
};