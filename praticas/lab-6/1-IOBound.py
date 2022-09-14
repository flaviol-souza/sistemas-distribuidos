import requests
import time

def download_site(url, session):
    response = session.get(url)
    print(f"Read {len(response.content)} from {url}")


def download_all_sites(sites):
    session = requests.Session()
    for url in sites:
        download_site(url, session)

if __name__ == "__main__":
    sites = [
        "https://ctd.ifsp.edu.br/",
        "https://ctd.ifsp.edu.br/index.php/cursos-2/72-tecnologia-em-analise-e-desenvolvimento-de-sistemas/140-tecnologia-em-analise-e-desenvolvimento-de-sistemas",
    ] * 80
    
    start_time = time.time()
    download_all_sites(sites)
    duration = time.time() - start_time
    
    print(f"Downloaded {len(sites)} in {duration} seconds")