import sqlite3

#code to run sql queries on games.db and prints results in terminal

conn = sqlite3.connect('games.db') #connect to db
cursor = conn.cursor()
 
listNum = 1

print("--- GAME DATABASE REPORT --- \n")

print("1. Total Games per Platform:") #query: find how many games per platfrom (pc, browser and both) order from most to least
cursor.execute('''
    SELECT platform, COUNT(*) as total 
    FROM games
    GROUP BY platform 
    ORDER BY total DESC;
''')
platforms = cursor.fetchall()
for plat, count in platforms:
    print(f"   - {plat}: {count} games")

print("\n" + "-"*30 + "\n") #formatting vosual break

print("2. Random Shooter Games:") #query: find 5 random shooter games
cursor.execute('''
    SELECT title, publisher, release_date 
    FROM games 
    WHERE genre = 'Shooter' 
    ORDER BY RANDOM() 
    LIMIT 5;
''')
shooters = cursor.fetchall()
for title, publisher, date in shooters:
    print(f"   - {title} (Pub: {publisher}, Released: {date})")

print("\n" + "-"*30 + "\n")

print("3. Recently released games:") #query: top 5 most recently released games
cursor.execute('''
    SELECT title, release_date, publisher, genre
    FROM games
    ORDER BY release_date DESC
    LIMIT 5;
''')
recent = cursor.fetchall()
for title, date, publisher, genre in recent:
    print(f"   - {title} (Released: {date}, Pub: {publisher}, Genre: {genre})")
    
print("\n" + "-"*30 + "\n")

print("4. Recently released Sandbox Games:") #query: top 5 most recently released sandbox games found by searching for "sandbox" in the short_description fieldu
cursor.execute('''
    SELECT title, publisher, release_date
    FROM games 
    WHERE short_description LIKE '%sandbox%' 
    ORDER BY release_date DESC
    LIMIT 5;
''')
recentSandbox = cursor.fetchall()
for title, publisher, date in recentSandbox:
    print(f"   - {title} (Pub: {publisher}, Released: {date})")

print("\n" + "-"*30 + "\n")

print("5. Random Game Recommendations:")  #query: 10 random games to recommend to the user
cursor.execute('''
    SELECT title, genre, platform 
    FROM games 
    ORDER BY RANDOM() 
    LIMIT 10;
''')
random_games = cursor.fetchall()
for title, genre, platform in random_games:
    print(f"   {listNum}: {title} ({genre} - {platform})")
    listNum += 1
    
print("\n" + "-"*30 + "\n")

# 4. Close connection
conn.close()