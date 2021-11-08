import sqlite3


def writeDatabase(name,lastName,num,department):
    student=[]
    student.append(name)
    student.append(lastName)
    student.append(num)
    student.append(department)
    connectDb=sqlite3.connect("students.db")
    query = "insert into students (Name,LastName,StudentNo,DepartmentName) values(?,?,?,?);"
    connectDb.execute(query,student)
    connectDb.commit()
    connectDb.close()
    return True

def getStudent(studentNo):
    student=[]
    res=[]
    student.append(studentNo)
    connectDb=sqlite3.connect("students.db")
    query="select * from students where StudentNo=?;"
    info=connectDb.execute(query,student)
    res=info.fetchone()
    connectDb.close()
    return res

def updateStudent(name,lastName,num,department):
    student=[]
    student.append(name)
    student.append(lastName)
    student.append(num)
    student.append(department)
    student.append(name)
    student.append(num)
    connectDb=sqlite3.connect("students.db")
    query="update students set Name=?,LastName=?,StudentNo=?,DepartmentName=? where Name=? or StudentNo=?;"
    connectDb.execute(query,student)
    connectDb.commit()
    connectDb.close()
    return True

def deleteStudent(studentIntNo):
    connectDb=sqlite3.connect("students.db")
    query="delete from students where StudentNo=?;"
    connectDb.execute(query,(studentIntNo,))
    connectDb.commit()
    connectDb.close()
    return True