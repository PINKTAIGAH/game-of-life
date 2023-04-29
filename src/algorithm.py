import numpy as np

class Algorithm(object):
#=================================================================
# Class that constains algrithm to update lattice according to game of life rules

    def findNeighbourPopulation(self):
        #=========================================================
        # Find nearest neighbour for each element in array

        arrayD= np.roll(self.arrayOld, +1, axis=0)
        arrayU= np.roll(self.arrayOld, -1, axis=0)
        arrayR= np.roll(self.arrayOld, +1, axis=1)
        arrayL= np.roll(self.arrayOld, -1, axis=1)
        arrayUL= np.roll(arrayL, -1, axis=0)
        arrayUR= np.roll(arrayR, -1, axis=0)
        arrayDL= np.roll(arrayL, +1, axis=0)
        arrayDR= np.roll(arrayR, +1, axis=0)
        
        self.nearestNeighbour= arrayD + arrayU + arrayL + arrayR +\
                                arrayUL + arrayUR + arrayDR + arrayDL
    
    def findUpdateMasks(self):
        #==========================================================
        # Find mask which return bool for each case of game of life update rules

        self.maskDeadToAlive= (self.arrayOld==0) & (self.nearestNeighbour==3)
        self.maskAliveToAlive= (self.arrayOld==1) & (self.nearestNeighbour==3)
        self.maskAliveToDead1= (self.arrayOld==1) & (self.nearestNeighbour<2)
        self.maskAliveToDead2= (self.arrayOld==1) & (self.nearestNeighbour>3)

    def applyUpdateRules(self):
        #=========================================================
        # Apply update rules for game of life to each element in cellular
        # automata 

        self.array[self.maskAliveToDead1]= 0
        self.array[self.maskAliveToDead2]= 0  
        self.array[self.maskAliveToAlive]= 1
        self.array[self.maskDeadToAlive]= 1
    
    
    def updateLattice(self, array):
        #=========================================================
        # Method to update a given array according to game of life rules

        self.array= array
        self.arrayOld= np.copy(self.array)
        self.findNeighbourPopulation()
        self.findUpdateMasks()
        self.applyUpdateRules()

        return self.array

if __name__ == '__main__':
    lattice= np.random.choice(np.array([1,0]), size=(50,50))
    algorithms= Algorithm()
    algorithms.updateLattice(lattice)