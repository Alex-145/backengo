FROM python:3.5
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 8000
RUN yes | python manage.py makemigrations accounts home mod_backend params sad space utils
RUN yes | python manage.py migrate
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]