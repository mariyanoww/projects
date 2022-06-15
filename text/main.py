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


tekst = pyperclip.paste()
tekst = tekst.replace('\r', '')
cosmos = tekst.split('\n')
for i in range(0, len(cosmos)):
    cosmos[i] = ('"' + clear_double_app(cosmos[i]) + '"')
pyperclip.copy('\n'.join(cosmos))
