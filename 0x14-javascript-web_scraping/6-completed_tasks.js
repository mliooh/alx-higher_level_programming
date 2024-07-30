#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    if (response.statusCode === 200) {
      const todos = JSON.parse(body);
      const completedTasksByUser = {};

      todos.forEach((todo) => {
        if (todo.completed) {
          const userId = todo.userId;
          if (completedTasksByUser[userId]) {
            completedTasksByUser[userId]++;
          } else {
            completedTasksByUser[userId] = 1;
          }
        }
      });

      console.log('{');
      for (const userId in completedTasksByUser) {
        console.log(`'${userId}': ${completedTasksByUser[userId]}`);
      }
      console.log('}');
    } else {
      console.log(`Error: ${response.statusCode}`);
    }
  }
});