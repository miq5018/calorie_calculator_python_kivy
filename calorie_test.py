"""
    CS5001_5003 Fall 2023 SV
    Final Project
    Mohan Qi
"""


import unittest
import calorie_calculation
from main import CalculatorApp, CalculatorGUI, GoalaskingGUI, WeightgoalGUI
from main import ScreenManager, ResultmaintainGUI, ResultgoalGUI


 
class CalculatorTest(unittest.TestCase):
    def test_validate_input_calculator(self):
        ''' This function tests the validate_input_calculator function 
            with different invalid values, and multiple invalid values.
        '''
        list1 = calorie_calculation.validate_input_calculator(
            '', 'Female', '195', '69', 
            "Sedentary: little or no exercise", 'kg', 'cm' )
        list2 = calorie_calculation.validate_input_calculator(
            '--', 'Female', '195', '69', 
            "Sedentary: little or no exercise", 'kg', 'cm' )
        list3 = calorie_calculation.validate_input_calculator(
            '100', 'Female', '195', '69', 
            "Sedentary: little or no exercise", 'kg', 'cm' )
        list4 = calorie_calculation.validate_input_calculator(
            '56', 'Please select a gender', '195', '69', 
            "Sedentary: little or no exercise", 'kg', 'cm' )
        list5 = calorie_calculation.validate_input_calculator(
            '56', 'Female', '', '69', 
            "Sedentary: little or no exercise", 'kg', 'cm' )
        list6 = calorie_calculation.validate_input_calculator(
            '56', 'Female', '+-', '69', 
            "Sedentary: little or no exercise", 'kg', 'cm' )
        list7 = calorie_calculation.validate_input_calculator(
            '56', 'Female', '499', '69', 
            "Sedentary: little or no exercise", 'kg', 'cm' )
        list8 = calorie_calculation.validate_input_calculator(
            '56', 'Female', '5', '69', 
            "Sedentary: little or no exercise", 'kg', 'cm' )
        list9 = calorie_calculation.validate_input_calculator(
            '2', 'Female', '159', '69', 
            "Sedentary: little or no exercise", 'kg', 'cm' )
        list10 = calorie_calculation.validate_input_calculator(
            '56', 'Female', '159', '', 
            "Sedentary: little or no exercise", 'kg', 'cm' )
        list11 = calorie_calculation.validate_input_calculator(
            '56', 'Female', '159', '//', 
            "Sedentary: little or no exercise", 'kg', 'cm' )
        list12 = calorie_calculation.validate_input_calculator(
            '56', 'Female', '159', '2', 
            "Sedentary: little or no exercise", 'kg', 'cm' )
        list13 = calorie_calculation.validate_input_calculator(
            '56', 'Female', '159', '999', 
            "Sedentary: little or no exercise", 'kg', 'cm' )
        list14 = calorie_calculation.validate_input_calculator(
            '56', 'Female', '159', '65', 
            "Select an activity level", 'kg', 'cm' )
        list15 = calorie_calculation.validate_input_calculator(
            '56', 'Female', '159', '2000', 
            "Sedentary: little or no exercise", 'lbs', 'cm' )
        list16 = calorie_calculation.validate_input_calculator(
            '56', 'Female', '159', '30', 
            "Sedentary: little or no exercise", 'lbs', 'cm' )
        list17 = calorie_calculation.validate_input_calculator(
            '56', 'Female', '15', '65', 
            "Sedentary: little or no exercise", 'kg', 'inches' )
        list18 = calorie_calculation.validate_input_calculator(
            '56', 'Female', '130', '65', 
            "Sedentary: little or no exercise", 'kg', 'inches' )
        list19 = calorie_calculation.validate_input_calculator(
            '', 'Female', '130', '65', 
            "Sedentary: little or no exercise", 'kg', 'inches' )
        list20 = calorie_calculation.validate_input_calculator(
            '56', 'Please select a gender', '130', '+-', 
            "Sedentary: little or no exercise", 'kg', 'cm' )
        self.assertEqual(list1, ['age_empty'])
        self.assertEqual(list2, ['age_not_number'])
        self.assertEqual(list3, ['age_out_of_range'])
        self.assertEqual(list4, ['gender_empty'])
        self.assertEqual(list5, ['height_empty'])
        self.assertEqual(list6, ['height_not_number'])
        self.assertEqual(list7, ['height_out_of_range'])
        self.assertEqual(list8, ['height_out_of_range'])
        self.assertEqual(list9, ['age_out_of_range'])
        self.assertEqual(list10, ['weight_empty'])
        self.assertEqual(list11, ['weight_not_number'])
        self.assertEqual(list12, ['weight_out_of_range'])
        self.assertEqual(list13, ['weight_out_of_range'])
        self.assertEqual(list14, ['activity_level_empty'])
        self.assertEqual(list15, ['weight_out_of_range'])
        self.assertEqual(list16, ['weight_out_of_range'])
        self.assertEqual(list17, ['height_out_of_range'])
        self.assertEqual(list18, ['height_out_of_range'])
        self.assertEqual(list19, ['age_empty', 'height_out_of_range'])
        self.assertEqual(list20, ['weight_not_number', 'gender_empty'])

    def test_validate_input_goal(self):
        ''' This function tests the validate_input_goal function 
            with different invalid values, and multiple invalid values.
        '''
        list1 = calorie_calculation.validate_input_goal(
            '', 'kg', '12', "Sedentary: little or no exercise")
        list2 = calorie_calculation.validate_input_goal(
            '*-', 'kg', '12', "Sedentary: little or no exercise")
        list3 = calorie_calculation.validate_input_goal(
            '999', 'kg', '12', "Sedentary: little or no exercise")
        list4 = calorie_calculation.validate_input_goal(
            '2', 'kg', '12', "Sedentary: little or no exercise")
        list5 = calorie_calculation.validate_input_goal(    
            '2100', 'lbs', '12', "Sedentary: little or no exercise")
        list6 = calorie_calculation.validate_input_goal(    
            '26', 'lbs', '12', "Sedentary: little or no exercise")
        list7 = calorie_calculation.validate_input_goal(    
            '65', 'kg', '', "Sedentary: little or no exercise")
        list8 = calorie_calculation.validate_input_goal(    
            '65', 'kg', '.+-', "Sedentary: little or no exercise")
        list9 = calorie_calculation.validate_input_goal(    
            '65', 'kg', '0', "Sedentary: little or no exercise")
        list10 = calorie_calculation.validate_input_goal(    
            '65', 'kgh', '100000', "Sedentary: little or no exercise")
        list11 = calorie_calculation.validate_input_goal(    
            '65', 'kg', '12', "Select an activity level")
        list12 = calorie_calculation.validate_input_goal(    
            '65', 'kg', '', "Select an activity level")
        self.assertEqual(list1, ['weight_goal_empty'])
        self.assertEqual(list2, ['weight_goal_not_number'])
        self.assertEqual(list3, ['weight_goal_out_of_range'])
        self.assertEqual(list4, ['weight_goal_out_of_range'])
        self.assertEqual(list5, ['weight_goal_out_of_range'])
        self.assertEqual(list6, ['weight_goal_out_of_range'])
        self.assertEqual(list7, ['months_empty'])
        self.assertEqual(list8, ['months_not_number'])
        self.assertEqual(list9, ['months_out_of_range'])
        self.assertEqual(list10, ['months_out_of_range'])
        self.assertEqual(list11, ['activity_level_empty'])
        self.assertEqual(list12, ['months_empty', 'activity_level_empty'])

    def test_bmr_calculator(self):
        """ This funtion tests the BMR calculator function 
            with 2 sets of values. 
        """
        result1 = calorie_calculation.bmr_calculator(20, 'Female', 65, 178)
        result2 = calorie_calculation.bmr_calculator(66, 'Male', 100, 192)
        self.assertEqual(result1, 1502)
        self.assertEqual(result2, 1875)
    
    def test_bmi_calculator(self):
        """ This funtion tests the BMI calculator function 
            with 2 sets of values. 
        """
        result1 = calorie_calculation.bmi_calculator(69, 155)
        result2 = calorie_calculation.bmi_calculator(150, 189)
        self.assertEqual(result1, 28.7)
        self.assertEqual(result2, 42)

    def test_total_calorie_calculator(self):
        """ This funtion tests the total calorie calculator function 
            with all different levels of activity and 
            with fixed and calculated BMR values. 
        """
        result1 = calorie_calculation.total_calorie_calculator(1502, 
        "Sedentary: little or no exercise")
        result2 = calorie_calculation.total_calorie_calculator(1655, 
        "Lightly Active: light exercise 1-3 times/week")
        bmr_result = calorie_calculation.bmr_calculator(25, 'Female', 50, 166)
        result3 = calorie_calculation.total_calorie_calculator(bmr_result, 
        "Moderately Active: light to moderate exercise 4-5 times/week")
        result4 = calorie_calculation.total_calorie_calculator(bmr_result, 
        "Active: moderate exercise 6-7 times/week or intense exercise 3-4 times/week")
        result5 = calorie_calculation.total_calorie_calculator(bmr_result, 
        "Very Active: intense exercise 6-7 times/week")
        self.assertEqual(result1, 1802)
        self.assertEqual(result2, 2276)
        self.assertEqual(result3, 1941)
        self.assertEqual(result4, 2160)
        self.assertEqual(result5, 2379)

    def test_carb_needs(self):
        """ This funtion tests the daily carb recommended needs function 
            with fixed and calculated daily total calorie values. 
        """
        result1 = calorie_calculation.daily_carb_rec_needs(2101)
        total_calorie_1 = calorie_calculation.total_calorie_calculator(1502, 
        "Sedentary: little or no exercise")
        result2 = calorie_calculation.daily_carb_rec_needs(total_calorie_1)
        self.assertEqual(result1, '236 - 341 grams/day')
        self.assertEqual(result2, '203 - 293 grams/day')
    
    def test_protein_needs(self):
        """ This funtion tests the daily protein recommended needs function 
            with fixed and calculated daily total calorie values. 
        """
        result1 = calorie_calculation.daily_protein_rec_needs(2101)
        total_calorie_1 = calorie_calculation.total_calorie_calculator(1502, 
        "Sedentary: little or no exercise")
        result2 = calorie_calculation.daily_protein_rec_needs(total_calorie_1)
        self.assertEqual(result1, '53 - 184 grams/day')
        self.assertEqual(result2, '45 - 158 grams/day')

    def test_fat_needs(self):
        """ This funtion tests the daily fat recommended needs function 
            with fixed and calculated daily total calorie values. 
        """
        result1 = calorie_calculation.daily_fat_rec_needs(2101)
        total_calorie_1 = calorie_calculation.total_calorie_calculator(1502, 
        "Sedentary: little or no exercise")
        result2 = calorie_calculation.daily_fat_rec_needs(total_calorie_1)
        self.assertEqual(result1, '47 - 82 grams/day')
        self.assertEqual(result2, '40 - 70 grams/day')

    def test_weight_goal(self):
        """ This funtion tests the weight goal function 
            with fixed and calculated daily total calorie values. 
        """
        result1 = calorie_calculation.weight_goal(2101, 99, 54, 10)
        total_calorie_1 = calorie_calculation.total_calorie_calculator(1502, 
        "Sedentary: little or no exercise")
        result2 = calorie_calculation.weight_goal(total_calorie_1, 65, 115, 12)
        self.assertEqual(result1, 3268)
        self.assertEqual(result2, 722)


class MainTest(unittest.TestCase):
    def test_checkbox_click(self):
        """ This funtion tests the gender checkbox click function 
            with and without selection. 
        """
        app = CalculatorApp()
        app.build()

        app.root.get_screen('calculator').checkbox_click(None, True, 'Male')
        self.assertEqual(app.root.get_screen('calculator').gender, 'Male')
        app.root.get_screen('calculator').checkbox_click(None, False, 'Female')
        self.assertEqual(app.root.get_screen('calculator').gender, 'Please select a gender')


'''
    def test_validate_input_valid_inputs(self):
        app = CalculatorApp()
        app.build()

        app.root.get_screen('calculator').ids.age.text = 25
        app.root.get_screen('calculator').gender = 'Male'
        app.root.get_screen('calculator').ids.height_input.text = '175'
        app.root.get_screen('calculator').weight.text = '70'
        app.activity_level = 'High'

        # Call the validate_input function
        app.root.get_screen('calculator').validate_input()

        # Assert that no error popup should be shown
        self.assertIsNone(app.root.get_screen('calculator').error_popup)
'''    

def main():
    unittest.main(verbosity = 3)

main()
