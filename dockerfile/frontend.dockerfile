# Base image
FROM ubuntu:20.04

# Set working directory
WORKDIR /app

# Env
ENV TZ=Asia/Taipei \
    DEBIAN_FRONTEND=noninteractive

# Install Node.js
RUN apt-get update && \
    apt-get install -y tzdata nodejs npm

# Install dependency for our Vue app
COPY ./frontend/package*.json ./
RUN npm install

# Build the Vue app
COPY ./frontend .
RUN npm run build

# Expose port for the Vue app
EXPOSE 5173

# Start the Vue app
CMD ["/bin/bash", "-c", "npm run dev"]