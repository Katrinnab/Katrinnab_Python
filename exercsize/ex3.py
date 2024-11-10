from student import Student
from course_group import CourseGroup

cg = CourseGroup(Student("Вася", "Петров", 20, 1),
                 [Student("Катя", "Иванова", 19, 1),
                  Student("Ольга", "Спиридонова", 19, 1),
                  Student("Коля", "Котов", 21, 1)])

print(cg)
'''
print(f'{cg.student.first_name} {cg.student.last_name} {cg.student.age} лет')

print(f'учится на курсе {cg.student.course} вместе с:')
[print(student) for student in cg.classmates]
'''
