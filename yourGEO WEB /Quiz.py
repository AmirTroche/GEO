import pymysql


def get_quiz_north():
    # Ansluter till vår databas
    db = pymysql.connect("localhost", "root", "", "quiz", cursorclass=pymysql.cursors.DictCursor)
    # Skapar en pekare mot databasen
    cursor = db.cursor()
    # Skickar iväg en frågor för att hämta alla filmer från tabellen "movies"
    cursor.execute("SELECT * FROM questions where Area = Norra Europa ")
    # Tar emot svaret, sparar det i variabeln "movies
    questions_north = cursor.fetchall()
    # Stänger databasanslutningen
    db.close()
    # Skickar tillbaka filmerna
    return questions_north

