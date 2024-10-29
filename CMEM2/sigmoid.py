#This will plot out test functions to see what they look like. 

import numpy as np 
import matplotlib.pyplot as plt 

class sigmoid():
    def __init__(self, r):
        '''This takes in any initial values to initialise the function.'''
        
        self.r = r 
        
        #Calculate a set of logistic functions, varying k. 
        self.sigmoid_all = [] 
        self.sigmoid_rev_all = [] 
        self.k_list = [0.5,1,2,5,10,50,100]
        for k in self.k_list:
            sigmoid = self.logistic_func(k=k, r0=0.1)
            self.sigmoid_all.append(sigmoid)
        
            sigrev = self.logistic_rev_func(k=k, r0=0.1)
            self.sigmoid_rev_all.append(sigrev)
            
    def logistic_func(self, L=1, k=1, r0=0):
        '''Calculate the logistic function.'''
        
        return L/(1+np.exp(-k*(self.r-r0)))
    
    def logistic_rev_func(self, L=1, k=1, r0=0):
        '''Calculate the logistic function.'''
        
        return L/(1+np.exp(k*(self.r-r0)))
           
    def plot_logistic(self):
        '''This will plot the function. '''
        
        fig = plt.figure()
        ax1 = fig.add_subplot(211)
        ax2 = fig.add_subplot(212) 
        
        for k, kval in enumerate(self.k_list):
            
        
            ax1.plot(self.r, self.sigmoid_all[k], label='k = {}'.format(kval))
            ax2.plot(self.r, self.sigmoid_rev_all[k], label='k = {}'.format(kval))
        
        
        ax1.set_xlim(self.r.min(), self.r.max()) 
        ax1.set_xlabel('r')
        ax1.grid()
        ax1.legend(loc='upper left')
        ax2.set_xlim(self.r.min(), self.r.max()) 
        ax2.set_xlabel('r')
        ax2.grid()
        ax2.legend(loc='upper right')
         
