import os
import sys
from urllib import request

import pymysql
import sqlite3


class KeyDatabaseExternal(object):

    def __init__(self, **kwargs):
        self._connection = pymysql.connect(**kwargs)
        self.cursor = self._connection.cursor()

    @property
    def connection(self):
        return self._connection

    def get_colums_couplet_data(self):
        sql = "SHOW COLUMNS FROM couplet_data;"
        try:
            self.cursor.execute(sql)
            columns_couplet_data = self.cursor.fetchall()
            columns_couplet_data = [i[0] for i in columns_couplet_data]
        except Exception as e:
            raise e
        return columns_couplet_data

    def get_table_couplet_data(self):
        sql = "SELECT * FROM couplet_data;"
        try:
            self.cursor.execute(sql)
            couplet_data = self.cursor.fetchall()
        except pymysql.Error as e:
            raise e
        return couplet_data

    def get_columns_species_states(self):
        sql = "SHOW COLUMNS FROM species_states;"
        try:
            self.cursor.execute(sql)
            columns_species_states = self.cursor.fetchall()
            columns_species_states = [i[0] for i in columns_species_states]
        except Exception as e:
            raise e
        return columns_species_states

    def get_table_species_states(self):
        sql = "SELECT * FROM species_states;"
        try:
            self.cursor.execute(sql)
            species_states = self.cursor.fetchall()
        except pymysql.Error as e:
            raise e
        return species_states


class KeyDatabaseInternal(object):

    def __init__(self, database_path):
        self._connection = sqlite3.connect(database_path)
        self.cursor = self._connection.cursor()

    @property
    def connection(self):
        return self._connection


###
def sync_key_database(user, host, passwd, db, sqlite_database_path, images_path):
    """
    Despite the name, this actually just drops the tables in the
    target local database and rebuilds them based on the provided
    mysql database. It's like a one-way syncronization.
    """
    ###
    try:
        server = KeyDatabaseExternal(user=user, host=host, passwd=passwd, db=db)
    except pymysql.Error as e:
        raise e # if can't connect to server, stop all
    ###
    ###
    try:
        client = KeyDatabaseInternal(database_path=sqlite_database_path)
    except sqlite3.Error as e:
        try:
            server.connection.close()
        except pymysql.Error as e:
            raise e
        raise e
    ###
    ###
    # drop local tables like an egg
    try:
        client.cursor.execute("DROP TABLE couplet_data;")
        client.connection.commit()
    except sqlite3.Error as e:
        client.connection.rollback()
        connection_error_handler(e)
    #
    try:
        client.cursor.execute("DROP TABLE species_states;")
        client.connection.commit()
    except sqlite3.Error as e:
        client.connection.rollback()
        connection_error_handler(e)
    ###
    ###
    # remake local tables
    try:
        client.cursor.execute("""
            CREATE TABLE couplet_data (
                couplet VARCHAR(100) PRIMARY KEY,
                weight FLOAT(2) DEFAULT 0.0,
                zero_text VARCHAR(1048) DEFAULT '',
                one_text VARCHAR(1048) DEFAULT '',
                zero_pic VARCHAR(2048) DEFAULT 'https://i.imgur.com/4ZL1L8e.png',
                one_pic VARCHAR(2048) DEFAULT 'https://i.imgur.com/4ZL1L8e.png'
            );
        """)
        client.connection.commit()
    except sqlite3.Error as e:
        client.connection.rollback()
        connection_error_handler(e)
    #
    try:
        client.cursor.execute("""
            CREATE TABLE species_states (
                couplet VARCHAR(100) PRIMARY KEY
            );
        """)
        client.connection.commit()
    except sqlite3.Error as e:
        client.connection.rollback()
        connection_error_handler(e)
    ###
    ###
    # fetching columns
    columns_couplet_data = server.get_colums_couplet_data()
    #
    columns_species_states = server.get_columns_species_states()
    #
    # formating names
    names_cd = "`{}`, "*len(columns_couplet_data)
    names_cd = names_cd.format(*columns_couplet_data)
    names_cd = names_cd[:-2]

    names_ss = "`{}`, "*len(columns_species_states)
    names_ss = names_ss.format(*columns_species_states)
    names_ss = names_ss[:-2]
    #
    # building sqlite database couplet_data table
    couplet_data = server.get_table_couplet_data()
    for values in couplet_data:
        ###
        # cache images
        zero_pic_urls = values[names_cd.split(', ').index('`zero_pic`')]
        one_pic_urls = values[names_cd.split(', ').index('`one_pic`')]
        #
        for url in zero_pic_urls.split(','):
            zero_pic_file = url.split('/')[-1]
            if not os.path.exists(os.path.join(images_path, zero_pic_file)):
                zero_pic = request.urlopen(url).read()
                with open(os.path.join(images_path, zero_pic_file), 'wb') as f:
                    f.write(zero_pic)
        #
        for url in one_pic_urls.split(','):
            one_pic_file = url.split('/')[-1]
            if not os.path.exists(os.path.join(images_path, zero_pic_file)):
                one_pic = request.urlopen(url).read()
                with open(os.path.join(images_path, one_pic_file), 'wb') as f:
                    f.write(one_pic)
        ###
        sql = f"""
        INSERT INTO `couplet_data` ({names_cd})
          VALUES {values};
        """
        try:
            client.cursor.execute(sql)
            client.connection.commit()
        except sqlite3.Error as e:
            client.connection.rollback()
            connection_error_handler(e)
    #
    # building sqlite database species_states columns
    column_species = names_ss.replace('`couplet`, ', '')
    for sp in column_species.split(', '):
        sql = f"""
        ALTER TABLE species_states ADD {sp} VARCHAR(2);
        """
        try:
            client.cursor.execute(sql)
            client.connection.commit()
        except sqlite3.Error as e:
            client.connection.rollback()
            connection_error_handler(e)
    #
    # building sqlite database species_states table
    species_states = server.get_table_species_states()
    for values in species_states:
        values = str(values)
        values = values.replace('None', 'NULL')
        sql = f"""
        INSERT INTO `species_states` ({names_ss})
          VALUES {values};
        """
        try:
            client.cursor.execute(sql)
            client.connection.commit()
        except sqlite3.Error as e:
            client.connection.rollback()
            connection_error_handler(e)
    #
    # closing connections
    try:
        server.connection.close()
    except pymysql.Error as e:
        raise e
    finally:
        try:
            client.connection.close()
        except sqlite3.Error as e:
            raise e

###
def connection_error_handler(e):
    try:
        server.connection.close()
    except pymysql.Error as e:
        raise e
    finally:
        try:
            client.connection.close()
        except sqlite3.Error as e:
            raise e

###
if __name__ == '__main__':
    user = sys.argv[1]
    host = sys.argv[2]
    passwd = sys.argv[3]
    db = sys.argv[4]
    sqlite_database_path = sys.argv[5]
    images_path = sys.argv[6]
    sync_key_database(user, host, passwd, db, sqlite_database_path, images_path)
