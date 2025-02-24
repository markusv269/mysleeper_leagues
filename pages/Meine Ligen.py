import streamlit as st

from sleeper_wrapper import League, Drafts, User

col1, col2 = st.columns(2)
with col1:
    insert_sleeper_name = st.text_input("Gib deinen sleeper-Usernamen ein:")
with col2:
    insert_year = st.text_input("Gib das Ligajahr ein:")

if insert_sleeper_name and insert_year:
    user = User(insert_sleeper_name)
    user_leagues = user.get_all_leagues(sport="nfl", season=insert_year)

    if not user_leagues:
        st.write("Keine Ligen gefunden.")
    else:
        for league in user_leagues:  # Falls es eine Liste ist
            st.write(f"{league.get('name')} ({league.get('league_id')})")