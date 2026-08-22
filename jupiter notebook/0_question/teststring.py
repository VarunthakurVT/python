from stringt import hello
def test_default():
    assert hello()=="hello,world"
def test_argunment():
    assert hello("varun")=="hello,varun"
