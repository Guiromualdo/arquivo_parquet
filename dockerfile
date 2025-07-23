FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
RUN chmod +x start.sh download_parquet.sh
CMD ["./start.sh"]