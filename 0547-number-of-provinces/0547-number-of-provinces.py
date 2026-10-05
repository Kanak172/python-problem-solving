class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        stack = []
        provinces = 0
        
        
        for i in range(len(isConnected)):
            if isConnected[i][i] == 0:
                continue
            
            
            isConnected[i][i] = 0
            stack.append(i)
            
            
            while stack:
                idx = 0
                j = stack.pop()
                
                
                for connection in isConnected[j]:
                    if connection == 1 and isConnected[idx][idx] == 1:
                        isConnected[idx][idx] = 0
                        stack.append(idx)
                    
                    
                    idx += 1
            
            
            provinces +=1
        
        
        return provinces