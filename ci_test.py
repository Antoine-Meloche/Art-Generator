import time
import defaultGen


def test_defaultGen():
    start = time.time()
    assert defaultGen.generate(
        2100, 1300, "#ffffff", "#242424", 50, 30, 10, 100, 10, 0, "./image.png") == 201
    end = time.time()
    print(":\nThe Default algorithm took %ss to complete" %
          (end - start), end="")