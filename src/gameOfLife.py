import sys

def main():
    if len(sys.argv) != 3:
        print('Run file in command line as ==>\npython3 gameOfLife.py [Lattice size] [Init lattice type]')

    N= int(sys.argv[1])
    initLattice= str(sys.argv[2])
    
