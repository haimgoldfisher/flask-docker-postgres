FROM python:3.9-slim

WORKDIR /app

# Copy the application files into the container
COPY . .

# Install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5555

CMD ["python3", "app.py"]
