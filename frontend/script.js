const API_BASE = "https://openoa-27j0.onrender.com";

const output = document.getElementById("output");

async function callAPI(endpoint) {
  output.textContent = "Loading...";
  try {
    const response = await fetch(`${API_BASE}${endpoint}`);
    const data = await response.json();
    output.textContent = JSON.stringify(data, null, 2);
  } catch (error) {
    output.textContent = "Error: " + error;
  }
}

function checkHealth() {
  callAPI("/health");
}

function getVersion() {
  callAPI("/version");
}

function getModules() {
  callAPI("/modules");
}
