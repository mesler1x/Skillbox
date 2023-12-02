import re

def is_valid_password(password):
    if len(password) < 8:
        return False

    if re.findall(r'(\w)\1', password) is None:
        return False

    if re.search(r'\d', password) is None:
        return False

    special_chars = re.findall('[^a-zA-Z0-9]', password)
    if len(set(special_chars)) < 3:
        return False

    if re.search(r'[,\.!?]', password) is not None:
        return False

    return True

def test_is_valid_password():
    """
    >>> is_valid_password('rtG&3FG#Tr^e')
    True
    >>> is_valid_password('a^A1@*@1Aa')
    True
    >>> is_valid_password('oF^a1D@y5%e6')
    True
    >>> is_valid_password('enroi#$*rkdeR#$*092uwedchf34tguv394h')
    True
    >>> is_valid_password('пароль')
    False
    >>> is_valid_password('password')
    False
    >>> is_valid_password('qwerty')
    False
    >>> is_valid_password('lOngPa$$W0Rd')
    False
    """
    pass

test_is_valid_password()