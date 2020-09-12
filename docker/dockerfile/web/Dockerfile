# Build React app
FROM node:14.7.0-alpine3.10 as react-builder

WORKDIR /app

COPY ./web/ .

RUN yarn

EXPOSE 3000

RUN  yarn build

# Nginx Build
FROM nginx:alpine

# Erase Default config
RUN rm -rf /etc/nginx/conf.d

COPY ./web/conf /etc/nginx

WORKDIR /usr/share/nginx/html

COPY --from=react-builder /app/build /usr/share/nginx/html

EXPOSE 80

CMD ["/usr/sbin/nginx"]