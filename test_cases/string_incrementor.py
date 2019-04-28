def increment_string(words):
    count = len(words)
    words = list(words)
    num = []
    output = []
    for n in words:
        count -= 1
        #if last value in list is a digit, add its count to the front of num.
        if words[count].isdigit() == True:
            num.insert(0, count)
        #if last value in list is not a digit, add 1.
        elif words[-1].isdigit() == False:
            words = "".join(words)
            output = words + "1"
            return output
        #stop adding to num if value is a letter.
        elif words[count].isdigit() == False:
            break
    if len(words) == 0:
        output = "1"

    else:
        #take the first value in num.
        div = num[0]
        #use the value to seperate the digits from the letters in the input. Store in num_1.
        nums_1 = words[div:]
        #join all the digits.
        nums_1 = "".join(nums_1)
        #turn the digits into an integer and then add 1.
        nums_2 = int(nums_1)
        nums_2 = nums_2 + 1
        #take the letters from the input and add it to the output. Join them together.
        output = words[:div]
        output = "".join(output)
        #num_l is the length of the digits after 1 was added.
        num_l = str(nums_2)
        num_l = len(num_l)
        #total is the length of the digits before 1 was added.
        total = str(nums_1)
        total = len(total)
        #finding how much longer original num length is to present num length
        if total > num_l:
            nums_2 = str(nums_2)
            #fill extra space with zeros.
            nums_2 = nums_2.zfill(total)
        #add letters with numbers.
        output = output + str(nums_2)
    return output


print(increment_string("foo"))
