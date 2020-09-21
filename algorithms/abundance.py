import math
def abundance_score(allowed_couplets, percent, species_list, key_database):
    candidate_couplets = list()
    for couplet in allowed_couplets:
        species_list = sorted(species_list, key=lambda x: x[1], reverse=True)
        top_percent = math.ceil(len(species_list)*(percent/100))
        top = [s[0] for s in species_list[:top_percent]]
        states = list()
        for sp in species_list:
            states.append((sp[0], key_database.get_state(sp[0], couplet)))
        zero = list()
        one = list()
        for s in states:
            if '0' in s[1]:
                zero.append(s[0])
            elif '1' in s[1]:
                one.append(s[0])
        p_zero = (1 - sum([s in top for s in zero])/len(top)) + abs(len(zero)-len(top))
        p_one = (1 - sum([s in top for s in one])/len(top)) + abs(len(one)-len(top))
        ab_score = max([p_zero, p_one])
        # return ab_score to candidate_couplets
        # lower is better
        candidate_couplets.append((couplet, ab_score))
    # return candidate_couplets as sorted list of (couplet, score)
    return sorted(candidate_couplets, key=lambda x: x[1])
