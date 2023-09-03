# Import neccessary things for web application
from django.http import HttpResponse
from django.shortcuts import render, redirect
from prediction_database.models import Input, InputForm, Output
import os
import pickle
import numpy as np

# Get the directory of the current script
current_directory = os.path.dirname(os.path.abspath(__file__))

# Sepecify the relative path to the model file
model_relative_path = './AI_Core/Model/A1_Predicting_Car_Price.model'

# Create the absolute path to the model file
model_absolute_path = os.path.join(current_directory, model_relative_path)

# Load the Model from disk
loaded_model = pickle.load(open(model_absolute_path, 'rb'))

def index(request):

    if request.method == 'POST':
        user_input = InputForm(request.POST)
        if user_input.is_valid(): # Check Frontend form is filled valid then press Submit button
            user_input.save() # Save input data into the database
            
            # Load last input data from the database
            last_row_input = Input.objects.last() 
            input_form = InputForm(initial=last_row_input.__dict__)
            year = last_row_input.input_year
            max_power = last_row_input.input_max_power
            km_driven = last_row_input.input_km_driven

            # Area of predicting the selling price
            last_row_input_data = np.array([[year, km_driven, max_power]])
            predicted_output = loaded_model.predict(last_row_input_data)
            predicted_output = predicted_output[0] # Get element inside array

            # Save the predicted_output into database
            Output(output_selling_price=predicted_output).save()

            # Read last row data from the output database
            selling_price = Output.objects.last()
            selling_price = selling_price.output_selling_price

            return render(request, 'index.html', {'input_form': input_form,
                                                  'selling_price': selling_price})
            # return render(request, 'index.html', {'input_form': input_form})           
        else:
            print("Some Code in Backend lead to bug!")
            message = {'warning_message': "Input wrong!"}
            return render(request, 'index.html', message)

    else:
        # Initial input when load index.html
        input_form = InputForm()

        # Initial output when load index.html
        selling_price = 'Not show'

        # Render html file on the browser with including variables
        return render(request, 'index.html', {'input_form': input_form,
                                              'selling_price': selling_price})