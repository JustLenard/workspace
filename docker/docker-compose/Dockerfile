FROM node:18-alpine as development
ENV NODE_ENV development

WORKDIR /app

COPY package.json .
COPY package-lock.json .
RUN npm i

COPY . .

EXPOSE 5173

CMD ["npm", "run", "dev"]