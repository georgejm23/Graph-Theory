import streamlit as st
import random
from PIL import Image

st.title('Graph Theory Project')

st.header('Game Description')

st.write('''This is a two player drinking game in which there are multiple shot glasses filled with clear liquids. 
         Some of the glasses are filled with salt water and the rest are filled with drinking water. The order in which the glasses are ordered is random.
         The goal is drink less salt water than the other player by choosing to either take or give a shot.
         If the player chooses to take a shot, they take the shot and get another turn. 
         If the player chooses to give a shot, their turn is over and the opposing player must take the shot.
         If the player chooses to take a shot and it is salt water, their turn ends.''')

st.divider()

if 'difficulty' not in st.session_state:
    st.session_state.difficulty = '0'

if 'num_water' not in st.session_state:
    st.session_state.num_water = 0

if 'num_shot' not in st.session_state:
    st.session_state.num_shot = 0

st.session_state.difficulty = st.radio('Select Difficulty', ['Easy', 'Medium', 'Hard', 'Extreme'], horizontal = True, index = 1)

if st.session_state.difficulty == 'Easy':
    st.session_state.num_water = 2
    st.session_state.num_shot = 1
elif st.session_state.difficulty == 'Medium':
    st.session_state.num_water = 3
    st.session_state.num_shot = 2
elif st.session_state.difficulty == 'Hard':
    st.session_state.num_water = 4
    st.session_state.num_shot = 3
elif st.session_state.difficulty == 'Extreme':
    st.session_state.num_water = 5
    st.session_state.num_shot = 4

st.session_state.total_shots = st.session_state.num_water + st.session_state.num_shot

st.divider()

if 'shot_list' not in st.session_state:
    st.session_state.shot_list = []

image = []

for i in range(st.session_state.total_shots):
    image.append('shot.jpg')

if 'count' not in st.session_state:
    st.session_state.count = 0

if st.button('Start Game'):
    st.image(image, width = 75)
    st.write(f'There are {st.session_state.num_water} shots filled with water and {st.session_state.num_shot} shots filled with salt water.')
    for i in range(st.session_state.num_water):
        st.session_state.shot_list.append('0')

    for i in range(st.session_state.num_shot):
        st.session_state.shot_list.append('1')
    random.shuffle(st.session_state.shot_list)

st.divider()

take = st.button('Take Shot')
give = st.button('Give Shot')

if 'player' not in st.session_state:
    st.session_state.player = '1'

if 'p1_score' not in st.session_state:
    st.session_state.p1_score = 0

if 'p2_score' not in st.session_state:
    st.session_state.p2_score = 0

if take:
    st.session_state.count += 1
    for i in range(st.session_state.count):
        if st.session_state.count >= st.session_state.total_shots:
            break
        del image[0]
        st.image(image, width = 75)
    if st.session_state.shot_list[st.session_state.count - 1] == '1':
        st.write('That was salt water!')
        if st.session_state.player == '1':
            st.session_state.player = '2'
            st.session_state.p1_score += 1
            st.write("Player 2's Turn")
        elif st.session_state.player == '2':
            st.session_state.player = '1'
            st.session_state.p2_score += 1
            st.write("Player 1's Turn")
    else:
        st.write('That was drinking water!')
        if st.session_state.player == '1':
            st.write("Player 1's Turn")
        elif st.session_state.player == '2':
            st.write("Player 2's Turn")
    
if give:
    st.session_state.count += 1
    for i in range(st.session_state.count):
        if st.session_state.count >= st.session_state.total_shots:
            break
        del image[0]
        st.image(image, width = 75)
    if st.session_state.shot_list[st.session_state.count - 1] == '1':
        st.write('That was salt water!')
        if st.session_state.player == '1':
            st.session_state.p2_score += 1
            st.session_state.player = '2'
            st.write("Player 2's Turn")
        elif st.session_state.player == '2':
            st.session_state.p1_score += 1
            st.session_state.player = '1'
            st.write("Player 1's Turn")
    else:
        st.write('That was drinking water!')
        if st.session_state.player == '1':
            st.session_state.player = '2'
            st.write("Player 2's Turn")
        elif st.session_state.player == '2':
            st.session_state.player = '1'
            st.write("Player 1's Turn")

st.divider()

if st.button('Finish Game'):
    st.divider()
    if st.session_state.p1_score > st.session_state.p2_score:
        st.title('Player 2 Wins!')
        st.balloons()
    elif st.session_state.p2_score > st.session_state.p1_score:
        st.title('Player 1 Wins!')
        st.balloons()
    else:
        st.title('Tie Game! Both players drank the same amount of salt water!')

    st.header('Score')
    st.subheader(f'Player 1: {st.session_state.p1_score} shots of salt water')
    st.subheader(f'Player 2: {st.session_state.p2_score} shots of salt water')
    del st.session_state.shot_list
    del st.session_state.count
    del st.session_state.player
    del st.session_state.p1_score
    del st.session_state.p2_score
    
    st.divider()

    decision_tree = Image.open('decision_tree.png')

    st.image(decision_tree)


