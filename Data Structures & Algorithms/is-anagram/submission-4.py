class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_dict = dict()
        for ch in s:
            if ch in s_dict:
                s_dict[ch] += 1
            else:
                s_dict[ch] = 1
        
        t_dict = dict()
        for ch in t:
            if ch in t_dict:
                t_dict[ch] += 1
            else:
                t_dict[ch] = 1
        
        print(f"s_dict: {s_dict}")
        print(f"t_dict: {t_dict}")
        return s_dict == t_dict