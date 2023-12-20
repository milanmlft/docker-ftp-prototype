FROM python:3.10.6-slim-bullseye
SHELL ["/bin/bash", "-o", "pipefail", "-e", "-u", "-x", "-c"]

WORKDIR /app
COPY uploader/pyproject.toml /app/
RUN pip install -e .
COPY uploader/upload.py /app/
COPY uploader/public.zip /app/data/

CMD ["python3", "upload.py"]