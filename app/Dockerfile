FROM python:3.8

# Install the Flask web framework and the Docker Python module
RUN pip install -r requirements.txt

# Copy the application code to the container
COPY app.py /app.py

# Set the working directory to the location of the application code
WORKDIR /

# Expose the application's port
EXPOSE 5000

# Run the application when the container starts
CMD ["python", "app.py"]
