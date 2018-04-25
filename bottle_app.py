from bottle import run, route, template, request, static_file
import quiz

""" Hämtar Main & Fakta sidorna"""

@route('/')
def main():
    return template('main')

@route('/north_facts')
def get_north_facts():
    return template('north_facts')

@route('/east_facts')
def get_east_facts():
    return template('east_facts')

@route('/west_facts')
def get_west_facts():
    return template('west_facts')

@route('/south_facts')
def get_south_facts():
    return template('south_facts')

""" Hämtar Quiz"""

@route('/quiz_north')
def get_quiz_north():
    questions = quiz.get_quiz()
    return template('quiz_north', questions = questions)

@route('/quiz_east')
def get_quiz_east():
    return template('quiz_east')

@route('/quiz_west')
def get_quiz_west():
    return template('quiz_west')

@route('/quiz_south')
def get_quiz_south():
    return template('quiz_south')

""" Hämtar kontaktsidan"""

@route('/contact')
def contact():
    return template('contact')


@route('/test')
def test():
    answer = request.query['answer']
    print(answer)

@route("/static/<filename:path>")
def server_static(filename):
    '''Handles the routes to our static files

    Returns:
            file : the static file requested by URL
    '''
    return static_file(filename, root="static")

run(host='localhost', port=8080)
