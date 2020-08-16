FROM nginx

# Remove default nginx default conf
RUN rm /etc/nginx/conf.d/default.conf

# replace with our nginx conf
COPY nginx.conf	/etc/nginx/conf.d/
