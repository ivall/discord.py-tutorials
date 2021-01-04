from models.database import Database

mysql = Database()


def is_registered(ctx):
    user_id = ctx.author.id

    query = mysql.execute("SELECT * FROM users WHERE user_id=%s" % (user_id))
    if not query:
        mysql.execute("INSERT INTO users (user_id,money) VALUES (%s, %s)" % (user_id, 0))

    return True
