from config.global_config import CONFIG

def log(msg):
    if CONFIG.debug:
        print(f"[LOG] {msg}")
