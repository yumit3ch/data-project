import sqlite3
import json

#if any issues with table, delete db file and rerun this file with corrected code

conn = sqlite3.connect('games.db') #open (or create) sqlite db file
cursor = conn.cursor() #create a cursor object to execute SQL commands

#table to hold games data
cursor.execute('''
    CREATE TABLE IF NOT EXISTS games (
        id INTEGER PRIMARY KEY,
        title TEXT,
        genre TEXT,
        platform TEXT,
        publisher TEXT,
        developer TEXT,
        release_date TEXT,
        thumbnail TEXT,
        short_description TEXT,
        game_url TEXT
    )
''')

with open('raw_games.json', 'r') as file: #open the raw json file in read mode
    games_data = json.load(file) #load data into python object

# loop through each game and insert it into table
for game in games_data:
    cursor.execute('''
    INSERT OR REPLACE INTO games (id, title, genre, platform, publisher, developer, release_date, thumbnail, short_description, game_url)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        game.get('id'),
        game.get('title'),
        game.get('genre'),
        game.get('platform'),
        game.get('publisher'),
        game.get('developer'),
        game.get('release_date'),
        game.get('thumbnail'),
        game.get('short_description'),
        game.get('game_url')
    ))

conn.commit() #commit changes to db
conn.close() #close the connection db

print("Data successfully loaded and transformed into SQLite database ('games.db')!") #confirmation message