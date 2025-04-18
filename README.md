# Pokemon Database

**Authors**: Sophie Meronek 
**Date**: 4/17/25

## Introduction

This repository contains the code and data required for my project that involves creating a flask app to look at pokemon statistics and to run queries on the data.  It also allows for the user to access different databases.

The goal of this project is to create an application that allows for people to create Pokemon teams and to look at different statistics based on the queries they run.  

The project is still a work in progress and has multiple areas that it can be improved.

## Data Source and Preparation

For this project, I used a data set from Kaggle and turned it into two different SQL databases utilizing Python code that was created utilizing CHATGPT.

### Pokemon

The **Pokemon Data** is the first half of the data I found on Kaggle.  It will hold all different statisitics for each pokemon.

The Pokemon data is made up of pokedex_number, name, type1, type2, hp, attack, defense, special attack, and special defense.

Thus, Pokemon data will be used to hold all the info pertaining to one pokemon. 

### Pokemon Damage

The **Pokemon Damage Data** is the second half of the data I found on Kaggle.  It looks at how different types do against Pokemon.

It has a column for each Pokemon types and will help one of 3 values: Weak, Standard, and Strong

### Data Preparation

For data preparation, I worked with CHATGPT to create code that will take CSV data and make it into SQL quereis to enter the data.  We created two different data sets.  One being the Pokemon Data and the other was the Pokemon Damage.

## Repository Structure

The repository contains the following key sections:

- **scr**: Scripts creating SQL queries and for turning data into SQL queries.
- **data**: The datasets.
- **templates**: The different HTML templates that are utilized to show the different queries and pages.  Utilized CHATGPT to create the templates.
- **static\imgs**: This will be used to hold any images I will use so I can insert them later.

## Requirements

To run the code in this repository, you will need the following installed:

- Python
- Flask and other files
- boto3
- pymysql
- Credentials that I have

In addition, I utilized VS CODE, AWS, and GITHUB to create the code.

## Code Execution

To run the application:

1. Download the pokemon.csv and pokemon_weakness.csv files.
2. Download the files all the files in the directory.
3. Install the required packages.
4. Run the scripts create_pokemon_damage.py and create_pokemon_database.py to create the SQL data
5. Either upload the data or reach out for access to my SQL databases
6. Run the Flask apps

## Disclaimer

This project was completed for CS 178: Cloud and Database Management at Drake University. Throughout the project, I relied on CHATGPT to help create templates and to check why I would get error in my code.  I have done a previous project similar to this in CS 188.

# Project #1 Rubric (100 Points Total)

## Part 1: Core Functionality (65 points)

| Criteria                                                                 | Points | Proposed Score |
|--------------------------------------------------------------------------|--------|----------------|
| Website uses Flask and runs independently from VS Code (not relying on terminal interaction) | 10     |    10            |
| Relational database (MySQL/RDS) is correctly used in the project        | 15     |               15 |
| Non-relational database (DynamoDB) is correctly used (e.g., user info stored/retrieved) | 10     |    8 (I have this working on my local machine, but it is being difficult on AWS)        |
| Implements full CRUD operations (Create, Read, Update, Delete)          | 10     |          8 (I have this fully implemented, but it is not working due to credentials in AWS.  See Blackboard for evidence.)      |
| Incorporates at least one SQL JOIN query                                | 5      |          5      |
| Uses own RDS instance inside student’s VPC                              | 5      |       5         |
| Uses own IAM account (e.g., ProjectOneUser)                             | 5      |       5    (I created a while new root account with a new IAM user for my EC2 Instance and Dynamo DB.  See Blackboard for Proof)     |
| Application avoids storing credentials in public GitHub (e.g., creds.py is excluded via .gitignore) | 5      |     5           |

## Part 2: Code Quality and GitHub Submission (25 points)

| Criteria                                                                 | Points | Proposed Score |
|--------------------------------------------------------------------------|--------|----------------|
| Code is organized across multiple files (e.g., flaskapp.py, dbCode.py)  | 10     |            10    |
| Good software practices (clear naming, comments, error handling with try/except, modular functions) | 10     |    10            |
| GitHub repository is submitted with a clear commit history and a README file | 5   |        5        |

## Part 3: Checkpoint Completion (10 points)

| Criteria                                                                 | Points | Proposed Score |
|--------------------------------------------------------------------------|--------|----------------|
| Checkpoint submitted on time with a working Flask app that connects to RDS and renders dynamic data | 10     |    10            |
