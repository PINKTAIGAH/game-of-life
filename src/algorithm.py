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
    
    def applyUpdateRules(self):
        #=========================================================
        # Apply update rules for game of life to each element in cellular
        # automata 

        pass
    
    def updateLattice(self, array):
        #=========================================================
        # Method to update a given array according to game of life rules

        self.arrayOld= np.copy(array)
        self.findNeighbourPopulation()
        