# Base image
FROM node:lts-hydrogen

WORKDIR /app


# Install dependency for our Vue app
COPY frontend/package.json ./
RUN npm install

# Build the Vue app
# Remember to delete the `./frontend/node_modules` folder or it will override the newly installed dependencies
COPY frontend ./
RUN npm run build

# Expose port for the Vue app
EXPOSE 5173

# Start the Vue app
CMD ["npm", "run", "dev"]