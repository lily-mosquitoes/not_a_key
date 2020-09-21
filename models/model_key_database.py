import sqlite3


class KeyDatabase(object):

    def __init__(self, path):
        self._connection = sqlite3.connect(path)
        self.cursor = self._connection.cursor()

    @property
    def connection(self):
        return self._connection

    def _get_couplet_info(self, info, couplet):
        sql = f"""
        SELECT {info} FROM couplet_data
            WHERE couplet_data.couplet = '{couplet}';
        """
        try:
            self.cursor.execute(sql)
            info = self.cursor.fetchone()[0]
        except sqlite3.Error as e:
            raise e
        return info

    def get_weight(self, couplet):
        weight = self._get_couplet_info('weight', couplet)
        return weight

    def get_couplet(self, couplet):
        zero_text = self._get_couplet_info('zero_text', couplet)
        zero_pic = self._get_couplet_info('zero_pic', couplet)
        one_text = self._get_couplet_info('one_text', couplet)
        one_pic = self._get_couplet_info('one_pic', couplet)
        return zero_text, zero_pic, one_text, one_pic

    def list_species(self):
        sql = "PRAGMA table_info(species_states)"
        try:
            self.cursor.execute(sql)
            species = self.cursor.fetchall()
            species = [i[1] for i in species] # in sqlite [0] is an index
            species.remove('couplet')
        except sqlite3.Error as e:
            raise e
        return species

    def list_couplets(self):
        sql = """
        SELECT couplet FROM species_states;
        """
        try:
            self.cursor.execute(sql)
            couplets = self.cursor.fetchall()
            couplets = [c[0] for c in couplets]
        except sqlite3.Error as e:
            raise e
        return couplets

    def get_state(self, species, couplet):
        sql = f"""
        SELECT `{species}` FROM species_states
            WHERE species_states.couplet = '{couplet}';
        """
        try:
            self.cursor.execute(sql)
            state = self.cursor.fetchone()[0]
        except sqlite3.Error as e:
            raise e
        return state
