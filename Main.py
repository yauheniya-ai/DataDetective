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


col1, col2, col3 = st.columns(3)
with col1:
    if st.button("Win"):
        st.balloons()
with col2:
    if st.button("Lose"):
        st.snow()
with col3:
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


st.divider()
st.header("What metrics is being compared between these companies?")
with st.expander("Translate to German"):
    st.success("Welche Kennzahl wird zwischen diesen Unternehmen verglichen?")


tab1, tab2, tab3, tab4 = st.tabs(["Cryptic", "Hint 1", "Hint 2", "Decoded"])

with tab1:
    st.image("assets/question_functions.png", width=800)
with tab2:
    st.image("assets/hint1_functions.png", width=800)
with tab3:
    st.image("assets/hint2_functions.png", width=800)
with tab4:
    st.image("assets/answer_functions.png", width=800)

col1, col2, col3 = st.columns(3)
with col1:
    if st.button("Win", key="win_03"):
        st.balloons()
with col2:
    if st.button("Lose", key="lose_03"):
        st.snow()

with col3:
    with st.expander("Data Sources"):
        st.write("""
                [Apple Numbers](https://www.apple.com/au/mac/numbers/compatibility/functions.html#:~:text=250%2B%20Functions,Numbers%20couldn't%20be%20clearer.)

                [Google Spreadsheets](https://support.google.com/docs/table/25273?hl=en)

                [Microsoft Excel](https://support.microsoft.com/en-us/office/excel-functions-alphabetical-b3944572-255d-4efb-bb96-c6d90033e188)
                """)


st.divider()
st.header("Welche Kennzahl zur Versorgungssituation in Deutschland wird hier dargestellt?")
with st.expander("Translate to English"):
    st.success("Which key figure on the supply situation in Germany is shown here?")

tab1, tab2, tab3, tab4 = st.tabs(["Cryptic", "Hint 1", "Hint 2", "Decoded"])

with tab1:
    st.image("assets/question_tiere.png", width=800)
with tab2:
    st.image("assets/hint1_tiere.png", width=800)
with tab3:
    st.image("assets/hint2_tiere.png", width=800)
with tab4:
    st.image("assets/answer_tiere.png", width=800)

col1, col2, col3 = st.columns(3)
with col1:
    if st.button("Win", key="win_04"):
        st.balloons()
with col2:
    if st.button("Lose", key="lose_04"):
        st.snow()

with col3:
    with st.expander("Data Sources"):
        st.write("""
                [BLE](https://www.ble.de/SharedDocs/Downloads/DE/BZL/Daten-Berichte/Fleisch/2024BerichtFleisch.pdf?__blob=publicationFile&v=2), 
                [BMEL](https://www.bmel-statistik.de/ernaehrung/versorgungsbilanzen/fleisch), 
                [Destatis](https://www-genesis.destatis.de/datenbank/online/statistic/41321/details)
                """)





st.divider()
st.header("Which US transportation statistics does this treemap chart show, and which categories are hidden?")
with st.expander("Übersetze auf Deutsch"):
    st.success("Welche US-Verkehrsstatistik zeigt dieses Treemap-Diagramm, und welche Kategorien sind verborgen?")

tab1, tab2, tab3 = st.tabs(["Cryptic", "Hint", "Decoded"])

with tab1:
    st.components.v1.html(open("assets/question_autos.html", "r").read(), height=500)
with tab2:
    st.components.v1.html(open("assets/hint1_autos.html", "r").read(), height=500)
with tab3:
    st.components.v1.html(open("assets/answer_autos.html", "r").read(), height=500)


col1, col2, col3 = st.columns(3)
with col1:
    if st.button("Win", key="win_05"):
        st.balloons()
with col2:
    if st.button("Lose", key="lose_05"):
        st.snow()
with col3:
    with st.expander("Data Sources"):
        st.write("""
                [Alternative Fuels Data Center (AFDC)](https://afdc.energy.gov/vehicle-registration)
                """)
        

###################################################################################################################
st.divider()
st.header("Welche technologische Statistik wird in diesem Balkendiagramm zwischen verschiedenen Ländern verglichen?")

with st.expander("Translate to English"):
    st.success("Which technological statistic is being compared between different countries in this bar chart?")

tab1, tab2, tab3 = st.tabs(["Cryptic", "Hint", "Decoded"])

with tab1:
    st.image("assets/question_github_fixed.png", width=800)
with tab2:
    st.image("assets/hint_github_fixed.png", width=800)
with tab3:
    st.image("assets/answer_github_fixed.png", width=800)


col1, col2, col3 = st.columns(3)
with col1:
    if st.button("Win", key="win_06"):
        st.balloons()
with col2:
    if st.button("Lose", key="lose_06"):
        st.snow()
with col3:
    with st.expander("Data Sources"):
        st.write("""
                [reddit](https://www.reddit.com/r/dataisbeautiful/comments/1cliefe/the_economies_with_the_most_github_devs_per/)
                """)
        