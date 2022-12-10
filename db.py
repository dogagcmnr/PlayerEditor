import sqlite3

class gamedb:
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        sql = """
         CREATE TABLE IF NOT EXISTS players(
            id Integer Primary Key,
            username varchar(64),
            password varchar(64),
            nickname varchar(64),
            email varchar(254),
            gender text,
            confirmation_code varchar(128),
            confirmation_date timestamp,
            date_of_reg timestamp,
            date_of_link timestamp
        )
        """
        self.cur.execute(sql)
        self.con.commit()

    def insert(self, username, password, nickname, email, gender, confirmation_code, confirmation_date,date_of_reg,date_of_link):
        self.cur.execute("insert into players values (NULL,?,?,?,?,?,?,?,?,?)",
                         (username, password, nickname, email, gender, confirmation_code, confirmation_date,date_of_reg,date_of_link))
        self.con.commit()

    def fetch(self):
        self.cur.execute("SELECT * from players")
        rows = self.cur.fetchall()
        return rows

    def remove(self, id):
        self.cur.execute("delete from players where id=?", (id,))
        self.con.commit()

    def update(self, id, username, password, nickname, email, gender, confirmation_code, confirmation_date,date_of_reg,date_of_link):
        self.cur.execute(
            "update players set username=?, password=?, nickname=?, email=?, gender=?, confirmation_code=?, confirmation_date=?, date_of_reg=?, date_of_link=? where id=?",
            (username, password, nickname, email, gender, confirmation_code, confirmation_date,date_of_reg,date_of_link, id))
        self.con.commit()
