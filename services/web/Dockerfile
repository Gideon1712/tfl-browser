FROM nginx:alpine
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY index.html script.js /usr/share/nginx/html/
RUN adduser -D -u 101 appuser && chown -R appuser:appuser /var/cache/nginx /var/run /var/log/nginx /usr/share/nginx/html
USER 101
EXPOSE 8080
