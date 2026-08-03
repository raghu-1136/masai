
def process_roster(roster):
    # Step 1: convert tuples to lists, append "active", convert back to tuples
    # print(roster)
    tmplst = []
    updated_roster = []
    names = []
    delivery = []

    for i in roster:
       tmplst.append( list(i))
    # print(tmplst)
    for i in tmplst:
        i.append("active")
    # print(tmplst)
        updated_roster.append(tuple(i))
    # Step 2: extract driver names into a new list
        names.append(i[0])

    print(names)
    print(updated_roster)

    # Step 3: sort names in place
    #names.sort()
    sorted_names = sorted(names)
    print(sorted_names)
    # Step 4: count high performers (deliveries > 50)
    for i in updated_roster:
        if i[1]> 50:
            delivery.append(i)
    high_performers = len(delivery)
    print(high_performers)
    # Step 5: return summary dictionary
    dict_ = {"roster":updated_roster,"sorted_names":sorted_names,"High_performers":high_performers}
    print(dict_)
    pass

if __name__ == "__main__":
    roster = [
        ("Chen Wei", 63),
        ("Maria Santos", 45),
        ("Carlos Mendes", 78),
        ("Fatima Al-Amin", 50),
        ("Kofi Mensah", 91),
        ("Lena Fischer", 30),
        ("Takeshi Yamamoto", 55),
    ]
    print(process_roster(roster))
