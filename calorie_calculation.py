"""
    CS5001_5003 Fall 2023 SV
    Final Project
    Mohan Qi
"""


def validate_input_calculator(age, gender, height, weight, 
                              activity_level, weight_unit, height_unit):
    ''' This function will validate all inputs from the CalculatorGUI screen
        and returns an input_validation list which includes the error code(s)
        to generate the error pop-ups in kivy app.
    '''
    input_validation = []   #initiate the list to store error code(s)

    # check if age input is empty
    if age == '':
        input_validation.append('age_empty')
    else:
        # check if age input is a number
        if not age.isnumeric():
            input_validation.append('age_not_number')
        else:
            # check if age input is in range 19-78, inclusively
            if float(age) < 19 or float(age) > 78:
                input_validation.append('age_out_of_range')

    # check if height input is empty
    if height == '':
        input_validation.append('height_empty')
    else:
        # check if height input is a number
        if not height.isnumeric():
            input_validation.append('height_not_number')
        else:
            # if the height unit is inches, convert height to cm
            if height_unit == 'inches':
                height = float(height) * 2.54
            # check if height input is in range from 50-280 cm, inclusively
            if float(height) < 50 or float(height) > 280:
                input_validation.append('height_out_of_range')
    
    # check if weight input is empty
    if weight == '':
        input_validation.append('weight_empty')
    else:
        # check if weight input is a number
        if not weight.isnumeric():
            input_validation.append('weight_not_number')
        else:
            # if the weight unit is lbs, convert weight to kg
            if weight_unit == 'lbs':
                weight = float(weight) * 0.4536
            # check if weight input is in range from 15-650 kg, inclusively
            if float(weight) < 15 or float(weight) > 650:
                input_validation.append('weight_out_of_range')

    # check if gender checkbox is selected
    if gender == 'Please select a gender':
        input_validation.append('gender_empty')

    # check if the activity level spinner is selected with a value 
    if activity_level == 'Select an activity level':
        input_validation.append('activity_level_empty')
    
    return input_validation

def validate_input_goal(weight_goal, goal_weight_unit, months, 
                        activity_level):
    input_validation = []   #initiate the list to store error code(s)

    # check if weight goal input is empty
    if weight_goal == '':
        input_validation.append('weight_goal_empty')
    else:
        # check if weight input is a number
        if not weight_goal.isnumeric():
            input_validation.append('weight_goal_not_number')
        else:
            # if the goal weight unit is lbs, convert goal weight to kg
            if goal_weight_unit == 'lbs':
                weight_goal = float(weight_goal) * 0.4536
            # check if weight input is in range from 15-650 kg, inclusively
            if float(weight_goal) < 15 or float(weight_goal) > 650:
                input_validation.append('weight_goal_out_of_range')

    # check if months input is empty
    if months == '':
        input_validation.append('months_empty')
    else:
        # check if months input is a number
        if not months.isnumeric():
            input_validation.append('months_not_number')
        else:
        # check if months input is in range from 0-120 months
            if float(months) <= 0 or float(months) > 120:
                input_validation.append('months_out_of_range')
    
    # check if the activity level spinner is selected with a value 
    if activity_level == 'Select an activity level':
        input_validation.append('activity_level_empty')
    
    return input_validation
            

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
        1 gram of carb has 4 calories.
    '''
    carb_needs_low = round((0.45 * daily_calorie_needs) / 4)
    carb_needs_high = round((0.65 * daily_calorie_needs) / 4)
    carb_daily_needs = str(carb_needs_low) + " - " + str(carb_needs_high) + " grams/day"
    return carb_daily_needs


def daily_protein_rec_needs(daily_calorie_needs):
    ''' This function calculates the recommended daily needs of protein.
        The recommended daily protein needs is 10-35% of total calorie.
        1 gram of protein has 4 calories.
    '''
    pro_needs_low = round((0.1 * daily_calorie_needs) / 4)
    pro_needs_high = round((0.35 * daily_calorie_needs) / 4)
    pro_daily_needs = str(pro_needs_low) + " - " + str(pro_needs_high) + " grams/day"
    return pro_daily_needs


def daily_fat_rec_needs(daily_calorie_needs):
    ''' This function calculates the recommended daily needs of fat.
        The recommended daily fat needs is 20-35% of total calorie.
        1 gram of fat has 9 calories.
    '''
    fat_needs_low = round((0.2 * daily_calorie_needs) / 9)
    fat_needs_high = round((0.35 * daily_calorie_needs) / 9)
    fat_daily_needs = str(fat_needs_low) + " - " + str(fat_needs_high) + " grams/day"
    return fat_daily_needs


def weight_goal(daily_calorie_needs, weight_goal, weight, months):
    weight_change = weight_goal - weight
    days = months * 30
    daily_calorie_needs_weight_change = ((weight_change / 0.45) * 3500) / days + daily_calorie_needs
    return round(daily_calorie_needs_weight_change)
