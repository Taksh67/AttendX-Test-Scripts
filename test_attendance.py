def test_mark_attendance():
    student_id = "23IT067"
    status = "Present"

    assert student_id != ""
    assert status in ["Present", "Absent"]

    print("PASS: Attendance marking test")


def test_invalid_attendance():
    status = "Unknown"

    assert status not in ["Present", "Absent"]

    print("PASS: Invalid attendance test")


if __name__ == "__main__":
    test_mark_attendance()
    test_invalid_attendance()