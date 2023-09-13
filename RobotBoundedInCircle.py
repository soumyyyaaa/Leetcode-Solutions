def isRobotBounded(instructions):
    instructions = list(instructions)
    coordinates = [0, 0, 'N']
    n = ['W', 'E']
    s = ['E', 'W']
    e = ['N', 'S']
    w = ['S', 'N']
    for i in range(0, len(instructions)):
        if instructions[i] == 'G':
            if coordinates[2] == 'N':
                coordinates[1] += 1
            elif coordinates[2] == 'S':
                coordinates[1] -= 1
            elif coordinates[2] == 'E':
                coordinates[0] += 1
            elif coordinates[2] == 'W':
                coordinates[0] -= 1
        elif instructions[i] == 'L':
            if coordinates[2] == 'N':
                coordinates[2] = n[0]
            elif coordinates[2] == 'S':
                coordinates[2] = s[0]
            elif coordinates[2] == 'E':
                coordinates[2] = e[0]
            elif coordinates[2] == 'W':
                coordinates[2] = w[0]
        elif instructions[i] == 'R':
            if coordinates[2] == 'N':
                coordinates[2] = n[1]
            elif coordinates[2] == 'S':
                coordinates[2] = s[1]
            elif coordinates[2] == 'E':
                coordinates[2] = e[1]
            elif coordinates[2] == 'W':
                coordinates[2] = w[1]
        
    if (coordinates[0] == 0 and coordinates[1] == 0) or (coordinates[2] != 'N'):
        return True

    return False

instructions = "GG"
print(isRobotBounded(instructions))