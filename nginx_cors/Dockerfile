FROM anroe/nginx-geoip2:1.19.2-geoip2-3.3

RUN rm /etc/nginx/conf.d/default.conf
COPY ./nginx.conf ./etc/nginx/
COPY ./d_nginx.conf ./etc/nginx/conf.d/
COPY ./vhost.conf ./etc/nginx/conf.d/
COPY ./htpasswd ./etc/nginx/

EXPOSE 8001
