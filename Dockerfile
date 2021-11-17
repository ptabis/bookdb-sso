FROM python:3.9.9-alpine3.14 AS base

ENV PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    PYTHONUNBUFFERED=1

WORKDIR /

FROM base as builder

ENV PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1

RUN apk add --no-cache gcc libffi-dev musl-dev postgresql-dev
RUN python -m venv /venv

COPY requirements.txt ./
RUN /venv/bin/pip install -r requirements.txt

FROM base AS final

COPY --from=builder /venv /venv
COPY app/ app/
CMD ["/venv/bin/uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]