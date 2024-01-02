class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lst=[]
        ln=len(strs)
        each=min(strs,key=len)
        sl=len(each)
        print(sl)
        for i in range(sl):
            count=0
            for j in range(ln):
                if (strs[0][i]!=strs[j][i]):
                    return "".join(lst)
                    break
                else:
                    count=count+1
                    if(count==ln):
                        lst.append(strs[0][i])
                    
                


        return "".join(lst)   
