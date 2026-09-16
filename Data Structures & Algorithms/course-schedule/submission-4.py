class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjMap = {i:[] for i in range(numCourses)}
        
        for crs, pre in prerequisites:
            if crs == pre:
                return False
            adjMap[crs].append(pre)
        
        path = set()

        def dfs(crs, pre):
            if crs in path:
                return False
            if pre == []:
                return True
            path.add(crs)
            

            for p in pre:
                if not dfs(p, adjMap[p]):
                    return False

            path.remove(crs)

            adjMap[crs] = []
            return True

        for key in adjMap:
            if not dfs(key, adjMap[key]):
                return False
        return True