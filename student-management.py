class Student:
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no
    def display(self):
        print("Name",self.name,"Roll_no",self.roll_no)
class StudentManager:
    def __init__(self):
        self.students=[]
    def add_students(self,name,roll_no):
        self.students.append(Student(name,roll_no))
        print(f"student:{name} added successfully")
    def show_students(self):
        if not self.students:
            print("no student found")
            return
        print("students lists:")
        for student in self.students:
            student.display()
    def delete_students(self,roll):
        for student in self.students:
            if student.roll_no==roll:
                self.students.remove(student)
                print(f"student with {roll} removed successfully")
                return
        print(f"no roll_no with {roll} found")
    def search_students(self,roll):
        for student in self.students:
            if student.roll_no==roll:
                print(f"student with {roll} found successfully")
                student.display()
                return
        print(f"no roll_no with {roll} found")
sm=StudentManager()
sm.add_students("hiba",221)
sm.add_students("wafa",222)
sm.add_students("amna",223)
sm.show_students()
sm.delete_students(224)
sm.delete_students(223)
sm.show_students()
sm.search_students(221)

        
    
