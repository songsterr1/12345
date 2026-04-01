/**
 * Fetch data from an external API.
 * @param {string} url - The URL to fetch data from.
 * @returns {Promise<any>} The parsed JSON response.
 */
async function fetchData(url) {
  const response = await fetch(url);
  if (!response.ok) {
    throw new Error(`HTTP error ${response.status} (${response.statusText}) when fetching ${url}`);
  }
  return response.json();
}

module.exports = { fetchData };
