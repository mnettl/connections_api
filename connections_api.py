from flask import Flask, request
from flask_restful import Resource, Api
import json
from sql_connection import SQL_Connection

app = Flask(__name__)
api = Api(app)


answers = {
    "YELLOW": {"category_name": "category_name",
              "category_words" : "category_words"},
    "BLUE" : {"category_name" : "category_name2",
              "category_words" : "category_words2"},
    "PURPLE" : {"category_name" : "category_name2",
               "category_words" : "category_words2"},
    "GREEN" : {"category_name" : "category_name2",
              "category_words" : "category_words2"},
}

words = {"puzzle_no": "puzzle_no","words": "BLAH, BLAH, BLAH, BLAH"}

puzzle = {
     "words" : "BLAH, BLAH, BLAH, BLAH",
     "answers" : {
     "YELLOW": {"category_name": "category_name",
              "category_words" : "category_words"},
     "BLUE" : {"category_name" : "category_name2",
              "category_words" : "category_words2"},
     "PURPLE" : {"category_name" : "category_name2",
               "category_words" : "category_words2"},
     "GREEN" : {"category_name" : "category_name2",
              "category_words" : "category_words2"},
     }
}
def get_puzzle (puzzle_no):
     sqlc_ = SQL_Connection()

     puzzle['words'] = sqlc_.get_words(puzzle_no)
     # puzzle['answers'] = sqlc_.get_answers
     for x in range (0, 4):
          color = sqlc_.get_answers(puzzle_no)[x][1]
          puzzle['answers'][color]['category_name'] = sqlc_.get_answers(puzzle_no)[x][2]
          puzzle['answers'][color]['category_words'] = sqlc_.get_answers(puzzle_no)[x][3]
     puzzle['puzzle_no'] = puzzle_no
     return puzzle    


# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"

class Puzzle (Resource):
    @app.get ('/puzzles/<puzzle_no>/answers')
    def get_answers (puzzle_no):
          sqlc = SQL_Connection()
          answers['puzzle_no'] = puzzle_no
          for x in range (0, 4):
               color = sqlc.get_answers(puzzle_no)[x][1]
               answers[color]['category_name'] = sqlc.get_answers(puzzle_no)[x][2]
               answers[color]['category_words'] = sqlc.get_answers(puzzle_no)[x][3]
          return answers


    @app.get ('/puzzles/<puzzle_no>/words')
    def get_words (puzzle_no):
         sqlc = SQL_Connection()
         words['words'] = sqlc.get_words(puzzle_no)
         words['puzzle_no'] = puzzle_no
         return words
    
    @app.get ('/puzzles/<puzzle_no>')
    def gp (puzzle_no):
          puzzleo = get_puzzle(puzzle_no)
          return puzzleo
#     def get_puzzle (puzzle_no):
#           sqlc_ = SQL_Connection()

#           puzzle['words'] = sqlc_.get_words(puzzle_no)
#           # puzzle['answers'] = sqlc_.get_answers
#           for x in range (0, 4):
#                color = sqlc_.get_answers(puzzle_no)[x][1]
#                puzzle['answers'][color]['category_name'] = sqlc_.get_answers(puzzle_no)[x][2]
#                puzzle['answers'][color]['category_words'] = sqlc_.get_answers(puzzle_no)[x][3]
#           puzzle['puzzle_no'] = puzzle_no
#           return puzzle

    @app.route('/puzzles/')
    def get_date ():
          date = request.args.get('date')
          sqlc_ = SQL_Connection()
          p_ = str(sqlc_.get_puzzle_by_date(date))
          puzzle_ = get_puzzle (p_)
          return puzzle_




if __name__ == '__main__':
	app.run()