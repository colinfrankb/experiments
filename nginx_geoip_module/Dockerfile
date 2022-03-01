FROM anroe/nginx-geoip2:1.19.2-geoip2-3.3

RUN rm /etc/nginx/conf.d/default.conf
COPY ./nginx.conf ./etc/nginx/conf.d/
COPY ./vhost.conf ./etc/nginx/conf.d/
COPY ./GeoLite2-Country_20210928/GeoLite2-Country.mmdb ./etc/GeoLite2-Country.mmdb

EXPOSE 8001
