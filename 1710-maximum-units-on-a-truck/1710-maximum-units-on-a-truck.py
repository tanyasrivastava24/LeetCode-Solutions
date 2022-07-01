class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda box:box[1],reverse=True)
        totalunit=0
        for numberofBoxes,numberofUnitsPerBox in boxTypes:
        
            numbox= min(truckSize,numberofBoxes)
            totalunit+=numbox*numberofUnitsPerBox
            truckSize-=numbox
        return totalunit
        
        
        
        
        