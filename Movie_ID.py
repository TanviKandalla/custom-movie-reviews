import csv
import tmdbsimple as tmdb

# Set your TMDB API key here
tmdb.API_KEY = 'c9d551e739a762e86e3188ff857ed627'

# Open the CSV file containing movie titles
with open('Movies.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # skip the header row
    # Open a new CSV file to write the movie titles and IDs
    with open('movie_ids.csv', 'w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(['Title', 'ID'])  # write the header row
        # Loop through each row of the input CSV file
        for row in reader:
            title = row[0]
            try:
                # Search for the movie by title using the TMDB API
                search = tmdb.Search()
                response = search.movie(query=title)
                # Get the first search result (most relevant) and its ID
                movie_id = response['results'][0]['id']
                writer.writerow([title, movie_id])  # write the title and ID to the output CSV file
            except:
                print(f"Could not find ID for movie: {title}")
