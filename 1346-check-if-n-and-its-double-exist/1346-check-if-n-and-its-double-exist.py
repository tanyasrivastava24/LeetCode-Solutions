class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        n=len(arr)
        for i in range(n):
            for j in range(n):
                if arr[i]==arr[j]*2 and i!=j:
                    return True
        return False
            
        