import pymysql

def connectDB():
    """Ansluter till databas"""
    db = pymysql.connect(host="localhost",
                         user="root",
                         passwd="",
                         db="yourgeo",
                         cursorclass=pymysql.cursors.DictCursor)

    """Skapar en cursor för databasen"""
    cursor = db.cursor()
    return db, cursor


    
def grade_question(answer, real_question_id):

    """Funktion som räknar antal rätt i quiz"""
    db, cursor = connectDB()
    """skickar en fråga för att hämta fråga och svar som hör ihop och det rätta svaret från tabellen "right_answer"""
    sql2 = "SELECT right_answer from answers join questions on questions.questionID=answers.answersID WHERE QuestionID = '{}' and right_answer = '{}'".format(real_question_id, answer)
    """Kör select satsen"""
    cursor.execute(sql2)
    """Hämtar all data och sparar det i variabeln "resultat"""
    result = cursor.fetchall()
    
    show_result=len(result)
    return show_result
    

def get_quiz_north():
    db, cursor = connectDB()
    """skickar en fråga för att hämta alla frågor från tabellen "questions"""
    sql = "SELECT * from answers join questions on questions.questionID=answers.answersID WHERE Area='{}'".format("Norra Europa")

    cursor.execute(sql)
     #Får svar och sparar den i variablen "north"
    north = cursor.fetchall()
    return north


def get_quiz_east():
    db, cursor = connectDB()
    """skickar en fråga för att hämta alla frågor från tabellen "questions"""
    sql = "SELECT * from answers join questions on questions.questionID=answers.answersID WHERE Area='{}'".format("Östra Europa")

    cursor.execute(sql)
    """Får svar och sparar den i variablen "East"""
    east = cursor.fetchall()
    return east


def get_quiz_west():
    db, cursor = connectDB()
    """skickar en fråga för att hämta alla frågor från tabellen "questions"""
    sql = "SELECT * from answers join questions on questions.questionID=answers.answersID WHERE Area='{}'".format("Västra Europa")

    cursor.execute(sql)
    """Får svar och sparar den i variablen "West"""
    west = cursor.fetchall()
    return west


def get_quiz_south():
    db, cursor = connectDB()
    """skickar en fråga för att hämta alla frågor från tabellen "questions"""
    sql = "SELECT * from answers join questions on questions.questionID=answers.answersID WHERE Area='{}'".format("Södra Europa")

    cursor.execute(sql)
     #Får svar och sparar den i variablen "South"
    south = cursor.fetchall()
    return south
