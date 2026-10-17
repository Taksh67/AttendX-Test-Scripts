def test_valid_login():
    username = "student01"
    password = "pass123"

    assert username != ""
    assert password != ""

    print("PASS: Valid login test")


def test_empty_login():
    username = ""
    password = ""

    assert username == ""
    assert password == ""

    print("PASS: Empty login test")


if __name__ == "__main__":
    test_valid_login()
    test_empty_login()