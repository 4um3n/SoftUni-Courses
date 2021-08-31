def tribonacci_sequence(n):
    sequence = [1, 1, 2]
    if n <= 3:
        return sequence[:n]
    
    i = 0
    while n > len(sequence):
        new_n = sequence[i] + sequence[i +1] + sequence[i +2]
        sequence.append(new_n)
        i += 1
    
    return sequence


numbers = tribonacci_sequence(int(input()))
print(' '.join(str(s) for s in numbers))
