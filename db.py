import mysql.connector
import os, hashlib, hmac, binascii

# ---------------- Password hashing (no external deps) ---------------- #
def _pbkdf2_hash(password: str, salt_hex: str | None = None, iterations: int = 200_000) -> str:
    if salt_hex is None:
        salt = os.urandom(16)
    else:
        salt = binascii.unhexlify(salt_hex)
    dk = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, iterations)
    return f"pbkdf2_sha256${iterations}${binascii.hexlify(salt).decode()}${binascii.hexlify(dk).decode()}"

def verify_password(password: str, stored: str) -> bool:
    try:
        alg, iter_str, salt_hex, hash_hex = stored.split('$', 3)
        if alg != 'pbkdf2_sha256':
            return False
        iterations = int(iter_str)
        candidate = _pbkdf2_hash(password, salt_hex, iterations)
        # constant-time compare
        return hmac.compare_digest(candidate, stored)
    except Exception:
        return False

# ---------------- DB connection and schema ---------------- #
def get_connection(user, password, host="localhost", database="HMS"):
    c = mysql.connector.connect(host=host, user=user, passwd=password)
    cur = c.cursor()
    cur.execute("CREATE DATABASE IF NOT EXISTS HMS")
    cur.execute("COMMIT")
    c.close()
    conn = mysql.connector.connect(host=host, user=user, passwd=password, database=database)
    return conn

def create_tables(conn):
    cur = conn.cursor()
    cur.execute("USE HMS")
    cur.execute("""CREATE TABLE IF NOT EXISTS C_DETAILS(
        CID VARCHAR(20) PRIMARY KEY,
        C_NAME VARCHAR(30),
        C_ADDRESS VARCHAR(60),
        C_AGE VARCHAR(10),
        C_COUNTRY VARCHAR(30),
        P_NO VARCHAR(15),
        C_EMAIL VARCHAR(60)
    )""")
    cur.execute("""CREATE TABLE IF NOT EXISTS ROOMS(
        R_NO VARCHAR(20) PRIMARY KEY,
        ROOM_TYPE VARCHAR(30),
        COST INT,
        STATUS VARCHAR(1)
    )""")
    cur.execute("""CREATE TABLE IF NOT EXISTS ROOM_RENT(
        CID VARCHAR(20) PRIMARY KEY,
        CHECK_IN DATE,
        CHECK_OUT DATE,
        ROOM_QUALITY VARCHAR(30),
        NO_OF_DAYS INT,
        ROOMNO VARCHAR(20),
        ROOMRENT INT
    )""")
    cur.execute("""CREATE TABLE IF NOT EXISTS FOOD(
        ID VARCHAR(20) PRIMARY KEY,
        CUISINE_TYPE VARCHAR(30),
        CUISINE VARCHAR(30),
        COST INT
    )""")
    cur.execute("""CREATE TABLE IF NOT EXISTS RESTAURENT(
        ORDER_NO VARCHAR(20) PRIMARY KEY,
        CID VARCHAR(20),
        CUISINE_CHOICE VARCHAR(30),
        CUISINE VARCHAR(30),
        QUANTITY INT,
        BILL INT
    )""")
    cur.execute("""CREATE TABLE IF NOT EXISTS FASHION(
        ORDER_NO VARCHAR(20) PRIMARY KEY,
        CID VARCHAR(20),
        DRESS_CHOICE VARCHAR(30),
        DRESS VARCHAR(30),
        AMOUNT INT,
        BILL INT
    )""")
    cur.execute("""CREATE TABLE IF NOT EXISTS GAMING(
        ORDER_NO VARCHAR(20) PRIMARY KEY,
        CID VARCHAR(20),
        GAME_CHOICE VARCHAR(30),
        GAMES VARCHAR(30),
        HOURS INT,
        GAMING_BILL INT
    )""")
    cur.execute("""CREATE TABLE IF NOT EXISTS TOTAL(
        CID VARCHAR(20) PRIMARY KEY,
        C_NAME VARCHAR(30),
        ROOMRENT INT,
        RESTAURENTBILL INT,
        GAMINGBILL INT,
        FASHIONBILL INT,
        TOTALAMOUNT INT
    )""")
    # Users table for app-level auth (no secrets in code)
    cur.execute("""CREATE TABLE IF NOT EXISTS USERS(
        USERNAME VARCHAR(50) PRIMARY KEY,
        ROLE VARCHAR(20),
        PASSWORD_HASH VARCHAR(255),
        CREATED_AT TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )""")
    cur.execute("COMMIT")
    cur.close()

# ---------------- Query helper ---------------- #
def q(conn, sql, params=None, fetch=False, many=False):
    try:
        cur = conn.cursor()
        if many:
            cur.executemany(sql, params or [])
        else:
            cur.execute(sql, params or ())
        if fetch:
            rows = cur.fetchall()
            cur.close()
            return rows
        cur.execute("COMMIT")
        cur.close()
        return None
    except Exception:
        try:
            cur.close()
        except Exception:
            pass
        print("Operation failed.")
        return [] if fetch else None

# ---------------- App auth helpers ---------------- #
def admin_exists(conn) -> bool:
    rows = q(conn, "SELECT COUNT(*) FROM USERS WHERE ROLE='admin'", fetch=True)
    try:
        return rows and int(rows[0][0]) > 0
    except Exception:
        return False

def create_user(conn, username: str, role: str, password: str) -> bool:
    try:
        if not username or not role or not password:
            return False
        if q(conn, "SELECT USERNAME FROM USERS WHERE USERNAME=%s", (username,), fetch=True):
            return False
        ph = _pbkdf2_hash(password)
        q(conn, "INSERT INTO USERS(USERNAME,ROLE,PASSWORD_HASH) VALUES(%s,%s,%s)", (username, role, ph))
        return True
    except Exception:
        return False

def verify_user(conn, username: str, password: str, role: str | None = None) -> bool:
    try:
        if not username or not password:
            return False
        rows = q(conn, "SELECT PASSWORD_HASH,ROLE FROM USERS WHERE USERNAME=%s", (username,), fetch=True)
        if not rows:
            return False
        stored, r = rows[0]
        if role and r != role:
            return False
        return verify_password(password, stored)
    except Exception:
        return False
