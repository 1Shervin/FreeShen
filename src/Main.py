# FreeShen Main | Powered by ☬SHΞN™
import requests
from .config import SUBSCRIPTION_LINKS  # تغییر نحوه ایمپورت با اضافه کردن نقطه (.)
from .utils import decode_subscription, extract_configs  # همین تغییر برای utils

def fetch_subscription(url):
    """Fetch content from a subscription link."""
    print(f"Fetching URL: {url}")
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        content = decode_subscription(response.text)
        print(f"Content fetched: {content[:100]}...")  # فقط 100 کاراکتر اول برای لاگ
        return content
    except Exception as e:
        print(f"Failed to fetch {url}: {e}")
        return ""

def fetch_and_process_links(master_url):
    """Fetch a master link containing other subscription links and process them."""
    content = fetch_subscription(master_url)
    if not content:
        return []
    
    # فرض می‌کنیم محتوا یه لیست از لینک‌ها باشه (هر خط یه لینک)
    links = [line.strip() for line in content.splitlines() if line.strip()]
    print(f"Found {len(links)} links in {master_url}")
    all_configs = []

    for link in links:
        # فقط لینک‌هایی که http یا https دارن رو پردازش می‌کنیم
        if link.startswith("http://") or link.startswith("https://"):
            raw_data = fetch_subscription(link)
            if raw_data:
                configs = extract_configs(raw_data)
                print(f"Extracted {len(configs)} configs from {link}")
                all_configs.extend(configs)
    
    return all_configs

def main():
    all_configs = []
    
    # پردازش لینک‌های سابسکریپشن
    for link in SUBSCRIPTION_LINKS:
        configs = fetch_and_process_links(link)
        all_configs.extend(configs)
    
    # ذخیره کانفیگ‌ها
    with open("../output/configs.txt", "w", encoding="utf-8") as f:
        for config in all_configs:
            f.write(config + "\n")
    
    # ساخت لینک سابسکریپشن مادر
    subscription_data = "\n".join(all_configs)
    with open("../output/subscription.txt", "w", encoding="utf-8") as f:
        f.write(subscription_data)
    
    print(f"Total: Collected {len(all_configs)} configs by ☬SHΞN™")

if __name__ == "__main__":
    main()
