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
- **templates**: The different HTML templates that are utilized to show the different queries and pages.
- **static\imgs**: This will be used to hold any images I will use so I can insert them later.

## Requirements

To run the code in this repository, you will need the following installed:

- Python
- Flask


## Variables

Below is a list of predictor (X) variables used to predict the outcome (Y) variables.

### Predictor Variables (X)
- **hhsize**: The number of people in a household.
- **female**: The number of females in a household.
- **hispanic**: The number of Hispanics in a household.
- **black**: The number of Black individuals in a household.
- **kids**: The number of children (under 18) in a household.
- **elderly**: The number of seniors (over 60) in a household.
- **education**: The number of people with a college degree in a household.
- **married**: The number of married individuals in a household.

### Outcome Variables (Y)
- **FSFOODS**: The household lacks enough food and/or variety.
- **FSSTATUS**: The household lacks food security.

## Methods

The analysis follows these steps:

1. **Data Cleaning and Preprocessing**: Preparing the data for analysis.
2. **Model Training**: Training a predictive model using the CPS data.
3. **Model Application**: Applying the model to ACS data to predict food insecurity in Iowa.
4. **Aggregation**: Aggregating household-level predictions to the PUMA level.

The model is trained using the CPS data and tested for accuracy. For each outcome variable (Y), two Bernoulli models are trained with a logit link function using Lasso (where unimportant variables have coefficients set to zero) and Ridge (where unimportant variables have coefficients close to zero). Since food insecurity is a binary outcome (insecurity exists or not), the logit link ensures the output remains between 0 and 1. The models are evaluated using testing data, and the one with the highest Area Under the Curve (AUC) on a ROC plot is selected as the best model. Finally, the best model is used to predict food insecurity in the ACS data, and weighted means are calculated for each PUMA to identify regions with the highest probabilities of food insecurity.

## Code Execution

To reproduce the results:

1. Download the CPS and ACS data from the provided links.
2. Download the files into the `src/` directory.
3. Install the required packages by running the setup script.
4. Run the scripts `src/FSFOODS.R` and `src/FSSTATUS_Analysis.R`.
5. All interpretations are commented within the code.
6. Compare the results with those in the `outputs/` directory to verify the accuracy of the predictions.

## References

1. U.S. Bureau of Labor Statistics, **Current Population Survey**: [https://www.bls.gov/cps/](https://www.bls.gov/cps/)
2. IPUMS, **Current Population Survey (CPS)**: [https://cps.ipums.org/cps/](https://cps.ipums.org/cps/)
3. U.S. Census Bureau, **American Community Survey (ACS)**: [https://www.census.gov/programs-surveys/acs/data.html](https://www.census.gov/programs-surveys/acs/data.html)

## Disclaimer

This project was completed for STAT 172: Data Mining and General Linear Model at Drake University. We partnered with WesleyLife for this project, and all recommendations were tailored to their plans and needs.
