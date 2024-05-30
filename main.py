import datetime
import os, random, time

FILE_PATH = 'README.md'
script = '''
import datetime
import os, random, time

FILE_PATH = 'README.md'

def push_to_github():
    random_number = random.randint(1, 12)
    for _ in range(random_number):
        time.sleep(3)
        current_time = str(datetime.datetime.now())
        try:
            update_file(current_time,FILE_PATH)
            os.system('git add README.md')
            commit_message = 'Commit - '+ current_time
            os.system(f'git commit -m "{commit_message}"')
            os.system(f'git push -u origin main')
            time.sleep(2)
            print("File pushed to GitHub successfully!")
        except Exception as e:
            print(f"Error: {e}")

def update_file(current_time,file_path):
    os.system('echo. > README.md')
    os.system(f'echo "*Updated at: {current_time}" >> {file_path}')

if __name__ == "__main__":
    push_to_github()
'''
def push_to_github():
    random_number = random.randint(1, 12)
    for _ in range(random_number):
        time.sleep(3)
        current_time = str(datetime.datetime.now())
        try:
            update_file(current_time,FILE_PATH)
            os.system('git add README.md')
            commit_message = 'Commit - '+ current_time
            os.system(f'git commit -m "{commit_message}"')
            os.system(f'git push -u origin main')
            time.sleep(2)
            print("File pushed to GitHub successfully!")
        except Exception as e:
            print(f"Error: {e}")

def update_file(current_time,file_path):
    os.system('echo. > README.md')
    os.system(f'echo "*Updated at: {current_time}" >> {file_path}')


if __name__ == "__main__":
    push_to_github()