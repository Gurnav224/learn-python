import sqlite3

connection = sqlite3.connect("manager.db")

cursor = connection.cursor()


cursor.execute(
    "CREATE TABLE IF NOT EXISTS videos (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, time TEXT)"
)


def add_video(title, time):
    cursor.execute("INSERT INTO videos (title, time) VALUES (?,?)", (title, time))
    connection.commit()
    print("\nVideo added successfully\n")


def list_videos():
    cursor.execute("SELECT * FROM videos")
    videos = cursor.fetchall()
    print("\n List of videos: \n")
    print("*" * 50)
    for video in videos:
        print(f"ID: {video[0]}, Title: {video[1]}, Time: {video[2]}")
    print("*" * 50)

def update_video(video_id, title, time):
    cursor.execute("UPDATE videos SET title =?, time =? WHERE id =?", (title, time, video_id))
    connection.commit()
    
    if cursor.rowcount == 0:
        print(f"\n No video found with ID {video_id}. No update performed. \n")
    else:
        print("\n Video updated successfully \n")

def delete_video():
    video_id = int(input("Enter the ID of the video to delete: "))
    cursor.execute("DELETE FROM videos WHERE id =?", (video_id,))
    connection.commit()
    print("\n Video deleted successfully \n")

def main():
    while True:
        print("\nyoutube video manager with db\n")
        print("1. add new video")
        print("2. list all the videos")
        print("3. update the video")
        print("4. delete the video")
        print("5.exiting")

        choice = input("enter your choice: ")

        match choice:
            case "1":
                title = input("Enter the title of the video: ")
                time = input("Enter the time of the video: ")
                add_video(title, time)
            case "2":
                list_videos()
            case "3":
                video_id = int(input("Enter the ID of the video to update: "))
                title = input("Enter the new title of the video: ")
                time = input("Enter the new time of the video: ")
                update_video(video_id, title, time)
            case "4":
                delete_video()
            case "5":
                break
            case _:
                print("invalid input choice")

    connection.close()


if __name__ == "__main__":
    main()
    