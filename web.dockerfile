# Base image
FROM ubuntu:20.04

# Set working directory
WORKDIR /app

# Env
ENV TZ=Asia/Taipei \
    DEBIAN_FRONTEND=noninteractive

# Copy React app files
COPY web/frontend/ ./frontend

# Install Node.js and dependencies (for React)
RUN apt-get update && \
    apt-get install -y tzdata nodejs npm && \
    npm install -g react-scripts && \
    npm install

# Build React app for production
WORKDIR /app/frontend
RUN npm run build

# Copy Flask app files
WORKDIR /app
COPY web/backend/ ./backend

# Install Python dependencies (for Flask)
RUN apt-get update && apt-get install -y python3 python3-pip python3-venv libmysqlclient-dev && python3 -m venv venv && source venv/bin/activate && pip install Flask SQLAlchemy pymysql

# Environment variables (replace with your database details)
ENV DB_HOST=radius
ENV DB_NAME=locasync
ENV DB_USER=admin
ENV DB_PASSWORD=admin

# Expose Flask app port
EXPOSE 5000

# Create SQL database and tables and start Flask development server
CMD ["/bin/bash", "-c", "python backend/init_db.py; gunicorn --bind 0.0.0.0:5000 backend:app"]