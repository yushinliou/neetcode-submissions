class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_ct = {}
        k_ct = 0
        ans = []
        for num in nums:
            if str(num) in num_ct:
                num_ct[str(num)] += 1
            else:
                num_ct[str(num)] = 1
        print(f"k: {k}")
        for key, value in sorted(num_ct.items(), key=lambda item: item[1], reverse=True):
            ans.append(key)
            k_ct+=1
            print(f"k_ct: {k_ct}")
            print(f"ans: {ans}")
            if k_ct == k:
                print()
                break           
        return ans
        

