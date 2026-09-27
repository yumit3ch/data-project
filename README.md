# data-project
Data Engineering Project for The Information Lab
Data source: FreeToGame.com

## What Does This Project Do? 
I've always had a keen interest in games and so I decided to use an API that holds data of several games of different generes. I made a simple project that pulls the information from the API of games that meet the criteria of the select statements.

This project pulls the data held in the FreeToGame API and saves a copy of the data to a json file in this repository (raw_games.json). This allows another section of code to transform aqnd stores this as rows and columns in a SQLite database table (games.db). The code then queries this database (query_games.py) with SQL staements and retuns applicable data as a terminal displayed report.

## 📁 Project Structure

```text
data-project/
│
├── extract.py          # Step 1: Fetches API data & saves raw JSON in new file raw_games.json
├── raw_games.json      # Raw data snapshot
├── load_data.py        # Step 2: Creates SQLite database and loads/transforms data
├── games.db            # Local SQLite database file
├── query_games.py      # Step 3: Runs analytical queries & prints reports
└── README.md           # Project documentation
```

## AI Usage

I used the assistance of AI to help me write the code for getting the data from the API, saving the data to a file and running queries on it. I also used AI to help me understand what each line of code was doing, for which I then wrote my own comments for to show my understanding of the code being executed. I also used AI to help me write part of this readme file so that others tryiing to access my project have all the required materials and understand what each file's purpose is. Where I could I used my own knowledge and where I struggled I asked AI to find me resources that I could use to help with my understanding of the project and code (included websites like w3schools, stack overflow and youtube tutorials)

## Getting Started & Prerequisites
You only need Python 3 installed on your machine. The pipeline uses built-in Python libraries (requests, json, sqlite3), meaning no heavy external dependencies or complex database servers are required.

1. Clone the Repository
    git clone [https://github.com/your-username/data-project.git](https://github.com/your-username/data-project.git)
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