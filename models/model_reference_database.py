from collections import defaultdict

import sqlite3


class ReferenceDatabase(object):

    def __init__(self, path):
        self._connection = sqlite3.connect(path)
        self.cursor = self._connection.cursor()

        # set up some dicts for ease of translation later
        self.seasons = {
            'Winter': ['12', '01', '02'],
            'Spring': ['03', '04', '05'],
            'Summer': ['06', '07', '08'],
            'Fall': ['09', '10', '11']
        }
        self.months = {
            'January': ['01'],
            'February': ['02'],
            'March': ['02'],
            'April': ['04'],
            'May': ['05'],
            'June': ['06'],
            'July': ['07'],
            'August': ['08'],
            'September': ['09'],
            'October': ['10'],
            'November': ['11'],
            'December': ['12']
        }
        self.sort_list_alias = {
            'season': self.seasons,
            'month': self.months
        }

    @property
    def connection(self):
        return self._connection

    def get_locations(self):
        sql = "SELECT state FROM species_data;"
        try:
            self.cursor.execute(sql)
            locations = self.cursor.fetchall()
            locations = [i[0] for i in locations]
            locations = sorted(set(locations))
            locations.remove('') # remove "" (empty) state (no state info)
        except sqlite3.Error as e:
            raise e
        return locations


    def _get_species_entries(self, state):
        if state == 'all states':
            sql = "SELECT * FROM species_data;"
        else:
            sql = f"SELECT * FROM species_data WHERE state = '{state}';"
        #
        try:
            self.cursor.execute(sql)
            species_entries = self.cursor.fetchall()
        except sqlite3.Error as e:
            raise e
        #
        return species_entries

    def _filter_entries(self, location, sortby, sortby2):
        raw_entry_data = self._get_species_entries(location)
        # raw_entry_data == [species, state, month, count]
        #
        entries = defaultdict(int)
        # if all months selected, return all entries
        if sortby == 'full year':
            for entry in raw_entry_data:
                species, count = entry[0], entry[3]
                entries[species] += int(count)
            return entries
        # else, return filtered entries
        elif sortby == 'season' or sortby == 'month':
            sort_list = self.sort_list_alias[sortby]
            for entry in raw_entry_data:
                month = entry[2] # months are: MM
                species = entry[0]
                count = entry[3]
                if month in sort_list[sortby2]:
                    entries[species] += int(count)
                else:
                    entries[species] += 0
            return entries

    def get_abundance_matrix(self, location, sortby, sortby2):
        """
        This returns all species in the 'location', and their
        relative abundance for the 'sortby' time frame; this means
        that it will show species with zero abundance. This is
        important to catch new records / shifting occurrence
        """
        #
        entries = self._filter_entries(location, sortby, sortby2)
        #
        total_individuals = sum([i[1] for i in entries.items()])
        #
        for sp, count in entries.items():
            entries[sp] = round((count/total_individuals)*100, 2)
        #
        return entries
