
FROM python:3.9-slim


WORKDIR /app


COPY requirements.txt .


RUN pip install --no-cache-dir -r requirements.txt


COPY . .


EXPOSE 80


ENV PORT=80

# Command to run the application
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
