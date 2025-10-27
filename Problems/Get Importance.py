
class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        mapping = {}
        target = None
        for i in employees:
            mapping[i.id] = i
            if i.id == id:
                target = i

        def dfs(employee):
            if not employee:
                return 0
            total = employee.importance
            for i in employee.subordinates:
                total += dfs(mapping[i])
            return total


        return dfs(target)
