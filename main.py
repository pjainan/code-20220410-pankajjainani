import json
import pandas as pd
import numpy as np

bmitable = pd.DataFrame([
    ['Underweight', 0, 18.4, 'Malnutrition risk'],
    ['Normal weight', 18.5, 24.9, 'Malnutrition risk'],
    ['Overweight', 25, 29.9, 'Enhanced risk'],
    ['Moderately obese', 30, 34.9, 'Enhanced risk'],
    ['Severely obese', 35, 39.9, 'High risk'],
    ['Very severely obese', 40, 100, 'Very High risk']
    ], columns=['BMI_category', 'BMI_Min', 'BMI_Max', 'Health_risk'])

if __name__=='__main__':
    f=open('data.json')
    data = json.load(f)
    df = pd.DataFrame(data, columns=['Gender', 'HeightCm', 'WeightKg'])
    f.close()
    df['bmi'] = df['WeightKg']/((df['HeightCm']/100)**2)
    df['Health_risk'] = df['bmi'].apply(lambda b: bmitable['Health_risk'][(b > bmitable['BMI_Min']) & (b <= bmitable['BMI_Max'])].values[0])
    df['BMI_category'] = df['bmi'].apply(lambda b: bmitable['BMI_category'][(b > bmitable['BMI_Min']) & (b <= bmitable['BMI_Max'])].values[0])
    print(df)