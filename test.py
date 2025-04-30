from Attendence import register, view_attendence, mark_attendence

def test_cases():
    assert register("Gayathri", "gayathri@gmail.com", "12345678") == "Email already exists"
    assert mark_attendence("001", "gayathri@gmail.com", "30-04-2025") == "Attendence marked"
    assert view_attendence("001", "gayathri@gmail.com") == "Attendence of 001 : ['30-04-2025']"

test_cases()