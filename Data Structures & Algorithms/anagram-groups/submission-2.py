class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_dict = {}
        for string in strs:
            str_set = str(sorted(list(string)))
            if str_set in ana_dict:
                ana_dict[str_set].append(string)
                # print(ana_dict)
            else:
                ana_dict[str_set] = [string]
                # print(ana_dict)
        reLst = []
        for lst in ana_dict.values():
            reLst.append(lst)
        return reLst
        