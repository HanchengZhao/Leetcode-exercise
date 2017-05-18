class Solution(object):
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        if self.isIpv4(IP):
            return "IPv4"
        if self.isIpv6(IP):
            return "IPv6"
        else:
            return "Neither"

    def isIpv4(self, address):
        Split = address.split(".")
        if len(Split) != 4:
            return False
        for i in Split:
            if not i or not i.isdigit():
                return False
            if int(i) < 0 or int(i) >= 256:
                return False
            if i[0] == "0" and i != "0":
                return False
        return True

    def isIpv6(self, address):
        valid = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","A","B","C","D","E","F"]
        Split = address.split(":")
        if len(Split) != 8:
            print 1
            return False
        for i in Split:
            if len(i) > 4 or i == "":
                print 2
                return False
            for char in i:
                if char not in valid:
                    print 3
                    return False
        return True
s = Solution()
print s.validIPAddress("172.16.254.1")
print s.isIpv6("2001:0db8:85a3:0:0:8A2E:0370:7334")
