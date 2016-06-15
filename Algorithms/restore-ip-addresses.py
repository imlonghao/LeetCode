class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        def valid(ip):
            t = ip.split('.')
            a = ''
            for i in t:
                if i[0] == '0' and len(i) != 1:
                    return False
                if 0 <= int(i) <= 255:
                    a += str(int(i)) + '.'
                else:
                    return False
            return a[:-1]

        if len(s) > 12:
            return []
        anwser = list()
        length = len([x for x in s])
        for x in range(1, length - 2):
            for y in range(1 + x, length):
                for z in range(1 + y, length):
                    ip = [i for i in s]
                    ip.insert(x, '.')
                    ip.insert(1 + y, '.')
                    ip.insert(2 + z, '.')
                    ip = ''.join(ip)
                    ip = valid(ip)
                    if ip:
                        anwser.append(ip)
        return list(set(anwser))
