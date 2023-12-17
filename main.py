class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def grade_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            lecturer.grades.setdefault(course, []).append(grade)
        else:
            return 'Ошибка'

    def __str__(self):
        average_grade = sum([sum(grade) for grade in self.grades.values()]) / sum(
            [len(grade) for grade in self.grades.values()]) if len(self.grades) > 0 else 0
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {average_grade}\n'
                f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
                f'Завершенные курсы: {", ".join(self.finished_courses)}')

    def __le__(self, other):
        return self.compare <= other.compare

    def __lt__(self, other):
        return self.compare < other.compare

    def __ge__(self, other):
        return self.compare >= other.compare

    def __gt__(self, other):
        return self.compare > other.compare

    def __eq__(self, other):
        return self.compare == other.compare

    def __ne__(self, other):
        return self.compare != other.compare

    @property
    def compare(self):
        return sum([sum(grade) for grade in self.grades.values()]) / sum(
            [len(grade) for grade in self.grades.values()]) if len(self.grades) > 0 else 0


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}


class Lecturer(Mentor):
    def __str__(self):
        average_grade = sum([sum(grade) for grade in self.grades.values()]) / sum(
            [len(grade) for grade in self.grades.values()]) if len(self.grades) > 0 else 0
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {average_grade}')

    def __le__(self, other):
        return self.compare <= other.compare

    def __lt__(self, other):
        return self.compare < other.compare

    def __ge__(self, other):
        return self.compare >= other.compare

    def __gt__(self, other):
        return self.compare > other.compare

    def __eq__(self, other):
        return self.compare == other.compare

    def __ne__(self, other):
        return self.compare != other.compare

    @property
    def compare(self):
        return sum([sum(grade) for grade in self.grades.values()]) / sum(
            [len(grade) for grade in self.grades.values()]) if len(self.grades) > 0 else 0


class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}')


def students_average_grade(students_list, course):
    average_grade = sum(
        [sum(student.grades[course]) if course in student.grades else 0 for student in students_list]) / sum(
        [len(student.grades[course]) if course in student.grades else 0 for student in students_list]) if any(
        course in student.grades and len(student.grades[course]) > 0 for student in students_list) else 0
    return average_grade


def lector_average_grade(lectors_list, course):
    average_grade = sum(
        [sum(lector.grades[course]) if course in lector.grades else 0 for lector in lectors_list]) / sum(
        [len(lector.grades[course]) if course in lector.grades else 0 for lector in lectors_list]) if any(
        course in lector.grades and len(lector.grades[course]) > 0 for lector in lectors_list) else 0
    return average_grade


best_student1 = Student('Ruoy', 'Eman', 'your_gender')
best_student1.courses_in_progress += ['Python']
best_student2 = Student('Ruoy', 'Eman', 'your_gender')
best_student2.courses_in_progress += ['Java']

cool_mentor1 = Lecturer('Some1', 'Buddy1')
cool_mentor2 = Lecturer('Some2', 'Buddy2')
cool_mentor1.courses_attached += ['Python']
cool_mentor2.courses_attached += ['Java']

best_student1.grade_lecturer(cool_mentor1, 'Python', 10)
best_student1.grade_lecturer(cool_mentor1, 'Python', 1)
best_student2.grade_lecturer(cool_mentor2, 'Java', 1)
best_student2.grade_lecturer(cool_mentor2, 'Java', 5)

reviewer1 = Reviewer('Some1', 'Buddy1')
reviewer2 = Reviewer('Some2', 'Buddy2')
reviewer1.courses_attached += ['Python']
reviewer2.courses_attached += ['Java']

reviewer1.rate_hw(best_student1, 'Python', 10)
reviewer1.rate_hw(best_student1, 'Python', 10)
reviewer1.rate_hw(best_student1, 'Python', 10)
reviewer2.rate_hw(best_student2, 'Java', 10)
reviewer2.rate_hw(best_student2, 'Java', 10)

print(students_average_grade([best_student1, best_student2], 'Python'))
print(students_average_grade([best_student1, best_student2], 'Java'))
print(lector_average_grade([cool_mentor1, cool_mentor2], 'Python'))
print(lector_average_grade([cool_mentor1, cool_mentor2], 'Java'))

print(best_student1 < cool_mentor2)
print(best_student2 != cool_mentor2)
print(best_student1 > cool_mentor1)
print(best_student2 == cool_mentor1)
