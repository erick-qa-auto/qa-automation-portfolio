# the password validation
def is_valid_password(password):
    if len(password) < 8:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char in "!@#$%^&*" for char in password):
        return False
    return True

# test1: positive user journey
def test_is_valid_password_positive():
    assert is_valid_password("Password1!") == True # all true

#  tests2: negative user journey                          
def test_is_valid_password_negative():
    assert is_valid_password("password1!") == False # without isupper
    assert is_valid_password("Password!") == False # without isdigit
    assert is_valid_password("Password1") == False # without symbols

# test3: boundary char.isdigit len
def test_is_valid_password_boundary():
    assert is_valid_password("Sword1!") == False # 7 characters
    assert is_valid_password("Assword1!") == True # 9 characters
    assert is_valid_password("Password1@") == True # 8 characters

# tests4: other tests
def test_is_valid_password_other():
    assert is_valid_password("pppPPPaaaAAAsssSSSwwwWxfghsnsfyhynjsergthbzbtgabefgzawetyubdrvsteztrfaveygesrbhtyfyuolfdutkjhregtsveacshtrQ#%$##$Q@QWWoooOOOrrrDDD1234567890!#@&%^&*") == True # any more characters
    assert is_valid_password("") == False # empty input field
   # assert is_valid_password("_SELECT * FROM users WHERE username = 'admin' OR '1'='1';") == True # sql Li injection