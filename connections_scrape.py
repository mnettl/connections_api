from bs4 import BeautifulSoup
import requests
import json
import sqlite3
import sys

def get_html (puzzle_no):
    address = str("https://connections.swellgarfo.com/nyt/" + puzzle_no)
    # html_doc = requests.get('https://connections.swellgarfo.com/nyt/89', headers={'User-Agent': 'Custom user agent'})
    html_doc = requests.get(address, headers={'User-Agent': 'Custom user agent'})
    html_source = html_doc.text

    with open ('html_doc_' + puzzle_no + '.html', "w", encoding='utf-8') as html_doc_:
        html_doc_.write (html_source)

# ===
# Get everything in the script tag - script id="__NEXT_DATA__"

def get_answers (puzzle_no)->list:
    docname = 'html_doc_' + puzzle_no + '.html'
    with open (docname, 'r') as htmldoc:
        soup = BeautifulSoup (htmldoc,'html.parser')
        answers_script = soup.find(attrs={"id" : "__NEXT_DATA__"}).contents[0]

    answers_script_json = json.loads(answers_script)
    answers = answers_script_json['props']['pageProps']['answers']
    return answers


def get_words (puzzle_no)->list:
    words_ = []
    words_list = []
    for y in range (0,4):
        words_.append(get_answers(puzzle_no)[y]['words'])

    for x in range (0, 4):
        for y in range (0,4):
            words_list.append(words_[x][y])
    words = ", ".join(words_list)
    return words

def get_colors (puzzle_no)->list:
    colors = []
    scraped_colors = []

    for y in range (0, 4):
        scraped_colors.append(get_answers(puzzle_no)[y]['color'])

    for x in range (0, 4):
        if scraped_colors[x] == "#fbd400":
            colors.append("YELLOW")
        elif scraped_colors[x] == "#5492ff":
            colors.append("BLUE")
        elif scraped_colors[x] == "#69e352":
            colors.append("GREEN") 
        elif scraped_colors[x] == "#df7bea":
            colors.append("PURPLE")  

    return colors



# ==== SQL Update Functions

def get_date (puzzle_no)->str:
    with open ('connections_puzzle_nos.json','r') as jsonfile:
        json_data = json.load(jsonfile)
        date = json_data[puzzle_no]['Date']
        return date

def add_puzzle (puzzle_no):
    date = get_date (puzzle_no)
    connection_ = sqlite3.connect("connections_db.db")
    cursor = connection_.cursor()
    sql_statement = "INSERT INTO Puzzles (puzzle_no, date) VALUES (?, ?);"
    cursor.execute(sql_statement, (puzzle_no, date,))
    connection_.commit()
    cursor.close()
    connection_.close()

def add_words (puzzle_no):
    words = get_words (puzzle_no)
    connection_ = sqlite3.connect("connections_db.db")
    cursor = connection_.cursor()
    sql_statement = "INSERT INTO Words (puzzle_no, words) VALUES (?, ?);"
    cursor.execute(sql_statement, (puzzle_no, words,))
    connection_.commit()
    cursor.close()
    connection_.close()

def add_answers (puzzle_no):
    connection_ = sqlite3.connect("connections_db.db")
    cursor = connection_.cursor()
    sql_statement = "INSERT INTO Answers (puzzle_no, color, category, words_in_category) VALUES (?, ?, ?, ?);"
    
    # colors = ["BLUE","GREEN","YELLOW","PURPLE"]
    colors = get_colors(puzzle_no)
    
    for x in range (0, 4):
        words = ", ".join(get_answers(puzzle_no)[x]['words'])
        cursor.execute (sql_statement, (puzzle_no, colors[x], get_answers(puzzle_no)[x]['description'], words,))
        
    connection_.commit()
    cursor.close()
    connection_.close()

# ======

puzzle_no = sys.argv[1]

get_html (puzzle_no)
add_puzzle (puzzle_no)
add_words (puzzle_no)
add_answers (puzzle_no)