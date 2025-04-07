## Copilot generated this code with the following prompt:
# generate data with faker with the following data: 
# * 20 'country'  
# * 50 years of  medical data (life expectancy, 5 cause of death, separated to the male/female )
# use pandas to save the data to a csv file

# This script generates synthetic medical data using the Faker library and saves it to a CSV file.
# https://pypi.org/project/Faker/
from faker import Faker
import random
import pandas as pd

fake = Faker()

# Generate 20 countries
countries = [fake.country() for _ in range(20)]

# Generate 50 years of medical data
medical_data = []
for year in range(1973, 2023):  # 50 years
    for country in countries:
        data = {
            "year": year,
            "country": country,
            "life_expectancy_male": round(random.uniform(50, 85), 1),
            "life_expectancy_female": round(random.uniform(55, 90), 1),
            "heart_disease_male": random.randint(100, 1000),
            "heart_disease_female": random.randint(100, 1000),
            "cancer_male": random.randint(100, 1000),
            "cancer_female": random.randint(100, 1000),
            "stroke_male": random.randint(50, 500),
            "stroke_female": random.randint(50, 500),
            "diabetes_male": random.randint(20, 300),
            "diabetes_female": random.randint(20, 300),
            "respiratory_disease_male": random.randint(30, 400),
            "respiratory_disease_female": random.randint(30, 400)
        }
        medical_data.append(data)

# Convert to a pandas DataFrame
df = pd.DataFrame(medical_data)

# Save to a CSV file
output_file = "medical_data.csv"
df.to_csv(output_file, index=False)

print(f"Generated data saved to {output_file}")
