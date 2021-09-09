#https://thispointer.com/subtract-months-from-a-date-in-python/
from datetime import date
from datetime import datetime
from dateutil.relativedelta import relativedelta


alarmas = [
    {'months':21,
     'days':0
    },
    {'months':20,
     'days':0
    },
    {'months':15,
     'days':17
    },
    {'months':15,
     'days':2
    },
    {'months':12,
     'days':0
    },
]

resolucion_ejemplo = \
{   'id_programa':1,
    'estado':'ACTIVO',
    'resolucion': 1,
    'fecha_resolucion': '2021-1-1',
    'vigencia': 7,
    'fecha_notificacion': '2021-1-1',
    'fecha_ejecutoria':  '2021-1-1',
    'fecha_vencimiento_dec_1330': '2021-1-1',
    'ajuste_dec_1330':'c1',
    'fecha_vencimiento': '2021-1-1',
}

actividad = \
    { 'reg_id': 1,
      'est_id': 1,
      'nombre': 'Alarma 21 meses antes  ',
      'descripcion': 'Alarma 21 meses antes',
      'fecha_inicio': '2020-2-2',
      'fecha_fin': '2020-2-2',
      'requiere_recordatorio': 'true'
   }

def time_(increment=True ,months=0, days=0,date_to_change=date.today()):
    date_format = '%Y-%m-%d'
    if increment:
        past_date = date_to_change + relativedelta(months=months, days=days)
    else:
        past_date = date_to_change - relativedelta(months=months, days=days)
    past_date_str = past_date.strftime(date_format)
    return past_date_str



def insert_resoluciones():
    resoluciones = ''
    for i in range(len(alarmas)):
        date_ = time_(increment=False,  months=alarmas[i]["months"], days=alarmas[i]["days"])
        resolucion = resolucion_ejemplo.copy()

        resolucion.update({'id_programa': i+1,
                           'resolucion': i+1,
                           'fecha_resolucion': time_(increment=False, months=24),
                           'fecha_vencimiento':date_})
        query = f""" INSERT INTO registro_acreditacion(id_programa, estado, resolucion, fecha_resolucion, vigencia,fecha_notificacion, fecha_ejecutoria,fecha_vencimiento_dec_1330, ajuste_dec_1330, fecha_vencimiento) VALUES( {resolucion["id_programa"]}, '{resolucion["estado"]}', {resolucion["resolucion"]}, '{resolucion["fecha_resolucion"]}', {resolucion["vigencia"]},'{resolucion["fecha_notificacion"]}', '{resolucion["fecha_ejecutoria"]}', '{resolucion["fecha_vencimiento_dec_1330"]}','{resolucion["ajuste_dec_1330"]}','{resolucion["fecha_vencimiento"]}' );\n"""
        resoluciones +=query
    return resoluciones



def sql_actividades(id_resolucion):
    sql=''
    for alarma in alarmas:
        fecha_inicio = time_(increment=False, months=alarma["months"], days=alarma["days"])
        fecha_fin = time_(increment=True, days=15, date_to_change=datetime.strptime(fecha_inicio,'%Y-%m-%d'))
        actividad.update(
            {'reg_id': id_resolucion,
             'est_id': 1,
             'nombre': f" nombre Alarma {alarma['months']} meses antes  ",
             'descripcion': f"descripcion Alarma {alarma['months']} meses antes  ",
             'fecha_inicio': fecha_inicio,
             'fecha_fin': fecha_fin,
             'requiere_recordatorio': 'true'
             }
        )
        sql += f"INSERT INTO actividades(reg_id, est_id, nombre, descripcion, fecha_inicio, fecha_fin, requiere_recordatorio)	VALUES ({actividad['reg_id']}, {actividad['est_id']}, '{actividad['nombre']}', '{actividad['descripcion']}', '{actividad['fecha_inicio']}', '{actividad['fecha_fin']}', '{actividad['requiere_recordatorio']}');\n"
    return sql







sql_actividades(1)
