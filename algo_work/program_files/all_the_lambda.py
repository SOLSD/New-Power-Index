
def Lambda(conductance, cep):
    return cep/conductance


def assign_Lambda(parties, list_of_conductances, list_of_ceps):
    """
    Generates and assigns lambda value to each party.

    Finds the conductance and cep of each mwc and uses that to generate a value for lambda.
    From there it applies to a party, the largest lambda from a mwc that the party in question is a part of.
    """
    list_of_Lambda = []
    party_lambdas = []
    for i in range(len(list_of_conductances)):
        Lambda_to_use = Lambda(list_of_conductances[i][-1], list_of_ceps[i][-1])  # Finds the corresponding conductance
        # and cep for each mwc and divides the latter by the former
        list_of_Lambda.append((list_of_conductances[i][0], Lambda_to_use))  # Adds the mwc and its lambda value as a
        # tuple to the list
    for party in parties:
        best_lambda = 0
        for i in range(len(list_of_Lambda)):
            if party in list_of_Lambda[i][0] and list_of_Lambda[i][-1] > best_lambda:  # Checks if the party is in the
                # mwc and that the current value of lambda is larger than the previous largest
                best_lambda = list_of_Lambda[i][-1]
                party_lambda = list_of_Lambda[i][-1]
        party_lambdas.append((party, party_lambda))
    return party_lambdas


def score_lambda_fun_times(scores, lambdas):
    """
    Function to multiply lambda values and tally of each party together.
    """
    final_scores = []
    for i in range(len(scores)):
        final_scores.append((scores[i][0], scores[i][-1]*lambdas[i][-1]))  # Multiplies the tally from
        # tallying_parties.py by the lambda for each party
    return final_scores


def normalise(scores):
    """
    Normalises the scores so that they are relative to each other.
    """
    final_scores = []
    denominator = 0
    for party in scores:
        denominator += party[-1]  # denominator is the sum of all scores from parties
    for i in range(len(scores)):
        final_scores.append((scores[i][0], scores[i][-1]/denominator))  # Normalisation step
    print("The final results are:")
    print(final_scores)
    return final_scores
