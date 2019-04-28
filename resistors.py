def encode_resistor_colors(ohms_string):
    hash = {'0': 'black', '1': 'brown', '2': 'red', '3': 'orange', '4': 'yellow', '5': 'green', '6': 'blue', '7': 'violet', '8': 'gray', '9': 'white', 'ohms' : 'gold'}
    string = str.split(ohms_string)
    change = string[0]
    #replaces letter with value in zeros in last position of array.
    if "k" in change:
        new = [w.replace('k', '000') for w in change]
    elif "M" in change:
        new = [w.replace('M', '000000') for w in change]
    else:
        new = change

    num = list(new)
    new_arr = []
    # removes letter value and adds the equivalent in zeros with each zero as a separate element.
    if len(num[-1]) > 1:
        x = list(num[-1])
        num.remove(num[-1])
        numb = num + x
    else:
        numb = num
    # removes one decimal space if there is a decimal in the list.
    if "." in numb:
        numb.remove(".")
        numb.remove(numb[-1])
    # divides array into two. First half has the first two numbers, second half has the rest.
    # the length of the second half replaces the zeros.
    # the zero is turned into a string and added to the array.
    one = numb[0:2]
    two = numb[2::]
    ans = str(len(two))
    del numb[2::]
    numb.append(ans)
    # replaces number values for colors using the dictionary.
    for key, value in hash.items():
        for n in numb:
            new_arr.append(hash[n])
        output = " ".join(new_arr)

        return output + " gold"


ohms_string = "100k ohms"

print(encode_resistor_colors(ohms_string))
