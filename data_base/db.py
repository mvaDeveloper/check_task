import sqlite3 as sq


def sql_start():
    global base, cur
    base = sq.connect(r'C:\Users\Дмитрий\PycharmProjects\project_distributor\bot_distributor\finam.db')
    cur = base.cursor()
    if base:
        print('connect')


async def select_tasks(status):
    cur.execute("SELECT * FROM tasks WHERE status = (?)", (status,))
    return cur.fetchall()


async def select_user(executor):
    cur.execute("SELECT tg_login FROM users WHERE fio = (?) OR finam_login = (?)", (executor, executor,))
    return cur.fetchall()


async def update_task(id, status):
    cur.execute("UPDATE tasks SET status = (?) WHERE ID = (?)",
                (status, id))
    base.commit()


"""
async def add_user(state):
    async with state.proxy() as data:
        print(tuple(data.values()))
        cur.execute('INSERT INTO users(tg_login, fio, finam_login) VALUES (?,?,?)', tuple(data.values()))
        base.commit()


async def add_online(tg_login):
    cur.execute('INSERT INTO onLine(tg_login, break) VALUES (?,?)', (tg_login, 'хуй1'))
    base.commit()


async def insert_at_work(tg_login, time_start, reason):
    cur.execute('INSERT INTO not_at_work(tg_login, time_start, reason) VALUES (?,?,?)', (tg_login, time_start, reason))
    base.commit()


async def update_at_work(id_diner, time_stop):
    cur.execute("UPDATE not_at_work SET time_stop = (?) WHERE ID = (?)",
                (time_stop, id_diner))
    base.commit()


async def select_not_at_work(tg_login):
    cur.execute("SELECT users.finam_login, not_at_work.ID FROM users "
                "JOIN not_at_work  ON not_at_work.tg_login=users.tg_login "
                "WHERE users.tg_login =(?) AND not_at_work.time_stop IS NULL", (tg_login,)
                )
    return cur.fetchall()


async def give_user(tg_login):
    cur.execute("SELECT * FROM users WHERE tg_login = (?)", (tg_login,))
    return cur.fetchall()


async def select_state_diner(tg_login):
    cur.execute("SELECT * FROM onLine WHERE tg_login =(?)", (tg_login,))
    return cur.fetchall()


async def select_diner():
    cur.execute("SELECT * FROM diner")
    return cur.fetchall()


async def select_null_diner(tg_login):
    cur.execute("SELECT ID FROM diner WHERE tg_login =(?) AND diner_stop IS NULL", (tg_login,))
    return cur.fetchall()

async def select_account(tg_login):
    cur.execute("SELECT * FROM accounts WHERE tg_login =(?)", (tg_login,))
    return cur.fetchall()


async def give_user(tg_login):
    cur.execute("SELECT * FROM users WHERE tg_login = (?)", (tg_login,))
    return cur.fetchall()


async def give_count(tg_login):
    cur.execute("SELECT count FROM accounts WHERE tg_login = (?)", (tg_login,))
    return cur.fetchall()
"""


