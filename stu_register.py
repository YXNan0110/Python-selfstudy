# 学生学籍注册程序

file = "Student Data.db"

def register_api():

    student_data = {}

    print("Welcome to our registration system".center(60, "-"))
    name = input("Name:").strip()
    age = input("Age:").strip()
    tel = input("Tel:").strip()
    id_card = input("ID card:").strip()

    course_list = ["English", "Math", "Computer", "Science"]
    for index, course in enumerate(course_list):
        index = int(index)
        index += 1
        print(f"{index}. {course}")

    subj = input("Subject:")
    if subj.isdigit():
        subj = int(subj)-1
        for index, course in enumerate(course_list):
            if subj == int(index):
                subj_select = course

    student_data["Name"] = name
    student_data["Age"] = age
    student_data["Tel"] = tel
    student_data["ID card"] = id_card
    student_data["Subject"] = subj_select

    return student_data

def document(filename, data):
    f = open(filename, 'a')
    info = f"{data['Name']}, {data['Age']}, {data['Tel']}, {data['ID card']}, {data['Subject']}\n"
    f.write(info)
    f.close()

stu_data = register_api()

document(file, stu_data)













