class Excel(object):

    def __init__(self, H, W):
        """
        :type H: int
        :type W: str
        """
        self.E_formula = []
        for h in range(H):
            new = []
            for w in range(ord(W)-ord('A')+1):
                new.append([])
            self.E_formula.append(new)
        #E_formula = [[[] for w in range(ord(W)-ord('A')] for h in range(H)]
        self.E_value = [[0 for w in range(ord(W)-ord('A')+1)] for h in range(H)]
        

    def set(self, r, c, v):
        """
        :type r: int
        :type c: str
        :type v: int
        :rtype: void
        """
        self.E_formula[r-1][ord(c) - ord('A')] = []  
        self.E_value[r-1][ord(c) - ord('A')] = v
    
    def calculate(self, r, c, strs):
        total = 0
        for i in range(len(strs)):
            #print("i=",i, " str=",strs[i])
            index = strs[i].find(":")
            if index >= 0:
                start_pos = (int(strs[i][1:index])-1, ord(strs[i][0])- ord('A')) 
                end_pos = (int(strs[i][index+2:])-1, ord(strs[i][index+1])- ord('A'))
                #print("start_pos=", start_pos)
                #print("end_pos=", end_pos)
                for i in range(start_pos[0], end_pos[0]+1):
                    for j in range(start_pos[1], end_pos[1]+1):
                        val = self.get(i+1, chr(ord('A')+j))
                        total += val
                        #print("i=", i, " j=",j, " val=", val)
                #print(total)
            else:    
                total += self.get(int(strs[i][1:]), strs[i][0])
                #print(total)
        return total
    def get(self, r, c):
        """
        :type r: int
        :type c: str
        :rtype: int
        """
        if len(self.E_formula[r-1][ord(c) - ord('A')]) > 0:
            # calculate
            return self.calculate(r-1, ord(c)-ord('A'), self.E_formula[r-1][ord(c)-ord('A')])
        else:
            return self.E_value[r-1][ord(c)-ord('A')]
        

    def sum(self, r, c, strs):
        """
        :type r: int
        :type c: str
        :type strs: List[str]
        :rtype: int
        """
        self.E_formula[r-1][ord(c)-ord('A')] = strs
        #print(self.E_value)
        #print(self.E_formula)
        return self.calculate(r-1, ord(c)-ord('A'), strs)

# Your Excel object will be instantiated and called as such:
# obj = Excel(H, W)
# obj.set(r,c,v)
# param_2 = obj.get(r,c)
# param_3 = obj.sum(r,c,strs)
