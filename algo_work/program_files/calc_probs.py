def get_them_probs():
    statement1 = "Enter location of red probabilities: "
    red_prob = str(input(statement1))

    statement2 = "Enter location of blue probabilities: "
    blue_prob = str(input(statement2))

    red_probs = []
    fileobj = open(red_prob)
    reading_red = fileobj.readlines()
    reading_red = [line.strip() for line in reading_red]
    for line in reading_red:
        red_probs.append(line)

    blue_probs = []
    fileobj2 = open(blue_prob)
    reading_blue = fileobj2.readlines()
    reading_blue = [line.strip() for line in reading_blue]
    for line in reading_blue:
        blue_probs.append(line)

    print(red_probs)
    print(blue_probs)

    all_probs = []
    for i in range(len(red_probs)):
        for j in range(len(blue_probs)):
            if i < j:
                r1 = float(red_probs[i])
                r2 = float(red_probs[j])
                b1 = float(blue_probs[i])
                b2 = float(blue_probs[j])
                maths = (r1/100 * r2/100) + (b1/100 * b2/100)
                all_probs.append(maths)
    print(all_probs)


get_them_probs()