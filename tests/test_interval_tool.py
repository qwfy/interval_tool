from interval_tool import geq_threshold_and_merge_linear_id


def test_linear_id():
    #     0  1  2  3  4  5  6  7  8  8  10 11 12 13 14
    xs = [0, 2, 2, 1, 2, 2, 2, 2, 1, 1, 1, 2, 3, 3, 3]
    w = 0.2
    threshold = 2
    min_length = 0.401
    max_break = 0.5
    expectation = [
        [[1, 2], [2, 2], [4, 2], [5, 2], [6, 2], [7, 2]],
        [[11, 2], [12, 3], [13, 3], [14, 3]]
    ]
    actual = geq_threshold_and_merge_linear_id(xs, threshold, max_break, min_length, w)
    assert actual == expectation

    w = 0.2
    threshold = 2
    min_length = 0.401
    max_break = 0.19
    expectation = [
        [[4, 2], [5, 2], [6, 2], [7, 2]],
        [[11, 2], [12, 3], [13, 3], [14, 3]]
    ]
    actual = geq_threshold_and_merge_linear_id(xs, threshold, max_break, min_length, w)
    assert actual == expectation
