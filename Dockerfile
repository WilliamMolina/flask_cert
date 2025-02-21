FROM python:3.6
COPY . .
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python","cert.py"]