FROM python:3.13-slim
# Create a directory for the app
RUN mkdir /app
# Set the working directory in the container
WORKDIR /app
# Prevents Python from writing pyc files to disk
ENV PYTHONDONTWRITEBYTECODE=1

# Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip

# Copy the Django project  and install dependencies
COPY requirements.txt  /app/
# Run all requirrements 
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django project to the container
COPY . /app/

# Expose the Django port
EXPOSE 8000

# Run Django’s development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]