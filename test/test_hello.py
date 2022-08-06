from main import hello


def test_hello():

    assert hello("Ray") == "Hello, Ray"
    

def test_default():

    assert hello() == "Hello, world"