import json
import pandas as pd
import numpy as np
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-f','--filepath',help='enter filepath for json file', default="data.json")
# parser.add_argument('-j','--jsondata',help='enter json ', default="data.json")
args = vars(parser.parse_args())
bmitable = pd.DataFrame([
    ['Underweight', 0, 18.4, 'Malnutrition risk'],
    ['Normal weight', 18.5, 24.9, 'Malnutrition risk'],
    ['Overweight', 25, 29.9, 'Enhanced risk'],
    ['Moderately obese', 30, 34.9, 'Enhanced risk'],
    ['Severely obese', 35, 39.9, 'High risk'],
    ['Very severely obese', 40, 100, 'Very High risk']
    ], columns=['BMI_category', 'BMI_Min', 'BMI_Max', 'Health_risk'])

def bmicalc(df):
    df['bmi'] = df.apply(lambda x: -1 if (x['HeightCm'] <=0 or x['WeightKg'] <=0 ) else (x['WeightKg']/((x['HeightCm']/100)**2)),axis=1)
    df['Health_risk'] = df['bmi'].apply(lambda b: "NA" if (b==-1) else (bmitable['Health_risk'][(b > bmitable['BMI_Min']) & (b <= bmitable['BMI_Max'])].values[0]))
    df['BMI_category'] = df['bmi'].apply(lambda b: "NA" if (b==-1) else (bmitable['BMI_category'][(b > bmitable['BMI_Min']) & (b <= bmitable['BMI_Max'])].values[0]))
    # print(df)
    return df

if __name__=='__main__':
    if args['filepath']:
        print(args['filepath'])
        f=open(args['filepath'])
        data = json.load(f)
        f.close()
        try:
            df = pd.DataFrame(data, columns=['Gender', 'HeightCm', 'WeightKg'])
            ret = bmicalc(df)
            print(ret)
        except IndexError:
            print("IndexError")
        