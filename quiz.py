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
    sql = "SELECT * from answers join questions on questions.questionID=answers.answersID WHERE Area='{}'".format("Norra Europa")
    
    cursor.execute(sql)
    # Tar emot svaret, sparar det i variabeln "north"
    north = cursor.fetchall()
    return north

'''def get_answers_north():
    db, cursor = connectDB()
    # Skickar iväg en fråga för att hämta alla svar från tabellen "answers"
    sql = "SELECT * from answers join questions on questions.questionID=answers.answersID WHERE Area='{}'".format("Norra Europa")
    cursor.execute(sql)
    # Tar emot svaret, sparar det i variabeln "north"
    north_answers = cursor.fetchall()
    print(north_answers)
    return north_answers'''




