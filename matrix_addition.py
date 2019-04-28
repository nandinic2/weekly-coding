def matrix_addition(a, b):
    m = len(a)
    output = []
    #create matrix with zeros
    for i in range(0,m):
      output.append([])
      for j in range(0,m):
          output[i].append(0)
    #replace zeros in matrix with the sums
    for row in range(len(a)):
        for col in range(len(a)):
            output[row][col] =  a[row][col] + b[row][col]
    return output
