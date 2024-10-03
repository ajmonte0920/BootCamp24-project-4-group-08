const TMDB_API_KEY = ''; // Enter your TMDb API key here
const TMDB_IMAGE_BASE_URL = 'https://image.tmdb.org/t/p/w500';
let movieData = [];

// Fetch movie data from a CSV file
async function loadMovieData() {
    const response = await fetch('../Project_4_Web_app_Deployment/cleaned_movies_data.csv');
    const text = await response.text();
    // Parse the CSV data
    Papa.parse(text, {
        header: true,
        skipEmptyLines: true,
        complete: (results) => {
            movieData = results.data; // Store parsed data in movieData
        }
    });
}

// Get poster URL
async function getPosterUrl(title, year) {
    const searchUrl = `https://api.themoviedb.org/3/search/movie?api_key=${TMDB_API_KEY}&query=${encodeURIComponent(title)}&year=${year}&language=en-US&page=1&include_adult=false`;
    const response = await fetch(searchUrl);
    const data = await response.json();

    if (data.results.length > 0 && data.results[0].poster_path) {
        return TMDB_IMAGE_BASE_URL + data.results[0].poster_path;
    }
    return null;
}

// Get recommendations
function getRecommendations(title) {
    const lowerCaseTitle = title.toLowerCase().trim();
    const movieIndex = movieData.findIndex(movie => movie.Title.toLowerCase() === lowerCaseTitle);
    
    if (movieIndex === -1) {
        return "Movie title not found. Please check the spelling and try again.";
    }

    const cosineSim = computeCosineSimilarity();
    const simScores = cosineSim[movieIndex].map((score, idx) => ({ score, idx }))
        .sort((a, b) => b.score - a.score)
        .slice(1, 11); // Top 10 recommendations

    return simScores.map(({ idx }) => movieData[idx]);
}

// Compute cosine similarity (simplified example)
function computeCosineSimilarity() {
    // Implement your cosine similarity logic here
    // This is a placeholder and should return a similarity matrix based on movie descriptions and genres
    return [...Array(movieData.length)].map(() => new Array(movieData.length).fill(0));
}

// Display recommendations
function displayRecommendations(recommendations) {
    const outputDiv = document.getElementById('recommendationsOutput');
    outputDiv.innerHTML = '';

    if (typeof recommendations === 'string') {
        outputDiv.innerHTML = `<p style="color: red;">${recommendations}</p>`;
        return;
    }

    recommendations.forEach(movie => {
        const movieCard = `
            <div class="movie-card">
                <img src="${movie.Poster_URL || 'https://via.placeholder.com/200x300?text=No+Image'}" alt="${movie.Title}">
                <h3>${movie.Title}</h3>
                <p>${movie.Genres}</p>
                <p>Rating: ${movie.Rating}</p>
            </div>
        `;
        outputDiv.innerHTML += movieCard;
    });
}

// Event listener for the button
document.getElementById('recommendButton').addEventListener('click', async () => {
    const movieInput = document.getElementById('movieInput').value;
    const recommendations = getRecommendations(movieInput);
    displayRecommendations(recommendations);
});

// Load the movie data when the page loads
loadMovieData();





