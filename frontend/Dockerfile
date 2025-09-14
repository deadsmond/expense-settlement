FROM node:18-alpine AS builder
WORKDIR /app
COPY . .
RUN yarn install && yarn build

FROM nginx:alpine
COPY --from=builder /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/nginx.conf
