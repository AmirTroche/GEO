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
    north=quiz.get_quiz_north()
    
    return template('north_quiz',questions=north)

    


@route('/east_quiz')
def get_east_quiz():
    east=quiz.get_quiz_north()
    
    return template('east_quiz', questions=east)

@route('/west_quiz')
def get_west_quiz():
    west=quiz.get_quiz_west()
    
    return template('west_quiz', questions=west)

@route('/south_quiz')
def get_south_quiz():
    south=quiz.get_quiz_south()
    
    return template('south_quiz', questions=south)


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

run(host='localhost', port=8050, debug=True, reloader=True)
