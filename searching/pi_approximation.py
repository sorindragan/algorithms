import sys
import numpy as np

def simulate(rounds=5000):
    circle_points = 0
    square_points = rounds
    for _ in range(rounds):
        point_x, point_y = np.random.uniform(-1, 1), np.random.uniform(-1, 1)
        if np.linalg.norm(np.array([point_x, point_y]) - np.array([0, 0])) <= 1:
            circle_points += 1
    
    pi_value = 4*circle_points / square_points 
    return f"After {rounds} rounds, PI is approximately {pi_value}"

def main():
    print(simulate(int(sys.argv[1])))

if __name__ == '__main__':
    main()

