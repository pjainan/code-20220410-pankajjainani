import unittest
import json
import pandas as pd
from bmicalculator.bmi import bmicalc
# import bmicalculator.bmi as bm


class TestBMI(unittest.TestCase):    
    def test_negative_or_zero_height(self):
        js='[{"Gender": "Male", "HeightCm": -2, "WeightKg": 85}]'
        data = json.loads(js)
        df = pd.DataFrame(data, columns=['Gender', 'HeightCm', 'WeightKg'])
        # print(df)
        ret = bmicalc(df)
        self.assertEqual(ret['bmi'],float(-1))

    def test_negative_or_zero_weight(self):
        js='[{"Gender": "Male", "HeightCm": 170, "WeightKg": 0}]'
        data = json.loads(js)
        df = pd.DataFrame(data, columns=['Gender', 'HeightCm', 'WeightKg'])
        ret = bmicalc(df)
        self.assertEqual(ret['bmi'],float(-1))

    def test_valid_input(self):
        js='[{"Gender": "Male", "HeightCm": 180, "WeightKg": 77}]'
        data = json.loads(js)
        df = pd.DataFrame(data, columns=['Gender', 'HeightCm', 'WeightKg'])
        ret = bmicalc(df)
        self.assertEqual(ret['bmi'],float(23.765432))

    def test_invalid_input(self):
        js='[{"Gender": "Male", "WeightKg": 77}]'
        data = json.loads(js)
        try:
            df = pd.DataFrame(data, columns=['Gender', 'HeightCm', 'WeightKg'])
            ret = bmicalc(df)
        except IndexError: 
            self.assertEqual("IndexError","IndexError")
        
if __name__=='__main__':
    unittest.main()