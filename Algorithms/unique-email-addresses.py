class Solution:
    def numUniqueEmails(self, emails) -> int:
        r = []
        for i in emails:
            c = i.split("@")
            n = c[0].replace(".", "").split('+')[0]
            r.append('%s@%s' % (n, c[1]))
        return len(set(r))
