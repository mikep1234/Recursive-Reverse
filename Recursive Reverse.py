def Reverse(string, nstring, i):
    if len(nstring) == len(string):
        return nstring
    nstring += string[i]
    return Reverse(string, nstring, i - 1)

x = "hello"

print(Reverse(x, "", len(x) - 1))

x = "nohtyp"

print(Reverse(x, "", len(x) - 1))