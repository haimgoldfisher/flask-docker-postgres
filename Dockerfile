FROM python:3.9-slim
WORKDIR /app/
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY .venv .
EXPOSE 5555
CMD ["python3", "app.py"]