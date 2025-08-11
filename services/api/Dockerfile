FROM python:3.12-slim
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
RUN useradd -u 1001 -m appuser
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py stations.json lines.json ./
EXPOSE 8000
USER 1001
CMD ["gunicorn","-w","2","-b","0.0.0.0:8000","app:app"]
