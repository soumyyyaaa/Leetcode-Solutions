def checkStraightLine(coordinates):
    y1 = coordinates[1][1] - coordinates[0][1]
    x1 = coordinates[1][0] - coordinates[0][0]
    if x1 != 0:
        m1 = y1 / x1
        for i in range(1,len(coordinates) - 1):
            y2 = coordinates[i+1][1] - coordinates[i][1]
            x2 = coordinates[i+1][0] - coordinates[i][0]
            if x2 != 0:
                m2 = y2 / x2
                if m1 != m2:
                    return False
            else:
                return False
    else:
        for i in range(1,len(coordinates) - 1):
            x2 = coordinates[i+1][0] - coordinates[i][0]
            if x2 != 0:
                return False
    return True

coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
print(checkStraightLine(coordinates))