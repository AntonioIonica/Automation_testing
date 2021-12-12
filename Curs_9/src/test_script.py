"""
Test case-fuzzywuzzy
"""
from fuzzywuzzy import fuzz


def test_case1(input_data, expected_data):
    similarity = fuzz.partial_ratio(input_data, expected_data)
    if similarity > 90:
        print(f'Test passed with the score of {similarity}!')
    elif 80 < similarity < 90:
        print(f'Test passed with the score of {similarity}! There is a warning!')
    else:
        print(f'Test failed with the score of {similarity}!')
    return similarity

def test_case2(input_data, expected_data):
    q_ratio = fuzz.QRatio(input_data, expected_data)
    if q_ratio > 80:
        print(f'Test passed with the score of QRatio of {q_ratio}!')
    elif 60 < q_ratio < 80:
        print(f'QRatio test passed with a score of {q_ratio}!')
    else:
        print(f'Test failed with a QRatio of {q_ratio}!')
    return q_ratio

# TODO QRatio from fuzzywuzzy
