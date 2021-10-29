import time
import defaultGen
import pipesGen


def test_defaultGen():
    start = time.time()
    assert defaultGen.generate(
        2100, 1300, "#ffffff", "#242424", 50, 30, 10, 100, 10, 0, "./image.png") == 201
    end = time.time()
    print(":\nThe Default algorithm took %ss to complete" %
          (end - start), end="")


def test_pipesGen():
    start = time.time()
    assert pipesGen.generate(2100, 1300, "#242424",
                             "#ffffff", 3, .75, "./image.gif")
    end = time.time()
    print("\nThe Pipes algorithm took %ss to complete" % (end - start))
