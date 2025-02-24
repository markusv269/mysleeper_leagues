import streamlit as st

from sleeper_wrapper import League, Drafts, User

col1, col2 = st.columns(2)
with col1:
    insert_sleeper_name = st.text_input("Gib deinen sleeper-Usernamen ein:")
with col2:
    insert_year = st.text_input("Gib das Ligajahr ein:")

if insert_sleeper_name and insert_year:
    user = User(insert_sleeper_name)
    user_name = user.get_display_name()
    user_data = user.get_user_id()
    user_leagues = user.get_all_leagues(sport="nfl", season=insert_year)

    if not user_leagues:
        st.write("Keine Ligen gefunden.")
    else:
        n_leagues = st.container()
        i = 0
        n_checkwinner = 0
        for league in user_leagues:  # Falls es eine Liste ist
            league_id = League(league.get('league_id'))
            rosters = league_id.get_rosters()
            league_data = league_id.get_league()
            league_winner = league_data["metadata"].get("latest_league_winner_roster_id", 0)
            map = league_id.map_rosterid_to_ownerid(rosters)
            check_winner = map.get(int(league_winner)) == str(user_data)
            if check_winner:
                n_checkwinner += 1
            i += 1
            st.write(f"{i}. {league.get('name')} (League-ID: {league.get('league_id')})")
            if check_winner:
                st.write("**Leaguewinner!!!**")
            # st.write(league_data)
        n_leagues.write(f"**{user_name} ist {insert_year} in {i} Ligen aktiv und hat {n_checkwinner} gewonnen!**")