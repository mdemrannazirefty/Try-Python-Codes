import random

def createCromosome(n):
    c = ''
    for i in range(n):
        c += str(random.randint(0, n - 1))
    return c

def find_attack(chromosome):
    n = len(chromosome)
    attack = 0
    for i in range(n):
        for j in range(i + 1, n):
            if chromosome[i] == chromosome[j]:
                attack += 1
            elif abs(int(chromosome[i]) - int(chromosome[j])) == abs(i - j):
                attack += 1
    return attack

def createBoard(c1):
    m = []
    n = len(c1)
    for i in range(n):
        c = []
        for j in range(n):
            c.append(0)
        m.append(c)
    for i in range(n):
        m[i][int(c1[i])] = 1
    return m

def printBoard(m):
    for row in m:
        print(row)

def calculate_non_attacks(chromosome):
    n = len(chromosome)
    total_pairs = n * (n - 1) // 2
    attack_pairs = find_attack(chromosome)
    non_attacks = total_pairs - attack_pairs
    return non_attacks

def fitness(p):
    n = len(p[0])
    fitness_value = {}
    total_sum = 0
    for i in range(len(p)):
        fitness_value[p[i]] = (n * (n - 1) // 2) - find_attack(p[i])
    for k in fitness_value.keys():
        total_sum += fitness_value[k]
    fitness_percent = {}
    for k in fitness_value.keys():
        fitness_percent[k] = (fitness_value[k] / total_sum) * 100
    return fitness_percent

def selection(fit_p):
    sort_key_value = sorted(fit_p.items(), key=lambda x: x[1])
    print(sort_key_value)
    return sort_key_value[-1][0], sort_key_value[-3][0]

def crossover(parent1, parent2, crossover_point):
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

def mutation(chromosome, mutation_rate):
    chromosome = list(chromosome)
    n = len(chromosome)
    for i in range(n):
        if random.random() < mutation_rate:  # Mutation probability
            chromosome[i] = str(random.randint(0, n - 1))  # Mutate the gene at index i
    return ''.join(chromosome)

n = 5
p = []
for i in range(4):
    c1 = createCromosome(n)
    print("Chromosome:", c1)
    p.append(c1)
    m = createBoard(c1)
    printBoard(m)
    attack1 = find_attack(c1)
    print("Attacks:", attack1)
    non_attacks = calculate_non_attacks(c1)
    print("Non-Attacks:", non_attacks)

fitness_value = fitness(p)
print("Fitness Values:", fitness_value)

parent1, parent2 = selection(fitness_value)
print("Selected Parents:", parent1, parent2)

child1, child2 = crossover(parent1, parent2, 3)
print("Crossover Children:", child1, child2)

# Perform mutation on children
mutation_rate = 0.1  # Define mutation rate
child1_mutated = mutation(child1, mutation_rate)
child2_mutated = mutation(child2, mutation_rate)

# Print mutated children
print("Mutated Child 1:", child1_mutated)
print("Mutated Child 2:", child2_mutated)
