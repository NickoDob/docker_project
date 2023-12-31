FROM python:3.10-alpine

WORKDIR /app/src

COPY ./requirements.txt ./requirements.txt

RUN pip install pydantic[dotenv] && pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./src ./

CMD ["app:app", "--host", "0.0.0.0", "--port", "8080"]