from sqlite3.dbapi2 import Error
import dbconnet as db

#this methods control some input variable and , connection database method.
def dataControl(name,lastName,studentIntNo,department):
    try:
        studentNo=int(studentIntNo)
        if(db.writeDatabase(name,lastName,studentNo,department)):
            return True
        else:
            return False
    except ValueError:
        return False
    except Error:
        return False
         
def searchRecordControl(searchValue):
    try:
        searchValInt=int(searchValue)
        res=db.getStudent(searchValInt)
            #control record is null
        if (type(res)==None):
            return False
        else:
            return res
    except ValueError:
        return False


def updateRecordControl(name,lastName,studentNo,department):
    try:
        studentIntNo=int(studentNo)
        if(db.updateStudent(name,lastName,studentIntNo,department)):
            return True
        else:
            return False
    except ValueError:
        return False

def deleteRecordControl(res):
    try:
        studentIntNo=int(res)
        if(db.deleteStudent(studentIntNo)):
            return True
        else:
            return False
    except ValueError:
        return False