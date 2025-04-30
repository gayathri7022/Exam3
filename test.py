from Attendence import register, view_attendence, mark_attendence, students



def test_cases():
    students.clear()
    assert register("Gayathri", "gayathri@gmail.com", "12345678") == "Registration successfull"
    assert mark_attendence("001", "gayathri@gmail.com", "30-04-2025") == "Attendence marked"
    result = view_attendence("001","gayathri@gmail.com" )
    assert result == "Attendence of 001 : ['30-04-2025']"

test_cases()