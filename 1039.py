ode
class Solution {
public:
    static const int MAX = 55;
    static const int INF = 1e9 + 5;

    int n;
    vector<int> A;
    int dp[MAX][MAX];

    int prev(int x) {
        return (x + n - 1) % n;
    }

    int next(int x) {
        return (x + 1) % n;
    }

    int solve(int start, int end) {
        if (start == end || next(start) == end || prev(start) == end)
            return 0;

        int &answer = dp[start][end];

        if (answer >= 0)
            return answer;

        answer = INF;

        for (int i = next(start); i != end; i = next(i))
            answer = min(answer, A[start] * A[i] * A[end] + solve(start, i) + solve(i, end));

        return answer;
    }

    int minScoreTriangulation(vector<int>& _A) {
        A = _A;
        n = A.size();
        memset(dp, -1, sizeof(dp));
        int best = INF;

        for (int i = 0; i < n; i++)
            for (int j = i + 1; j < n; j++)
                for (int k = j + 1; k < n; k++)
                    best = min(best, A[i] * A[j] * A[k] + solve(i, j) + solve(j, k) + solve(k, i));

        return best;
    }
};


# import functools
# class Solution:
#     def minScoreTriangulation(self, A: List[int]) -> int:
#         @functools.lru_cache(None)
#         def solve(labels):
#             if len(labels) == 3:
#                 return functools.reduce(operator.mul, labels)
#             res = math.inf
#             n = len(labels)
#             for i in range(2, n - 1):
#                 left = solve(labels[:i + 1])
#                 right = solve((labels[0],) + labels[i:])
#                 res = min(res, left + right)
#             return min(res, labels[-1] * labels[0] * labels[1] + solve(labels[1:]))
            
#         return solve(tuple(A))