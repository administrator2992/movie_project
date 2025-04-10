
// search movie based on movie name at movie list
document.getElementById('searchInput').addEventListener('input', function(e) {
    // lowercase the input
    const searchTerm = e.target.value.toLowerCase();
    document.querySelectorAll('.movie-card').forEach(card => {
        // scrape title at h2 in movie-card class
        const title = card.querySelector('h2').textContent.toLowerCase();
        // show only the movie that searched or none if no any
        card.style.display = title.includes(searchTerm) ? 'block' : 'none';
    });
});