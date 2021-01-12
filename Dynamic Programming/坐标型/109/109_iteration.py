class Solution:
    """
    自底向上：
        当前层的结果等于他后面那层的结果，类似分治法，root的结果等于左右子树的结果，
        所以循环要倒着来！
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """

    def minimumTotal(self, triangle):
        n = len(triangle)

        # 状态：坐标 但是我们只需要三角形对应的坐标
        # state: dp[i][j] 代表从i, j 走到最底层的最短路径
        dp = [[0] * (i + 1) for i in range(n)]

        # 初始化：重点
        # initialize: 初始化重点 最后一层
        for i in range(n):
            dp[n - 1][i] = triangle[n - 1][i]

        # 方程：到哪去
        # function: 从下往上倒过来推到，计算每个坐标到哪儿去
        # i j 和他的左右子最小 加上当前ij的只相关
        # 从倒数第二层，到第0层，（-1），倒着来 -1
        for i in range(n - 2, -1, -1):
            for j in range(i + 1):
                dp[i][j] = min(dp[i + 1][j], dp[i + 1][j + 1]) + triangle[i][j]

        # 答案answer：起点就是答案
        return dp[0][0]


class Solution:
    """
    自顶向下：
        当前点是跟上一层所走的最短路径有关系，比如走到5这个点，要么从3来，要么从4来。
        最优的走到5是235走过来，所以5的最短路径是10，所以走到每个店要看从根尖点走到当前最短的
        而们所找的最小的，就是看最后一层所以记录里面的最小值

    状态：坐标
    方程：从哪来
    初始化：起点, 左边和右边
    答案：终点（终点是最下面一排）
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """

    def minimumTotal(self, triangle):
        n = len(triangle)

        # state: dp[i][j] 代表从0, 0走到i, j的最短路径值
        dp = [[0] * (i + 1) for i in range(n)]

        # intialize: 三角形的左边和右边要初始化
        # 因为它们分别没有左上角和右上角的点，如果不初始化，放在下面的function里面计算，回outof index
        dp[0][0] = triangle[0][0]
        # 从第二排开始把最左边最右边的两流都计算一下
        for i in range(1, n):
            dp[i][0] = dp[i - 1][0] + triangle[i][0]
            dp[i][i] = dp[i - 1][i - 1] + triangle[i][i]

        # function: i, j这个位置是从他的左上角和右上角，左上角其实是左上方 i-1,j-1 ，右上角其实是正上方！i-1, j
        # 这里其实前两排都是初始化了，所以我们就从第三排开始
        for i in range(2, n):
            # 不用考虑两头，因为两头初始化好了（只有一条边相连
            for j in range(1, i):
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]

        # answer: 最后一层的任意位置都可以是路径的终点
        return min(dp[n - 1])

