#translates all letters into their corresponding numbers.
let_num = {
"a" : 1,
"b" : 2,
"c" : 3,
"d" : 4,
"e" : 5,
"f" : 6,
"g" : 7,
"h" : 8,
"i" : 9,
"j" : 10,
"k" : 11,
"l" : 12,
"m" : 13,
"n" : 14,
"o" : 15,
"p" : 16,
"q" : 17,
"r" : 18,
"s" : 19,
"t" : 20,
"u" : 21,
"v" : 22,
"w" : 23,
"x" : 24,
"y" : 25,
"z" : 26,
}
num_let = {
1: "a",
2: "b",
3: "c",
4: "d",
5: "e",
6: "f",
7: "g",
8: "h",
9: "i",
10: "j",
11: "k",
12: "l",
13: "m",
14: "n",
15: "o",
16: "p",
17: "q",
18: "r",
19: "s",
20: "t",
21: "u",
22: "v",
23: "w",
24: "x",
25: "y",
26: "z",

}

def encrypt(str, shift):
    #makes entire str lowercase
    let = str.lower()
    #lists all string input
    let = list(let)
    new_arr = []
    ans = []
    output = []

    for key, value in let_num.items():
        for n in let:
            if n in let_num:
                new_arr.append(let_num[n])
            else:
                new_arr.append(n)
        #adds shift to each number
        for n in new_arr:
            if n in num_let:
                n = n + shift
                if n > 26:
                    n = n%26
                    ans.append(n)
                else:
                    ans.append(n)
            else:
                ans.append(n)
        #translates all numbers into their corresponding letters.
        for key,value in num_let.items():
            for n in ans:
                if n in num_let:
                    output.append(num_let[n])
                else:
                    output.append(n)
            #joins the list.
            output = "".join(output)
            return output


print(encrypt("How are you?", 5))

def decrypt(str, shift):
    #makes entire str lowercase
    let = str.lower()
    let = list(let)
    new_arr = []
    ans = []
    output = []
    for key, value in let_num.items():
        for n in let:
            if n in let_num:
                new_arr.append(let_num[n])
            else:
                new_arr.append(n)
        #subtracts shift from each number
        for n in new_arr:
            if n in num_let:
                n = n - shift
                if n < 0:
                    n = n + 26
                    ans.append(n)
                elif n >= 26:
                    n = n%26
                    ans.append(n)
                else:
                    ans.append(n)

            else:
                ans.append(n)
        #return ans
        for key,value in num_let.items():
            for n in ans:
                if n in num_let:
                    output.append(num_let[n])
                else:
                    output.append(n)

            #joins the list.
            output = "".join(output)
            return output



print(decrypt("mtb fwj dtz?", 5))
