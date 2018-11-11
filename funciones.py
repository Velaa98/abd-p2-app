import psycopg2

def run_query(db_host,db_name,db_user,db_pass):
	try:
		#conexion_str = 	'dbname="" user="" host="{}" + \\ password="{}"'.format(db_name,db_user,db_host,db_pass)
		connect_str  =  "dbname = '{}' user = '{}' host = '{}'".format(db_name,db_user,db_host)  + \
		"password = '{}'".format(db_pass)

		# Conexión a la base de datos
		conn = psycopg2.connect(connect_str)

		# Crea un cursor
		cursor = conn.cursor()

		# Ejecutar consulta
		cursor.execute("""select distinct usename,client_addr from pg_stat_activity;""")

		# Guardar el resultado de la consulta
		datos = cursor.fetchall()

		# Cerrar el cursor
		cursor.close()

		# Cerrar la conexión
		conn.close()
		return datos
	except:
		pass
