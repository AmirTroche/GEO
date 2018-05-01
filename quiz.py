import pymysql


def connectDB():
    # Ansluter till vår databas
    db = pymysql.connect(host="localhost",
                         user="root",
                         passwd="",
                         db="quiz",
                         cursorclass=pymysql.cursors.DictCursor)
    
    # Skapar en pekare mot databasen
    cursor = db.cursor()
    return db, cursor
                      

def get_quiz_north(db, cursor):
    # Skickar iväg en fråga för att hämta alla fakta från tabellen "north facts"
    sql = "SELECT * FROM questions where Area = Norra Europa"
    cursor.execute(sql)
    # Tar emot svaret, sparar det i variabeln "north"
    north = cursor.fetchall()
    return north
