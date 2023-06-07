from services.repository import find_repositories, pull_repositories

repositories = find_repositories('/home/sneuder/Documents')
pull_repositories(repositories)