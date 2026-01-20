#Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:

#     '?' Matches any single character.
#     '*' Matches any sequence of characters (including the empty sequence).

# The matching should cover the entire input string (not partial).

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        counter = 0
        if len(s) != len(p) and '*' not in s and '*' not in p:return False
        elif  '*' in s or '*' in p :return True
        for i in s:
            for j in p:
                if i == j or (i in '*?') or (j in '*?'):
                    counter+=1
                else:
                    return False
        if counter == len(s):return True
        