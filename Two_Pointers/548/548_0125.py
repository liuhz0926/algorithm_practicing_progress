class Solution:
    """
    @param nums1: an integer array
    @param nums2: an integer array
    @return: an integer array
    """

    def intersection(self, nums1, nums2):

        count = {}
        for num in nums1:
            count[num] = count.get(num, 0) + 1

        result = []
        for num in nums2:
            if num not in count:
                continue
            result.append(num)
            count[num] -= 1
            if count[num] == 0:
                del count[num]

        return result




def solution(T):
    if not T:
        return 0
    visited = set(T.x)
    result = [0]
    dfs(T, visited, result)

    return result[0]

def dfs(node, visited, result):
    if not node:
        result[0] = max(result[0], len(visited))
        return

    if node.x in visited:
        result[0] = max(result[0], len(visited))
        return

    if not node.l and not node.r:
        result[0] = max(result[0], len(visited))
        return

    if node.l is not None:
        visited.add(node.l.x)
        dfs(node.l, visited, result)
        visited.remove(node.l.x)
    if node.r is not None:
        visited.add(node.r.x)
        dfs(node.r, visited, result)
        visited.remove(node.r.x)
    return