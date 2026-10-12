class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        st = []

        for ix, temp in enumerate((temperatures)):
            # print(f"temp: {temp}, i: {ix}")
            while st and temp > st[-1][0]:
                t, i = st.pop()
                res[i] = ix - i
            st.append((temp, ix))

        return res