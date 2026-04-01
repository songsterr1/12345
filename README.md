# 12345

## Fetch Data from API

`fetch.js` provides a simple utility to fetch JSON data from an external API.

### Usage

```js
const { fetchData } = require('./fetch');

fetchData('https://api.example.com/data')
  .then(data => console.log(data))
  .catch(err => console.error(err));
```
