import os
import subprocess

def is_repository(path):
  try:
    result = subprocess.run(['git', '-C', path, 'rev-parse', '--is-inside-work-tree'], capture_output=True)
    return result.returncode == 0 and result.stdout.strip() == b'true'
  except:
    return False
  
def find_repositories(folder):
    repositories = []
    no_directories = []

    for directory in os.listdir(folder):
        path = os.path.join(folder, directory)
        
        if os.path.isdir(path) and is_repository(path):
            repositories.append(path)
        else:
          no_directories.append(directory)

    if no_directories:
      for no_directory in no_directories:
        new_folder = os.path.join(folder, no_directory)
        repositories.extend(find_repositories(new_folder))
      
    return repositories

def pull_repositories(repositories):
  for repository in repositories:
    os.chdir(repository)
    print(repository)
    subprocess.run(['git', 'pull', '--all'])