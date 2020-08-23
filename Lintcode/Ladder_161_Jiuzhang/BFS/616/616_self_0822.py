class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: the course order
    """

    def findOrder(self, numCourses, prerequisites):

        edge, indegree = self.get_edge_indegree(numCourses, prerequisites)

        start_course = []
        for i in range(len(indegree)):
            if indegree[i] == 0:
                start_course.append(i)

        queue, order = collections.deque(start_course), []

        while queue:
            curt_course = queue.popleft()
            order.append(curt_course)
            for second in edge[curt_course]:
                indegree[second] -= 1
                if indegree[second] == 0:
                    queue.append(second)

        if len(order) == numCourses:
            return order
        return []

    def get_edge_indegree(self, numCourses, prerequisites):
        edge = {course: [] for course in range(numCourses)}
        indegree = [0 for _ in range(numCourses)]

        for second, first in prerequisites:
            edge[first].append(second)
            indegree[second] += 1

        return edge, indegree