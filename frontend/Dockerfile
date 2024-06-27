FROM node:latest

# COPY . .

WORKDIR /app

EXPOSE 3000

RUN npm init -y
RUN npm install http fs path url

CMD ["node", "server.js"]