def is_valid_email(email):
    if "@" not in email:
        return False
    if "." not in email:
        return False
    if email.index("@") > email.rindex("."):
        return False
    if len(email) < 5:
        return False
    return True

#test1 positive test
def test_is_valid_email_with_valid():
    assert is_valid_email("user@mail.com") == True
    assert is_valid_email("user@mail.by") == True
    assert is_valid_email("uSe_r123@outlook.com") == True

#test2 negative test 
def test_is_valid_email_without_valid():
    assert is_valid_email("usermail.com") == False # without @
    assert is_valid_email("user@mailcom") == False # without "."
    assert is_valid_email("user.mail@com") ==False # position of @ after the last dot

#test3 email boundary
def test_is_valid_email_boundary():
    assert is_valid_email("a@b.c") == True # 5 simbols
    assert is_valid_email("a@.b") == False # 4 simbols
    assert is_valid_email("ab@.cD") == True # 6 simbols

#test4 other test
def test_is_valid_email_other():
    assert is_valid_email("@mail.com") == True # The function does not check for the presence of a username.
    assert is_valid_email("user@com.") == True # bad email - the function is imperfect 