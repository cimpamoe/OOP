class Registration:
    def __init__(self, name, reg_no, course, year, department):
        self.name = name
        self.reg_no = reg_no
        self.course = course
        self.year = year
        self.department = department
        
    def __str__(self):
        return (f"NAME: {self.name}\n"
                f"REG_NO: {self.reg_no}\n"
                f"COURSE: {self.course}\n"
                f"YEAR: {self.year}\n"
                f"DEPARTMENT: {self.department}")

student1 = Registration("Nantongo Nessa", "S23B13/087", "Information Technology", "2023", "Engineering")

student2 = Registration("Sentamu Fredrick", "M23B13/007", "Social Sciences", "2023", "Business")

student3 = Registration("Mandisa Mary", "S20D13/011", "Information Technology", "2020", "Engineering")

student4 = Registration("Arikod James", "S23C13/087", "Computer Science", "2023", "Engineering")

student5 = Registration("Tiayi Patricia", "S23B13/088", "Information Technology", "2023", "Engineering")

student6 = Registration("Mungufeni Gerald", "S23B13/080", "Information Technology", "2023", "Engineering")

student7 = Registration("Ekaba Brian", "S18B13/009", "Information Technology", "2018", "Engineering")

student8 = Registration("Nicole Johnson", "S22B13/081", "Information Technology", "2022", "Engineering")

student9 = Registration("Kayesu Joy", "S20B13/089", "Information Technology", "2020", "Engineering")

student10 = Registration("Senteza Henry", "S19B13/099", "Information Technology", "2019", "Engineering")

print(student1)
print(student2)
print(student3)
print(student4)
print(student5)
print(student6)
print(student7)
print(student8)
print(student9)
print(student10)

    
    