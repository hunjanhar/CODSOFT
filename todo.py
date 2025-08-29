import pymysql
import tabulate
import prompt_toolkit

class todo:
    def __init__(self):
        print(r'''
 _____         _       
|_   _|__   __| | ___  
  | |/ _ \ / _` |/ _ \ 
  | | (_) | (_| | (_) |
  |_|\___/ \__,_|\___/ 

''')
        self.database_conn()
        while True:
            self.printtodos()
            try:
                user_opt = int(input("1. Add Todo 📋\n2. Delete Todo ❎\n3. Edit/Update Todo 📝\n4. Exit🚪\n"))
                if user_opt == 1:
                    self.inserttodo()
                elif user_opt == 2:
                    self.deletetodo()
                elif user_opt == 3:
                    self.updatetodo()
                elif user_opt == 4:
                    self.connection.close()
                    print("Bye")
                    break
                else:
                    print("Invalid Option ❎")
            except ValueError:
                print("Invalid Input 🔢")
    
    def database_conn(self):
        conn = pymysql.connect(host="",user="",password="")
        try:
            with conn.cursor() as cursor:
                sql = 'SHOW DATABASES LIKE "todo";'
                cursor.execute(sql)
                res = cursor.fetchall()
                if not res:
                    create_db = 'CREATE DATABASE todo;'
                    cursor.execute(create_db)
                    self.connection = pymysql.connect(host="",user="",password="",database="")
                    with self.connection.cursor() as c:
                        check_table = 'SHOW TABLES LIKE "todos"'
                        c.execute(check_table)
                        ress = c.fetchall()
                        if not ress:
                            create_table = 'CREATE TABLE todos(id int auto_increment primary key ,name varchar(500));'
                            c.execute(create_table)
                else:
                    self.connection = pymysql.connect(host="",user="",password="",database="")
        except pymysql.MySQLError as error:
            print(f"Error : {error}")
    
    def printtodos(self):
        with self.connection.cursor() as c:
            c.execute("SELECT * FROM TODOS;")
            result = c.fetchall()
            column_names = [i[0] for i in c.description]
            if result:
               print(tabulate.tabulate(result,headers=column_names,tablefmt="grid"))
            else:
                print(" NO TODOS HAVE 📋")
                c.execute("ALTER TABLE todos auto_increment = 1;")
                self.connection.commit()

            
    def inserttodo(self):
        try:
            desc = input("Enter the Description of Todo 📝 :- ")
            try:
                with self.connection.cursor() as c:
                    c.execute(f'INSERT INTO TODOS(name) values("{desc}");')
                    self.connection.commit()
            except pymysql.MySQLError as e:
                print(f"Error : {e}")
        except ValueError:
            print("Invalid Input 🔢")
    

    def deletetodo(self):
        try:
            id = int(input("Enter the id of Todo 🆔:- "))
            try:
                with self.connection.cursor() as c:
                    res = c.execute(f'DELETE FROM todos WHERE ID = {id};')
                    if res == 0:
                        print("Invalid id ❎")
                    self.connection.commit()
            except pymysql.MySQLError as e:
                print(f"Error : {e}")
        except ValueError:
            print("Invalid input 🔢")

    def updatetodo(self):
        try:
            id = int(input("Enter the id of Todo 🆔 :- "))
            try:
                with self.connection.cursor() as c:
                    c.execute(f'SELECT NAME FROM TODOS WHERE ID = {id};')
                    res = c.fetchone()
                    if res:
                        edit = prompt_toolkit.prompt("Edit the text:\n",default=res[0], multiline=False)
                        c.execute(f'update todos set name = "{edit}" where id = {id};')
                        self.connection.commit()
                    else:
                        print("Invalid id  ❎")
            except pymysql.MySQLError as e:
                print(f"Error : {e}")
        except ValueError:
            print("Invalid input 🔢")

obj = todo()