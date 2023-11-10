FROM python:3-alpine

WORKDIR /app

RUN echo "Flask" > requirements.txt && echo "requests" >> requirements.txt
RUN pip install -r requirements.txt
COPY fake.py .

EXPOSE 5000

CMD ["python", "fake.py"]