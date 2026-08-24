from app import calculate_grade, scholarship_eligible


def test_grade_a():
    assert calculate_grade(95) == "A"


def test_grade_b():
    assert calculate_grade(82) == "A"


def test_grade_fail():
    assert calculate_grade(35) == "F"


def test_scholarship_eligible():
    assert scholarship_eligible(85, 80) is True


def test_scholarship_not_eligible():
    assert scholarship_eligible(85, 70) is False
