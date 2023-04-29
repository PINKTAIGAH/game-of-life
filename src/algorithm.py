import numpy as np

class Algorithm(object):
#=================================================================
# Class that constains algrithm to update lattice according to game of life rules

    def findNeighbourPopulation(self):
        #=========================================================
        # Find nearest neighbour for each element in array

        arrayDown= np.roll(self.arrayOld, +1, axis=0)
        arrayUp= np.roll(self.arrayOld, -1, axis=0)
        arrayRight= np.roll(self.arrayOld, +1, axis=1)
        arrayLeft= np.roll(self.arrayOld, -1, axis=1)
        
        self.nearestNeighbour= arrayDown + arrayUp + arrayLeft + arrayRight
    
    def findUpdateMasks(self):
        #==========================================================
        # Find mask which return bool for each case of game of life update rules

        self.maskDeadToAlive= (self.arrayOld==0) & (self.nearestNeighbour==3)
        self.maskAliveToDead1= (self.arrayOld==1) & (self.nearestNeighbour<2)
        self.maskAliveToDead2= (self.arrayOld==1) & (self.nearestNeighbour>3)

    def applyUpdateRules(self):
        #=========================================================
        # Apply update rules for game of life to each element in cellular
        # automata 

        self.array[self.maskDeadToAlive]= 0
        self.array[self.maskAliveToDead1 | self.maskAliveToDead2]= 1        
    
    def updateLattice(self, array):
        #=========================================================
        # Method to update a given array according to game of life rules

        self.array= array
        self.arrayOld= np.copy(array)
        self.findNeighbourPopulation()
        self.findUpdateMasks()
        self.applyUpdateRules()

        return self.array

if __name__ == '__main__':
    lattice= np.random.choice(np.array([1,0]), size=(50,50))
    algorithms= Algorithm()
    algorithms.updateLattice(lattice)