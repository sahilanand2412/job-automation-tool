import pymongo
import gridfs
from pymongo import MongoClient

# MongoDB Connection
MONGO_URI = "mongodb+srv://msahilworks:test_jobApplication@users.rfvtt.mongodb.net/?retryWrites=true&w=majority&appName=users"
client = MongoClient(MONGO_URI)
db = client["job_application"]
collection = db["users"]
fs = gridfs.GridFS(db)  # GridFS for storing files

# Function to get the database and collection
def get_db():
    return db

def get_collection():
    return collection

def get_fs():
    return fs