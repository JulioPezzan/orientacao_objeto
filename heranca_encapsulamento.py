class DataBaseConn:

    def __int__(self) -> None:
        self.__database = 'Postgres'
        self._conn = '// connection_string'
        self.user = 'Lhama'

    def get_database(self) -> None:
        print(self.__database)

    def _testing_conection(self) -> None:
        print('Conection OK!')


class Repository(DataBaseConn):

    def __init__(self) -> None:
        super().__init__()


    def select(self) -> None:
        self._testing_conection()
        #print('Connecting to {}'.format(self._conn))
        print('(SELECT) * From table')


repo = Repository()
repo.select()

# OBS: # _ protegido ; __ privado ; sem nada publico