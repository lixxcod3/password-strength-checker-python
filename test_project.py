from project import password_recommendation, len_valid, content_valid

def test_password_recommendation():
    password = password_recommendation()
    assert isinstance(password, str)
    assert len(password) == 8
    assert any(char.isdigit() for char in password)
    assert any(char.isupper() for char in password)
    assert any(char.islower() for char in password)


def test_len_valid():
    assert len_valid("12345678") == True
    assert len_valid("1234567") == False

def test_content_valid():
    assert content_valid("$1234Hhh") == True
    # Missing number
    assert content_valid("$HHhhhhh") == False
    # Missing uppercase
    assert content_valid("$1234hhh") == False
    # Missing lowercase
    assert content_valid("$1234HHH") == False
    # Missing symbol
    assert content_valid("1234Hhhh") == False
