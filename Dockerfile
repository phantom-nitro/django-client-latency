# Use the official Python image as the base
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1  
ENV PYTHONUNBUFFERED 1        

# Set the working directory
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django project into the container
COPY . /app/

# Environment Variable passing
ARG DJANGO_ENV_FILE
RUN ["/bin/bash", "-c", "echo \"$DJANGO_ENV_FILE\" > /app/.env && chmod 600 /app/.env"]

# Ensure the .env file content isn't printed
RUN ["/bin/bash", "-c", "ls -al /app && echo '.env file created successfully'"]

# Run collectstatic
RUN python manage.py collectstatic --noinput


# Expose the port your Django app runs on (default is 8000)
EXPOSE 8000

# Command to run the Django app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
