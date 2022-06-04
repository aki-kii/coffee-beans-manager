FROM python:3.9-buster
ENV PYTHONBUFFERED=1


WORKDIR /src

# pip -> poetry
RUN pip install poetry

# copy: poetry difined file
COPY pyproject.toml* poetry.lock* ./

# install: lib from poetry
RUN poetry config virtualenvs.in-project true
RUN if [ -f pyproject.toml ]; then poetry install; fi

# startup: uvivorn server
ENTRYPOINT [ "poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--reload" ]