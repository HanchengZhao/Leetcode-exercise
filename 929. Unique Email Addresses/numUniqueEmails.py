class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        s = set()
        for i in emails:
            local, domain = i.split("@")
            local = local.split("+")[0].replace(".", "")
            new = local + "@" + domain
            if new not in s:
                s.add(new)
        return len(s)
