# 1) LISTA STUDENTÓW:
students = []
students.append('c, 16, Milena Napierała'.split(','))
students.append('d, 17, Zuza Napierała'.split(','))
students.append('d, 13, Ola Napierała'.split(','))

# 2) DODAWANIE STUDENTÓW:
def add_student():
    student = input('Wpisz klasę, numer, imię i nazwisko: ').split(',')
    students.append(student)
    print('Dodano ucznia')
add_student() #można to wykomentować podczas sprawdzania części kodu

# 3) WYŚWIETLANIE LISTY WSZYSTKICH STUDENTÓW:
def show_students(students: list):
    for student in students:
        print(student)
show_students() #można to wykomentować podczas sprawdzania części kodu

# 4) WYŚWIETLANIE STUDENTÓW Z POSZCZEGÓLNYCH KLAS:
class_name = input('Którą klasę chcesz wyświetlić?')

def show_students_from_one_class(students: list, class_name: str):
    for student in students:
        # print(student[0]) - bierzemy pod uwagę tylko 1-wszy element z listy
        if student[0] == class_name:
            print(student)
        # else: - niepotrzebne jeśli po nim jest pass
        #     pass
show_students_from_one_class(students)