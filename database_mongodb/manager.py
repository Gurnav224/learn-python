from pymongo import MongoClient
from bson import ObjectId


client = MongoClient(
    "",
)

db = client["youtube_manager_db"]


videos_collection = db["videos"]

print(f"database name: {videos_collection.database.name}")
print(f"collection name: {videos_collection.name}")

def add_video(title, time):
    videos_collection.insert_one({"title": title, "time": time})
    print("new video inserted successfully")


def list_videos():
    videos = videos_collection.find()

    for video in videos:
        print(f"_id: {video['_id']}, title: {video['title']}, time: {video['time']}")


def update_video(video_id, title, time):
    result = videos_collection.update_one(
        {"_id": ObjectId(video_id)}, {"$set": {"title": title, "time": time}}
    )
    if result.matched_count == 0:
        print("❌ No document found with that id")
    elif result.modified_count == 0:
        print("⚠️ Document found but nothing was updated (same values?)")
    else:
        print("✅ Video updated successfully")


def delete_video(video_id):
    videos_collection.delete_one({"_id": ObjectId(video_id)})
    print("✅  video deleted successfully")


def main():
    while True:
        print("Youtube Manager with Mongodb ")
        print("1 . Add new video")
        print("2. list all the videos")
        print("3. upate the video ")
        print("4. delete the video ")
        print("5. Exiting")

        choice = input("Enter your choice : ")

        match choice:
            case "1":
                title = input("enter video title: ")
                time = input("enter video time: ")

                add_video(title, time)
            case "2":
                list_videos()
            case "3":
                video_id = input("enter video id: ")
                title = input("enter video title: ")
                time = input("enter video time: ")
                update_video(video_id, title, time)
            case "4":
                video_id = input("enter video id: ")

                delete_video(video_id)
            case "5":
                break
            case _:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
