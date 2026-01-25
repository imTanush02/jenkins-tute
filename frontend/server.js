const express = require('express');
const axios = require('axios');
const path = require('path');
const app = express();
const PORT = 3000;

// Middleware
app.use(express.static('public'));
app.use(express.json());

// Serve the HTML file
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

// Proxy endpoint to fetch characters from Flask backend
app.get('/api/characters', async (req, res) => {
    try {
        const response = await axios.get('http://localhost:5000/api/characters');
        res.json(response.data);
    } catch (error) {
        console.error('Error fetching characters:', error);
        res.status(500).json({ error: 'Failed to fetch characters' });
    }
});

app.listen(PORT, () => {
    console.log(`Express server running on http://localhost:${PORT}`);
});
