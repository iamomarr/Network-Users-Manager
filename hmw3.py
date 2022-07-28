import mysql.connector

# Done BY omarabuali 11923947 && amrshekha 11923707
mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="123",
    database="hmw3"

)
cursor = mydb.cursor()
# check if the ip of the user is in blacklist
check_if_blocked = "SELECT * FROM  IPs_blacklist WHERE userID = '119' and IP_address = '192.168.2.12'"
cursor.execute(check_if_blocked)
result = mydb.fetchall()
if result is None:
    print("Failed login you are blocked")
    exit()  # i couldn't use a break function here ,so i used exit()

else:
    print("login success!!")
while True:

    q_insert = """INSERT INTO users( userID, username, password, firstName, lastName, status) VALUES ('119', 'OA', 
    'OA2', 'omar', 'amr', 'true') """
    q_remove = "DELETE FROM IPs_blacklist WHERE userID = '119'"
    q_update = '''UPDATE users SET status = 'false' WHERE  username= 'OA' '''
    q_users_list = "SELECT users FROM hmw3"
    q_block = """INSERT INTO IPs_blacklist(userID, IP_address) VALUES ('119', '192.168.2.12')"""
    q_unblock = "DELETE FROM IPs_blacklist WHERE userID = '119'"

    try:
        cursor.execute(q_insert, q_remove, q_update, q_users_list)  # run all the commands
        cursor.commit()  # to make sure the changes is Done or saved!

    except:
        print("!!!ERROR!!!")
    mydb.close()
