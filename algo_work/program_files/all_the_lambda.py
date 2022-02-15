list_of_lambda = []


def assign_Lambda(mwc, conductance, cep):
    """
    Generates and assigns lambda value to each party.

    Finds the conductance and cep of each mwc and uses that to generate a value for lambda.
    From there it applies to a party, the largest lambda from a mwc that the party in question is a part of.
    """

    lambda_of_mwc = cep/conductance
    if len(list_of_lambda) == 0:    # Makes sure there is an entry to iterate over
        list_of_lambda.append((mwc[0][-1], 0))
    for i in range(len(mwc)):
        count = 0   # It's a Surprise Tool That Will Helps Us Later
        for j in range(len(list_of_lambda)):
            if mwc[i][-1] in list_of_lambda[j][0] and list_of_lambda[j][-1] < lambda_of_mwc:
                list_of_lambda.pop(j)   # Replaces the tuple
                list_of_lambda.insert(j, (mwc[i][-1], lambda_of_mwc))
                break
            elif mwc[i][-1] in list_of_lambda[j][0] and list_of_lambda[j][-1] >= lambda_of_mwc:
                break
            else:
                count += 1  # Counting each time the party being checked isn't in the list
                if count >= len(list_of_lambda):    # If not in list at all (count == length) add to list
                    list_of_lambda.append((mwc[i][-1], lambda_of_mwc))
    return list_of_lambda


def score_lambda_fun_times(scores, lambdas):
    """
    Function to multiply lambda values and tally of each party together.
    """
    final_scores = []
    for i in range(len(scores)):
        final_scores.append((scores[i][-1]*lambdas[i][-1], scores[i][0]))  # Multiplies the tally from
        # tallying_parties.py by the lambda for each party
    sorted(final_scores)
    for score in final_scores:
        num = score[0]
        name = score[-1]
        index = final_scores.index(score)
        final_scores.pop(index)
        final_scores.insert(index, (name, num))
    print("Unnormalised Scores are:", final_scores)
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
