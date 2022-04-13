Require Python 3.8

Create a virtual environment
- open terminal (powershell)
- execute: pip install virtualenv
- execute: virtualenv venv -p python3
- execute: .\venv\scripts\activate.ps1

Install dependencies
- execute: pip install numpy
- execute: pip install pandas
- OR: pip install -r .\requirements.txt

Execute Program
- execute: python -m bmicalculator.bmi

Execute Tests
- execute: python -m unittest discover
- OR, execute: python .\test\test_bmi.py