# data-project
Data Engineering Project for The Information Lab
Data source: [FreeToGame.com](https://www.freetogame.com/api-doc)

## About Me & Why I'm Applying

Hello! I'm Ayumi. Growing up with an older brother who would let me watch him play games, I developed a lifelong love for games and the thought process that goes into developing one. I am applying to The Information Lab because I found the Data Engineering Gradutate scheme to be exactly what I'm looking for. I am deeply fascinated by the intersection of technical engineering and business impact. My time as a java peer tutor during my studies at university showed me that I enjoyed the intersection of the puzzle solving aspect of untanging a coding problem and the rewarding feeling of helping someone else understand it, which naturally sparked my interest in client facing consultancy where technical solutions must be clearly translated into business value. I like that The Information Lab's 29 month scheme is rotational so that I can experience a range of different business environments and challenges. I believe my technical foundation and passion for problem solving make me a great fit for this Data Engineering role.

## What Does This Project Do? 
I've always had a keen interest in games and so I decided to use an API that holds data of several games of different generes. I made a simple project that pulls the information from the API of games that meet the criteria of the select statements.

This project pulls the data held in the FreeToGame API and saves a copy of the data to a json file in this repository (raw_games.json). This allows another section of code to transform aqnd stores this as rows and columns in a SQLite database table (games.db). The code then queries this database (query_games.py) with SQL staements and retuns applicable data as a terminal displayed report.

## Project Structure

data-project/
│
├── extract.py          # Step 1: Fetches API data & saves raw JSON in new file raw_games.json
├── raw_games.json      # Raw data snapshot
├── load_data.py        # Step 2: Creates SQLite database and loads/transforms data
├── games.db            # Local SQLite database file
├── query_games.py      # Step 3: Runs analytical queries & prints reports
└── README.md           # Project documentation

## AI Usage

I used the assistance of AI to help me write the code for getting the data from the API, saving the data to a file and running queries on it. I also used AI to help me understand what each line of code was doing, for which I then wrote my own comments for to show my understanding of the code being executed. I also used AI to help me write part of this readme file so that others tryiing to access my project have all the required materials and understand what each file's purpose is. Where I could I used my own knowledge and where I struggled I asked AI to find me resources that I could use to help with my understanding of the project and code (included websites like w3schools, stack overflow and youtube tutorials)

## Getting Started & Prerequisites
You only need Python 3 installed on your machine. The pipeline uses built-in Python libraries (requests, json, sqlite3), meaning no heavy external dependencies or complex database servers are required.

1. Clone the Repository
    git clone [https://github.com/yumit3ch/data-project.git](https://github.com/yumit3ch/data-project.git)
    cd data-project
2. Run the Pipeline
Execute the scripts in order:
    Step 1: Extract the raw data from the API
            python3 extract.py
            (Creates raw_games.json)
    Step 2: Load and transform the data into SQLite
        python3 load_data.py
        (Creates games.db with a structured schema including thumbnails and metadata)
    Step 3: Run analytical reports
        python3 query_games.py
        (Generates a breakdown of the database metrics)

## Future Improvements

Because this is one of my first data engineering and API coding projects, I kept the scope focused on building a solid, working pipeline from scratch. However there are a few features and improvements I would implement in the future:

1. Interactive Visual Interface: At the moment the reports print out as text in the terminal. As an improvement I would build a simple user facing web app or dashboard so users can view the game data visually with images and clean UI layouts

2. Custom Search Filtering: Instead of just hardcoded SQL queries, I want to build an interactive filtering system where the user can choose their own search criteria, such as picking a specific release year (e.g., games from 2018), platform or genre on the fly

3. Automatic API Updates: Implement a task scheduler so the extraction script automatically checks the API for fresh game data on a regular schedule without manual intervention

4. Data Quality Checks: Add automated checks to catch missing values, malformed data or unexpected changes in the API layout before it gets saved into the database as in the event of a missing or incorrect data type in the data, this can prevent the code from running correctly and may break the system