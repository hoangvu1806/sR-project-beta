import datetime
import os, random, time

FILE_PATH = 'test2.py'

def push_to_github():
    random_number = random.randint(1, 12)
    for _ in range(random_number):
        time.sleep(3)
        current_time = str(datetime.datetime.now())
        try:
            update_file(current_time,FILE_PATH)
            os.system(f'git add {FILE_PATH}')
            commit_message = 'Commit - '+ current_time
            os.system(f'git commit -m "Update"')
            os.system(f'git push -u origin main')
            time.sleep(2)
            print("File pushed to GitHub successfully!")
        except Exception as e:
            print(f"Error: {e}")

def update_file(current_time,file_path):
    os.system(f'echo. > {file_path}')
    os.system(f"echo [print('{current_time}') for i in range(3)] >> {file_path}")


if __name__ == "__main__":
    # current_time = str(datetime.datetime.now())
    # update_file(current_time,FILE_PATH)
    push_to_github()