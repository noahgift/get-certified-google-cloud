from app import marco


def test_marco():
    assert marco("Marco") == "Polo"
    assert marco("Peter") == "Bob"
