import hashlib, requests, getpass

pwd    = getpass.getpass("Введите пароль (не показывается): ")
sha1   = hashlib.sha1(pwd.encode()).hexdigest().upper()
prefix, suffix = sha1[:5], sha1[5:]

resp = requests.get(f"https://api.pwnedpasswords.com/range/{prefix}", timeout=15)
resp.raise_for_status()

compromised = dict(line.split(":") for line in resp.text.splitlines())
found       = compromised.get(suffix, None)

print("⚠️ Найден в утечках!" if found else "✅ В утечках не найден.")
if found:
    print("Сколько раз встречался:", int(found))
