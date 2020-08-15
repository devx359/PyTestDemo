import  pytest

@pytest.mark.skip
def test_b():
    print("Hey in test A")

@pytest.mark.reg
def test_a():
    print("In Test B")

@pytest.mark.sanity
def test_c():
    print("In Test C")
