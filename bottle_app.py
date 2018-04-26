from bottle import run, route, template, request, static_file
import quiz

""" Hamtar Main & Fakta sidorna"""

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

""" Hamtar Quiz"""

@route('/north_quiz')
def get_north_quiz():
    questions = quiz.get_quiz()
    return template('quiz_north', questions = questions)

@route('/east_quiz')
def get_east_quiz():
    return template('quiz_east')

@route('/west_quiz')
def get_west_quiz():
    return template('quiz_west')

@route('/south_quiz')
def get_south_quiz():
    return template('quiz_south')

""" Hamtar kontaktsidan"""

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
