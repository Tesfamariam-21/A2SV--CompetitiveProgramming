class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        count = defaultdict(int)
        def dfs(u, parent):
            label_count = defaultdict(int)
            for v in adj[u]:
                if v != parent:
                    dfs(v, u)
                    for label, cnt in count[v].items():
                        label_count[label] += cnt
            label_count[labels[u]] += 1
            count[u] = label_count
        
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        dfs(0, -1)
        
 
        res = [0] * n
        def dfs2(u, parent):
            res[u] = count[u][labels[u]]
            for v in adj[u]:
                if v != parent:
                    dfs2(v, u)
        dfs2(0, -1)
        return res