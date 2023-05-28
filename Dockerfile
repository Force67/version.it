FROM python:3.11.3-bullseye

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./python/ /app/

ENTRYPOINT ["/bin/bash", "-c", "\
    git config --global user.email \"lovelyforce67@gmail.com\" && \
    git config --global user.name \"version-it\" && \
    git config --global credential.username \"version-it\" && \
    git config --global --add safe.directory /github/workspace && \
    python /app/version_it.py\
"]
