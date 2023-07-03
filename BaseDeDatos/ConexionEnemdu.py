import mysql.connector as mysql
import csv

# Establecer la conexión
db = mysql.connect(
    host='localhost',
    user='root',
    password='MySQL'
)

cursor = db.cursor()

cursor.execute("DROP SCHEMA IF EXISTS `enemdu`;")
cursor.execute("CREATE SCHEMA IF NOT EXISTS `enemdu` DEFAULT CHARACTER SET utf8;")
cursor.execute("USE enemdu;")
cursor.execute("create table enemdu_vivienda_hogar " +
               "(area         int         null," +
               "ciudad       text        null," +
               "conglomerado int         null," +
               "panelm       int         null," +
               "vivienda     int         null," +
               "hogar        int         null," +
               "vi01         int         null," +
               "vi02         int         null," +
               "vi03a        int         null," +
               "vi03b        int         null," +
               "vi04a        int         null," +
               "vi04b        int         null," +
               "vi05a        int         null," +
               "vi05b        int         null," +
               "vi06         int         null," +
               "vi07         int         null," +
               "vi07a        int         null," +
               "vi07b        int         null," +
               "vi08         int         null," +
               "vi09         int         null," +
               "vi09a        text        null," +
               "vi09b        text        null," +
               "vi10         int         null," +
               "vi101        text        null," +
               "vi102        text        null," +
               "vi10a        int         null," +
               "vi11         int         null," +
               "vi12         int         null," +
               "vi13         int         null," +
               "vi14         int         null," +
               "vi141        int         null," +
               "vi142        text        null," +
               "vi143        text        null," +
               "vi144        text        null," +
               "vi1511       int         null," +
               "vi1521       text        null," +
               "vi1512       int         null," +
               "vi1522       text        null," +
               "vi1531       text        null," +
               "vi1541       text        null," +
               "vi1532       text        null," +
               "vi1542       text        null," +
               "vi1533       text        null," +
               "vi1543       text        null," +
               "vi1534       text        null," +
               "vi1544       text        null," +
               "vi1535       text        null," +
               "vi1545       text        null," +
               "vi1536       text        null," +
               "vi1546       text        null," +
               "estrato      int         null," +
               "fexp         text        null," +
               "upm          double      null," +
               "id_vivienda  varchar(30) null," +
               "id_hogar     varchar(30) null," +
               "periodo      int         null," +
               "mes          int         null);")

with open('../../../../Desktop/ProyectoIntegrador/enemdu.csv'
        , newline='') as csvfile:
    csv_data = csv.reader(csvfile, delimiter=';')
    next(csv_data)
    for fila in csv_data:
        consulta = f"INSERT INTO enemdu.enemdu_vivienda_hogar VALUES ({fila[0]},'{fila[1]}',{fila[2]},{fila[3]},{fila[4]},{fila[5]}" \
                   f",{fila[6]},{fila[7]},{fila[8]},{fila[9]},{fila[10]},{fila[11]},{fila[12]},{fila[13]},{fila[14]}," \
                   f"{fila[15]},{fila[16]},{fila[17]},{fila[18]},{fila[19]},'{fila[20]}','{fila[21]}',{fila[22]},'{fila[23]}'," \
                   f"'{fila[24]}',{fila[25]},{fila[26]},{fila[27]},{fila[28]},{fila[29]},{fila[30]},'{fila[31]}','{fila[32]}'," \
                   f"'{fila[33]}',{fila[34]},'{fila[35]}',{fila[36]},'{fila[37]}','{fila[38]}','{fila[39]}','{fila[40]}','{fila[41]}'," \
                   f"'{fila[42]}','{fila[43]}','{fila[44]}','{fila[45]}','{fila[46]}','{fila[47]}','{fila[48]}','{fila[49]}',{fila[50]}," \
                   f"'{fila[51]}',{fila[52]},'{fila[53]}','{fila[54]}',{fila[55]},{fila[56]})"
        cursor.execute(consulta)


alter_query = f"ALTER TABLE enemdu.enemdu_vivienda_hogar " \
              f"CHANGE vi01 via_acceso INT NULL, " \
              f"CHANGE vi02 tipo_vivienda INT NULL, " \
              f"CHANGE vi03a tipo_techo INT NULL, " \
              f"CHANGE vi03b estado_techo INT NULL," \
              f"CHANGE vi04a tipo_piso INT NULL," \
              f"CHANGE vi04b estado_piso INT NULL," \
              f"CHANGE vi05a tipo_paredes INT NULL," \
              f"CHANGE vi05b estado_paredes INT NULL," \
              f"CHANGE vi06 numero_cuartos INT NULL," \
              f"CHANGE vi07 numero_dormitorios INT NULL," \
              f"CHANGE vi07a numero_cuartos_negocio INT NULL," \
              f"CHANGE vi07b numero_cuartos_cocinar INT NULL," \
              f"CHANGE vi08 materiales_cocinar INT NULL," \
              f"CHANGE vi09 tipo_servicio_higienico INT NULL," \
              f"CHANGE vi09a no_servicio_higienco TEXT NULL," \
              f"CHANGE vi09b tipo_instalacion_sanitaria_cp TEXT NULL," \
              f"CHANGE vi10 origen_agua INT NULL," \
              f"CHANGE vi101 tiene_medidor TEXT NULL," \
              f"CHANGE vi102 junta_agua TEXT NULL," \
              f"CHANGE vi10a recepcion_agua INT NULL," \
              f"CHANGE vi11 tipo_ducha INT NULL," \
              f"CHANGE vi12 tipo_alumbrado INT NULL," \
              f"CHANGE vi13 eliminacion_basura INT NULL," \
              f"CHANGE vi14 tipo_tenencia_vivienda INT NULL," \
              f"CHANGE vi141 valor_arriendo INT NULL," \
              f"CHANGE vi142 inclusion_agua TEXT NULL," \
              f"CHANGE vi143 inclusion_luz TEXT NULL," \
              f"CHANGE vi144 parentesco_propietario_vivienda TEXT NULL," \
              f"CHANGE vi1511 tenencia_vehiculo INT NULL," \
              f"CHANGE vi1521 numero_vehiculos TEXT NULL," \
              f"CHANGE vi1512 tenencia_motos INT NULL," \
              f"CHANGE vi1522 numero_motos TEXT NULL," \
              f"CHANGE vi1531 abastecimiento_super TEXT NULL," \
              f"CHANGE vi1541 gasto_super TEXT NULL," \
              f"CHANGE vi1532 abastecimiento_extra TEXT NULL," \
              f"CHANGE vi1542 gasto_extra TEXT NULL," \
              f"CHANGE vi1533 abastecimiento_diesel TEXT NULL," \
              f"CHANGE vi1543 gasto_diesel TEXT NULL," \
              f"CHANGE vi1534 abastecimiento_ecopais TEXT NULL," \
              f"CHANGE vi1544 gasto_ecopais TEXT NULL," \
              f"CHANGE vi1535 abastecimiento_electricidad TEXT NULL," \
              f"CHANGE vi1545 gasto_electricidad TEXT NULL," \
              f"CHANGE vi1536 abastecimiento_gas TEXT NULL," \
              f"CHANGE vi1546 gasto_gas TEXT NULL;"
cursor.execute(alter_query)
db.commit()
db.close()