import collections


class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: true if can finish all courses or false
    """

    def canFinish(self, numCourses, prerequisites):
        if not numCourses:
            return False

        edge, indegree = self.get_edge_indegree(numCourses, prerequisites)

        start_course = []
        for i in range(len(indegree)):
            if indegree[i] == 0:
                start_course.append(i)

        queue = collections.deque(start_course)
        count = 0

        while queue:
            curt_course = queue.popleft()
            count += 1
            for second in edge[curt_course]:
                indegree[second] -= 1
                if indegree[second] == 0:
                    queue.append(second)

        return count == numCourses

    def get_edge_indegree(self, numCourses, prerequisites):
        edge = {num: [] for num in range(numCourses)}
        indegree = [0 for _ in range(numCourses)]

        for second, first in prerequisites:
            edge[first].append(second)
            indegree[second] += 1

        return edge, indegree