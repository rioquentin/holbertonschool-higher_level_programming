#!/usr/bin/node
const request = require('request');

const API_URL = 'https://jsonplaceholder.typicode.com/todos';

// Make a GET request to the API to retrieve the list of tasks
request(API_URL, { json: true }, (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  }
  // Create a Map to store the number of completed tasks for each user
  const completedTasks = new Map();

  // Loop through the tasks and count the number of completed tasks for each user
  body.forEach(task => {
    if (task.completed) {
      if (completedTasks.has(task.userId)) {
        // Increment the count for this user if they already have a count
        completedTasks.set(task.userId, completedTasks.get(task.userId) + 1);
      } else {
        // Set the initial count for this user to 1
        completedTasks.set(task.userId, 1);
      }
    }
  });
  const dict = {};
  // Print the number of completed tasks for each user
  completedTasks.forEach((count, userId) => {
    dict[userId] = count;
  });
  console.log(dict);
});
