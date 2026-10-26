class Solution:
    def countAndSay(self, n: int) -> str:
        from collections import deque
        q=deque(["1"])
        count=0
        for i in range(n-1):
            count=1
            node=q.popleft()
            for j in range(len(q)):
                if q[0]==node:
                    count+=1
                    q.popleft()
                else:
                    q.append(str(count))
                    q.append(node)
                    count=1
                    node=q.popleft()
            q.append(str(count))
            q.append(node)
            
        return "".join(q)