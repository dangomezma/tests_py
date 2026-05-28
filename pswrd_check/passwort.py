def is_over_8(text):
    return len(text) >= 8

def has_caps(text):
    return any(i.isupper() for i in text)

def has_minuscule(text):
    return any(i.islower() for i in text)

def has_num(text):
    return any(i.isdigit() for i in text)

def has_no_blanks(text):
    return " " not in text
    
def is_valid_password(text):
    check=[is_over_8(text), has_caps(text), has_minuscule(text), has_num(text), has_no_blanks(text)]
    return all(check)

if __name__ == "__main__":
    password = input("Passwort eingeben: ")
    is_valid_password(password)