import pyperclip


def clear_double_app(string):
    final = []
    bad_index = '"'
    for x in string:
        string = list(string)
        if x == bad_index:
            x = "'"
        final.append(x)
    final = ''.join(final)
    return final


bad_indexes = ["(", ")", "[", "]"]
tekst = pyperclip.paste()
tekst = tekst.replace('\r', '')
cosmos = tekst.split('\n')
beautiful_cosmos = []
finale_cosmos = []
for x in cosmos:
    if x == '':
        continue
    if x[0] == "(" or x[0] == "[":
        continue
    beautiful_cosmos.append(x)

for i in range(0, len(beautiful_cosmos)):
    beautiful_cosmos[i] = ('"' + clear_double_app(beautiful_cosmos[i]) + '"')

pyperclip.copy('\n'.join(beautiful_cosmos))
