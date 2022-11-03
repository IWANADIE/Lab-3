import bmi_calculator as bmi

def test_bmi_over_weight():
    result = bmi.test_calculate_bmi(1.73,100)
    assert (result == 1)

def test_bmi_normal_weight():
    result = bmi.test_calculate_bmi(1.75,60)
    assert (result == 0)

def test_bmi_under_weight():
    result = bmi.test_calculate_bmi(1.75,40)
    assert (result == -1)