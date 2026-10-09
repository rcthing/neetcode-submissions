class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        res = [0] * len(temperatures)
        for i in range(len(temperatures)):
            if not st or temperatures[i] < temperatures[st[-1]]:
                st.append(i)
            else:
                while st and temperatures[i] > temperatures[st[-1]]:
                    res[st[-1]] = i - st[-1]
                    st.pop()
                st.append(i)

        return res



