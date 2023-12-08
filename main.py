"""
    CS5001_5003 Fall 2023 SV
    Final Project
    Mohan Qi
"""


import calorie_calculation
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.config import Config


# set window size 
Config.set('graphics', 'resizable', True)
Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '800')

class ScreenManagement(ScreenManager):
    pass

class CalculatorGUI(Screen):
    # set value for unselected gender and activity level widgets
    gender = 'Please select a gender'
    activity_level = 'Select activity level'
    weight_unit = 'kg'
    height_unit = 'cm'

    def checkbox_click(self, instance, value, sex):
        """ set up the checkbox for gender """
        if value:
            self.gender = sex
        else:
            self.gender = 'Please select a gender'
        return self.gender

    def weight_unit_toggle(self, instance):
        self.weight_unit = instance.text
        return self.weight_unit
    
    def height_unit_toggle(self, instance):
        self.height_unit = instance.text
        return self.height_unit

    def spinner_selected(self, values):
        """" set up the spinner for activity level """
        if values:
            self.activity_level = values
        else:
            self.activity_level = 'Select activity level'
        return self.activity_level



    def validate_input(self):
            age = self.ids.age.text
            gender = self.gender
            height = self.ids.height_input.text
            weight = self.ids.weight.text
            activity_level = self.activity_level
            
            input_validation = []

            # check if age input is empty
            if age == '':
                input_validation.append('age_empty')
                    
            else:
                # check if age input is a number
                if not age.isnumeric():
                    self.ids.age.text = ''  # Clear the input field
                    input_validation.append('age_not_number')
                # check if age input is in range 19-78, inclusively
                if float(age) < 19 or float(age) > 78:
                    self.ids.age.text = ''  # Clear the input field
                    input_validation.append('age_out_of_range')

            # check if height input is empty
            if height == '':
                input_validation.append('height_empty')
            else:
                # check if height input is a number
                if not height.isnumeric():
                    self.ids.height_input.text = ''  # Clear the input field
                    input_validation.append('height_not_number')
                # check if height input is in range from 50-280 cm, inclusively
                if float(height) < 50 or float(height) > 280:
                    self.ids.height_input.text = ''  # Clear the input field
                    input_validation.append('height_out_of_range')
            
            # check if weight input is empty
            if weight == '':
                input_validation.append('weight_empty')
            else:
                # check if weight input is a number
                if not weight.isnumeric():
                    self.ids.weight.text = ''  # Clear the input field
                    input_validation.append('weight_not_number')
                # check if weight input is in range from 15-650 kg, inclusively
                if float(weight) < 15 or float(weight) > 650:
                    self.ids.weight.text = ''  # Clear the input field    
                    input_validation.append('weight_out_of_range')

            # check if gender checkbox is selected
            if gender == 'Please select a gender':
                input_validation.append('gender_empty')

            # check if the activity level spinner is selected with a value 
            if activity_level == 'Select activity level':
                input_validation.append('activity_level_empty')
            
            # pops error message if there are more than 1 error
            if len(input_validation) > 1:
               self.show_error_popup("Multiple invalid inputs or missed inputs. Please check.")
            elif len(input_validation) == 1:
                if input_validation == ['age_empty']:
                    self.show_error_popup("Please enter an age.")
                elif input_validation == ['age_not_number']:
                    self.show_error_popup("Invalid age input. Please enter a number.")
                elif input_validation == ['age_out_of_range']:
                    self.show_error_popup("Invalid age input. Age input range: 19 to 78.")
                elif input_validation == ['height_empty']:
                    self.show_error_popup("Please enter a height.")
                elif input_validation == ['height_not_number']:
                    self.show_error_popup("Invalid height input. Please enter a number.")
                elif input_validation == ['height_out_of_range']:
                    self.show_error_popup("Invalid height input. Height input range: 50-280 cm.")
                elif input_validation == ['weight_empty']:
                    self.show_error_popup("Please enter a weight.")
                elif input_validation == ['weight_not_number']:
                    self.show_error_popup("Invalid weight input. Please enter a number.")
                elif input_validation == ['weight_out_of_range']:
                    self.show_error_popup("Invalid weight input. Weight input range: 15-650 kg.")
                elif input_validation == ['gender_empty']:
                    self.show_error_popup("Please select a gender.")
                elif input_validation == ['activity_level_empty']:
                    self.show_error_popup("Please select an activity level.")

    def show_error_popup(self, message):
        content = BoxLayout(orientation='vertical')
        content.add_widget(Label(text=message))
        content.add_widget(Button(text="OK", on_press=self.dismiss_popup))

        self.error_popup = Popup(title="Error", content=content, size_hint=(None, None), size=(800, 400))
        self.error_popup.open()

    def dismiss_popup(self, instance):
        self.error_popup.dismiss()
        self.manager.current = 'calculator'


class GoalaskingGUI(Screen):
        def result_maintain(self):
            """ get results for weight maintainence goal, results include:
                BMR, BMI, daily total calorie needs, daily carb needs, daily protein needs and daily fat needs
            """
            age = int(self.manager.get_screen('calculator').ids.age.text)
            gender = str(self.manager.get_screen('calculator').gender)
            height = float(self.manager.get_screen('calculator').ids.height_input.text)
            weight = float(self.manager.get_screen('calculator').ids.weight.text)
            activity_level = str(self.manager.get_screen('calculator').activity_level)
            weight_unit = str(self.manager.get_screen('calculator').weight_unit)
            height_unit = str(self.manager.get_screen('calculator').height_unit)


            if weight_unit == 'lbs':
                weight = weight * 0.4536
            if height_unit == 'inches':
                height = height * 2.54

            result_bmr = calorie_calculation.bmr_calculator(age, gender, weight, height)
            result_bmi = calorie_calculation.bmi_calculator(weight, height)
            result_total_calorie = calorie_calculation.total_calorie_calculator(result_bmr, activity_level)
            carb_daily_needs = calorie_calculation.daily_carb_rec_needs(result_total_calorie)
            pro_daily_needs = calorie_calculation.daily_protein_rec_needs(result_total_calorie)
            fat_daily_needs = calorie_calculation.daily_fat_rec_needs(result_total_calorie)
            

            self.manager.get_screen('result_maintain').ids.result_bmr_label.text = f'Current Basal Metabolic Rate (BMR): {result_bmr} calories/day'
            self.manager.get_screen('result_maintain').ids.result_bmi_label.text = f'Current Body Mass Index (BMI): {result_bmi} kg/m^2'
            self.manager.get_screen('result_maintain').ids.result_total_calorie_label.text = f'Total Calorie Needs: {result_total_calorie} calories/day'
            self.manager.get_screen('result_maintain').ids.carb_daily_needs_label.text = 'Daily Carbohydrate Needs: ' + carb_daily_needs
            self.manager.get_screen('result_maintain').ids.pro_daily_needs_label.text = 'Daily Protein Needs: ' + pro_daily_needs
            self.manager.get_screen('result_maintain').ids.fat_daily_needs_label.text = 'Daily Fat Needs: ' + fat_daily_needs


class ResultmaintainGUI(Screen):
    pass


class WeightgoalGUI(Screen):
    weight_unit = 'kg'
    activity_level = 'Select activity level'


    def weight_unit_toggle(self, instance):
        self.weight_unit = instance.text
        return self.weight_unit

 
    def spinner_selected(self, values):
        """" set up the spinner for activity level """
        if values:
            self.activity_level = values
        else:
            self.activity_level = 'Select activity level'
        return self.activity_level





    def result_goal(self):
        
        age = int(self.manager.get_screen('calculator').ids.age.text)
        gender = str(self.manager.get_screen('calculator').gender)
        height = float(self.manager.get_screen('calculator').ids.height_input.text)
        weight = float(self.manager.get_screen('calculator').ids.weight.text)
        activity_level = str(self.activity_level)
        weight_goal = float(self.manager.get_screen('weight_goal').ids.weight_goal.text)
        months = float(self.manager.get_screen('weight_goal').ids.months.text)
        weight_unit = str(self.manager.get_screen('calculator').weight_unit)
        height_unit = str(self.manager.get_screen('calculator').height_unit)


        if weight_unit == 'lbs':
            weight = weight * 0.4536
        if height_unit == 'inches':
            height = height * 2.54

        result_bmr = calorie_calculation.bmr_calculator(age, gender, weight, height)
        result_bmi = calorie_calculation.bmi_calculator(weight, height)
        result_total_calorie = calorie_calculation.total_calorie_calculator(result_bmr, activity_level)
        result_weight_goal_calorie = calorie_calculation.weight_goal(result_total_calorie, weight_goal, weight, months)
        carb_daily_needs = calorie_calculation.daily_carb_rec_needs(result_weight_goal_calorie)
        pro_daily_needs = calorie_calculation.daily_protein_rec_needs(result_weight_goal_calorie)
        fat_daily_needs = calorie_calculation.daily_fat_rec_needs(result_weight_goal_calorie)
        

        self.manager.get_screen('result_goal').ids.result_bmr_label.text = f'Current Basal Metabolic Rate (BMR): {result_bmr} calories/day'
        self.manager.get_screen('result_goal').ids.result_bmi_label.text = f'Current Body Mass Index (BMI): {result_bmi} kg/m^2'
        self.manager.get_screen('result_goal').ids.achieve_goal.text = f'To achieve your Goal Weight of {int(weight_goal)} kg in {int(months)} months with your Current Activity Level:'
        self.manager.get_screen('result_goal').ids.carb_daily_needs_label.text = 'Daily Carbohydrate Needs: ' + carb_daily_needs
        self.manager.get_screen('result_goal').ids.pro_daily_needs_label.text = 'Daily Protein Needs: ' + pro_daily_needs
        self.manager.get_screen('result_goal').ids.fat_daily_needs_label.text = 'Daily Fat Needs: ' + fat_daily_needs
        self.manager.get_screen('result_goal').ids.result_weight_goal_calorie_label.text = f'Total Calorie Needs: {result_weight_goal_calorie} calories/day'


class ResultgoalGUI(Screen):
    pass


class CalculatorApp(App):
    def build(self):
        return ScreenManagement()
    


if __name__ == '__main__':
    CalculatorApp().run()