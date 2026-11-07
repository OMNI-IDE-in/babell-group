import json
import urllib.request
import urllib.error

# IndexNow Broadcast Configuration for Babell Group & Subsidiaries
HOST = "babellgroup.com"
KEY = "c0379c6560934e6293901b0451cf5713"
KEY_LOCATION = f"https://{HOST}/{KEY}.txt"

URL_LIST = [
    f"https://{HOST}/",
    f"https://{HOST}/omni/",
    f"https://{HOST}/interns/",
    f"https://{HOST}/docs/",
    f"https://{HOST}/terms-of-use/",
    f"https://{HOST}/privacy-policy/",
    f"https://{HOST}/open-source-ai-coding-ide/",
    f"https://{HOST}/open-source-ai-ide/",
    f"https://{HOST}/windsurf-alternative/",
    f"https://{HOST}/assets/images/b-mark.png",
    f"https://{HOST}/assets/images/og-babell-group.png",
    f"https://{HOST}/assets/images/msme-qr.png",
    f"https://{HOST}/assets/images/nihan-nihu-founder-omni-ide.png",
    f"https://{HOST}/assets/images/mohammed-nihan-founder-ceo-omniide.jpeg",
    f"https://{HOST}/assets/images/nihan-nihu-founder-ceo-omni.jpg",
    f"https://{HOST}/assets/images/mohammed-nihan-nihu-founder-omniide.jpg",
    f"https://{HOST}/assets/images/logo.jpg",
    f"https://{HOST}/assets/images/arogya-omni-logo.png",
    f"https://{HOST}/assets/images/syncgraph-logo.jpg",
    f"https://{HOST}/assets/images/omni_rovis_icon.png",
    f"https://{HOST}/assets/images/scanai-logo.png",
    f"https://{HOST}/assets/images/mohammed-bilal.jpg",
    f"https://{HOST}/assets/images/wokspace-images/founder_ceo.jpeg",
    f"https://{HOST}/assets/images/wokspace-images/founder-ceo.jpeg",
    f"https://{HOST}/assets/images/wokspace-images/founder.jpeg",
    f"https://{HOST}/assets/images/wokspace-images/ceo_coo.jpeg",
    f"https://{HOST}/assets/images/wokspace-images/team-omni.jpeg",
    f"https://{HOST}/assets/images/wokspace-images/team.jpeg",
    f"https://{HOST}/assets/images/wokspace-images/working.jpeg",
    f"https://{HOST}/assets/images/wokspace-images/core-team.jpeg",
    f"https://{HOST}/sitemap.xml",
    f"https://{HOST}/robots.txt",
    f"https://{HOST}/llms.txt",
    f"https://{HOST}/llm.txt"
]

payload = {
    "host": HOST,
    "key": KEY,
    "keyLocation": KEY_LOCATION,
    "urlList": URL_LIST
}

endpoints = [
    "https://api.indexnow.org/indexnow",
    "https://www.bing.com/indexnow",
    "https://yandex.com/indexnow"
]

data = json.dumps(payload).encode("utf-8")
headers = {
    "Content-Type": "application/json; charset=utf-8",
    "User-Agent": "BabellGroup-IndexNow-Broadcaster/2.0"
}

print(f"[*] Submitting {len(URL_LIST)} clean canonical URLs & assets to IndexNow Network for host '{HOST}'...")

successful = 0
for endpoint in endpoints:
    try:
        req = urllib.request.Request(endpoint, data=data, headers=headers, method="POST")
        with urllib.request.urlopen(req, timeout=15) as resp:
            status = resp.getcode()
            print(f"[+] Endpoint: {endpoint} -> HTTP {status} (SUCCESS)")
            successful += 1
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="ignore")
        if e.code in [200, 202]:
            print(f"[+] Endpoint: {endpoint} -> HTTP {e.code} (SUCCESS)")
            successful += 1
        else:
            print(f"[-] Endpoint: {endpoint} -> HTTP {e.code}: {body[:120]}")
    except Exception as ex:
        print(f"[!] Endpoint: {endpoint} -> Connection Error: {ex}")

print(f"\n[+] IndexNow Broadcast configured for {HOST}.")
