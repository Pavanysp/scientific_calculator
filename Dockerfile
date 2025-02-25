# Use the official Python image
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Copy all files from the current directory to /app in the container
COPY . .

# Install dependencies if requirements.txt exists
RUN pip install --no-cache-dir -r requirements.txt || true

# Default command to run the calculator
CMD ["python", "calculator.py"]
