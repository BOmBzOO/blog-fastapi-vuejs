FROM node:lts-alpine

WORKDIR /home/app/frontend

COPY package*.json ./

# RUN npm install
RUN yarn install

EXPOSE 8080

# CMD ["npm", "run", "serve"]
CMD ["yarn", "run", "serve"]