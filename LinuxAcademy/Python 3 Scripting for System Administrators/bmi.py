#!/usr/bin/env python3.6

# BMI = (weight in kg / height in meters squared)
# Imperial version: BMI *703

def gather_info():
    height = float(input("what is your height? (inches or meters) ")) 
    weight = float(input("what is your weight? (pounds or kilograms) ")) 
    system = input("Are your measurments in metric or imperial units? ").lower().strip()
    return (height, weight, system)

def calculate_bmi(weight, height, system='metric'):
    """
    Return the Body Mass Idex (BMI) for the
    given weight, height, and measurment system
    """
    if system == 'metric':
        bmi = (weight / (height ** 2))
    else:
        bmi = 703 * (weight / (height ** 2))    
    return bmi

while True:
    height, weight, system = gather_info()
    if system.startswith('i'):
        bmi = calculate_bmi(weight, system=system, height=height)
        print(f"Your BMI is {bmi}")
    elif system.startswith('m'):
        bmi = calculate_bmi(weight, height)
        print(f"Your BMI is {bmi}")
        break
    else:
        print("Error: Unknown measurment system. Please use imperial or metric")