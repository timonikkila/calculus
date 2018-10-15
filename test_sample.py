from string_to_val import calculate

# content of test_sample.py
def inc(x):
    return x + 1


def test_answer():

    test_val = calculate("2 * (23/(33))- 23 * (23)")
    assert test_val > -527.6060606060607
    assert test_val < -527.6060606060605
