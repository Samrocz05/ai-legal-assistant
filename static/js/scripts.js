// script.js

function uploadDocument() {
    const fileInput = document.getElementById('fileInput');
    const file = fileInput.files[0];
    const formData = new FormData();
    formData.append('file', file);
    fetch('/upload', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('documentSummary').textContent = data.summary;
        document.querySelector('.query-section').style.display = 'block';
    });
}

function askQuestion() {
    const queryInput = document.getElementById('queryInput');
    const query = queryInput.value;
    const summary = document.getElementById('documentSummary').textContent;
    fetch('/query', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ query: query, summary: summary })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('responseText').textContent = data.response;
    });
}

document.addEventListener('DOMContentLoaded', () => {
    fetch('/directories')
    .then(response => response.json())
    .then(data => {
        const directoriesList = document.getElementById('directoriesList');
        for (const [name, url] of Object.entries(data)) {
            const listItem = document.createElement('li');
            listItem.innerHTML = `<a href="${url}" target="_blank">${name}</a>`;
            directoriesList.appendChild(listItem);
        }
    });
});
