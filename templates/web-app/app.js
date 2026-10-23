"use strict";

const input = document.querySelector("#idea");
const button = document.querySelector("#show-idea");
const result = document.querySelector("#result");

button.addEventListener("click", () => {
  const idea = input.value.trim();
  result.textContent = idea
    ? `Your starting idea: ${idea}`
    : "Enter an idea first, then try again.";
});
