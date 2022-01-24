from algo_work.program_files import all_the_lambda, find_mwc, graph_theory_section, tallying_parties, edge_cases

statement = "Enter number of parties: "
number_of_parties = int(input(statement))

parties = []


def run():
    fileobj = open("US_states_votes")
    parties_and_votes = fileobj.readlines()
    parties_and_votes = [line.strip() for line in parties_and_votes]
    for i in range(0, number_of_parties*2, 2):
        name = parties_and_votes[i]
        votes = int(parties_and_votes[i+1])
        parties.append((name, votes))
    if edge_cases.same_name_check(parties):
        run()

    statement = "Enter the number of votes needed to win: "
    target = int(input(statement))

    if edge_cases.sum_is_target_check(parties, target):
        final_scores = []
        for i in range(len(parties)):
            name = parties[i][0]
            final_scores.append((name, 1/len(parties)))
        print("1The final results are:")
        print(final_scores)
        quit()

    target_check = edge_cases.party_hits_target_check(parties, target)
    if target_check > -1:
        print("2The final results are:")
        print(edge_cases.winning_party(parties, target_check))
    else:
        prob_matrix = graph_theory_section.set_up_prob_matrix(parties)
        print("Matrix complete")
        list_of_mwcs = find_mwc.generate_coalitions(parties, target)
        print("MWCs found")
        conductances = graph_theory_section.conductance(parties, list_of_mwcs, prob_matrix)
        print("Conductances calculated")
        ceps = graph_theory_section.cep(parties, list_of_mwcs, prob_matrix)
        tally = tallying_parties.tally(list_of_mwcs)
        list_of_lambdas = all_the_lambda.assign_Lambda(parties, conductances, ceps)
        tally = sorted(tally)
        list_of_lambdas = sorted(list_of_lambdas)
        unnormalised_scores = (all_the_lambda.score_lambda_fun_times(tally, list_of_lambdas))
        all_the_lambda.normalise(unnormalised_scores)


run()
