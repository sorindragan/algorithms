import random
import copy

from collections import Counter

WORLD_SIZE = 100

class Building:
    def __init__(self, x, length, height) -> None:
        self.x = x
        self.length = length
        self.x_end = x + length
        self.height = height
    
    def get_limits(self) -> list:
        return [self.x, self.x_end]
    
    def __repr__(self) -> str:
        return f"B: ({self.x} - {self.x_end}) h: {self.height}"


class Airplane:
    def __init__(self) -> None:
        self.x = int(random.uniform(0, 1) * WORLD_SIZE)
        self.y = 100
        self.velocity = 5
    
    def set_position(self, x) -> None:
        self.x = x
    
    def __repr__(self) -> str:
        return f"P: {self.x} "
    
    def sense(self, buildngs, noisy=False) -> float:
        noise = 0
        if noisy:
            noise = random.uniform(-1, 1)
        intervals = [b.get_limits() for b in buildngs]
        return self.y - buildngs[intervals.index(
            list(filter(lambda i: i[0] <= self.x <= i[1],
            intervals))[0]
            )].height + noise

    def move(self, noisy=False) -> None:
        noise = 0
        if noisy:
            noise = random.uniform(-1, 1)
        self.x = int((self.x + self.velocity + noise) % WORLD_SIZE) 
    

def generate_buildings(buildings_no=10) -> list:
    buildings = []
    last_x = 0
    for _ in range(buildings_no):
        buildings.append(
            Building(x=last_x, 
                     length=int(random.uniform(0, 1) * WORLD_SIZE / (buildings_no-1)),
                     height=random.uniform(0, 1) * (WORLD_SIZE - 10)
                     ))
        last_x += buildings[-1].length + 1
    buildings[-1].length = 100 - buildings[-1].x
    buildings[-1].x_end = 100
    return buildings


def generate_particles(particle_no=100) -> list:
    return [Airplane() for _ in range(particle_no)]


def measure_probability(particle_list, observation, buildings) -> list:
    print([abs(observation - p.sense(buildings)) for p in particle_list])
    weights = [1/(1 + abs(observation - p.sense(buildings))) for p in particle_list]
    sum_ = sum(weights)
    print([w/sum_ for w in weights])
    return [w/sum_ for w in weights]

def resample(particles, weights, particle_no=100) -> list:
    new_partcles = []
    indices = list(random.choices([i for i in range(len(particles))], weights=weights, k=particle_no))
    for idx in indices:
        h = Airplane()
        h.set_position(particles[idx].x)
        new_partcles.append(h)
    return new_partcles

def main():
    updates = 10
    particle_number = 100

    buildings = generate_buildings(10)
    print(buildings)

    test_h = Airplane()
    test_h.set_position(2)
    real_observation = test_h.sense(buildings, noisy=False)
    
    particles = generate_particles(particle_no=particle_number)
    particles.sort(key=lambda p: p.x)
    
    particle_weights = measure_probability(particles, real_observation, buildings)
    
    resampled_particles = resample(copy.deepcopy(particles), particle_weights, particle_no=particle_number)
    resampled_particles.sort(key=lambda p: p.x)
    
    for _ in range(updates):
        test_h.move(noisy=False)
        new_observation = test_h.sense(buildings, noisy=False)
        
        for particle in resampled_particles:
            particle.move()
        
        resampled_particles.sort(key=lambda p: p.x)
        particle_weights = measure_probability(resampled_particles, new_observation, buildings)
        
        resampled_particles = resample(copy.deepcopy(
            particles), particle_weights, particle_no=particle_number)
        resampled_particles.sort(key=lambda p: p.x)

        print(test_h)
        print(resampled_particles)
        position_counter = Counter([particle.x for particle in resampled_particles])
        print(position_counter.most_common(5))



if __name__ == "__main__":
    main()
