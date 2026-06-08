class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # create adj list
        # use a searched (visited) map
        # for each un-visited course start dfs
        # for each dfs search use a separated visited tracking
        adj_list = {i: [] for i in range(numCourses)} # defaultdict(list)
        for req in prerequisites:
            adj_list[req[0]].append(req[1]) # no duplicate input

        visited = [False]*numCourses
        order = []
        ordered = set()
        for course in adj_list:
            # print("Course", course)
            if not visited[course]:
                # print("D F S")
                prereq = [False]*numCourses
                if not self.dfs(course, adj_list, visited, prereq, order, ordered):
                    return []

        # for c in visited:
        #     if not visited:
        #         order.append(c)

        # order.reverse()
        return order

    def dfs(self, course: int, adj_list: map, visited: [], prereq: [], order: [], ordered: set) -> bool:
        # print("dfs", course)
        if prereq[course]:
            return False
        # If we visited - that means we searched this path and 
        # didn't return False. So we can just return True.
        # But I don't know WHY not having this causes TLE ???
        if visited[course]:
            return True
        # OK!! I was getting Output Limit Exceeded not TLE. This was not the casue.

        prereq[course] = True
        visited[course] = True
        for c in adj_list[course]:
            if not self.dfs(c, adj_list, visited, prereq, order, ordered):
                return False
        prereq[course] = False

        # if course not in ordered:
        order.append(course)
        # ordered.add(course)

        return True