#!/usr/bin/node
const request = require('request');

const API_URL = process.argv[2];

request(API_URL, { json: true }, (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const completedTasks = new Map();

  body.forEach(task => {
    if (task.completed) {
      if (completedTasks.has(task.userId)) {
        completedTasks.set(task.userId, completedTasks.get(task.userId) + 1);
      } else {
        completedTasks.set(task.userId, 1);
      }
    }
  });
  let dict = {}
  completedTasks.forEach((count, userId) => {
    dict[userId] = count
  });
  console.log(dict)
});
