import streamlit as st


st.set_page_config(
    page_title="Data Detective", page_icon='🕵️‍♀️',
    layout="wide",  
    #initial_sidebar_state="expanded" 
)

st.code("""
                                                                                                                                                                                          

▓█████▄  ▄▄▄     ▄▄▄█████▓ ▄▄▄         ▓█████▄ ▓█████▄▄▄█████▓▓█████  ▄████▄  ▄▄▄█████▓ ██▓ ██▒   █▓▓█████ 
▒██▀ ██▌▒████▄   ▓  ██▒ ▓▒▒████▄       ▒██▀ ██▌▓█   ▀▓  ██▒ ▓▒▓█   ▀ ▒██▀ ▀█  ▓  ██▒ ▓▒▓██▒▓██░   █▒▓█   ▀ 
░██   █▌▒██  ▀█▄ ▒ ▓██░ ▒░▒██  ▀█▄     ░██   █▌▒███  ▒ ▓██░ ▒░▒███   ▒▓█    ▄ ▒ ▓██░ ▒░▒██▒ ▓██  █▒░▒███   
░▓█▄   ▌░██▄▄▄▄██░ ▓██▓ ░ ░██▄▄▄▄██    ░▓█▄   ▌▒▓█  ▄░ ▓██▓ ░ ▒▓█  ▄ ▒▓▓▄ ▄██▒░ ▓██▓ ░ ░██░  ▒██ █░░▒▓█  ▄ 
░▒████▓  ▓█   ▓██▒ ▒██▒ ░  ▓█   ▓██▒   ░▒████▓ ░▒████▒ ▒██▒ ░ ░▒████▒▒ ▓███▀ ░  ▒██▒ ░ ░██░   ▒▀█░  ░▒████▒
 ▒▒▓  ▒  ▒▒   ▓▒█░ ▒ ░░    ▒▒   ▓▒█░    ▒▒▓  ▒ ░░ ▒░ ░ ▒ ░░   ░░ ▒░ ░░ ░▒ ▒  ░  ▒ ░░   ░▓     ░ ▐░  ░░ ▒░ ░
 ░ ▒  ▒   ▒   ▒▒ ░   ░      ▒   ▒▒ ░    ░ ▒  ▒  ░ ░  ░   ░     ░ ░  ░  ░  ▒       ░     ▒ ░   ░ ░░   ░ ░  ░
 ░ ░  ░   ░   ▒    ░        ░   ▒       ░ ░  ░    ░    ░         ░   ░          ░       ▒ ░     ░░     ░   
   ░          ░  ░              ░  ░      ░       ░  ░           ░  ░░ ░                ░        ░     ░  ░
 ░                                      ░                            ░                          ░          
                                                                                                                                                                     
                                                                                                                                                                       
""", language="python")


st.header("What indicator is being compared between Germany 🇩🇪 and Japan 🇯🇵 in this line chart?")


tab1, tab2 = st.tabs(["Cryptic", "Decoded"])

with tab1:
    st.image("assets/question.png", width=800)
with tab2:
    st.image("assets/answer.png", width=800)


col1, col2 = st.columns(2)
with col1:
    if st.button("Win"):
        st.balloons()
with col2:
    if st.button("Lose"):
        st.snow()

with st.expander("Data Source"):
    st.write("WORLD BANK GROUP: https://data.worldbank.org/indicator/SP.POP.TOTL")

st.divider()
st.header("What phenomenon has exhibited exponential growth over the past several decades?")
with st.expander("Explain normal vs. exponential scale"):
    st.success("""
            A normal (linear) scale uses equal intervals between values, 
            while an exponential (logarithmic) scale increases by orders of magnitude, 
            compressing large ranges of data and revealing patterns in values that span several orders of magnitude.
            """)


tab1, tab2 = st.tabs(["Cryptic", "Decoded"])

with tab1:
    st.components.v1.html(open("assets/question_exponential.html", "r").read(), height=500)
with tab2:
    st.components.v1.html(open("assets/answer_exponential.html", "r").read(), height=500)

col1, col2 = st.columns(2)
with col1:
    if st.button("Win", key="win_02"):
        st.balloons()
with col2:
    if st.button("Lose", key="lose_02"):
        st.snow()

with st.expander("Data Source"):
    st.write("Our World in Data: https://ourworldindata.org/grapher/transistors-per-microprocessor")
    st.success("""
               Moore's Law is the observation that the number of transistors 
               in an integrated circuit doubles approximately every two years 
               due to improvements in production. The law was first described in 1965 by Gordon E. Moore, 
               co-founder of Intel. In 1971, the Intel® 4004 processor had 2,300 transistors.
               """)
    st.image("assets/Intel_4004_first_microprocessor.webp", width=800)



