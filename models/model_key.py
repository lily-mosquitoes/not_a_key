import itertools

from .model_key_database import KeyDatabase


class Key(object):
    """
    This class is initiated with the path to the key database
    and provides the methods to use its data to key out a provided
    list of species (given directly to methods); it also requires
    a scoring algorithm and its argument dict to be given on
    initialization
    """

    def __init__(self, key_database_path, scoring_algorithm, params):
        #
        self.scoring_algorithm = scoring_algorithm
        #
        self.params = params
        #
        try:
            self.key_database = KeyDatabase(path=key_database_path)
        except Exception as e:
            raise e
        #
        self.key_list = self.key_database.list_species()
        #
        self.key_couplets = self.key_database.list_couplets()

    def _allowed_couplets(self, species_list, used_couplets):
        allowed_couplets = list()
        for couplet in self.key_couplets:
            states_list = list()
            for sp, abundance in species_list:
                states_list.append(self.key_database.get_state(sp, couplet))
            if None not in states_list and 'NA' not in states_list and not all(x == states_list[0] for x in states_list) and couplet not in used_couplets:
                allowed_couplets.append(couplet)
        #
        return allowed_couplets

    def _load_candidate_couplets(self, species_list, used_couplets):
        # get allowed_couplets
        allowed_couplets = self._allowed_couplets(species_list, used_couplets)
        # load params
        self.params['allowed_couplets'] = allowed_couplets
        self.params['species_list'] = species_list
        self.params['key_database'] = self.key_database
        # get candidate_couplets from chosen scoring_algorithm
        candidate_couplets = self.scoring_algorithm(**self.params)
        # candidate_couplets = self._get_candidate_couplets(species_list)
        # strip scores
        candidate_couplets = [c[0] for c in candidate_couplets]
        # handle absence of candidate_couplets
        if candidate_couplets == []:
            candidate_couplets = ['End of Key']
        #
        self.len_candidate_couplets = len(candidate_couplets)
        self.candidate_couplets = itertools.cycle(candidate_couplets)

    def choose_new_couplet(self, species_list, used_couplets):
        self._load_candidate_couplets(species_list, used_couplets)
        return next(self.candidate_couplets)

    def skip_new_couplet(self):
        return next(self.candidate_couplets)
