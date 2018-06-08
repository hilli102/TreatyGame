# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 14:42:01 2018

@author: tran260
"""

class PlayerA():
    def __init__(self,alpha_0):
        self.alpha_0 = alpha_0
        
    def income_a(alpha_t):
        return alpha_t**(1/2)
    
    def aquisition_a(x,alpha_t):
        return 2*x**(1/2)*(1-alpha_t)
    
class PlayerB():
    def __init__(self,alpha_0):
        self.alpha_0 = alpha_0
    
    def income_b(alpha_t):
        return 2*(1-alpha_t)**(1/2)

    def aquisition_b(x,alpha_t):
        return x**(1/2)*(alpha_t)
    
class GenAlg():
    def fitness():
        return
    
    def generate():
        return
    
    def crossover():
        return
    
    def mutate():
        return
    