movie = {
    "სახელი": "Inception",
    "რეჟისორი": "Christopher Nolan",
    "წელი": 2010,
    "ჟანრები": ("Sci-Fi", "Action"),
    "მსახიობები": ["Leonardo DiCaprio", "Joseph Gordon-Levitt"]
}

print("სიგრძე:", len(movie))


director = movie["რეჟისორი"]
print("რეჟისორი:", director)

del movie["წელი"]
print(movie)

movie.clear()
print(movie)