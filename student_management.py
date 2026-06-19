students = []
#add student
def add_student():
    
    name = input("Enter student name:")
    Roll_no = input("Enter student Roll no:")
    student = {"name": name, "Roll_no": Roll_no}
    students.append(student)
    

    # view students
    def view_students():
        if not students:
            print("No students found.")
            return
        print("List of students:")
        for idx, s in enumerate(students, 1):
            print(f"{idx}. Name: {s['name']}, Roll no: {s['Roll_no']}")


    def main():
        while True:
            print('\n1. Add student\n2. View students\n3. Exit')
            choice = input('Choose an option: ')
            if choice == '1':
                add_student()
            elif choice == '2':
                view_students()
            elif choice == '3':
                break
            else:
                print('Invalid choice')

    if __name__ == '__main__':
        main()
        add_student()
        view_students()
        