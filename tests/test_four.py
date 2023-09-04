def test_passing():
    x = ['a', 'b', 'c']
    y: list[int] = [1, 2, 3]
    assert not x == y
