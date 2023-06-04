FROM python:3.10 as requirements

WORKDIR /code

# CREATE REQUIREMENTS FIlE
COPY Pipfile.lock /code/Pipfile.lock 
RUN pip install pipenv
RUN pipenv requirements > /code/requirements.txt

FROM python:3.10

WORKDIR /code

# COPY APP & REQUIREMENTS
COPY app /code/app
COPY --from=requirements /code/requirements.txt /code/requirements.txt

# INSTALL DEPENDENCIES
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# PORT REQUIRED
EXPOSE 80
EXPOSE 8001

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
