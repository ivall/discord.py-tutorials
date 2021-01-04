from models.database import Database

mysql = Database()


class User:
    def __init__(self, id):
        self._id = id

    def get_money(self):
        query = mysql.execute("SELECT money FROM users WHERE user_id=%s" % (self._id))
        return query[0]
