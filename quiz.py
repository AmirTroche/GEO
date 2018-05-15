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
                      
#North
def get_quiz_north():
    db, cursor = connectDB()
    # Skickar iväg en fråga för att hämta alla frågor från tabellen "questions"
    sql = "SELECT * from answers join questions on questions.questionID=answers.answersID WHERE Area='{}'".format("Norra Europa")
    
    cursor.execute(sql)
    # Tar emot svaret, sparar det i variabeln "north"
    north = cursor.fetchall()
    return north

#East
def get_quiz_east():
    db, cursor = connectDB()
    # Skickar iväg en fråga för att hämta alla frågor från tabellen "questions"
    sql = "SELECT * from answers join questions on questions.questionID=answers.answersID WHERE Area='{}'".format("Östra Europa")
    
    cursor.execute(sql)
    # Tar emot svaret, sparar det i variabeln "east"
    east = cursor.fetchall()
    return east

#West
def get_quiz_west():
    db, cursor = connectDB()
    # Skickar iväg en fråga för att hämta alla frågor från tabellen "questions"
    sql = "SELECT * from answers join questions on questions.questionID=answers.answersID WHERE Area='{}'".format("Västra Europa")
    
    cursor.execute(sql)
    # Tar emot svaret, sparar det i variabeln "west"
    west = cursor.fetchall()
    return west

#South
def get_quiz_south():
    db, cursor = connectDB()
    # Skickar iväg en fråga för att hämta alla frågor från tabellen "questions"
    sql = "SELECT * from answers join questions on questions.questionID=answers.answersID WHERE Area='{}'".format("South Europa")
    
    cursor.execute(sql)
    # Tar emot svaret, sparar det i variabeln "south"
    south = cursor.fetchall()
    return south

'''def get_answers_north():
    db, cursor = connectDB()
    # Skickar iväg en fråga för att hämta alla svar från tabellen "answers"
    sql = "SELECT * from answers join questions on questions.questionID=answers.answersID WHERE Area='{}'".format("Norra Europa")
    cursor.execute(sql)
    # Tar emot svaret, sparar det i variabeln "north"
    north_answers = cursor.fetchall()
    print(north_answers)
    return north_answers'''




