"""
    CS5001_5003 Fall 2023 SV
    Final Project
    Mohan Qi
"""


# import calorie calculation py file and kivy packages for GUI
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
    ''' This sets up the screen management '''
    pass


class CalculatorGUI(Screen):
    ''' This sets up different funtions under the calculatorGUI screen '''
    # set value for unselected gender and default weight and height units
    gender = 'Please select a gender'
    weight_unit = 'kg'
    height_unit = 'cm'

    def checkbox_click(self, instance, value, sex):
        """ The function sets up the checkbox for gender """
        if value:
            self.gender = sex
        else:
            self.gender = 'Please select a gender'
        return self.gender

    def weight_unit_toggle(self, instance):
        ''' This function sets up the weight unit toggle with kg and lbs '''
        self.weight_unit = instance.text
        return self.weight_unit

    def height_unit_toggle(self, instance):
        ''' This function sets up the height unit toggle with cm and inches '''
        self.height_unit = instance.text
        return self.height_unit

    def spinner_selected(self, values):
        ''' This function sets up the activity level spinner with the default
            value of "Select an activity level"
        '''
        if values:
            App.activity_level = values
        else:
            App.activity_level = 'Select an activity level'
        return App.activity_level

    def validate_input(self):
        ''' This function calls the validate_input_calculator function in
            calorie_calculation.py and triggers error popups based on the
            invalid input types.
        '''
        age = self.ids.age.text
        gender = self.gender
        height = self.ids.height_input.text
        weight = self.ids.weight.text
        activity_level = self.ids.activity_spinner.text
        weight_unit = self.weight_unit
        height_unit = self.height_unit

        # calls the validate_input_calculator function
        input_validation = calorie_calculation.validate_input_calculator(
            age, gender, height, weight,
            activity_level, weight_unit, height_unit)

        # pops error message if there are more than 1 error
        if len(input_validation) > 1:
            self.show_error_popup("Multiple invalid inputs or missed "
                                  "inputs. Please check.")
            if 'age_not_number' in input_validation:
                self.ids.age.text = ''
            if 'age_out_of_range' in input_validation:
                self.ids.age.text = ''
            if 'height_out_of_range' in input_validation:
                self.ids.height_input.text = ''
            if 'height_not_number' in input_validation:
                self.ids.height_input.text = ''
            if 'weight_out_of_range' in input_validation:
                self.ids.weight.text = ''
            if 'weight_not_number' in input_validation:
                self.ids.weight.text = ''
        # pops error message if there is only 1 error
        elif len(input_validation) == 1:
            if input_validation == ['age_empty']:
                self.show_error_popup("Please enter an age.")
            elif input_validation == ['age_not_number']:
                self.ids.age.text = ''
                self.show_error_popup("Invalid age input. Please "
                                      "enter an integer number.")
            elif input_validation == ['age_out_of_range']:
                self.ids.age.text = ''
                self.show_error_popup("Invalid age input. Age input "
                                      "range: 19 to 78.")
            elif input_validation == ['height_empty']:
                self.show_error_popup("Please enter a height.")
            elif input_validation == ['height_not_number']:
                self.ids.height_input.text = ''
                self.show_error_popup("Invalid height input. Please "
                                      "enter an integer number.")
            elif input_validation == ['height_out_of_range']:
                self.ids.height_input.text = ''
                self.show_error_popup("Invalid height input. Height input"
                                      " range: 50-280 cm (20-110 inches)."
                                      )
            elif input_validation == ['weight_empty']:
                self.show_error_popup("Please enter a weight.")
            elif input_validation == ['weight_not_number']:
                self.ids.weight.text = ''
                self.show_error_popup("Invalid weight input. Please "
                                      "enter an integer number.")
            elif input_validation == ['weight_out_of_range']:
                self.ids.weight.text = ''
                self.show_error_popup("Invalid weight input. Weight input "
                                      "range: 15-650 kg (33-1433 lbs).")
            elif input_validation == ['gender_empty']:
                self.show_error_popup("Please select a gender.")
            elif input_validation == ['activity_level_empty']:
                self.show_error_popup("Please select an activity level.")
        else:
            # goes to the goal asking screen if there is no error
            self.manager.current = "goal_asking"

    def show_error_popup(self, message):
        ''' This function shows error popup windows with the
            error messages.
        '''
        content = BoxLayout(orientation='vertical')
        content.add_widget(Label(text=message))
        content.add_widget(Button(text="OK", on_press=self.dismiss_popup))

        self.error_popup = Popup(title="Error", content=content,
                                 size_hint=(None, None), size=(1000, 400))
        self.error_popup.open()

    def dismiss_popup(self, instance):
        ''' This function closes the error popup windown and
            returns to the calculatorGUI screen.
        '''
        self.error_popup.dismiss()
        self.manager.current = 'calculator'


class GoalaskingGUI(Screen):
    def result_maintain(self):
        """ This function gets results for weight maintainence goal,
            results include:
            BMR, BMI, daily total calorie needs, daily carb needs,
            daily protein needs and daily fat needs.
        """
        age = int(self.manager.get_screen('calculator').ids.age.text)
        gender = str(self.manager.get_screen('calculator').gender)
        height = float(
            self.manager.get_screen('calculator').ids.height_input.text)
        weight = float(
            self.manager.get_screen('calculator').ids.weight.text)
        activity_level = str(App.activity_level)
        weight_unit = str(
            self.manager.get_screen('calculator').weight_unit)
        height_unit = str(
            self.manager.get_screen('calculator').height_unit)

        # covert unit to kg and cm if the unit toggle is changed
        if weight_unit == 'lbs':
            weight = weight * 0.4536
        if height_unit == 'inches':
            height = height * 2.54

        # calls the calculation functions in the calorie_calculation file
        result_bmr = calorie_calculation.bmr_calculator(age, gender,
                                                        weight, height)
        result_bmi = calorie_calculation.bmi_calculator(weight, height)
        result_total_calorie = calorie_calculation.total_calorie_calculator(
            result_bmr, activity_level)
        carb_daily_needs = calorie_calculation.daily_carb_rec_needs(
            result_total_calorie)
        pro_daily_needs = calorie_calculation.daily_protein_rec_needs(
            result_total_calorie)
        fat_daily_needs = calorie_calculation.daily_fat_rec_needs(
            result_total_calorie)

        # show the results on the resultmaintain screen
        result = self.manager.get_screen('result_maintain')
        result.ids.result_bmr_label.text = f'{result_bmr} calories/day'
        result.ids.result_bmi_label.text = f'{result_bmi} kg/m^2'
        result.ids.result_total_calorie_label.text = (
            f'{result_total_calorie} calories/day')
        result.ids.carb_daily_needs_label.text = carb_daily_needs
        result.ids.pro_daily_needs_label.text = pro_daily_needs
        result.ids.fat_daily_needs_label.text = fat_daily_needs


class ResultmaintainGUI(Screen):
    ''' Sets up the ResultmaintainGUI screen '''
    pass


class WeightgoalGUI(Screen):
    ''' Sets up the Weightgoal screen and several functions on this screen '''
    weight_unit = 'kg'

    def weight_unit_goal_toggle(self, instance):
        ''' This funtion sets up the weight unit toggle for
            weight goal with kg and lbs.
        '''
        self.weight_unit = instance.text
        return self.weight_unit

    def on_pre_enter(self):
        ''' This function sets up the default choice of the spinner
            in Screen Weight_goal based on the stored value.
        '''
        self.ids.goal_activity_spinner.text = App.activity_level

    def spinner_selected(self, values):
        """ This function sets up the spinner for activity level with the
            default value equals to the activity spinner selection on the
            calculatorGUI screen.
        """
        if values:
            App.activity_level = values
        return App.activity_level

    def validate_input(self):
        ''' This function calls the validate_input_goal function in
            calorie_calculation.py and triggers error popups based on the
            invalid input types.
        '''
        weight_goal = self.ids.weight_goal.text
        months = self.ids.months.text
        activity_level = self.ids.goal_activity_spinner.text
        goal_weight_unit = str(self.weight_unit)

        # calls the validate_input_calculator function
        input_validation = calorie_calculation.validate_input_goal(
            weight_goal, goal_weight_unit, months, activity_level)

        # pops error message if there are more than 1 error
        if len(input_validation) > 1:
            self.show_error_popup("Multiple invalid inputs or missed inputs. "
                                  "Please check.")
            if 'weight_goal_not_number' in input_validation:
                self.ids.weight_goal.text = ''
            if 'weight_goal_out_of_range' in input_validation:
                self.ids.weight_goal.text = ''
            if 'months_out_of_range' in input_validation:
                self.ids.months.text = ''
            if 'months_not_number' in input_validation:
                self.ids.months.text = ''
        # pops error message if there is only 1 error
        elif len(input_validation) == 1:
            if input_validation == ['weight_goal_empty']:
                self.show_error_popup("Please enter a goal weight.")
            elif input_validation == ['weight_goal_not_number']:
                self.ids.weight_goal.text = ''
                self.show_error_popup("Invalid goal weight input. Please "
                                      "enter an integer number.")
            elif input_validation == ['weight_goal_out_of_range']:
                self.ids.weight_goal.text = ''
                self.show_error_popup("Invalid goal weight input. Goal "
                                      "weight input range: 15-650 kg "
                                      "(33-1433 lbs).")
            elif input_validation == ['months_empty']:
                self.show_error_popup("Please enter a time duration.")
            elif input_validation == ['months_not_number']:
                self.ids.months.text = ''
                self.show_error_popup("Invalid time duration input. Please "
                                      "enter an integer number.")
            elif input_validation == ['months_out_of_range']:
                self.ids.months.text = ''
                self.show_error_popup("Invalid time duration input. "
                                      "Time duration input range: "
                                      "0-120 months. ")
            elif input_validation == ['activity_level_empty']:
                self.show_error_popup("Please select an activity level.")
        else:
            # calls the result function if there is no error
            self.result_goal()
            # goes to the result goal screen if there is no error
            self.manager.current = "result_goal"

    def show_error_popup(self, message):
        ''' This function shows error popup windows with the
            error messages.
        '''
        content = BoxLayout(orientation='vertical')
        content.add_widget(Label(text=message))
        content.add_widget(Button(text="OK", on_press=self.dismiss_popup))

        self.error_popup = Popup(
            title="Error", content=content,
            size_hint=(None, None), size=(1000, 400))
        self.error_popup.open()

    def dismiss_popup(self, instance):
        ''' This function dismisses error popup windows and returns to
            the weightgoalGUi screen.
        '''
        self.error_popup.dismiss()
        self.manager.current = 'weight_goal'

    def result_goal(self):
        ''' This function calls the calculation functions from the
            calorie_calculation.py and gets the result for bmr, bmi,
            total calorie needs to acheive the weight goal, daily carb needs,
            daily protein and fat needs.
        '''
        age = int(self.manager.get_screen('calculator').ids.age.text)
        gender = str(self.manager.get_screen('calculator').gender)
        height = float(
            self.manager.get_screen('calculator').ids.height_input.text)
        weight = float(self.manager.get_screen('calculator').ids.weight.text)
        activity_level = str(App.activity_level)
        weight_goal = float(
            self.manager.get_screen('weight_goal').ids.weight_goal.text)
        weight_goal_print = float(
            self.manager.get_screen('weight_goal').ids.weight_goal.text)
        months = float(self.manager.get_screen('weight_goal').ids.months.text)
        weight_unit = str(self.manager.get_screen('calculator').weight_unit)
        height_unit = str(self.manager.get_screen('calculator').height_unit)
        goal_weight_unit = str(self.weight_unit)

        # coverts the weight, height or goal weight from lbs/inches to kg/cm
        if weight_unit == 'lbs':
            weight = weight * 0.4536
        if height_unit == 'inches':
            height = height * 2.54
        if goal_weight_unit == 'lbs':
            weight_goal = weight_goal * 0.4536

        # calls the calculation functions from calorie_calculation file
        result_bmr = calorie_calculation.bmr_calculator(age, gender,
                                                        weight, height)
        result_bmi = calorie_calculation.bmi_calculator(weight, height)
        result_total_calorie = calorie_calculation.total_calorie_calculator(
            result_bmr, activity_level)
        result_weight_goal_calorie = calorie_calculation.weight_goal(
            result_total_calorie, weight_goal, weight, months)
        carb_daily_needs = calorie_calculation.daily_carb_rec_needs(
            result_weight_goal_calorie)
        pro_daily_needs = calorie_calculation.daily_protein_rec_needs(
            result_weight_goal_calorie)
        fat_daily_needs = calorie_calculation.daily_fat_rec_needs(
            result_weight_goal_calorie)

        # shows the results on the resultgoalGUI screen
        result = self.manager.get_screen('result_goal')
        result.ids.result_bmr_label.text = f'{result_bmr} calories/day'
        result.ids.result_bmi_label.text = f'{result_bmi} kg/m^2'
        result.ids.achieve_goal.text = (
            f'To achieve your Goal Weight of {int(weight_goal_print)} '
            f'{goal_weight_unit} in {int(months)} months:')
        result.ids.carb_daily_needs_label.text = carb_daily_needs
        result.ids.pro_daily_needs_label.text = pro_daily_needs
        result.ids.fat_daily_needs_label.text = fat_daily_needs
        result.ids.result_weight_goal_calorie_label.text = (
            f'{result_weight_goal_calorie} calories/day')


class ResultgoalGUI(Screen):
    ''' Sets up the ResultgoalGUI screen '''
    pass


class CalculatorApp(App):
    ''' Sets up the kivy app, stores an app value and
        sets up the restart function.
    '''
    activity_level = 'Select an activity level'

    def build(self):
        ''' Starts the program '''
        # Create an instance of ScreenManagement
        screen_manager = ScreenManagement()
        screen_manager.add_widget(CalculatorGUI(name='calculator'))
        screen_manager.add_widget(GoalaskingGUI(name='goal_asking'))
        screen_manager.add_widget(ResultmaintainGUI(name='result_maintain'))
        screen_manager.add_widget(WeightgoalGUI(name='weight_goal'))
        screen_manager.add_widget(ResultgoalGUI(name='result_goal'))
        # Assign it to the root attribute of the app
        self.root = screen_manager
        return screen_manager

    def restart_program(self):
        ''' Restarts the program if the "Starover" button is clicked '''
        CalculatorApp().run()


if __name__ == '__main__':
    CalculatorApp().run()
