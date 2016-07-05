class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        version1 = [int(x) for x in version1.split('.')]
        version2 = [int(x) for x in version2.split('.')]
        while len(version1) > len(version2):
            version2.append(0)
        while len(version1) < len(version2):
            version1.append(0)
        for i in range(len(version1)):
            if version1[i] > version2[i]:
                return 1
            elif version1[i] < version2[i]:
                return -1
        return 0
