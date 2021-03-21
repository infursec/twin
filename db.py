import sqlite3

conn = sqlite3.connect('base.db', check_same_thread=False)
c = conn.cursor()


c.execute('''CREATE TABLE IF NOT EXISTS keys
	(totp text)''')

c.execute('''CREATE TABLE IF NOT EXISTS creds
	(id INTEGER PRIMARY KEY NOT NULL, key_header text, proto text, login text, password text, ip text)''')



def add_totp(totp):
	print(totp)
	q = """INSERT INTO keys VALUES (?)"""
	c.execute(q, [(totp)])
	conn.commit()

def add_creds(kh, proto,login,password,ip):
	q = """INSERT INTO creds VALUES (NULL,?,?,?,?,?)"""
	c.execute(q, (kh,proto,login,password, ip))
	conn.commit()

def add_totp(totp):
	print(totp)
	q = """INSERT INTO keys VALUES (?)"""
	c.execute(q, [(totp)])
	conn.commit()


def get_maior_pass():
	q = """SELECT * FROM creds WHERE key_header=?"""
	c.execute(q, [("1")])
	conn.commit()
	return c.fetchone()

def get_totp():
	q = """SELECT * FROM keys"""
	c.execute(q)
	conn.commit()
	return c.fetchone()[0]

def get_all_passes():
	q = """SELECT * FROM creds WHERE key_header=?"""
	c.execute(q, [("0")])
	conn.commit()
	tmp = ""
	tmpl = "{} {} {} {}\n"
	alls = c.fetchall()
	for a in alls:
		print(a[0])
		tmp = tmp + tmpl.format(a[2],a[3],a[4],a[5])

	return tmp
