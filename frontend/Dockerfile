# Use official lightweight nginx image
FROM nginx:alpine

# Remove default nginx HTML
RUN rm -rf /usr/share/nginx/html/*

# Copy your static frontend into nginx web root
COPY index.html /usr/share/nginx/html/

# Expose the default web port
EXPOSE 80
