FROM python:3.7-alpine

WORKDIR /app

COPY . .

RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 8500

CMD ["python", "app.py"]