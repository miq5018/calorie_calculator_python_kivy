"""
    CS5001_5003 Fall 2023 SV
    Final Project
    Mohan Qi
"""

import calorie_calculation
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen


class ScreenManagement(ScreenManager):
    pass


class CalculatorGUI(Screen):

    def checkbox_click(self, instance, value, sex):
        if value == True:
            self.ids.gender.text = sex
        else:
            self.ids.gender.text = ''
        print(self.ids.gender.text)
        return self.ids.gender.text

    def spinner_selected(self, values):
        self.ids.activity_label.text = values
        return self.ids.activity_label.text


    def result(self):
        try:
            age = int(self.ids.age.text)
            gender = str(self.ids.gender.text)
            height = float(self.ids.height_input.text)
            weight = float(self.ids.weight.text)
            activity_level = str(self.ids.activity_label.text)
        except ValueError:
            print("An Error occurred.'")
        
        result_bmr = calorie_calculation.bmr_calculator(age, gender, weight, height)
        result_bmi = calorie_calculation.bmi_calculator(weight, height)
        result_total_calorie = calorie_calculation.total_calorie_calculator(result_bmr, activity_level)

        self.manager.get_screen('result').ids.result_bmr_label.text = f'Basal Metabolic Rate (BMR): {result_bmr} calories/day'
        self.manager.get_screen('result').ids.result_bmi_label.text = f'Body Mass Index (BMI): {result_bmi} kg/m^2'
        self.manager.get_screen('result').ids.result_total_calorie_label.text = f'Total Calorie Needs: {result_total_calorie} calories/day'

class ResultGUI(Screen):
    pass


class CalculatorApp(App):
    def build(self):
        return ScreenManagement()


if __name__ == '__main__':
    CalculatorApp().run()