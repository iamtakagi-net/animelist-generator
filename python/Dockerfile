FROM python:3.9.2

RUN apt update && \
    apt install -y \
    libopencv-dev \
    python-opencv

WORKDIR /app
COPY Pipfile .
COPY Pipfile.lock .
RUN pip install pipenv && \
    pipenv install --system
COPY . .

CMD ["python", "src/main.py"]