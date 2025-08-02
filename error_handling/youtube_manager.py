import json

def load_file():
    try:
        with open('videos.txt', 'r') as file:
            file = json.load(file)
            return file
    except FileNotFoundError:
        return []
    


def add_video(videos):
    video = input('Enter video title: ')
    time = input('Enter video time: ')
    videos.append({'title': video, 'time': time})
    save_data_helper(videos)
    

def list_videos(videos):
    for index, video in enumerate(videos, start=1):
       print(f'{index}. {video["title"]} - {video["time"]}')
    print("\n")
    print("*" * 50)
    
def delete_video(videos):
    list_videos(videos)
    index = int(input('Enter video index to delete: '))
    if 1 <= index <= len(videos):
        del videos[index - 1]
        save_data_helper(videos)
        print('Video deleted successfully.')
    else:
        print('Invalid index. Please try again.')
    
def update_video(videos):
    list_videos(videos)

    index = int(input('Enter video index to update: '))
    if 1 <= index <= len(videos):
        title = input('Enter new video title: ')
        time = input('Enter new video time: ')
        videos[index - 1] = {'title': title, 'time': time}
        save_data_helper(videos)
        print('Video updated successfully.')
    else:
        print('Invalid index. Please try again.')

def save_data_helper(videos):
    try:
        with open('videos.txt', 'w') as file:
            json.dump(videos, file)
    except (IOError, OSError) as e:
        print(f"Error saving data to file: {e}")
    with open('videos.txt', 'w') as file:
        json.dump(videos, file)



def main():
    videos = load_file()
    while True:
        print('\n Youtube manager')
        print('1. add new video')
        print('2. list all videos')
        print('3. delete video')
        print('4. update video')
        print('5. exit')
        
        choice = input('Enter your choice: ')
        
        match choice:
            case '1':
                add_video(videos)
            case '2':
               list_videos(videos)
            case '3':
                delete_video(videos)
            case '4':
                update_video(videos)
            case '5':
                print('Exiting...')
                break
            case _:
                print('Invalid choice. Please try again.')
                

if __name__ == '__main__':
    main()