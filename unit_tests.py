from gol import step_state

if __name__ == '__main__':

    test_boards = []

    # Test 1: Dead board should stay dead
    init = [
        [0,0,0],
        [0,0,0],
        [0,0,0],
    ]
    final = init
    test_boards.append((init, final))

    # Test 2: Dead cells with exactly 3 neighbors should come alive
    init = [
        [0,0,1],
        [0,1,1],
        [0,0,0]
    ]
    final = [
        [0,1,1],
        [0,1,1],
        [0,0,0]
    ]
    test_boards.append((init, final))

    # Test 3: Live cell dies with underpopulation (0 or 1 neighbors)
    init = [
        [1,0,0],
        [1,0,0],
        [0,0,0]
    ]
    final = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]
    test_boards.append((init, final))

    # Test 4: Live cells stay alive w/ 2 or 3 neighbors
    init = [
        [1,1,0],
        [1,1,0],
        [0,0,0]
    ]
    final = init
    test_boards.append((init,final))

    # Test 5: Live cell dies from overpopulation (>3 neighbors)
    init = [
        [1,0,0,0],
        [1,1,1,0],
        [1,0,1,0],
        [0,0,0,0]
    ]
    final = [
        [1,0,0,0],
        [1,0,1,0],
        [1,0,1,0],
        [0,0,0,0]
    ]
    test_boards.append((init,final))

    i = 0
    for init,final in test_boards:
        print("Test #" + str(i+1))
        result = step_state(init)
        if final == result:
            print("PASSED")
        else:
            print("FAILED")
            print("Expected:\n" + str(final))
            print("Got:\n" + str(result))

        i += 1
