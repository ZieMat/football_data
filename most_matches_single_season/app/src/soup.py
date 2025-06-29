from bs4 import BeautifulSoup

def test_soup():
    list_of_players = []
    list_of_clubs = []
    with open('sample_data.html', "r") as f:
        soup = BeautifulSoup(f, 'lxml')
        # players = soup.select(('table.items a[href*="/profil/spieler/"]'))
        # for player in players:
        #     list_of_players.append(player.text)
        player_rows = soup.select('table.items tr.odd, table.items tr.even')
        for row in player_rows:
            player_name = row.select_one('a[href*="/profil/spieler/"]').text
            position = row.select_one()
            club_data = row.select_one('td:has(a[href*="/startseite/verein/"])')
            club_name = club_data.find_all('a')[1].text.strip()
            list_of_players.append(player_name)
            list_of_clubs.append(club_name)

        print(list_of_players)
        print(list_of_clubs)

#### ZESCRAPOWAĆ CAŁĄ TABELĘ DO OSOBNYCH LIST ####