import sqlite3 as sql
import random
import threading
import time

db = "2FADataBase.db"

def CreateDB():
    conn = sql.connect(db)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users
                    (isim TEXT, soyisim TEXT,eposta TEXT, sifre TEXT,userid TEXT PRIMARY KEY, code INTEGER)''')
    conn.commit()
    conn.close()

def GenerateUserId():
    return ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890', k=2))
    #k=2, 2 haneli user id oluşturur. Güvenlik açısından k değeri minumum 10 haneli olmalıdır


def GenerateUserCode():
    return random.randint(99999, 1000000)


def Generate2FACode(isim, soyisim, eposta, sifre):
    userId = GenerateUserId()
    userCode = GenerateUserCode()

    conn = sql.connect(db)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (isim,soyisim,eposta,sifre,userid,code) VALUES (?,?,?,?,?,?)",
                   (isim, soyisim, eposta, sifre, userId, userCode))
    conn.commit()
    conn.close()

    return userId, userCode


def Verify(mail, codeToVerify):
    conn = sql.connect(db)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE eposta=? AND code=?", (mail, codeToVerify))
    result = cursor.fetchone()

    conn.close()

    if result is not None:
        return True
    else:
        return False


def VerifyID(mail, idToVerify):
    conn = sql.connect(db)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE eposta=? AND userid=?", (mail, idToVerify))
    result = cursor.fetchone()

    conn.close()

    if result is not None:
        return True
    else:
        return False


def Update2FACodes():
    conn = sql.connect(db)
    cursor = conn.cursor()
    cursor.execute("SELECT userid FROM users")
    userIds = cursor.fetchall()
    conn.close()

    for userId in userIds:
        newCode = GenerateUserCode()
        conn = sql.connect(db)
        cursor = conn.cursor()
        cursor.execute("UPDATE users SET code=? WHERE userid=?", (newCode, userId[0]))
        conn.commit()
        conn.close()


def StartTimedUpdates():
    threading.Timer(30.0, StartTimedUpdates).start()
    Update2FACodes()


def UserCodePrint(mail, id):
    conn = sql.connect(db)
    cursor = conn.cursor()

    cursor.execute("SELECT code FROM users WHERE eposta = ? AND userid = ?", (mail, id))
    result = cursor.fetchone()

    conn.close()

    if result:
        return result[0]
    else:
        return None


def UserNamePrint(mail):
    conn = sql.connect(db)
    cursor = conn.cursor()

    cursor.execute("SELECT isim, soyisim FROM users WHERE eposta = ?", (mail,))
    result = cursor.fetchone()

    conn.close()

    if result:
        return result[0], result[1]
    else:
        return None


def UserCodeLabel(mail):
    conn = sql.connect(db)
    cursor = conn.cursor()
    cursor.execute("SELECT userid FROM users WHERE eposta = ?", (mail,))
    result = cursor.fetchone()
    conn.close()

    if result:
        return result[0]
    else:
        return None


def DeleteUser(mail, verify):
    conn = sql.connect(db)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE eposta = ? AND code = ?", (mail, verify))
    conn.commit()
    conn.close()


if __name__ == "__main__":
    CreateDB()
    # StartTimedUpdates() #Kişiye özel olan 'code' değerini 30 saniyede bir günceller. Sadece 7/24 açık olacak olan sayfada bu kodun aktif olması gerekiyor.
