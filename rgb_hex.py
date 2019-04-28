def rgb(r,g,b):
    arr = [r,g,b]
    first = 0
    second = 0
    output = []
    numbers = []
    #all integer values and their hex equivalents
    hash = {0:"0",
    1:"1",
    2 :"2",
    3:"3",
    4:"4",
    5:"5",
    6:"6",
    7:"7",
    8:"8",
    9:"9",
    10:"A",
    11:"B",
    12:"C",
    13:"D",
    14:"E",
    15:"F"
    }
    for n in arr:
        #if number is greater than 255, assign 15 as value for first and second.
        if n> 255:
            first = 15
            second =15
        #if number is greater than zero, divide it by 16 first (store in first), and then store the remainder in second.
        elif n > 0:
            first = n // 16
            second = n % 16
        #if number less than 0, assign zero for value for first and second.
        else:
            first = 0
            second = 0
        #add both first and second to numbers
        numbers.append(first)
        numbers.append(second)
    #add hex equivalents to numbers in output using the hash.
    for key,value in hash.items():
        for num in numbers:
            if num in hash:
                output.append(hash[num])
        #join the list of values.
        return "".join(output)



print(rgb(-20,275,125))
