import json
from pymongo import MongoClient
from datetime import datetime
import os
from dotenv import load_dotenv
from bson.objectid import ObjectId
from database.db import movies_collection, actors_collection

# Load environment variables
load_dotenv()

# MongoDB connection
MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client["Movies_DB"]
movies_collection = db["Movies"]
actors_collection = db["Actors"]

# Load JSON data
with open("data/final_data.json", "r") as file:
    movies_data = json.load(file)

# Initialize the dictionary to store actors and their movies
actors_dict = {}

# Loop over each movie in the JSON data
for movie in movies_data:
    movie_name = movie["name"]
    movie_name_cleaned = " ".join(movie_name.split(" ")[1:])  # Clean the movie name
    movie_actors = [actor.strip() for actor in movie["actors"].split(",")]

    # Find the movie in the MongoDB movies collection to get its ID
    movie_record = movies_collection.find_one({"name": movie_name_cleaned})
    if movie_record:
        movie_id = str(movie_record["_id"])  # Get the movie ID

        for actor in movie_actors:
            if actor not in actors_dict:
                actors_dict[actor] = []
            actors_dict[actor].append(movie_id)  # Add the movie ID to the actor's list

# Print the actors dictionary (for debugging purposes)
print(actors_dict)



# Insert actors into the actors collection
for actor_name, movie_ids in actors_dict.items():
    actor_data = {
        "name": actor_name,
        "movies": movie_ids
    }
    # Insert or update the actor in the collection
    existing_actor = actors_collection.find_one({"name": actor_name})
    if existing_actor:
        # Update the existing actor's movies list
        actors_collection.update_one(
            {"_id": existing_actor["_id"]},
            {"$addToSet": {"movies": {"$each": movie_ids}}}
        )
    else:
        # Insert new actor
        actors_collection.insert_one(actor_data)

print("Actors added to MongoDB successfully.")
