# FreeShen Utilities | Crafted by ☬SHΞN™
import base64
import re

def decode_subscription(content):
    """Decode Base64-encoded subscription content if necessary."""
    try:
        # اگه محتوا Base64 باشه، دیکد می‌کنیم
        decoded = base64.b64decode(content).decode('utf-8')
        return decoded
    except:
        # اگه Base64 نبود، خود محتوا رو برمی‌گردونیم
        return content

def extract_configs(raw_data):
    """Extract Vless and Vmess configs and rename marker to FREΞ☬SHΞN™."""
    vmess_pattern = r'^vmess://[a-zA-Z0-9+/=]+'
    vless_pattern = r'^vless://[a-zA-Z0-9-]+@[\w\.:]+'
    configs = []

    for line in raw_data.splitlines():
        line = line.strip()
        if not line:
            continue
        # چک کردن اینکه کانفیگ Vless یا Vmess هست
        if re.match(vmess_pattern, line) or re.match(vless_pattern, line):
            # جدا کردن marker (بخش بعد از #)
            if '#' in line:
                config_base, _ = line.rsplit('#', 1)
                new_config = f"{config_base}#FREΞ☬SHΞN™"
            else:
                new_config = f"{line}#FREΞ☬SHΞN™"
            configs.append(new_config)
    return configs
