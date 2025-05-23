FROM python:3.13.3-alpine

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir flask

EXPOSE 5000

CMD ["python", "apiphytonbasica.py"]