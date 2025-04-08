# Use official Nginx image
FROM nginx:alpine

# Remove default nginx index page
RUN rm -rf /usr/share/nginx/html/*

# Copy your static files into the container
COPY index.html /usr/share/nginx/html/

# Expose port 80 for Docker Compose
EXPOSE 80
