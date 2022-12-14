import mysql.connector as mc
from read_config import read_db_config
try:
	from lib.config_ini import read_db_config
except:
	from  read_confing import read_db_config

import mysql.connector as mc
from read_config import read_db_config

class DB():
	def __init__(self):
		mysql_config = read_db_config('config.ini', 'mysql')
		print(mysql_config)
		try:
			self.conn = mc.connect(**mysql_config)
		except mc.Error as e:
			print(e)


	def create_radiotheaters_table(self):
		sql = """
			CREATE TABLE IF NOT EXISTS laptop_db(
				id INT AUTO_INCREMENT PRIMARY KEY,
				title VARCHAR(100) NOT NULL,
				page_date DATE NOT NULL,
				content TEXT,
				created_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
				updated_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
				CONSTRAINT title_date UNIQUE (title, pub_date)
			);
		"""

		with self.conn.cursor() as cursor:
			cursor.execute(sql)
			self.conn.commit()

	def drop_laptop_db_table(self):
		sql = "DROP TABLE IF EXISTS laptop_db";

		with self.conn.cursor() as cursor:
			cursor.execute(sql)
			self.conn.commit()

	def insert_rows(self, rows_data):
		sql = """
			INSERT IGNORE INTO laptop_db
			(title, page_date, content)
			VALUES ( %s, %s, %s)
		"""

		with self.conn.cursor() as cursor:
			cursor.executemany(sql, rows_data)
			self.conn.commit()

	def insert_row(self, row_data):
		sql = """
			INSERT IGNORE INTO laptop_db
				(title, page_date, content)
				VALUES ( %s, %s, %s)
		"""

		with self.conn.cursor(prepared=True) as cursor:
			cursor.execute(sql, tuple(row_data.values()))
			self.conn.commit()

	def select_all_data(self):
		sql = "SELECT id, title, page_date, content FROM  laptop_db"

		with self.conn.cursor() as cursor:
			cursor.execute(sql)
			result = cursor.fetchall()

		return result

	def get_last_updated_date(self):
		sql = 'SELECT MAX(updated_at) AS "Max Date" FROM  laptop_db;'
		with self.conn.cursor() as cursor:
			cursor.execute(sql)
			result = cursor.fetchone()

		if result:
			return result[0]
		else:
			raise ValueError('No data in table')

	def get_column_names(self):
		sql = "SELECT id, title, page_date, content FROM  laptop_db LIMIT 1;"

		with self.conn.cursor() as cursor:
			cursor.execute(sql)
			result = cursor.fetchone()

		return cursor.column_names

if __name__ == '__main__':
	db = DB()

	# db.get_column_names()
	res = db.get_last_updated_date()
	print(res)