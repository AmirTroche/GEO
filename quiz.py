import pymysql


def connectDB():
    """Connects to database"""
    db = pymysql.connect(host="localhost",
                         user="root",
                         passwd="",
                         db="yourgeo",
                         cursorclass=pymysql.cursors.DictCursor)
    
    """Creates a cursor for the database"""
    cursor = db.cursor()
    return db, cursor
                      

def get_quiz_north():
    db, cursor = connectDB()
    """Sends a question to get all questions from the table "questions"""
    sql = "SELECT * from answers join questions on questions.questionID=answers.answersID WHERE Area='{}'".format("Norra Europa")
    
    cursor.execute(sql)
    """Recieves answer, saves it in the variable "north"""
    north = cursor.fetchall()
    return north


def get_quiz_east():
    db, cursor = connectDB()
    """Sends a question to get all questions from the table "questions"""
    sql = "SELECT * from answers join questions on questions.questionID=answers.answersID WHERE Area='{}'".format("Östra Europa")
    
    cursor.execute(sql)
    """Recieves answer, saves it in the variable "east"""
    east = cursor.fetchall()
    return east


def get_quiz_west():
    db, cursor = connectDB()
    """Sends a question to get all questions from the table "questions"""
    sql = "SELECT * from answers join questions on questions.questionID=answers.answersID WHERE Area='{}'".format("Västra Europa")
    
    cursor.execute(sql)
    """Recieves answer, saves it in the variable "west"""
    west = cursor.fetchall()
    return west


def get_quiz_south():
    db, cursor = connectDB()
    """Sends a question to get all questions from the table "questions"""
    sql = "SELECT * from answers join questions on questions.questionID=answers.answersID WHERE Area='{}'".format("South Europa")
    
    cursor.execute(sql)
    """Recieves answer, saves it in the variable "south"""
    south = cursor.fetchall()
    return south






