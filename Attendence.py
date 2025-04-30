students = {

}

def register(name, email, password):
    if not email.endswith("@gmail.com"):
        return "Invalid email"
    if not len(password) >= 8:
        return "Password length must be 8 characters long" 
    if not email in students:
        students[email] = {"name" : name, "password" : password, "ID" : "001", "presence" : []}
        return "Registration successfull"
    else:
        return "Email already exists"

def login(email, password):
    if email not in students:
        return "Invalid email"
    if students[email]["password"] == password:
        return "Login successfull"
    return "Invalid password"
        

def mark_attendence(studentid, email, date):
    email = email.lower()
    if email not in students:
        return "Invalid email"
    if students[email]["ID"] == studentid:
        students[email]["presence"].append(date)
        return "Attendence marked"
    return "Invalid ID"

def view_attendence(studentid, email):
    if email not in students:
        return "Invalid email"
    return f"Attendence of {studentid} : {students[email]["presence"]}"


print(students)
print(register("Gayathri", "gayathri@gmail.com", "12345678"))
print(mark_attendence("001", "gayathri@gmail.com", "30-04-2025"))
print(view_attendence("001","gayathri@gmail.com" ))

