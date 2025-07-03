FROM python:3.12.11-slim
COPY app /app
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt && rm requirements.txt
ENTRYPOINT ["python", "main.py"]