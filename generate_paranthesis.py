class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        sList = list([])
        self.backtrace(sList, "", 0, 0, n)
        return sList
    
    
    def backtrace(self, sList, s, start, end, m):
        if(len(s) == m * 2):
            sList.append(s)
            return
        if start < m: # open parenthesis num is less than max
            self.backtrace(sList, s+"(", start+1, end, m)
        if end < start:# close parenthesis num is less than open num
            self.backtrace(sList, s+")", start, end+1, m)