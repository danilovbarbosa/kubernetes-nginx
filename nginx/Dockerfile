FROM nginx

# COPY files
COPY nginx.conf /etc/nginx/conf.d/nginx.conf
COPY load-balancer.conf /etc/nginx/conf.d/load-balancer.conf

RUN nginx -t

# Define working directory.
WORKDIR /etc/nginx

# Expose ports.
EXPOSE 80
EXPOSE 443