class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        st.append(len(temperatures) - 1)
        res = [0] * len(temperatures)
        for i in range(len(temperatures)-2, -1, -1):
            if temperatures[i] < temperatures[st[-1]]:
                res[i] = st[-1] - i
                st.append(i)
            else:
                while st and temperatures[i] >= temperatures[st[-1]]:
                    st.pop()

                if st:
                    res[i] = st[-1] - i
                else:
                    res[i] = 0
                st.append(i)

        return res



