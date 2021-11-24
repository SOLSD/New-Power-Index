
def Lambda(conductance, cep):
    return cep/conductance


def assign_Lambda(parties, list_of_conductances, list_of_ceps):
    list_of_Lambda = []
    party_lambdas = []
    for i in range(len(list_of_conductances)):
        Lambda_to_use = Lambda(list_of_conductances[i][-1], list_of_ceps[i][-1])
        print(Lambda_to_use)
        list_of_Lambda.append((list_of_conductances[i][0], Lambda_to_use))
        print(list_of_Lambda)
    for party in parties:
        best_lambda = 0
        for i in range(len(list_of_Lambda)):
            if party in list_of_Lambda[i][0] and list_of_Lambda[i][-1] > best_lambda:
                best_lambda = list_of_Lambda[i][-1]
                party_lambda = list_of_Lambda[i][-1]
        party_lambdas.append((party, party_lambda))
    print(party_lambdas)
    return party_lambdas


def score_lambda_fun_times(scores, lambdas):
    final_scores = []
    for i in range(len(scores)):
        print(scores[i][-1])
        print(lambdas[i][-1])
        final_scores.append((scores[i][0], scores[i][-1]*lambdas[i][-1]))
    print(final_scores)
    return final_scores


def normalise(scores):
    final_scores = []
    denominator = 0
    for party in scores:
        denominator += party[-1]
    for i in range(len(scores)):
        final_scores.append((scores[i][0], scores[i][-1]/denominator))
    print("The final results are:")
    print(final_scores)
    return final_scores
