import pymysql


def connectDB():
    # Ansluter till vår databas
    db = pymysql.connect(host="localhost",
                         user="root",
                         passwd="",
                         db="yourgeo",
                         cursorclass=pymysql.cursors.DictCursor)
    
    # Skapar en pekare mot databasen
    cursor = db.cursor()
    return db, cursor
                      

def get_quiz_north():
    db, cursor = connectDB()
    # Skickar iväg en fråga för att hämta alla frågor från tabellen "questions"
    sql = "SELECT * FROM questions where Area = '{}'".format("Norra Europa")
    cursor.execute(sql)
    # Tar emot svaret, sparar det i variabeln "north"
    north = cursor.fetchall()
    return north

def get_answers_north():
    db, cursor = connectDB()
    # Skickar iväg en fråga för att hämta alla svar från tabellen "answers"
    sql = "SELECT right_answer, wrong_answer_1, wrong_answer_2 from answers join questions on answers.answersID=questions.questionID"
    cursor.execute(sql)
    # Tar emot svaret, sparar det i variabeln "north"
    north_answers = cursor.fetchall()
    return north_answers
