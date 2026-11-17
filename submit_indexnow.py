import json
import urllib.error
import urllib.request

# IndexNow Broadcast Configuration for Babell Group
HOST = "babellgroup.com"
KEY = "f7ad0c5492da47ea88c220edc951d408"
KEY_LOCATION = f"https://{HOST}/{KEY}.txt"

URL_LIST = [
    f"https://{HOST}/",
    f"https://{HOST}/privacy-policy/",
    f"https://{HOST}/terms-of-use/",
    f"https://{HOST}/favicon.ico?v=20261117",
    f"https://{HOST}/favicon.png",
    f"https://{HOST}/site.webmanifest?v=20261117",
    f"https://{HOST}/assets/images/babell-favicon.png",
    f"https://{HOST}/assets/images/favicon-16x16.png?v=20261117",
    f"https://{HOST}/assets/images/favicon-32x32.png?v=20261117",
    f"https://{HOST}/assets/images/favicon-48x48.png?v=20261117",
    f"https://{HOST}/assets/images/favicon-96x96.png?v=20261117",
    f"https://{HOST}/assets/images/favicon-144x144.png?v=20261117",
    f"https://{HOST}/assets/images/favicon-180x180.png?v=20261117",
    f"https://{HOST}/assets/images/favicon-192x192.png?v=20261117",
    f"https://{HOST}/assets/images/favicon-512x512.png?v=20261117",
    f"https://{HOST}/assets/images/og-babell-group.png?v=20261117",
    f"https://{HOST}/assets/images/msme-qr.png",
    f"https://{HOST}/assets/images/nihan-nihu-founder-omni-ide.png",
    f"https://{HOST}/assets/images/mohammed-nihan-founder-ceo-omniide.jpeg",
    f"https://{HOST}/assets/images/nihan-nihu-founder-ceo-omni.jpg",
    f"https://{HOST}/assets/images/mohammed-nihan-nihu-founder-omniide.jpg",
    f"https://{HOST}/sitemap.xml",
    f"https://{HOST}/robots.txt",
    f"https://{HOST}/llms.txt",
    f"https://{HOST}/llm.txt",
    f"https://{HOST}/feed.xml",
]

payload = {
    "host": HOST,
    "key": KEY,
    "keyLocation": KEY_LOCATION,
    "urlList": URL_LIST,
}

endpoints = [
    "https://api.indexnow.org/indexnow",
    "https://www.bing.com/indexnow",
    "https://yandex.com/indexnow",
]

data = json.dumps(payload).encode("utf-8")
headers = {
    "Content-Type": "application/json; charset=utf-8",
    "User-Agent": "BabellGroup-IndexNow-Broadcaster/4.0",
}

print(f"[*] Submitting {len(URL_LIST)} live canonical URLs & assets to IndexNow for '{HOST}'...")

successful = 0
for endpoint in endpoints:
    try:
        req = urllib.request.Request(endpoint, data=data, headers=headers, method="POST")
        with urllib.request.urlopen(req, timeout=15) as resp:
            status = resp.getcode()
            print(f"[+] {endpoint} -> HTTP {status} (SUCCESS)")
            successful += 1
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="ignore")
        if e.code in (200, 202):
            print(f"[+] {endpoint} -> HTTP {e.code} (SUCCESS)")
            successful += 1
        else:
            print(f"[-] {endpoint} -> HTTP {e.code}: {body[:120]}")
    except Exception as ex:
        print(f"[!] {endpoint} -> Connection Error: {ex}")

print(f"\n[+] IndexNow Broadcast complete ({successful}/{len(endpoints)} succeeded) for {HOST}.")
