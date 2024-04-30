import streamlit as st

if 'og_txt' not in st.session_state:
    st.session_state['og_txt'] = ''
    st.session_state['display_txt'] = ''
    st.session_state['freq'] = {}
 
    for i in range (97,123):
        char = chr(i)
        st.session_state[char] = ''


def update_data(text):

    text_lowercase = text.lower()
    
    st.session_state['og_txt'] = text_lowercase
    st.session_state['display_txt'] = text_lowercase

    st.session_state['freq'].clear()

    temp_dict = {}

    
    for i in range (97,123):
        char = chr(i)
        count = text_lowercase.count(char)

        if count != 0:
            temp_dict[char] = count

    st.session_state['freq'] = temp_dict






def do_smt():
    temp = st.session_state['og_txt']



    for i in range (97,123):
        char = chr(i)
        if st.session_state[char] == '':
            st.session_state[char] = char
        else:
            #formatted_char = ":orange[" + st.session_state[char].capitalize() + "]"
            formatted_char = st.session_state[char].capitalize()
            temp = temp.replace(char, formatted_char)

    st.session_state['display_txt'] = temp


left, right = st.columns([5,1])

with left:
    with st.form("my_form"):
        text = st.text_area('input text here:')

        if st.form_submit_button("Submit"):
            update_data(text)


    with st.container(border=True):
        line_split = st.session_state['display_txt'].splitlines()
        for line in line_split:
            st.write(line)



    row_1 = st.columns(13)

    for i in range(0,13):
        with row_1[i]:
            char = chr(i+97)
            cap_char = chr(i+97-32)
            st.session_state[char] = st.text_input(cap_char,max_chars=1)


    row_2 = st.columns(13)

    for i in range(0,13):
        with row_2[i]:
            char = chr(i+97+13)
            cap_char = chr(i+97+13-32)
            st.session_state[char] = st.text_input(cap_char,max_chars=1)

    st.button("update", on_click=do_smt)

with right:
    st.image("freq_chart.jpg")
    st.write(st.session_state['freq'])
    
