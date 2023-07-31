FROM python:3.10

# This prevents Python from writing out pyc files
ENV PYTHONDONTWRITEBYTECODE 1

# This keeps Python from buffering stdin/stdout
ENV PYTHONUNBUFFERED 1

WORKDIR /user/src/personal_helper


COPY ./req.txt /user/src/req.txt
RUN pip install -r /user/src/req.txt

COPY . /user/src/personal_helper