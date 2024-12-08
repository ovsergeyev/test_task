FROM python:3.9-slim AS builder
ENV PYTHONUNBUFFERED=1

RUN pip install -U pip setuptools wheel

WORKDIR /wheels
COPY requirements.txt /requirements.txt
RUN pip wheel -r /requirements.txt

FROM python:3.9-slim
ENV PYTHONUNBUFFERED=1

COPY --from=builder /wheels /wheels
RUN pip install -U pip setuptools wheel \
  && pip install /wheels/* \
  && rm -rf /wheels \
  && rm -rf /root/.cache/pip/*

WORKDIR /code
COPY . .

RUN chmod a+x /code/scripts/app.sh

# EXPOSE 8000
ENV PYTHONPATH=/code

CMD ["sh", "/code/scripts/app.sh"]