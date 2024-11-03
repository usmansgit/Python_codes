"""
COMP.CS.100 Programming 1 / Ohjelmointi 1

Code template for basic exam.
Koodipohja perustenttiin.

Muhammad Usman
"""

def read_input_file(filename):
    statistics = {}

    try:
        file_object = open(filename, mode="r")

        for line in file_object:
            lower_limit, upper_limit, count_string = line.split(";")

            count = int(count_string)
            age_group_str = f"{lower_limit}-{upper_limit}yrs"
            age_group_str = f"{age_group_str:>9}"

            # HINT/VIHJE:
            # - You should probably make sure you know exactly
            #   what the variable age_group_str contains at this point.
            # - Sinun on syytä varmistaa, että tiedät täsmälleen, mikä
            #   muuttujan age_group_str arvo on tässä kohdassa.

            statistics[age_group_str] = count

    except OSError:
        print("Error in reading the input file.")
        return None

    return statistics

def total(statistics):
    total_population=0
    for group in sorted(statistics):
        total_population =total_population+statistics[group]
    #print(total_population)
    return total_population


def print_table(statistics):
    comu=0
    for group in sorted(statistics):
        comu = comu +statistics[group]
        print(f"{group} {statistics[group]} {(statistics[group]/total(statistics))*100:.1f} % {comu/total(statistics)*100:.1f} %")

def ages(statistics):
    sorted_dict = dict(sorted(statistics.items(), key=lambda item: item[1], reverse=True))


    higest_age = (max(sorted_dict, key=sorted_dict.get))
    lowest_age = (min(sorted_dict, key=sorted_dict.get))



    print("Biggest age group:", higest_age)
    print("Smallest age group:", lowest_age)


def main():
    age_groups = read_input_file("age_distribution.txt")

    print("Information crack about Finnish citizens 31.12.2013:")
    print()

    tot=total(age_groups)
    print("Population: ", tot)
    print()

    print_table(age_groups)
    print()

    ages(age_groups)

if __name__ == "__main__":
    main()
