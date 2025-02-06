

FROM python:3.9

WORKDIR /app

COPY requiriments.txt  /app/requiriments.txt

RUN pip install --no-cache-dir --upgrade -r /app/requiriments.txt

COPY . /app


CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]