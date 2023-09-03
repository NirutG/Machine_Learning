# Use the official Python base image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the project requirements file to the working directory
COPY requirements.txt .

# Install project dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the project code to the working directory
COPY . .

# Expose the Django development server port
EXPOSE 8000

# Define the command to run the Django development server
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]