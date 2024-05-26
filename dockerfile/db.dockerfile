# Base image
FROM ubuntu:20.04

# Set working directory
WORKDIR /etc/freeradius

# Env
ENV TZ=Asia/Taipei \
    DEBIAN_FRONTEND=noninteractive

# Install FreeRadius
RUN apt-get update && \
    apt-get install -y tzdata freeradius freeradius-mysql mysql-server && \
    rm -rf /var/lib/apt/lists/*

# Copy Radius configuration files
COPY db/conf host_conf
COPY db/db_entrypoint.sh db_entrypoint.sh

# Create FreeRadius data directory (persistent volume recommended)
RUN mkdir -p /var/run/radiusd/radiusd.sock

# Expose FreeRadius port
EXPOSE 1812

# Expose SQL port
EXPOSE 3306

# Start FreeRadius service
ENTRYPOINT ["./db_entrypoint.sh"]