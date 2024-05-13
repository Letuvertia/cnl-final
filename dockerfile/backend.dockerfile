# Base image
FROM ubuntu:20.04

# Set working directory
WORKDIR /app

# Env
ENV TZ=Asia/Taipei \
    DEBIAN_FRONTEND=noninteractive

# Install Python and Flask
RUN apt-get update && \
    apt-get install -y tzdata python3 python3-pip python3-venv libmysqlclient-dev && \
    rm -rf /var/lib/apt/lists/*
RUN python3 -m venv venv && . venv/bin/activate && \
    pip install Flask SQLAlchemy pymysql gunicorn

# Expose port for backend API
EXPOSE 5000

# Start the backend API server
CMD ["/bin/bash", "-c", ". venv/bin/activate && python3 backend/main.py"]