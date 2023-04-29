import numpy as np
from time import time
from animate import Animate
from algorithm import Algorithm

class Simulate(object):
#=================================================================
# Class to initialise and carry out simulation of game of life cellular automata

    def __init__(self, N, initialFlag):
        #=========================================================
        # Constructor to define inital parameters of the simulation

        self.N= N

        if initialFlag == str('r'):
            self.generateRandomInitLattice()
        elif initialFlag == str('g'):
            self.generateGliderInitLattice()
        elif initialFlag == str('b'):
            self.generateBlinkerInitLattice()
        else:
            raise Exception('Input valid flag\nInit latice type: r ==> random, g ==> glider, b ==> blinker')
        
        self.animation= Animate(self.lattice)
        self.algorithms= Algorithm()

    def generateRandomInitLattice(self):
        #==========================================================
        # Generate a random initial game of life lattice

        self.lattice= np.random.choice(np.array([0, 1]), size=(self.N, self.N))

    def generateGliderInitLattice(self):
        #==========================================================
        # Generate a initial game of life lattice with a glider

        self.lattice= np.loadtxt('../initialLattices/emptyGliderLattice.txt')

    def generateBlinkerInitLattice(self):
        #==========================================================
        # Generate a initial game of life lattice with a glider

        self.lattice= np.loadtxt('../initialLattices/emptyBlinkerLattice.txt')
    
    def runSimulation(self):
        #==========================================================
        # Run simulation and visualisation of cellular automata
        
        while True:
            t1= time()
            self.lattice= self.algorithms.updateLattice(self.lattice)
            self.animation.draw_image(self.lattice)
            print(f'{time()-t1:.5} s')

