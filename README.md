# HMS — Full GUI


## How it works
- On first run (after DB connect), the app checks the `USERS` table.
  - If no admin exists, a **Set Up Admin** dialog opens. You pick the admin username & password.
  - The password is stored **only as a PBKDF2-SHA256 hash** in MySQL (table `USERS`). No plaintext, no secrets in code.
- On later runs, the **Admin** tab is **locked**. To unlock, log in via the **Admin (locked)** tab.
- You can **Lock Admin** any time from the Admin top bar (acts like logout).

## Install & Run
```
python -m pip install -r requirements.txt
python main.py
```
Enter your MySQL host/user/password to connect. The app creates DB `HMS` and necessary tables.

### Requirements
```
mysql-connector-python
```
Tkinter is usually included; if missing:
- Ubuntu/Debian: `sudo apt-get install python3-tk`
- MSYS2 UCRT64: `pacman -S mingw-w64-ucrt-x86_64-tk`

## Security notes
- Passwords are hashed with **PBKDF2-SHA256 (200k iterations)** with a random 128-bit salt.
- Verification is constant-time (`hmac.compare_digest`).
- You can add more roles later by inserting users into `USERS` with different `ROLE` values.

## Files
- `main.py` – launches GUI
- `gui.py` – all screens, including **Admin lock & login**
- `db.py` – DB/schema + password hashing + user management helpers
- `requirements.txt` – MySQL driver
