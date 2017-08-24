class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        for i in path.split('/'): # this could remove '//' case
            if i == '..': # go back to upper level
                if stack:
                    stack.pop()
            elif i != '' and i != '.': # not empty and not equals to current dir
                stack.append(i)  
        return '/' + '/'.join(stack) # join function will put '/' in between
    # /... is a valid path
                