def encrypt(text, encryptKey):
    #all rows
    line_1 = list("qwertyuiop")
    line_1b = list("QWERTYUIOP")
    line_2 = list("asdfghjkl")
    line_2b = list("ASDFGHJKL")
    line_3 = list("zxcvbnm,.")
    line_3b = list("ZXCVBNM<>")
    encryptKey = list(str(encryptKey))
    num = []
    #turns encryptKey from a string into a list of integers
    for i in encryptKey:
        i = int(i)
        num.append(i)
    #adds zeros if length of encryptKey is less than three
    if len(num) == 2:
        num.append(0)
    if len(num) == 1:
        num.append(0)
        num.append(0)
    #create empty output array
    output = []
    #turns text into a list
    text = list(text)
    #adds encryptKey to index values of all letters in text, finds mod of that with length of the row and adds to the output array.
    for n in line_1 or line_2 or line_3 or line_1b or line_2b or line_3b:
        for l in text:
            if l in line_1:
                a = (line_1.index(l) + num[0]) % len(line_1)
                output.append(line_1[a])
            elif l in line_1b:
                a = (line_1b.index(l) + num[0]) % len(line_1b)
                output.append(line_1b[a])
            elif l in line_2:
                a = (line_2.index(l) + num[1]) % len(line_2)
                output.append(line_2[a])
            elif l in line_2b:
                a = (line_2b.index(l) + num[1]) %  len(line_2b)
                output.append(line_2b[a])
            elif l in line_3:
                a = (line_3.index(l) + num[2]) % len(line_3)
                output.append(line_3[a])
            elif l in line_3b:
                a = (line_3b.index(l) + num[2]) % len(line_3b)
                output.append(line_3b[a])
            elif l not in line_1 or line_2 or line_3 or line_1b or line_2b or line_3b:
                output.append(l)
            #if letter from text not in any rows, adds to output
            else:
                output.append(l)
        #joins output array and returns it
        return "".join(output)


def decrypt(text, encryptKey):
    #all rows
    line_1 = list("qwertyuiop")
    line_1b = list("QWERTYUIOP")
    line_2 = list("asdfghjkl")
    line_2b = list("ASDFGHJKL")
    line_3 = list("zxcvbnm,.")
    line_3b = list("ZXCVBNM<>")
    encryptKey = list(str(encryptKey))
    num = []
    #turns encryptKey from a string into a list of integers
    for i in encryptKey:
        i = int(i)
        num.append(i)
    #adds zeros if length of encryptKey is less than three
    if len(num) == 2:
        num.append(0)
    if len(num) == 1:
        num.append(0)
        num.append(0)
    #create empty output array
    output = []
    #turns text into a list
    text = list(text)
    #subtracts encryptKey from index values of all letters in text, finds mod of that with length of the row and adds to the output array.
    for n in line_1 or line_2 or line_3 or line_1b or line_2b or line_3b:
        for l in text:
            if l in line_1:
                a = (line_1.index(l) - num[0]) % 10
                output.append(line_1[a])
            elif l in line_1b:
                a = (line_1b.index(l) - num[0]) % 10
                output.append(line_1b[a])
            elif l in line_2:
                a = (line_2.index(l) - num[1]) % 9
                output.append(line_2[a])
            elif l in line_2b:
                a = (line_2b.index(l) - num[1]) % 9
                output.append(line_2b[a])
            elif l in line_3:
                a = (line_3.index(l) - num[2]) % 9
                output.append(line_3[a])
            elif l in line_3b:
                a = (line_3b.index(l) - num[2]) % 9
                output.append(line_3b[a])
            #if letter from text not in any rows, adds to output
            else:
                output.append(l)
        #joins output array and returns it
        return "".join(output)

print(encrypt("This is a test.", 348))


print(decrypt("Iaqh qh g iyhi,", 348))
