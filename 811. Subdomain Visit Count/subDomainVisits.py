class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        hits = {}
        for cp in cpdomains:
            count, domain = cp.split(" ")
            subdomain = domain.split(".")
            sub = ""
            for i in range(len(subdomain)-1, -1, -1):
                if sub == "":
                    sub = subdomain[i]
                else:
                    sub = subdomain[i] + "." + sub
                hits[sub] = hits.get(sub, 0) + int(count)
        res = []
        for domain, count in hits.items():
            res.append("{} {}".format(count, domain))
        return res
