import sys
from simulate import Simulate

def main():
    if len(sys.argv) != 3:
        raise Exception('Run file in command line as ==>\npython3 gameOfLife.py [Lattice size] [Init lattice type]')

    N= int(sys.argv[1])
    initLatticeFlag= str(sys.argv[2])
    
    simulation= Simulate(N, initLatticeFlag)
    simulation.runSimulation()

if __name__ == '__main__':
    main()
