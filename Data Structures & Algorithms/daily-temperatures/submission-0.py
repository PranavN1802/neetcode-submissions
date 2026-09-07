class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        leng = len(temperatures)
        results = [0] * leng

        for i in range(leng-1, -1, -1):
            while stack and temperatures[i] >= temperatures[stack[-1]]:
                stack.pop()
            
            if stack: 
                results[i] = stack[-1] - i

            stack.append(i)

        return results
