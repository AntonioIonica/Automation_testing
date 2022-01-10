"""
accumulator function by increasing with 1 or specified number
"""


def test_accumulator_init(accum):
    assert accum.count == 0


def test_accumulator_add_itself(accum):
    accum.add()
    assert accum.count == 1


def test_accumulator_set(accum):
    accum.add(3)
    assert accum.count == 3
