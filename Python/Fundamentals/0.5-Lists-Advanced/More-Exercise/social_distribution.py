population = [int(n) for n in input().split(", ")]
minimum_wealth = int(input())
for i in range(len(population)):
    wealthiest_ind = population.index(max(population))
    if population[i] < minimum_wealth:
        needed_wealth = minimum_wealth - population[i]
        if population[wealthiest_ind] - needed_wealth < minimum_wealth:
            print(f"No equal distribution possible")
            exit()
        
        population[i] += needed_wealth
        population[wealthiest_ind] -= needed_wealth

print(f"[{', '.join(str(n) for n in population)}]")
