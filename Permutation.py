# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 17:45:47 2019

@author: Arjan
"""

class permutation:
    def __init__(self, string1, string2):
        self.string1 = string1
        self.string2 = string2
        
    def checkIfPerm(self):
        sorted1 = ''.join(sorted(self.string1.lower()))
        sorted2 = ''.join(sorted(self.string2.lower()))
        if sorted1 == sorted2:
            return True
        else:
            return False
    
checkPerm = permutation("Hello", "Nope")
print(checkPerm.checkIfPerm())