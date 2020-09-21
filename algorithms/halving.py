def halving_score(allowed_couplets, species_list, key_database):
    candidate_couplets = list()
    for couplet in allowed_couplets:
        hv_score = 0
        goal = len(species_list)/2
        for sp in species_list:
            hv_score += int(key_database.get_state(sp[0], couplet))
        hv_score = abs(hv_score-goal)
        hv_score += float(key_database.get_weight(couplet))
        # return hv_score to candidate_couplets
        # lower is better
        candidate_couplets.append((couplet, hv_score))
    # return candidate_couplets as sorted list of (couplet, score)
    return sorted(candidate_couplets, key=lambda x: x[1])
