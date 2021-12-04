from algo_work.program_files import all_the_lambda, find_mwc, graph_theory_section, tallying_parties

statement = "Enter number of parties: "
number_of_parties = int(input(statement))

parties = []


def run():
    for i in range(number_of_parties):
        statement = "Enter the name of party:", i + 1
        name_of_party = str(input(statement))
        statement = "Enter number of votes the party has: "
        number_of_votes = int(input(statement))
        parties.append((name_of_party, number_of_votes))

    statement = "Enter the number of votes needed to win: "
    target = int(input(statement))
    prob_matrix = graph_theory_section.set_up_prob_matrix(parties)
    list_of_mwcs = find_mwc.generate_coalitions(parties, target)
    conductances = graph_theory_section.conductance(parties, list_of_mwcs, prob_matrix)
    ceps = graph_theory_section.cep(parties, list_of_mwcs, prob_matrix)
    tally = tallying_parties.tally(list_of_mwcs)
    list_of_lambdas = all_the_lambda.assign_Lambda(parties, conductances, ceps)
    tally = sorted(tally)
    list_of_lambdas = sorted(list_of_lambdas)
    unnormalised_scores = (all_the_lambda.score_lambda_fun_times(tally, list_of_lambdas))
    all_the_lambda.normalise(unnormalised_scores)


run()
