class SchoolMember:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Teacher(SchoolMember):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary
        self.courses = {}

    def getSalary(self):
        return self.salary

    def addCourse(self, signature, name):
        self.courses[signature] = name

    def getCourses(self):
        return "\n".join(f'{k} {v}' for k, v in self.courses.items())


class Student(SchoolMember):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.courses = {}

    def attendCourse(self, signature, year):
        self.courses[signature] = {'grade': [], 'year': year}

    def addGrade(self, signature, *args):
        if signature in self.courses:
            self.courses[signature]['grade'].extend(x for x in args)

    def getCourses(self):
        return "\n".join(f'{k} {v}' for k, v in self.courses.items())

    def getAvgGrade(self, signature):
        return sum(self.courses[signature]['grade']) / len(self.courses[signature]['grade'])

