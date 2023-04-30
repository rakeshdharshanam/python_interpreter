FROM node:18-alpine

WORKDIR /app

COPY . .

Run npm i axios

EXPOSE 3000

CMD [ "npm", "start"]