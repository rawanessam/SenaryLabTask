# Development Dockerfile for frontend
FROM node:20


WORKDIR /frontend
RUN node -v

# Copy package files
COPY package*.json ./

# Install dependencies
RUN npm install --legacy-peer-deps

# Copy source code
COPY . .

# Expose port
EXPOSE 5173

# Start development server
#CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]
