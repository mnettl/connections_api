import sqlite3
from contextlib import closing

class SQL_Connection:
    def get_words (self, puzzle_no) -> list:
        self.puzzle_no = puzzle_no
        connection_ = sqlite3.connect("connections_db.db")
        cursor = connection_.cursor()
        sql_statement = "SELECT words FROM Words WHERE puzzle_no = ?;"
        rows_ = cursor.execute(sql_statement, (puzzle_no,))
        rows = rows_.fetchall()
        cursor.close()
        connection_.close()
        word_list_data = str(rows[0][0]).split(', ')
        word_list = []

        for word in word_list_data:
            word_list.append(word)

        return word_list

    def get_answers_for_color (puzzle_no, color) -> list:
        connection_ = sqlite3.connect("connections_db.db")
        cursor = connection_.cursor()
        sql_statement = "SELECT * FROM Answers WHERE puzzle_no = ? and color = ?;"
        rows_ = cursor.execute(sql_statement, (puzzle_no, color,))
        rows = rows_.fetchall()[0]
        cursor.close()
        connection_.close()

        return rows

    def get_answers (self, puzzle_no) -> list:
        self.puzzle_no = puzzle_no
        connection_ = sqlite3.connect("connections_db.db")
        cursor = connection_.cursor()
        sql_statement = "SELECT * FROM Answers WHERE puzzle_no = ?;"
        rows_ = cursor.execute(sql_statement, (puzzle_no,))
        rows = rows_.fetchall()
        cursor.close()
        connection_.close()

        return rows

    def get_puzzle (puzzle_no) -> list:
        connection_ = sqlite3.connect("connections_db.db")
        cursor = connection_.cursor()
        sql_statement = "SELECT * FROM Puzzles WHERE puzzle_no = ?;"
        rows_ = cursor.execute(sql_statement, (puzzle_no,))
        rows = rows_.fetchall()
        cursor.close()
        connection_.close()


        return rows
    
    def get_puzzle_by_date (self, date) -> list:
        self.date = date
        connection_ = sqlite3.connect("connections_db.db")
        cursor = connection_.cursor()
        sql_statement = "SELECT * FROM Puzzles WHERE date = ?;"
        rows_ = cursor.execute(sql_statement, (date,))
        rows = rows_.fetchall()
        cursor.close()
        connection_.close()


        return rows[0][0]
    

# print (get_words('95')[15])

# print (get_answers ('95','YELLOW'))
# print (get_answers ('95','GREEN'))
# print (get_answers ('95','BLUE'))
# print (get_answers ('95','PURPLE'))
# print (get_puzzle ('94'))
# print (get_answers('95')[2][2])

# ===
# answers = {"00": {
#     "YELLOW": {"category_name": "category_name",
#               "category_words" : "category_words"},
#     "BLUE" : {"category_name" : "category_name2",
#               "category_words" : "category_words2"},
#     "PURPLE" : {"category_name" : "category_name2",
#                "category_words" : "category_words2"},
#     "GREEN" : {"category_name" : "category_name2",
#               "category_words" : "category_words2"},
# }
# }

# words = {"00": "BLAH, BLAH, BLAH, BLAH"}

# x = 0
# for x in range (0, 4):
#     color = get_answers('95')[x][1]
#     answers['00'][color]['category_name'] = get_answers('95')[x][2]
#     answers['00'][color]['category_words'] = get_answers('95')[x][3]

# print (answers)

# words['00'] = get_words('95')

# print (words)


