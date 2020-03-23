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
    assert kata.add("100") == 100

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

def test_more_than_two_numbers():
    assert kata.add("1,2,3") == 6
    assert kata.add("2,2,3") == 7
    assert kata.add("5,2,4") == 11
    assert kata.add("4,4,4,4,4,3") == 23
    assert kata.add("2,6,3") == 11
    assert kata.add("6,6,6") == 18
    assert kata.add("7,1,1,1,1,1,1") == 13
    assert kata.add("8,6,4") == 18
    assert kata.add("9,3,5,2") == 19
    assert kata.add("10,1,7") == 18

def test_new_lines():
    assert kata.add("1\n2,3") == 6
    assert kata.add("7\n1,1,1\n1,1\n1") == 13
    assert kata.add("8,6\n4") == 18
    assert kata.add("9,3\n5\n2") == 19
    assert kata.add("10\n1\n7") == 18

def test_greate_than_1000():
    assert kata.add("1001,2") == 2
    assert kata.add("10001\n1\n7") == 8
    assert kata.add("1000\n1\n7") == 1008
    assert kata.add("10000,10000,100001,3000000\n3") == 3

def test_negatives():
    assert kata.add("-1,3") == "Negatives not allowed: -1"
    assert kata.add("1,-3") == "Negatives not allowed: -3"
    assert kata.add("-1,-3") == "Negatives not allowed: -1,-3"
    assert kata.add("-1,3,4,6,2,-4,-6") == "Negatives not allowed: -1,-4,-6"
    assert kata.add("-1,3,4,6,2,-6") == "Negatives not allowed: -1,-6"
    assert kata.add("-1,-3,-9") == "Negatives not allowed: -1,-3,-9"

def test_different_methods():
    assert kata.add("//X\n1X2") == 3
    assert kata.add("//%\n1%2%3") == 6
    assert kata.add("/1/%\n%10000%3") == 4
    assert kata.add("/1/%\n%100%3") == 104
    assert kata.add("//%\n1%2%3") == 6
    assert kata.add("//%\n100%2%3") == 105
    assert kata.add("/909/%\n%2%3") == 914

    
## pytest <filename with the test> ###############