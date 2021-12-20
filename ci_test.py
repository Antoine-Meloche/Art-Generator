from time import time
import defaultGen
import perlinCircleGen
import wavesGen


def test_defaultGen():
    start = time()
    assert defaultGen.generate(
        2100, 1300, "#ffffff", "#242424", 50, 30, 10, 100, 10, 0, "./image.png") == 201
    end = time()
    print(":\nThe Default algorithm took %ss to complete" %
          (end - start), end="")


def test_perlinCircleGen():
    start = time()
    assert perlinCircleGen.generate(
        1200, 1200, "#ffffff", "#242424", "./image.png") == 201
    end = time()
    print(":\nThe Perlin Circle algorithm took %ss to complete" %
          (end - start), end="")


def test_wavesGen():
    start = time()
    assert wavesGen.generate(2100, 1300, "#ffffff",
                             "#242424", 10, 24, 2, "./waves.webp") == 201
    end = time()
    print(":\nThe Waves generation algorithm took %ss to complete" %
          (end - start), end="")
