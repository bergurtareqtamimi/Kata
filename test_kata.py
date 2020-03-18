import kata

def test_for_empty_str():
    assert kata.add("") == 0

def test_for_single_digit():
    
    assert kata.add("1") == 1
    assert kata.add("2") == 2
    assert kata.add("3") == 3
    assert kata.add("4") == 4
    assert kata.add("5") == 5
    assert kata.add("6") == 6
    assert kata.add("7") == 7
    assert kata.add("8") == 8
    assert kata.add("9") == 9
    assert kata.add("10") == 10

## pytest <filename with the test> ###############