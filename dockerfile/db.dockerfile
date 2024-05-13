# Base image
FROM ubuntu:20.04

# Set working directory
WORKDIR /etc/freeradius

# Env
ENV TZ=Asia/Taipei \
    DEBIAN_FRONTEND=noninteractive

# Install FreeRadius
RUN apt-get update && \
    apt-get install -y tzdata freeradius freeradius-mysql

# Copy Radius configuration files
COPY db db

# Create FreeRadius data directory (persistent volume recommended)
RUN mkdir -p /var/run/radiusd/radiusd.sock

# Expose FreeRadius port
EXPOSE 1812

# Start FreeRadius service
CMD ["/bin/bash", "-c", "freeradius -s default"]