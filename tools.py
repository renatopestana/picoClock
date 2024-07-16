def rjust(txt, lenght, character):
    while len(txt) < lenght:
        txt = character + txt
    return txt


def ljust(txt, lenght, character):
    while len(txt) < lenght:
        txt = txt + character
    return txt

