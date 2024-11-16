#!/usr/bin/node
/**
 * Fetch and display all characters from a Star Wars movie by Movie ID.
 */

const axios = require("axios");

// Base URL of the Star Wars API
const BASE_URL = "https://swapi-api.alx-tools.com/api/films/";

// Function to fetch characters
async function fetchCharacters(movieId) {
  try {
    // Fetch movie data
    const response = await axios.get(`${BASE_URL}${movieId}/`);
    const movieData = response.data;

    // Get the character URLs
    const characterUrls = movieData.characters;

    // Fetch and print each character name
    for (const url of characterUrls) {
      const charResponse = await axios.get(url);
      console.log(charResponse.data.name);
    }
  } catch (error) {
    if (error.response && error.response.status === 404) {
      console.error(`Error: Movie with ID ${movieId} not found.`);
    } else {
      console.error("An error occurred:", error.message);
    }
  }
}

// Main execution
if (process.argv.length !== 3) {
  console.error("Usage: ./star_wars_characters.js <Movie ID>");
  process.exit(1);
}

const movieId = process.argv[2];
if (isNaN(movieId)) {
  console.error("Error: Movie ID must be a number.");
  process.exit(1);
}

fetchCharacters(movieId);
