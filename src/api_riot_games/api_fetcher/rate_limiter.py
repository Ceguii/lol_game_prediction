import time
from collections import deque

class RateLimiter:
    def __init__(self, short_limit=20, short_window=1, long_limit=100, long_window=120):
        self.short_limit = short_limit  # 20 requêtes en 1 seconde
        self.short_window = short_window
        self.long_limit = long_limit  # 100 requêtes en 2 minutes
        self.long_window = long_window

        self.short_requests = deque()
        self.long_requests = deque()

    def wait_for_slot(self):
        """ Vérifie la disponibilité d'un slot et attend si nécessaire """
        current_time = time.time()

        # Nettoyage des timestamps trop anciens
        while self.short_requests and self.short_requests[0] < current_time - self.short_window:
            self.short_requests.popleft()
        while self.long_requests and self.long_requests[0] < current_time - self.long_window:
            self.long_requests.popleft()

        # Vérification des limites
        if len(self.short_requests) >= self.short_limit:
            sleep_time = self.short_requests[0] + self.short_window - current_time
            print(f"Rate limit atteint (court terme). Pause de {sleep_time:.2f} sec...")
            time.sleep(sleep_time)

        if len(self.long_requests) >= self.long_limit:
            sleep_time = self.long_requests[0] + self.long_window - current_time
            print(f"Rate limit atteint (long terme). Pause de {sleep_time:.2f} sec...")
            time.sleep(sleep_time)

        # Ajout d'un délai intelligent entre chaque requête pour éviter la limite longue
        if len(self.long_requests) > 0:
            min_delay = self.long_window / self.long_limit  # 120 sec / 100 requêtes = 1.2 sec
            last_request_time = self.long_requests[-1]
            time_since_last_request = current_time - last_request_time

            if time_since_last_request < min_delay:
                sleep_time = min_delay - time_since_last_request
                time.sleep(sleep_time)

        # Enregistrement de la requête actuelle
        self.short_requests.append(time.time())
        self.long_requests.append(time.time())

# Initialisation du rate limiter
rate_limiter = RateLimiter()

def rate_limited_request(request_func, *args, **kwargs):
    """ Applique le rate limiter avant d'exécuter la requête """
    rate_limiter.wait_for_slot()
    return request_func(*args, **kwargs)
