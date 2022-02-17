from algo_work.program_files import all_the_lambda, find_mwc, graph_theory_section, tallying_parties, edge_cases, display_graphs


def new_run():
    """
    Runs the program
    """
    # --------------------------------------------------------
    """
    Gets location of needed information from user.
    """
    statement1 = "Enter location of party names and votes: "
    party_location = str(input(statement1))
    statement2 = "Enter location of party probabilities: "
    prob_location = str(input(statement2))
    statement3 = "Enter number of parties: "
    num_parties = int(input(statement3))
    statement4 = "Enter votes needed to win: "
    target = int(input(statement4))
    # --------------------------------------------------------
    """
    Loads and reads file for parties and votes information.
    """
    parties = []
    fileobj = open(party_location)
    parties_and_votes = fileobj.readlines()
    parties_and_votes = [line.strip() for line in parties_and_votes]
    for i in range(0, num_parties * 2, 2):  # Takes each pair of party name and votes and assigns them as a tuple to
        # the parties list
        name = parties_and_votes[i]
        votes = int(parties_and_votes[i + 1])
        parties.append((votes, name))
    print(parties)
    parties = sorted(parties)
    parties.reverse()
    print(parties)
    # --------------------------------------------------------
    """
    Checks for edge cases
    """
    if edge_cases.same_name_check(parties):
        new_run()

    if edge_cases.can_reach_target(parties, target):
        print("Sum of votes doesn't reach target. Reduce target required")
        quit()

    """if edge_cases.sum_is_target_check(parties, target):
        final_scores = []
        for i in range(len(parties)):
            name = parties[i][0]
            final_scores.append((name, 1/len(parties)))
        print("The final results are:")
        print(final_scores)
        quit()
        """

    target_check = edge_cases.party_hits_target_check(parties, target)
    if target_check > -1:
        print("The final results are:")
        print(edge_cases.winning_party(parties, target_check))
    # --------------------------------------------------------
    """
    Set up the probability matrix
    """
    prob_matrix = graph_theory_section.set_up_prob_matrix(parties, prob_location)
    print("Matrix Complete!")
    # --------------------------------------------------------
    """
    Minimal Winning Coalition -> Score loop
    """
    starting_point = find_mwc.find_min_coalition(parties, target)
    print("Smallest coalitions consist of %d parties" % starting_point)
    l_and_t = find_mwc.generate_coalitions(parties, target, starting_point, prob_matrix)
    scores = tallying_parties.final_tally(l_and_t[-1])
    lambdas = l_and_t[0]
    unnormalised_scores = all_the_lambda.score_lambda_fun_times(scores, lambdas)
    print("---------------------------------------------------------------------")
    normalised_scores = all_the_lambda.normalise(unnormalised_scores)
    print("---------------------------------------------------------------------")
    display_graphs.plot_graph(normalised_scores)


new_run()




