with open('input.txt', 'r') as f:
    # Build a matrix
    matrix = []
    lines = f.readlines()
    for line in lines:
        line = line[:12]
        matrix.append([int(digit) for digit in line])
        
    # Transpose the rows and columns.
    matrix = zip(*matrix)
    
    # Calculate the rates.
    gamma = []
    epsilon = []
    for row in matrix:
        ones = sum(1 for digit in row if digit)
        zeros = sum(1 for digit in row if not digit)
        
        if ones > zeros:
            gamma.append('1')
            epsilon.append('0')
        elif zeros > ones:
            gamma.append('0')
            epsilon.append('1')
    
    # Convert binary to decimal.
    gamma = int(''.join(gamma), 2)
    epsilon = int(''.join(epsilon), 2)
    
    print(gamma * epsilon)
