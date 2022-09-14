import concurrent.futures
import requests
import threading
import time

thread_local = threading.local()

def get_session():
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()
    return thread_local.session

def download_site(url):
    session = get_session()
    response = session.get(url)
    print(f"Read {len(response.content)} from {url}")

def download_all_sites(sites):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(download_site, sites)
        print('Waiting for tasks to complete...')
    print('All tasks are done!')

if __name__ == "__main__":
    sites = [
        "https://ctd.ifsp.edu.br/",
        "https://ctd.ifsp.edu.br/index.php/cursos-2/72-tecnologia-em-analise-e-desenvolvimento-de-sistemas/140-tecnologia-em-analise-e-desenvolvimento-de-sistemas",
    ] * 80

    start_time = time.time()
    download_all_sites(sites)
    duration = time.time() - start_time
    
    print(f"Downloaded {len(sites)} in {duration} seconds")