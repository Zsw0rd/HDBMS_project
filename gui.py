import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from db import get_connection, create_tables, q, admin_exists, create_user, verify_user

GAMING_NAMES = {1:"Table Tennis",2:"Bowling",3:"Cart Racing",4:"VR Gaming",5:"Video Games",6:"Swimming Pool Games"}
GAMING_RATES = {1:150,2:100,3:250,4:400,5:300,6:350}

FASHION_NAMES = {1:"Shirts",2:"T-Shirts",3:"Pants",4:"Jeans",5:"Tassel top",6:"Gown",7:"Western dress",8:"Skirts",9:"Trousers",10:"InnerWear"}
FASHION_RATES = {1:1500,2:300,3:2000,4:4000,5:500,6:3000,7:3000,8:400,9:200,10:30}

def is_int(s, minval=None, maxval=None):
    try:
        v = int(s)
        if minval is not None and v < minval: return False
        if maxval is not None and v > maxval: return False
        return True
    except Exception:
        return False

def parse_date(s):
    try:
        return datetime.strptime(s, "%Y-%m-%d").date()
    except Exception:
        return None

class LoginFrame(ttk.Frame):
    def __init__(self, master, on_connected):
        super().__init__(master, padding=16)
        self.on_connected = on_connected
        ttk.Label(self, text="MySQL host").grid(row=0, column=0, sticky="w")
        ttk.Label(self, text="User").grid(row=1, column=0, sticky="w")
        ttk.Label(self, text="Password").grid(row=2, column=0, sticky="w")

        self.host = ttk.Entry(self); self.host.insert(0, "localhost")
        self.user = ttk.Entry(self)
        self.pw = ttk.Entry(self, show="*")

        self.host.grid(row=0, column=1, sticky="ew", padx=8, pady=4)
        self.user.grid(row=1, column=1, sticky="ew", padx=8, pady=4)
        self.pw.grid(row=2, column=1, sticky="ew", padx=8, pady=4)

        self.btn = ttk.Button(self, text="Connect", command=self.connect)
        self.btn.grid(row=3, column=0, columnspan=2, pady=8, sticky="ew")
        self.status = ttk.Label(self, text="", foreground="red")
        self.status.grid(row=4, column=0, columnspan=2, sticky="w")

        self.columnconfigure(1, weight=1)

    def connect(self):
        try:
            conn = get_connection(user=self.user.get().strip(), password=self.pw.get(), host=self.host.get().strip() or "localhost")
            create_tables(conn)
            self.on_connected(conn)
        except Exception:
            self.status.config(text="Invalid credentials or server unreachable.")

class SetupAdminDialog(tk.Toplevel):
    def __init__(self, master, conn, on_done):
        super().__init__(master)
        self.conn = conn
        self.on_done = on_done
        self.title("Set Up Admin")
        self.resizable(False, False)
        frm = ttk.Frame(self, padding=12); frm.pack(fill="both", expand=True)
        ttk.Label(frm, text="Create the first admin account").grid(row=0, column=0, columnspan=2, pady=(0,8))
        ttk.Label(frm, text="Username").grid(row=1, column=0, sticky="w"); self.u = ttk.Entry(frm, width=28); self.u.grid(row=1, column=1, padx=6, pady=4)
        ttk.Label(frm, text="Password").grid(row=2, column=0, sticky="w"); self.p = ttk.Entry(frm, show="*", width=28); self.p.grid(row=2, column=1, padx=6, pady=4)
        ttk.Label(frm, text="Confirm").grid(row=3, column=0, sticky="w"); self.c = ttk.Entry(frm, show="*", width=28); self.c.grid(row=3, column=1, padx=6, pady=4)
        self.msg = ttk.Label(frm, text="", foreground="red"); self.msg.grid(row=4, column=0, columnspan=2, sticky="w")
        btn = ttk.Button(frm, text="Create", command=self._create); btn.grid(row=5, column=0, columnspan=2, sticky="ew", pady=8)
        self.grab_set(); self.u.focus_set()

    def _create(self):
        try:
            u = self.u.get().strip()
            p = self.p.get()
            c = self.c.get()
            if not u or not p or p != c or len(p) < 6:
                self.msg.config(text="Invalid input. Passwords must match and be ≥ 6 chars.")
                return
            if create_user(self.conn, u, "admin", p):
                messagebox.showinfo("Done", "Admin created.")
                self.destroy(); self.on_done()
            else:
                self.msg.config(text="Could not create admin (maybe username exists).")
        except Exception:
            self.msg.config(text="Something went wrong.")

class AdminLoginFrame(ttk.Frame):
    def __init__(self, master, conn, on_unlock):
        super().__init__(master, padding=16)
        self.conn = conn
        self.on_unlock = on_unlock
        ttk.Label(self, text="Admin Login", font=("TkDefaultFont", 11, "bold")).grid(row=0, column=0, columnspan=2, pady=(0,8))
        ttk.Label(self, text="Username").grid(row=1, column=0, sticky="w"); self.u = ttk.Entry(self, width=24); self.u.grid(row=1, column=1, padx=6, pady=4)
        ttk.Label(self, text="Password").grid(row=2, column=0, sticky="w"); self.p = ttk.Entry(self, show="*", width=24); self.p.grid(row=2, column=1, padx=6, pady=4)
        self.msg = ttk.Label(self, text="", foreground="red"); self.msg.grid(row=3, column=0, columnspan=2, sticky="w")
        ttk.Button(self, text="Unlock Admin", command=self._login).grid(row=4, column=0, columnspan=2, sticky="ew", pady=6)

    def _login(self):
        try:
            u = self.u.get().strip(); p = self.p.get()
            if verify_user(self.conn, u, p, role="admin"):
                self.on_unlock()
            else:
                self.msg.config(text="Invalid credentials.")
        except Exception:
            self.msg.config(text="Something went wrong.")

# ------------------ App Tabs (Customer + Admin) ------------------ #
class CustomerTab(ttk.Frame):
    def __init__(self, master, conn):
        super().__init__(master, padding=8)
        self.conn = conn
        nb = ttk.Notebook(self)
        nb.pack(fill="both", expand=True)

        self.profile = ttk.Frame(nb, padding=8)
        self.booking = ttk.Frame(nb, padding=8)
        self.food = ttk.Frame(nb, padding=8)
        self.gaming = ttk.Frame(nb, padding=8)
        self.fashion = ttk.Frame(nb, padding=8)
        self.bills = ttk.Frame(nb, padding=8)
        self.checkout = ttk.Frame(nb, padding=8)

        nb.add(self.profile, text="Profile")
        nb.add(self.booking, text="Book Room")
        nb.add(self.food, text="Order Food")
        nb.add(self.gaming, text="Gaming")
        nb.add(self.fashion, text="Fashion")
        nb.add(self.bills, text="View Bills")
        nb.add(self.checkout, text="Checkout")

        self._build_profile()
        self._build_booking()
        self._build_food()
        self._build_gaming()
        self._build_fashion()
        self._build_bills()
        self._build_checkout()

    def _err(self): messagebox.showerror("Error", "Invalid input or operation failed.")

    # Profile
    def _build_profile(self):
        f = self.profile
        labels = ["CID","Name","Address","Age","Country","Phone","Email"]
        self.p_entries = {}
        for i, lbl in enumerate(labels):
            ttk.Label(f, text=lbl).grid(row=i, column=0, sticky="w")
            e = ttk.Entry(f, width=40); e.grid(row=i, column=1, sticky="ew", padx=8, pady=2)
            self.p_entries[lbl] = e
        f.columnconfigure(1, weight=1)
        ttk.Button(f, text="Save (Insert/Update)", command=self._save_profile).grid(row=len(labels), column=0, columnspan=2, pady=8, sticky="ew")

    def _save_profile(self):
        try:
            vals = {k:self.p_entries[k].get().strip() for k in self.p_entries}
            if not vals["CID"]:
                self._err(); return
            exists = q(self.conn, "SELECT CID FROM C_DETAILS WHERE CID=%s", (vals["CID"],), fetch=True)
            if exists:
                q(self.conn, "UPDATE C_DETAILS SET C_NAME=%s,C_ADDRESS=%s,C_AGE=%s,C_COUNTRY=%s,P_NO=%s,C_EMAIL=%s WHERE CID=%s",
                  (vals["Name"], vals["Address"], vals["Age"], vals["Country"], vals["Phone"], vals["Email"], vals["CID"]))
            else:
                q(self.conn, "INSERT INTO C_DETAILS VALUES(%s,%s,%s,%s,%s,%s,%s)",
                  (vals["CID"], vals["Name"], vals["Address"], vals["Age"], vals["Country"], vals["Phone"], vals["Email"]))
            messagebox.showinfo("Saved","Profile saved.")
        except Exception:
            self._err()

    # Booking
    def _build_booking(self):
        f = self.booking
        top = ttk.Frame(f); top.pack(fill="x")
        ttk.Label(top, text="CID").pack(side="left")
        self.b_cid = ttk.Entry(top, width=18); self.b_cid.pack(side="left", padx=6)
        ttk.Button(top, text="Load Free Rooms", command=self._load_rooms).pack(side="left")

        mid = ttk.Frame(f); mid.pack(fill="both", expand=True, pady=8)
        cols = ("R_NO","ROOM_TYPE","COST")
        self.rooms = ttk.Treeview(mid, columns=cols, show="headings", height=8)
        for c in cols: self.rooms.heading(c, text=c); self.rooms.column(c, width=120, anchor="center")
        vs = ttk.Scrollbar(mid, orient="vertical", command=self.rooms.yview)
        self.rooms.configure(yscroll=vs.set)
        self.rooms.pack(side="left", fill="both", expand=True)
        vs.pack(side="left", fill="y")

        bot = ttk.Frame(f); bot.pack(fill="x")
        ttk.Label(bot, text="Check-in YYYY-MM-DD").pack(side="left")
        self.in_date = ttk.Entry(bot, width=14); self.in_date.pack(side="left", padx=6)
        ttk.Label(bot, text="Check-out YYYY-MM-DD").pack(side="left")
        self.out_date = ttk.Entry(bot, width=14); self.out_date.pack(side="left", padx=6)
        ttk.Button(bot, text="Book Selected Room", command=self._book_selected).pack(side="right")

    def _load_rooms(self):
        try:
            for i in self.rooms.get_children(): self.rooms.delete(i)
            rows = q(self.conn, "SELECT R_NO,ROOM_TYPE,COST FROM ROOMS WHERE STATUS='F' ORDER BY ROOM_TYPE,COST", fetch=True)
            for r in rows:
                self.rooms.insert("", "end", values=r)
        except Exception:
            self._err()

    def _book_selected(self):
        try:
            cid = self.b_cid.get().strip()
            if not cid: self._err(); return
            exist = q(self.conn, "SELECT CID FROM C_DETAILS WHERE CID=%s", (cid,), fetch=True)
            if not exist: self._err(); return
            if q(self.conn, "SELECT CID FROM ROOM_RENT WHERE CID=%s", (cid,), fetch=True):
                self._err(); return
            sel = self.rooms.selection()
            if not sel: self._err(); return
            rno, rtype, cost = self.rooms.item(sel[0], "values")
            d1 = parse_date(self.in_date.get().strip()); d2 = parse_date(self.out_date.get().strip())
            if not d1 or not d2 or d2 <= d1: self._err(); return
            days = (d2 - d1).days
            rent = days * int(cost)
            q(self.conn, "INSERT INTO ROOM_RENT VALUES(%s,%s,%s,%s,%s,%s,%s)", (cid, d1, d2, rtype, days, rno, rent))
            q(self.conn, "UPDATE ROOMS SET STATUS='O' WHERE R_NO=%s", (rno,))
            messagebox.showinfo("Booked", f"Room {rno} booked. Bill: {rent}")
        except Exception:
            self._err()

    # Food
    def _build_food(self):
        f = self.food
        top = ttk.Frame(f); top.pack(fill="x")
        ttk.Label(top, text="CID").pack(side="left")
        self.f_cid = ttk.Entry(top, width=18); self.f_cid.pack(side="left", padx=6)
        ttk.Button(top, text="Load Menu", command=self._load_menu).pack(side="left")
        ttk.Label(top, text="Order No").pack(side="left", padx=8)
        self.oid = ttk.Entry(top, width=16); self.oid.pack(side="left")
        ttk.Label(top, text="Food ID").pack(side="left", padx=8)
        self.fid = ttk.Entry(top, width=12); self.fid.pack(side="left")
        ttk.Label(top, text="Qty").pack(side="left", padx=8)
        self.qty = ttk.Entry(top, width=6); self.qty.pack(side="left")
        ttk.Button(top, text="Place Order", command=self._place_order).pack(side="right")

        mid = ttk.Frame(f); mid.pack(fill="both", expand=True, pady=8)
        cols = ("ID","TYPE","CUISINE","COST")
        self.menu = ttk.Treeview(mid, columns=cols, show="headings", height=8)
        for c in cols: self.menu.heading(c, text=c); self.menu.column(c, width=120, anchor="center")
        vs = ttk.Scrollbar(mid, orient="vertical", command=self.menu.yview)
        self.menu.configure(yscroll=vs.set)
        self.menu.pack(side="left", fill="both", expand=True)
        vs.pack(side="left", fill="y")

    def _load_menu(self):
        try:
            for i in self.menu.get_children(): self.menu.delete(i)
            rows = q(self.conn, "SELECT ID,CUISINE_TYPE,CUISINE,COST FROM FOOD ORDER BY CUISINE_TYPE,ID", fetch=True)
            for r in rows: self.menu.insert("", "end", values=r)
        except Exception:
            self._err()

    def _place_order(self):
        try:
            cid = self.f_cid.get().strip()
            if not cid: self._err(); return
            if not q(self.conn, "SELECT CID FROM ROOM_RENT WHERE CID=%s", (cid,), fetch=True): self._err(); return
            oid = self.oid.get().strip(); fid = self.fid.get().strip()
            if not oid or not fid: self._err(); return
            if q(self.conn, "SELECT ORDER_NO FROM RESTAURENT WHERE ORDER_NO=%s", (oid,), fetch=True): self._err(); return
            f = q(self.conn, "SELECT CUISINE_TYPE,CUISINE,COST FROM FOOD WHERE ID=%s", (fid,), fetch=True)
            if not f: self._err(); return
            qty = self.qty.get().strip()
            if not is_int(qty, 1): self._err(); return
            typ, item, cost = f[0]; bill = int(cost) * int(qty)
            q(self.conn, "INSERT INTO RESTAURENT VALUES(%s,%s,%s,%s,%s,%s)", (oid, cid, typ, item, int(qty), bill))
            messagebox.showinfo("Order", f"{item} x{qty} bill {bill}")
        except Exception:
            self._err()

    # Gaming
    def _build_gaming(self):
        f = self.gaming
        top = ttk.Frame(f); top.pack(fill="x")
        ttk.Label(top, text="CID").pack(side="left")
        self.g_cid = ttk.Entry(top, width=18); self.g_cid.pack(side="left", padx=6)
        ttk.Label(top, text="Order No").pack(side="left", padx=8)
        self.g_oid = ttk.Entry(top, width=16); self.g_oid.pack(side="left")
        ttk.Label(top, text="Game").pack(side="left", padx=8)
        self.g_choice = ttk.Combobox(top, values=[f"{k}. {GAMING_NAMES[k]}" for k in sorted(GAMING_NAMES)], state="readonly", width=24)
        self.g_choice.pack(side="left")
        ttk.Label(top, text="Hours").pack(side="left", padx=8)
        self.g_hours = ttk.Entry(top, width=6); self.g_hours.pack(side="left")
        ttk.Button(top, text="Add Gaming", command=self._add_gaming).pack(side="right")

        info = ttk.Label(f, text="Rates: " + ", ".join([f"{GAMING_NAMES[k]} {GAMING_RATES[k]}/hr" for k in sorted(GAMING_NAMES)]))
        info.pack(anchor="w", pady=8)

    def _add_gaming(self):
        try:
            cid = self.g_cid.get().strip()
            if not cid: self._err(); return
            if not q(self.conn, "SELECT CID FROM ROOM_RENT WHERE CID=%s", (cid,), fetch=True): self._err(); return
            oid = self.g_oid.get().strip()
            if not oid: self._err(); return
            if q(self.conn, "SELECT ORDER_NO FROM GAMING WHERE ORDER_NO=%s", (oid,), fetch=True): self._err(); return
            ch = self.g_choice.get().split(".")[0] if self.g_choice.get() else ""
            if not is_int(ch,1,6): self._err(); return
            hrs = self.g_hours.get().strip()
            if not is_int(hrs,1): self._err(); return
            gidx = int(ch); name = GAMING_NAMES[gidx]; bill = int(hrs) * GAMING_RATES[gidx]
            q(self.conn, "INSERT INTO GAMING VALUES(%s,%s,%s,%s,%s,%s)", (oid, cid, str(gidx), name, int(hrs), bill))
            messagebox.showinfo("Gaming", f"{name} {hrs} hrs bill {bill}")
        except Exception:
            self._err()

    # Fashion
    def _build_fashion(self):
        f = self.fashion
        top = ttk.Frame(f); top.pack(fill="x")
        ttk.Label(top, text="CID").pack(side="left")
        self.fa_cid = ttk.Entry(top, width=18); self.fa_cid.pack(side="left", padx=6)
        ttk.Label(top, text="Order No").pack(side="left", padx=8)
        self.fa_oid = ttk.Entry(top, width=16); self.fa_oid.pack(side="left")
        ttk.Label(top, text="Dress").pack(side="left", padx=8)
        self.fa_choice = ttk.Combobox(top, values=[f"{k}. {FASHION_NAMES[k]}" for k in sorted(FASHION_NAMES)], state="readonly", width=24)
        self.fa_choice.pack(side="left")
        ttk.Label(top, text="Qty").pack(side="left", padx=8)
        self.fa_qty = ttk.Entry(top, width=6); self.fa_qty.pack(side="left")
        ttk.Button(top, text="Add Item", command=self._add_fashion).pack(side="right")

        info = ttk.Label(f, text="Prices: " + ", ".join([f"{FASHION_NAMES[k]} {FASHION_RATES[k]}" for k in sorted(FASHION_NAMES)]))
        info.pack(anchor="w", pady=8)

    def _add_fashion(self):
        try:
            cid = self.fa_cid.get().strip()
            if not cid: self._err(); return
            if not q(self.conn, "SELECT CID FROM ROOM_RENT WHERE CID=%s", (cid,), fetch=True): self._err(); return
            oid = self.fa_oid.get().strip()
            if not oid: self._err(); return
            if q(self.conn, "SELECT ORDER_NO FROM FASHION WHERE ORDER_NO=%s", (oid,), fetch=True): self._err(); return
            ch = self.fa_choice.get().split(".")[0] if self.fa_choice.get() else ""
            if not is_int(ch,1,10): self._err(); return
            qty = self.fa_qty.get().strip()
            if not is_int(qty,1): self._err(); return
            idx = int(ch); name = FASHION_NAMES[idx]; bill = int(qty) * FASHION_RATES[idx]
            q(self.conn, "INSERT INTO FASHION VALUES(%s,%s,%s,%s,%s,%s)", (oid, cid, str(idx), name, int(qty), bill))
            messagebox.showinfo("Fashion", f"{name} x{qty} bill {bill}")
        except Exception:
            self._err()

    # Bills
    def _build_bills(self):
        f = self.bills
        top = ttk.Frame(f); top.pack(fill="x")
        ttk.Label(top, text="CID").pack(side="left")
        self.bv_cid = ttk.Entry(top, width=18); self.bv_cid.pack(side="left", padx=6)
        ttk.Button(top, text="Show Bills", command=self._show_bills).pack(side="left")
        self.bill_text = tk.Text(f, height=16); self.bill_text.pack(fill="both", expand=True, pady=8)

    def _show_bills(self):
        try:
            cid = self.bv_cid.get().strip()
            self.bill_text.delete("1.0","end")
            rr = q(self.conn, "SELECT * FROM ROOM_RENT WHERE CID=%s", (cid,), fetch=True)
            room_bill = int(rr[0][6]) if rr else 0
            self.bill_text.insert("end", f"Room: {room_bill}\n")
            rest = q(self.conn, "SELECT COALESCE(SUM(BILL),0) FROM RESTAURENT WHERE CID=%s", (cid,), fetch=True)
            rest = int(rest[0][0]) if rest else 0
            self.bill_text.insert("end", f"Restaurant: {rest}\n")
            game = q(self.conn, "SELECT COALESCE(SUM(GAMING_BILL),0) FROM GAMING WHERE CID=%s", (cid,), fetch=True)
            game = int(game[0][0]) if game else 0
            self.bill_text.insert("end", f"Gaming: {game}\n")
            fash = q(self.conn, "SELECT COALESCE(SUM(BILL),0) FROM FASHION WHERE CID=%s", (cid,), fetch=True)
            fash = int(fash[0][0]) if fash else 0
            self.bill_text.insert("end", f"Fashion: {fash}\n")
            total = room_bill + rest + game + fash
            self.bill_text.insert("end", f"Total: {total}\n")
        except Exception:
            self._err()

    # Checkout
    def _build_checkout(self):
        f = self.checkout
        ttk.Label(f, text="CID").grid(row=0, column=0, sticky="w")
        self.c_cid = ttk.Entry(f, width=24); self.c_cid.grid(row=0, column=1, sticky="w", padx=6)
        ttk.Button(f, text="Checkout", command=self._checkout).grid(row=1, column=0, columnspan=2, pady=8, sticky="ew")

    def _checkout(self):
        try:
            cid = self.c_cid.get().strip()
            rr = q(self.conn, "SELECT ROOMNO FROM ROOM_RENT WHERE CID=%s", (cid,), fetch=True)
            if not rr: self._err(); return
            rno = rr[0][0]
            n = q(self.conn, "SELECT C_NAME FROM C_DETAILS WHERE CID=%s", (cid,), fetch=True)
            name = n[0][0] if n else ""
            room = q(self.conn, "SELECT ROOMRENT FROM ROOM_RENT WHERE CID=%s", (cid,), fetch=True)
            room_bill = int(room[0][0]) if room else 0
            rest = q(self.conn, "SELECT COALESCE(SUM(BILL),0) FROM RESTAURENT WHERE CID=%s", (cid,), fetch=True)
            rest = int(rest[0][0]) if rest else 0
            game = q(self.conn, "SELECT COALESCE(SUM(GAMING_BILL),0) FROM GAMING WHERE CID=%s", (cid,), fetch=True)
            game = int(game[0][0]) if game else 0
            fash = q(self.conn, "SELECT COALESCE(SUM(BILL),0) FROM FASHION WHERE CID=%s", (cid,), fetch=True)
            fash = int(fash[0][0]) if fash else 0
            total = room_bill + rest + game + fash
            if q(self.conn, "SELECT CID FROM TOTAL WHERE CID=%s", (cid,), fetch=True):
                q(self.conn, "UPDATE TOTAL SET C_NAME=%s,ROOMRENT=%s,RESTAURENTBILL=%s,GAMINGBILL=%s,FASHIONBILL=%s,TOTALAMOUNT=%s WHERE CID=%s",
                (name, room_bill, rest, game, fash, total, cid))
            else:
                q(self.conn, "INSERT INTO TOTAL VALUES(%s,%s,%s,%s,%s,%s,%s)", (cid, name, room_bill, rest, game, fash, total))
            q(self.conn, "UPDATE ROOMS SET STATUS='F' WHERE R_NO=%s", (rno,))
            q(self.conn, "DELETE FROM ROOM_RENT WHERE CID=%s", (cid,))
            messagebox.showinfo("Checkout", f"Total: {total}")
        except Exception:
            self._err()

class AdminTab(ttk.Frame):
    def __init__(self, master, conn, on_lock):
        super().__init__(master, padding=8)
        self.conn = conn
        self.on_lock = on_lock
        topbar = ttk.Frame(self); topbar.pack(fill="x")
        ttk.Label(topbar, text="Admin", font=("TkDefaultFont", 11, "bold")).pack(side="left")
        ttk.Button(topbar, text="Lock Admin", command=self.on_lock).pack(side="right")

        nb = ttk.Notebook(self)
        nb.pack(fill="both", expand=True)

        self.rooms = ttk.Frame(nb, padding=8)
        self.food = ttk.Frame(nb, padding=8)
        self.customers = ttk.Frame(nb, padding=8)
        self.reports = ttk.Frame(nb, padding=8)

        nb.add(self.rooms, text="Rooms")
        nb.add(self.food, text="Food Menu")
        nb.add(self.customers, text="Customers")
        nb.add(self.reports, text="Reports")

        self._build_rooms()
        self._build_food()
        self._build_customers()
        self._build_reports()

    def _err(self): messagebox.showerror("Error", "Invalid input or operation failed.")

    # Rooms
    def _build_rooms(self):
        f = self.rooms
        form = ttk.Frame(f); form.pack(fill="x")
        self.rno = ttk.Entry(form, width=10); self.rtype = ttk.Entry(form, width=12); self.rcost = ttk.Entry(form, width=8); self.rstatus = ttk.Entry(form, width=4)
        for i,(label,entry) in enumerate([("R_NO",self.rno),("TYPE",self.rtype),("COST",self.rcost),("STATUS(F/O)",self.rstatus)]):
            ttk.Label(form, text=label).grid(row=0, column=i*2, sticky="w"); entry.grid(row=0, column=i*2+1, padx=6)
        ttk.Button(form, text="Add/Update", command=self._save_room).grid(row=1, column=0, columnspan=2, pady=6, sticky="ew")
        ttk.Button(form, text="Delete", command=self._del_room).grid(row=1, column=2, columnspan=2, pady=6, sticky="ew")
        ttk.Button(form, text="Refresh", command=self._load_rooms).grid(row=1, column=4, columnspan=2, pady=6, sticky="ew")

        cols = ("R_NO","ROOM_TYPE","COST","STATUS")
        self.roomtv = ttk.Treeview(f, columns=cols, show="headings", height=10)
        for c in cols: self.roomtv.heading(c, text=c); self.roomtv.column(c, width=120, anchor="center")
        self.roomtv.pack(fill="both", expand=True, pady=8)
        self._load_rooms()

    def _load_rooms(self):
        try:
            for i in self.roomtv.get_children(): self.roomtv.delete(i)
            rows = q(self.conn, "SELECT * FROM ROOMS ORDER BY ROOM_TYPE,R_NO", fetch=True)
            for r in rows: self.roomtv.insert("", "end", values=r)
        except Exception:
            self._err()

    def _save_room(self):
        try:
            rno = self.rno.get().strip()
            rtype = self.rtype.get().strip().upper()
            cost = self.rcost.get().strip()
            status = self.rstatus.get().strip().upper()
            if not rno or not rtype or not status or (not cost.isdigit()) or status not in ("F","O"):
                self._err(); return
            if q(self.conn, "SELECT R_NO FROM ROOMS WHERE R_NO=%s", (rno,), fetch=True):
                q(self.conn, "UPDATE ROOMS SET ROOM_TYPE=%s,COST=%s,STATUS=%s WHERE R_NO=%s", (rtype, int(cost), status, rno))
            else:
                q(self.conn, "INSERT INTO ROOMS VALUES(%s,%s,%s,%s)", (rno, rtype, int(cost), status))
            self._load_rooms()
        except Exception:
            self._err()

    def _del_room(self):
        try:
            rno = self.rno.get().strip()
            if not rno: self._err(); return
            if not q(self.conn, "SELECT R_NO FROM ROOMS WHERE R_NO=%s", (rno,), fetch=True):
                self._err(); return
            q(self.conn, "DELETE FROM ROOMS WHERE R_NO=%s", (rno,))
            self._load_rooms()
        except Exception:
            self._err()

    # Food
    def _build_food(self):
        f = self.food
        form = ttk.Frame(f); form.pack(fill="x")
        self.fid = ttk.Entry(form, width=10); self.ftype = ttk.Entry(form, width=12); self.fname = ttk.Entry(form, width=18); self.fcost = ttk.Entry(form, width=8)
        for i,(label,entry) in enumerate([("ID",self.fid),("TYPE",self.ftype),("CUISINE",self.fname),("COST",self.fcost)]):
            ttk.Label(form, text=label).grid(row=0, column=i*2, sticky="w"); entry.grid(row=0, column=i*2+1, padx=6)
        ttk.Button(form, text="Add/Update", command=self._save_food).grid(row=1, column=0, columnspan=2, pady=6, sticky="ew")
        ttk.Button(form, text="Delete", command=self._del_food).grid(row=1, column=2, columnspan=2, pady=6, sticky="ew")
        ttk.Button(form, text="Refresh", command=self._load_food).grid(row=1, column=4, columnspan=2, pady=6, sticky="ew")

        cols = ("ID","TYPE","CUISINE","COST")
        self.foodtv = ttk.Treeview(f, columns=cols, show="headings", height=10)
        for c in cols: self.foodtv.heading(c, text=c); self.foodtv.column(c, width=120, anchor="center")
        self.foodtv.pack(fill="both", expand=True, pady=8)
        self._load_food()

    def _load_food(self):
        try:
            for i in self.foodtv.get_children(): self.foodtv.delete(i)
            rows = q(self.conn, "SELECT ID,CUISINE_TYPE,CUISINE,COST FROM FOOD ORDER BY CUISINE_TYPE,ID", fetch=True)
            for r in rows: self.foodtv.insert("", "end", values=r)
        except Exception:
            self._err()

    def _save_food(self):
        try:
            fid = self.fid.get().strip()
            ftype = self.ftype.get().strip().upper()
            fname = self.fname.get().strip().upper()
            cost = self.fcost.get().strip()
            if not fid or not ftype or not fname or not cost.isdigit():
                self._err(); return
            if q(self.conn, "SELECT ID FROM FOOD WHERE ID=%s", (fid,), fetch=True):
                q(self.conn, "UPDATE FOOD SET CUISINE_TYPE=%s,CUISINE=%s,COST=%s WHERE ID=%s", (ftype, fname, int(cost), fid))
            else:
                q(self.conn, "INSERT INTO FOOD VALUES(%s,%s,%s,%s)", (fid, ftype, fname, int(cost)))
            self._load_food()
        except Exception:
            self._err()

    def _del_food(self):
        try:
            fid = self.fid.get().strip()
            if not fid: self._err(); return
            if not q(self.conn, "SELECT ID FROM FOOD WHERE ID=%s", (fid,), fetch=True):
                self._err(); return
            q(self.conn, "DELETE FROM FOOD WHERE ID=%s", (fid,))
            self._load_food()
        except Exception:
            self._err()

    # Customers
    def _build_customers(self):
        f = self.customers
        form = ttk.Frame(f); form.pack(fill="x")
        self.ccid = ttk.Entry(form, width=10); self.cname = ttk.Entry(form, width=14); self.caddr = ttk.Entry(form, width=18)
        self.cage = ttk.Entry(form, width=6); self.ccountry = ttk.Entry(form, width=10); self.cphone = ttk.Entry(form, width=12); self.cemail = ttk.Entry(form, width=18)
        for i,(label,entry) in enumerate([("CID",self.ccid),("Name",self.cname),("Address",self.caddr),("Age",self.cage),("Country",self.ccountry),("Phone",self.cphone),("Email",self.cemail)]):
            ttk.Label(form, text=label).grid(row=0, column=i*2, sticky="w"); entry.grid(row=0, column=i*2+1, padx=6)
        ttk.Button(form, text="Add/Update", command=self._save_customer).grid(row=1, column=0, columnspan=2, pady=6, sticky="ew")
        ttk.Button(form, text="Delete", command=self._del_customer).grid(row=1, column=2, columnspan=2, pady=6, sticky="ew")
        ttk.Button(form, text="Refresh", command=self._load_customers).grid(row=1, column=4, columnspan=2, pady=6, sticky="ew")

        cols = ("CID","NAME","ADDRESS","AGE","COUNTRY","PHONE","EMAIL")
        self.ctv = ttk.Treeview(f, columns=cols, show="headings", height=12)
        for c in cols: self.ctv.heading(c, text=c); self.ctv.column(c, width=120, anchor="center")
        self.ctv.pack(fill="both", expand=True, pady=8)
        self._load_customers()

    def _load_customers(self):
        try:
            for i in self.ctv.get_children(): self.ctv.delete(i)
            rows = q(self.conn, "SELECT * FROM C_DETAILS ORDER BY CID", fetch=True)
            for r in rows: self.ctv.insert("", "end", values=r)
        except Exception:
            self._err()

    def _save_customer(self):
        try:
            cid = self.ccid.get().strip()
            if not cid: self._err(); return
            name = self.cname.get().strip(); addr = self.caddr.get().strip(); age = self.cage.get().strip()
            country = self.ccountry.get().strip(); phone = self.cphone.get().strip(); email = self.cemail.get().strip()
            if q(self.conn, "SELECT CID FROM C_DETAILS WHERE CID=%s", (cid,), fetch=True):
                q(self.conn, "UPDATE C_DETAILS SET C_NAME=%s,C_ADDRESS=%s,C_AGE=%s,C_COUNTRY=%s,P_NO=%s,C_EMAIL=%s WHERE CID=%s",
                  (name, addr, age, country, phone, email, cid))
            else:
                q(self.conn, "INSERT INTO C_DETAILS VALUES(%s,%s,%s,%s,%s,%s,%s)", (cid, name, addr, age, country, phone, email))
            self._load_customers()
        except Exception:
            self._err()

    def _del_customer(self):
        try:
            cid = self.ccid.get().strip()
            if not cid: self._err(); return
            if not q(self.conn, "SELECT CID FROM C_DETAILS WHERE CID=%s", (cid,), fetch=True):
                self._err(); return
            q(self.conn, "DELETE FROM C_DETAILS WHERE CID=%s", (cid,))
            self._load_customers()
        except Exception:
            self._err()

    # Reports
    def _build_reports(self):
        f = self.reports
        nb = ttk.Notebook(f); nb.pack(fill="both", expand=True)

        self.rep_room = self._tv_tab(nb, "Room Rents", ("CID","CHECK_IN","CHECK_OUT","QUALITY","DAYS","ROOMNO","ROOMRENT"),
                                     "SELECT CID,CHECK_IN,CHECK_OUT,ROOM_QUALITY,NO_OF_DAYS,ROOMNO,ROOMRENT FROM ROOM_RENT")
        self.rep_rest = self._tv_tab(nb, "Restaurant", ("ORDER_NO","CID","CUISINE","QTY","BILL"),
                                     "SELECT ORDER_NO,CID,CUISINE,QUANTITY,BILL FROM RESTAURENT")
        self.rep_game = self._tv_tab(nb, "Gaming", ("ORDER_NO","CID","GAME","HOURS","BILL"),
                                     "SELECT ORDER_NO,CID,GAMES,HOURS,GAMING_BILL FROM GAMING")
        self.rep_fash = self._tv_tab(nb, "Fashion", ("ORDER_NO","CID","DRESS","QTY","BILL"),
                                     "SELECT ORDER_NO,CID,DRESS,AMOUNT,BILL FROM FASHION")
        self.rep_tot = self._tv_tab(nb, "Totals", ("CID","NAME","ROOM","REST","GAME","FASH","TOTAL"),
                                     "SELECT CID,C_NAME,ROOMRENT,RESTAURENTBILL,GAMINGBILL,FASHIONBILL,TOTALAMOUNT FROM TOTAL")

    def _tv_tab(self, notebook, title, cols, sql):
        frame = ttk.Frame(notebook, padding=8)
        notebook.add(frame, text=title)
        tv = ttk.Treeview(frame, columns=cols, show="headings", height=12)
        for c in cols: tv.heading(c, text=c); tv.column(c, width=120, anchor="center")
        vs = ttk.Scrollbar(frame, orient="vertical", command=tv.yview)
        tv.configure(yscroll=vs.set)
        tv.pack(side="left", fill="both", expand=True)
        vs.pack(side="left", fill="y")
        btns = ttk.Frame(frame); btns.pack(side="bottom", fill="x")
        def refresh():
            try:
                for i in tv.get_children(): tv.delete(i)
                rows = q(self.conn, sql, fetch=True)
                for r in rows: tv.insert("", "end", values=r)
            except Exception:
                self._err()
        ttk.Button(btns, text="Refresh", command=refresh).pack(side="right", padx=6, pady=6)
        refresh()
        return tv

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("HMS - Full GUI (Admin Lock)")
        self.geometry("1040x720")
        self._frame = None
        self._conn = None
        self._admin_tab_index = None
        self._show_login()

    def _show_login(self):
        if self._frame: self._frame.destroy()
        self._frame = LoginFrame(self, self._on_connected)
        self._frame.pack(fill="both", expand=True)

    def _on_connected(self, conn):
        self._conn = conn
        if self._frame: self._frame.destroy()

        # If no admin exists, force setup dialog
        if not admin_exists(self._conn):
            def done(): self._build_main_ui()
            SetupAdminDialog(self, self._conn, on_done=done)
        else:
            self._build_main_ui()

    def _build_main_ui(self):
        nb = ttk.Notebook(self)
        nb.pack(fill="both", expand=True)
        nb.add(CustomerTab(nb, self._conn), text="Customer")

        # Admin locked tab
        locked_frame = ttk.Frame(nb, padding=8)
        nb.add(locked_frame, text="Admin (locked)")
        self._admin_tab_index = nb.index("end") - 1

        def unlock_admin():
            # Replace the locked tab content with real Admin tab
            nb.forget(self._admin_tab_index)
            admin_tab = AdminTab(nb, self._conn, on_lock=self._relock_admin(nb))
            nb.add(admin_tab, text="Admin")
            self._admin_tab_index = nb.index("end") - 1
            nb.select(self._admin_tab_index)

        # Fill locked tab with login widget
        login = AdminLoginFrame(locked_frame, self._conn, on_unlock=unlock_admin)
        login.pack(fill="both", expand=True)

        self._frame = nb

    def _relock_admin(self, nb):
        def _lock():
            try:
                # Remove current admin tab and re-add locked tab
                if self._admin_tab_index is not None:
                    nb.forget(self._admin_tab_index)
                locked_frame = ttk.Frame(nb, padding=8)
                nb.add(locked_frame, text="Admin (locked)")
                self._admin_tab_index = nb.index("end") - 1
                login = AdminLoginFrame(locked_frame, self._conn, on_unlock=lambda: self._unlock_from_locked(nb))
                login.pack(fill="both", expand=True)
                nb.select(0)
            except Exception:
                messagebox.showerror("Error", "Something went wrong.")
        return _lock

    def _unlock_from_locked(self, nb):
        try:
            nb.forget(self._admin_tab_index)
            admin_tab = AdminTab(nb, self._conn, on_lock=self._relock_admin(nb))
            nb.add(admin_tab, text="Admin")
            self._admin_tab_index = nb.index("end") - 1
            nb.select(self._admin_tab_index)
        except Exception:
            messagebox.showerror("Error", "Something went wrong.")
