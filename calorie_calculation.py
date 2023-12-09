"""
    CS5001_5003 Fall 2023 SV
    Final Project
    Mohan Qi
"""

def bmr_calculator(age, gender, weight, height):
    ''' This function will calulate one's basal metobolic rate (BMR).
        Parameters:
            age - an integer from 19 to 78, inclusively
            gender - female or male
            weight - float/integer in kg
            height - float/integer in centimeter
        Returns calculated BMR
    '''
    if gender == "Female":
        bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161
    elif gender == "Male": 
        bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
    return round(bmr)


def bmi_calculator(weight, height):
    ''' This function will calculate one's body mass index (BMI).
        Parameters: 
            weight - float/integer in kg
            height - float/integer in centimeter
        Returns calculated BMI
    '''
    bmi = weight / ((height / 100) ** 2)
    return round(bmi, 1)


def total_calorie_calculator(bmr, activity_level):
    ''' This function calculates daily total calorie needs.
        Parameters:
            bmr - calculated from function bmr
            activity_level: Sedentary, Lightly Active, Moderately Active, 
            Active, Very Active
        Returns daily calorie needs
    '''
    if activity_level == "Sedentary: little or no exercise":
        daily_calorie_needs = bmr * 1.2
    elif activity_level == "Lightly Active: light exercise 1-3 times/week":
        daily_calorie_needs = bmr * 1.375
    elif activity_level == "Moderately Active: light to moderate exercise 4-5 times/week":
        daily_calorie_needs = bmr * 1.55
    elif activity_level == "Active: moderate exercise 6-7 times/week or intense exercise 3-4 times/week":
        daily_calorie_needs = bmr * 1.725
    elif activity_level == "Very Active: intense exercise 6-7 times/week":
        daily_calorie_needs = bmr * 1.9
    return round(daily_calorie_needs)


def daily_carb_rec_needs(daily_calorie_needs):
    ''' This function calculates the recommended daily needs of carbohydrates.
        The recommended daily carb needs is 45-65% of total calorie.
    '''
    carb_needs_low = round(0.4 * daily_calorie_needs)
    carb_needs_high = round(0.65 * daily_calorie_needs)
    carb_daily_needs = str(carb_needs_low) + " -" + str(carb_needs_high) + " grams/day"
    return carb_daily_needs


def daily_protein_rec_needs(daily_calorie_needs):
    ''' This function calculates the recommended daily needs of protein.
        The recommended daily protein needs is 10-35% of total calorie.
    '''
    pro_needs_low = round(0.1 * daily_calorie_needs)
    pro_needs_high = round(0.35 * daily_calorie_needs)
    pro_daily_needs = str(pro_needs_low) + " - " + str(pro_needs_high) + " grams/day"
    return pro_daily_needs


def daily_fat_rec_needs(daily_calorie_needs):
    ''' This function calculates the recommended daily needs of fat.
        The recommended daily fat needs is 20-35% of total calorie.
    '''
    fat_needs_low = round(0.2 * daily_calorie_needs)
    fat_needs_high = round(0.35 * daily_calorie_needs)
    fat_daily_needs = str(fat_needs_low) + " - " + str(fat_needs_high) + " grams/day"
    return fat_daily_needs


def weight_goal(daily_calorie_needs, weight_goal, weight, months):
    weight_change = weight_goal - weight
    days = months * 30
    daily_calorie_needs_weight_change = ((weight_change / 0.45) * 3500) / days + daily_calorie_needs
    return round(daily_calorie_needs_weight_change)
