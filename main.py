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


class ScreenManagement(ScreenManager):
    pass

class CalculatorGUI(Screen):
    def checkbox_click(self, instance, value, sex):
        if value == True:
            self.ids.gender = sex
        else:
            self.ids.gender = ''
        return self.ids.gender

    def spinner_selected(self, values):
        self.ids.activity_label = values
        return self.ids.activity_label

    def result(self):
        try:
            age = int(self.ids.age.text)
            gender = str(self.ids.gender)
            height = float(self.ids.height_input.text)
            weight = float(self.ids.weight.text)
            activity_level = str(self.ids.activity_label)
        except ValueError:
            print("An Error occurred.'")
        
        result_bmr = calorie_calculation.bmr_calculator(age, gender, weight, height)
        result_bmi = calorie_calculation.bmi_calculator(weight, height)
        result_total_calorie = calorie_calculation.total_calorie_calculator(result_bmr, activity_level)

        self.manager.get_screen('result').ids.result_bmr_label.text = f'Basal Metabolic Rate (BMR): {result_bmr} calories/day'
        self.manager.get_screen('result').ids.result_bmi_label.text = f'Body Mass Index (BMI): {result_bmi} kg/m^2'
        self.manager.get_screen('result').ids.result_total_calorie_label.text = f'Total Calorie Needs: {result_total_calorie} calories/day'


    def validate_input(self):
            age = self.ids.age.text
            gender = self.ids.gender
            height = self.ids.height_input.text
            weight = self.ids.weight.text
            activity_level = self.ids.activity_label
            
            input_validation = True
            if not age.isnumeric():
                self.show_error_popup("Invalid age input. Please enter a number.")
                self.ids.age.text = ''  # Clear the input field
                input_validation = False

            if float(age) < 19 or float(age) > 78:
                self.show_error_popup("Invalid age input. Age input range: 19 to 78.")
                self.ids.age.text = ''  # Clear the input field
                input_validation = False

            if not height.isnumeric():
                self.show_error_popup("Invalid height input. Please enter a number.")
                self.ids.height_input.text = ''  # Clear the input field
                input_validation = False

            if float(height) < 50 or float(height) > 280:
                self.show_error_popup("Invalid height input. Height input range: 50-280 cm.")
                self.ids.height_input.text = ''  # Clear the input field
                input_validation = False
            
            if not weight.isnumeric():
                self.show_error_popup("Invalid weight input. Please enter a number.")
                self.ids.weight.text = ''  # Clear the input field
                input_validation = False

            if float(weight) < 15 or float(weight) > 650:
                self.show_error_popup("Invalid weight input. Weight input range: 15-650 kg.")
                self.ids.weight.text = ''  # Clear the input field    
                input_validation = False

            if gender == '':
                self.show_error_popup("Please select a gender.")
                input_validation = False

            if activity_level == "Select activity level":
                self.show_error_popup("Please select an gender.")
                input_validation = False
            
            if input_validation == True:
                self.result()

    def show_error_popup(self, message):
        content = BoxLayout(orientation='vertical')
        content.add_widget(Label(text=message))
        content.add_widget(Button(text="OK", on_press=self.dismiss_popup))

        self.error_popup = Popup(title="Error", content=content, size_hint=(None, None), size=(800, 400))
        self.error_popup.open()

    def dismiss_popup(self, instance):
        self.error_popup.dismiss()
        self.manager.current = 'calculator'



class ResultGUI(Screen):
    pass


class CalculatorApp(App):
    def build(self):
        return ScreenManagement()


if __name__ == '__main__':
    CalculatorApp().run()