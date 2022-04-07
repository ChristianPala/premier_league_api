from main import TeamService
from main import PlayerService, Player
from datetime import date

# We have some missing players from Chelsea and Tottenham with our search by surname, let's examine the problems:


if __name__ == '__main__':

    # Client library method to get an id from any row in the database
    print(TeamService.find_ids(name="Chelsea FC"))
    print(TeamService.find_ids(name="Tottenham Hotspur F.C."))

    def fixes():
        # Azpilicueta was in the database but his surname was saved as his name
        updated_player = Player('César', "DF", 'Azpilicueta', nationality="Spain")
        PlayerService.update_item_by_id(39158, updated_player)

        # Hojberg had the wrong surname:
        updated_player = Player('Pierre-Emile', "MF", 'Højbjerg')
        PlayerService.update_item_by_id(43106, updated_player)

        # Reguilon was not in the database:
        new_player = Player("Sergios", "DF", "Reguilon", date(1996, 12, 16), "Spain", 178)
        PlayerService.add_item(new_player)


    fixes()
