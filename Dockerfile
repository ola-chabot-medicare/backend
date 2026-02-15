FROM python:3.10:slim 

WORKDIR /backend

COPY . .

CMD ["uvicorn" ,"app.main:app", "--host", "0.0.0.0" , "--port", "8000"]

