import pandas as pd
import numpy as np

def calculate_demographic_data(print_data=True):
    # Read data from file
    data = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = data.race.value_counts()

    # What is the average age of men?
    average_age_men = data[data['sex'] == 'Male']['age'].mean()

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = len(data[data.education == 'Bachelors'])*100/len(data)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`



    # percentage with salary >50K
    higher_education_rich = np.mean(data[(data.education == 'Bachelors') | (data.education == 'Masters') | (data.education == 'Doctorate')]['salary'] == '>50K')*100
    lower_education_rich = np.mean(data[(data.education != 'Bachelors') & (data.education != 'Masters') & (data.education != 'Doctorate')]['salary'] == '>50K')*100

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = min(data['hours-per-week'])

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?

    rich_percentage =  np.mean(data[data['hours-per-week'] == min(data['hours-per-week'])]['salary'] == '>50K')*100


    # What country has the highest percentage of people that earn >50K?
    data['bool-sal'] = data['salary'].apply(lambda x: 1 if x == '>50K' else 0)
    

    highest_earning_country = data.groupby('native-country')['bool-sal'].mean().sort_values(ascending = False).index[0]
  
    highest_earning_country_percentage = data.groupby('native-country')['bool-sal'].mean().sort_values(ascending = False)[0] *100

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = data[(data['native-country'] == 'India') & (data['salary'] == '>50K')]['occupation'].value_counts().index[0]


    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", format(average_age_men,'.1f'))
        print(f"Percentage with Bachelors degrees: {percentage_bachelors:.1f}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich:.1f}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich:.1f}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage:.1f}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage:.1f}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': round(average_age_men, 1),
        'percentage_bachelors': round(percentage_bachelors, 1),
        'higher_education_rich': round(higher_education_rich, 1),
        'lower_education_rich': round(lower_education_rich, 1),
        'min_work_hours': min_work_hours,
        'rich_percentage': round(rich_percentage, 1),
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': round(highest_earning_country_percentage, 1),
        'top_IN_occupation': top_IN_occupation
    }