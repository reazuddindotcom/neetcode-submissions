class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # create adj list
        # use a searched (visited) map
        # for each un-visited course start dfs
        # for each dfs search use a separated visited tracking
        adj_list = {i: [] for i in range(numCourses)} # defaultdict(list)
        for req in prerequisites:
            adj_list[req[0]].append(req[1]) # no duplicate input

        visited = [False]*numCourses
        
        for course in adj_list:
            if not visited[course]:
                prereq = [False]*numCourses
                if not self.dfs(course, adj_list, visited, prereq):
                    return False

        return True

    def dfs(self, course: int, adj_list: map, visited: [], prereq: []) -> bool:
        if prereq[course]:
            return False
        visited[course] = True # what if we mark visited here??

        prereq[course] = True
        for c in adj_list[course]:
            if not self.dfs(c, adj_list, visited, prereq):
                return False
        prereq[course] = False

        return True

        