import sqlite3

conn = sqlite3.connect('youtube_videos.db')

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos (
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
    )
''')

def list_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)

def add_video(name,time):
    cursor.execute("INSERT INTO videos (name,time) VALUES (?, ?)",(name,time))
    conn.commit()

def update_video(new_name,new_time,id):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?",(new_name,new_time,id))
    conn.commit()

def delete_video(id):
    cursor.execute("DELETE FROM videos WHERE id = ?",(id,))
    conn.commit()

def main():
    while True:
        print("YOUTUBE MANAGER APP WITH sqlite DB")
        print("\n1. List Videos")
        print("\n2. Add Videos")
        print("\n3. Update Videos")
        print("\n4. Delete Videos")
        print("\n5. exit app")

        choice = input("\nEnter your choice: ")

        match choice:
            case '1':
                list_videos()
            case '2':
                name = input("Enter video name:")
                time = input("Enter video time:")
                add_video(name,time)
            case '3':
                id = input("Enter video ID to be updated: ")
                name = input("Enter video name:")
                time = input("Enter video time:")
                update_video(name,time,id)
            case '4':
                id = input("Enter video ID to be deleted: ")
                delete_video(id)
            case '5':
                break
            case _:
                print("Invalid choice")

    conn.close()

if __name__ == '__main__':
    main()