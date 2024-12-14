class Athlete:
    def __init__(self, name, country):
        self.name = name
        self.country = country
        self.medals = {'gold': 0, 'silver': 0, 'bronze': 0}

    def win_medal(self, medal_type):
        if medal_type in self.medals:
            self.medals[medal_type] += 1

    def __str__(self):
        return f"{self.name} from {self.country} | Medals: {self.medals}"


class Country:
    def __init__(self, name):
        self.name = name
        self.athletes = []
        self.total_medals = {'gold': 0, 'silver': 0, 'bronze': 0}

    def add_athlete(self, athlete):
        self.athletes.append(athlete)

    def update_medal_count(self, medal_type):
        if medal_type in self.total_medals:
            self.total_medals[medal_type] += 1

    def __str__(self):
        return f"{self.name} | Total Medals: {self.total_medals}"


class Event:
    def __init__(self, name):
        self.name = name
        self.results = []

    def add_result(self, athlete, medal_type):
        athlete.win_medal(medal_type)
        athlete.country.update_medal_count(medal_type)
        self.results.append((athlete, medal_type))

    def show_results(self):
        print(f"\nResults for {self.name}:")
        for athlete, medal_type in self.results:
            print(f"{athlete.name} from {athlete.country.name} won {medal_type} medal")


# Example Usage:

# Creating countries
usa = Country("USA")
japan = Country("Japan")
china = Country("China")
brazil = Country("Brazil")
russia = Country("Russia")
kenya = Country("Kenya")

# Creating athletes
athlete1 = Athlete("Michael Phelps", usa)
athlete2 = Athlete("Simone Biles", usa)
athlete3 = Athlete("Naomi Osaka", japan)
athlete4 = Athlete("Sun Yang", china)
athlete5 = Athlete("Usain Bolt", kenya)
athlete6 = Athlete("Allyson Felix", usa)
athlete7 = Athlete("Yelena Isinbayeva", russia)
athlete8 = Athlete("Gabriel Medina", brazil)

# Adding athletes to countries
usa.add_athlete(athlete1)
usa.add_athlete(athlete2)
usa.add_athlete(athlete6)
japan.add_athlete(athlete3)
china.add_athlete(athlete4)
kenya.add_athlete(athlete5)
russia.add_athlete(athlete7)
brazil.add_athlete(athlete8)

# Creating events
swimming = Event("Swimming")
gymnastics = Event("Gymnastics")
tennis = Event("Tennis")
track_and_field = Event("Track and Field")
surfing = Event("Surfing")
pole_vault = Event("Pole Vault")

# Adding results to events
swimming.add_result(athlete1, 'gold')  # Michael Phelps wins gold
gymnastics.add_result(athlete2, 'silver')  # Simone Biles wins silver
gymnastics.add_result(athlete3, 'gold')  # Naomi Osaka wins gold

track_and_field.add_result(athlete5, 'gold')  # Usain Bolt wins gold
track_and_field.add_result(athlete6, 'silver')  # Allyson Felix wins silver
pole_vault.add_result(athlete7, 'gold')  # Yelena Isinbayeva wins gold

surfing.add_result(athlete8, 'gold')  # Gabriel Medina wins gold
tennis.add_result(athlete3, 'bronze')  # Naomi Osaka wins bronze

# Displaying results
swimming.show_results()
gymnastics.show_results()
track_and_field.show_results()
surfing.show_results()
pole_vault.show_results()
tennis.show_results()

# Display total medals for countries
print("\nTotal Medal Count:")
print(usa)
print(japan)
print(china)
print(kenya)
print(russia)
print(brazil)

