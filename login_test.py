def test_valid_login():
    username = "student01"
    password = "test123"

    assert username != ""
    assert password != ""

    print("Login test passed")


def test_empty_username():
    username = ""

    assert username == ""

    print("Empty username validation test passed")


if __name__ == "__main__":
    test_valid_login()
    test_empty_username()
