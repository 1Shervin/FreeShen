# FreeShen Main | Powered by ☬SHΞN™
import requests
from config import SUBSCRIPTION_LINKS
from utils import decode_subscription, extract_configs

def fetch_subscription(url):
    """Fetch content from a subscription link."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return decode_subscription(response.text)
    except Exception as e:
        print(f"Failed to fetch {url}: {e}")
        return ""

def main():
    all_configs = []
    
    # جمع‌آوری کانفیگ‌ها از لینک‌ها
    for link in SUBSCRIPTION_LINKS:
        raw_data = fetch_subscription(link)
        if raw_data:
            configs = extract_configs(raw_data)
            all_configs.extend(configs)
    
    # ذخیره کانفیگ‌ها
    with open("output/configs.txt", "w", encoding="utf-8") as f:
        for config in all_configs:
            f.write(config + "\n")
    
    print(f"Collected {len(all_configs)} configs by ☬SHΞN™")

if __name__ == "__main__":
    main()
