
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        graph = [[] for _ in range(n)]       # adjacency list
        email_to_account = {}                 # email -> first account index

        # Build graph
        for i, acc in enumerate(accounts):
            for email in acc[1:]:
                if email in email_to_account:
                    j = email_to_account[email]
                    graph[i].append(j)
                    graph[j].append(i)        # bidirectional edge
                else:
                    email_to_account[email] = i

        visited = [False] * n
        merged = []

        for i in range(n):
            if not visited[i]:
                # Start a new component
                component_emails = set()
                stack = [i]
                visited[i] = True

                while stack:
                    node = stack.pop()
                    # Collect all emails of this account
                    for email in accounts[node][1:]:
                        component_emails.add(email)
                    # Traverse neighbors
                    for neighbor in graph[node]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            stack.append(neighbor)

                # Build result entry
                name = accounts[i][0]   # any account in the component works
                merged.append([name] + sorted(component_emails))

        return merged
        # Q What if two accounts are connected but have different names? Is that possible?
        