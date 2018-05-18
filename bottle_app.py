from bottle import run, route, template, request, static_file, post, redirect
import quiz

"""Returns main-page and fact- pages"""

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

"""Returns quiz- pages"""

@route('/north_quiz')
def get_north_quiz():
    north=quiz.get_quiz_north()
    return template('north_quiz',questions=north)




@route('/count_result', method="POST")
def count_result():
    for questionid in request.forms:
        answer = request.forms[questionid]
        real_question_id = questionid[1:] # Hämtar det riktigt id:t (t.ex. q2 blir 2, q15 blir 15, etc.)
        return answer
        return questionid
        
        
    
    
       
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


"""Returns contact- page"""

@route('/contact')
def contact():
    return template('contact')

'''Handles the routes to our static files. Returns: file : the static file requested by URL'''

@route("/static/<filename:path>")
def server_static(filename):
    return static_file(filename, root="static")

run(host='localhost', port=8050, debug=True, reloader=True)
