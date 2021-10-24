import defaultGen

def test_defaultGen():
    assert defaultGen.generate(2100, 1300, "#ffffff", "#242424", 50, 30, 10, 100, 10, 0, "./image.png") == 201
