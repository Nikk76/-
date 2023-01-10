import psycopg2

connection = psycopg2
connection.autocommit = True


def create_table_users():
    with connection.cursor() as cursor:
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS users(
                id serial,
                first_name varchar(30) NOT NULL,
                last_name varchar(30) NOT NULL,
                vk_id varchar(50) NOT NULL PRIMARY KEY;"""
        )


def create_table_seen_users():
    with connection.cursor() as cursor:
        cursor.execute(
            f"""CREATE TABLE IF NOT EXISTS seen_users(
            id serial,
            vk_id varchar(50) PRIMARY KEY);"""
        )


def insert_data_users(first_name, last_name, vk_id, vk_link):
    with connection.cursor() as cursor:
        cursor.execute(
            f"""INSERT INTO users (first_name, last_name, vk_id, vk_link) 
            VALUES ('{first_name}', '{last_name}', '{vk_id}', '{vk_link}');"""
        )


def insert_data_seen_users(vk_id):
    with connection.cursor() as cursor:
        cursor.execute(
            f"""INSERT INTO seen_users (vk_id) 
            VALUES ('{vk_id}');"""
        )
