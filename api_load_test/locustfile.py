import random
from locust import HttpUser, task, between

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/122.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 Version/17.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 13; Pixel 6) AppleWebKit/537.36 Chrome/121.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (iPad; CPU OS 17_0 like Mac OS X) AppleWebKit/605.1.15 Version/17.0 Mobile/15E148 Safari/604.1"
]

ACCEPT_LANGUAGE_HEADERS = [
    "en-US,en;q=0.9",
    "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
    "ms-MY,ms;q=0.9,en;q=0.8",
    "en-GB,en;q=0.9",
    "ja-JP,ja;q=0.9,en-US;q=0.8,en;q=0.7"
]

SEARCH_TERMS = ["buku", "novel", "anak", "pendidikan", "komik", "promo", "diskon", "literatur"]

CATEGORIES = [
    '/categories/buku/kerajinan-hobi',
'/categories/buku/olahraga-2',
'/categories/buku/buku-masakan',
'/categories/buku/desain',
'/categories/buku/fotografi',
'/categories/buku/humor',
'/categories/buku/filsafat',
'/categories/buku/travel',
'/categories/buku/hukum',
'/categories/buku/sosial',
'/categories/buku/pengembangan-diri',
'/categories/buku/kamus',
'/categories/buku/agama',
'/categories/buku/medis',
'/categories/buku/matematika',
'/categories/buku/sains',
'/categories/buku/teknik',
'/categories/buku/keluarga',
'/categories/buku/pendidikan',
'/categories/buku/komputer-teknologi',
'/categories/buku/bisnis-ekonomi',
'/categories/buku/humaniora',
'/categories/buku/teenlit',
'/categories/buku/lain-lain-2',
'/categories/buku/home-living',
'/categories/buku/seni-pertunjukan',
'/categories/buku/seni-rupa',
'/categories/buku/sastra-1',
'/categories/buku/musik-1',
'/categories/buku/arsitektur',
'/categories/buku/benda-antik-koleksi',
'/categories/buku/perawatan-hewan-peliharaan',
'/categories/buku/novel-8',
'/categories/buku/politik-pemerintah',
'/categories/buku/perkebunan',
'/categories/buku/biografi',
'/categories/buku/puisi-1',
'/categories/buku/non-fiksi',
'/categories/buku/buku-anak',
'/categories/buku/pengembangan-diri-1',
'/categories/buku/nature',
'/categories/buku/tubuh-pikiran-jiwa',
'/categories/buku/transportasi-1',
'/categories/buku/buku-pendukung-belajar',
'/categories/buku/refrensi',
'/categories/buku/game-aktivitas',
'/categories/buku/nonfiksi-anak-remaja',
'/categories/buku/fiksi-sastra',
'/categories/buku/komik'
]

INDONESIA_IPS = [
    "103.1.156.10",
    "103.10.50.55",
    "103.25.100.120",
    "103.52.88.15",
    "103.77.22.90",
    "103.94.145.200",
    "103.114.180.30",
    "103.128.5.75",
    "103.148.200.110",
    "103.167.40.180",
    "103.194.10.25",
    "103.213.130.249",
    "103.224.80.60",
    "103.248.150.95",
    "110.138.160.5",
    "110.139.88.175",
    "114.4.20.130",
    "114.31.55.210",
    "114.108.12.45",
    "114.147.90.165",
    "116.10.30.70",
    "116.50.29.50",
    "116.88.115.235",
    "116.110.170.10",
    "118.98.20.85",
    "118.99.105.190",
    "124.81.15.115",
    "124.158.70.205",
    "125.160.5.35",
    "125.166.198.165",
    "180.248.10.20",
    "180.250.55.140",
    "182.1.200.80",
    "182.25.75.195",
    "182.253.12.65",
    "183.91.30.110",
    "183.171.145.220",
    "202.152.10.40",
    "202.158.160.100",
    "202.162.5.175",
    "202.182.35.90",
    "203.0.25.15",
    "203.11.100.125",
    "203.194.115.20",
    "203.215.60.75",
    "203.223.118.180",
    "203.235.85.5",
    "203.240.15.190",
    "203.245.20.60",
    "203.252.90.115",
    "101.50.10.5",
    "101.100.35.150",
    "101.128.70.200",
    "101.150.95.45",
    "101.170.120.230",
    "101.190.5.115",
    "101.224.30.80",
    "101.250.155.10",
    "117.102.40.60",
    "117.105.85.175",
    "117.108.120.30",
    "117.110.155.210",
    "117.115.20.95",
    "117.118.65.180",
    "117.120.90.5",
    "117.125.135.190",
    "182.0.5.25",
    "182.10.40.160",
    "182.20.75.35",
    "182.30.110.215",
    "182.40.145.80",
    "182.50.180.240",
    "182.60.5.105",
    "182.70.40.185",
    "182.80.75.50",
    "182.90.110.230",
    "182.168.5.120",
    "182.170.35.200",
    "182.180.70.65",
    "182.190.105.245",
    "182.200.140.110",
    "182.210.175.20",
    "182.220.210.180",
    "182.230.245.40",
    "182.240.10.220",
    "182.250.45.95",
    "202.146.50.70",
    "202.148.85.155",
    "202.150.120.25",
    "202.154.155.205",
    "202.160.20.80",
    "202.164.55.160",
    "202.166.90.30",
    "202.170.125.215",
    "202.172.160.90",
    "202.174.195.170",
    "202.40.10.195",
    "202.45.45.70",
    "202.50.80.250",
    "202.55.115.115",
    "202.60.150.40",
    "202.65.185.220",
    "202.70.220.95",
    "202.75.255.175"
]


class RealisticUser(HttpUser):
    wait_time = between(1, 5)  # Think time between 1-5 seconds

    def on_start(self):
        # Each simulated user has a unique session, language, and device
        self.client.headers.update({
            "User-Agent": random.choice(USER_AGENTS),
            "Accept-Language": random.choice(ACCEPT_LANGUAGE_HEADERS),
            "X-Forwarded-For": self._generate_random_ip()  # Fake IP for geo simulation
        })

    def _generate_random_ip(self):
        # Simulate users from random IPs
        return random.choice(INDONESIA_IPS)

    @task(3)
    def homepage(self):
        with self.client.get("/", name="Homepage", catch_response=True) as response:
            if response.status_code != 200:
                response.failure(f"Homepage failed with status {response.status_code}")

    @task(2)
    def visit_category(self):
        category = random.choice(CATEGORIES)
        with self.client.get(category, name="Category Page", catch_response=True) as response:
            if response.status_code != 200:
                response.failure(f"Category failed: {category}")

    @task(2)
    def search_books(self):
        term = random.choice(SEARCH_TERMS)
        with self.client.get(f"/search?query={term}", name="Search", catch_response=True) as response:
            if response.status_code != 200:
                response.failure(f"Search failed for {term}")

    @task(1)
    def slow_reader(self):
        # Simulate a user staying idle longer (like reading a book description)
        self.client.get("/")
        self.wait_time = between(5, 10)
