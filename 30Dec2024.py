import random

def createNonAttackChromosome(n):
    # Generate a random permutation of numbers 0 to n-1
    chromosome = list(range(n))
    random.shuffle(chromosome)
    return ''.join(map(str, chromosome))

def find_attack(chromosome):
    n = len(chromosome)
    attack = 0
    for i in range(n):
        for j in range(i + 1, n):
            # Check for diagonal conflicts
            if abs(int(chromosome[i]) - int(chromosome[j])) == abs(i - j):
                attack += 1
    return attack

def total_pairs(n):
    # Total number of pairs in n queens
    return n * (n - 1) // 2

def non_attack_pairs(chromosome):
    n = len(chromosome)
    attacks = find_attack(chromosome)
    total = total_pairs(n)
    return total - attacks

def createBoard(c1):
    m = []
    n = len(c1)
    for i in range(n):
        c = [0] * n
        m.append(c)
        
    for i in range(n):
        m[i][int(c1[i])] = 1
    return m

def printBoard(m):
    for row in m:
        print(row)

n = 5  # You can set the board size here
non_attack_chromosome = createNonAttackChromosome(n)

# Verify the solution to ensure no diagonal attacks
while find_attack(non_attack_chromosome) != 0:
    non_attack_chromosome = createNonAttackChromosome(n)

print("Non-Attacking Chromosome: ", non_attack_chromosome)

m = createBoard(non_attack_chromosome)
printBoard(m)

attack_count = find_attack(non_attack_chromosome)
non_attack_count = non_attack_pairs(non_attack_chromosome)

print("Total Pairs: ", total_pairs(n))
print("Attack Count: ", attack_count)
print("Non-Attack Pairs: ", non_attack_count)
