#input:
# 1 str: n substrings
#n>=2
#nested loop to compare matrix
s = "466960, 469060, 111111"

def pos_average(s):
    arr = s.split(", ")
    matrix = []

    pos = 0
    for n in arr:
        n = list(n)
        matrix.append(n)
    count = len(matrix)
    for row in range(len(matrix)):
        count -=1
        for col in range(len(matrix)):
            if matrix[row][col] == matrix[count][col]:
                pos += 1

    return pos


    return matrix

print(pos_average(s))
