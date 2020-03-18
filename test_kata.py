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

def test_two_numbers():
    assert kata.add("1,2") == 3
    assert kata.add("2,3") == 5
    assert kata.add("3,4") == 7
    assert kata.add("4,5") == 9
    assert kata.add("5,6") == 11
    assert kata.add("6,6") == 12
    assert kata.add("7,1") == 8
    assert kata.add("8,9") == 17
    assert kata.add("9,4") == 13
    assert kata.add("10,6") == 16

#def test_more_than_one_numbers():
    #assert kata.add("1,2") == 3
    #assert kata.add("2,2,3") == 7
    #assert kata.add("5,2,4") == 11
    #assert kata.add("4,4,4,4,4,3") == 25
    #assert kata.add("2") == 2
    #assert kata.add("6,6") == 12
    #assert kata.add("7,1,1,1,1,1,1") == 13
    #assert kata.add("8,6,4") == 18
    #assert kata.add("9,3,5,2") == 19
    #assert kata.add("10,1") == 11

## pytest <filename with the test> ###############