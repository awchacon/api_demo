FROM python:3.10-slim

WORKDIR /app

COPY serve/main.py /app/
COPY serve/pydantic_types.py /app/
COPY serve/requirements.txt /app/

RUN pip install -r requirements.txt

EXPOSE 8080
CMD ["python", "main.py"]