
class MiException(Exception):
    def __init__(self,err):
        print(f'{err}')

# raise ZeroDivisionError('diviste por cero ')

# manejando mi propia excepcion
try:
    raise MiException('cometiste un error')
except:
    print('acabas de divir por cero')
        
# lanzando mi propia excepcion
raise MiException('cometiste un error')

