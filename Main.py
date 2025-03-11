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
                [Destatis](https://www-genesis.destatis.de/datenbank/online/statistic/41321/table/41321-0001/table-toolbar#filter=JTdCJTIyaGlkZUVtcHR5Q29scyUyMiUzQWZhbHNlJTJDJTIyaGlkZUVtcHR5Um93cyUyMiUzQWZhbHNlJTJDJTIyY2FwdGlvbiUyMiUzQSU1QiU3QiUyMnZhcmlhYmxlSWQlMjIlM0ElMjI0MTMyMSUyMiUyQyUyMmlkJTIyJTNBJTIyZmlsdGVyLjAlMjIlMkMlMjJ2YWx1ZXNJZHMlMjIlM0ElNUIlMjI0MTMyMSUyMiU1RCUyQyUyMmNoaWxkcmVuJTIyJTNBJTVCJTdCJTIydmFyaWFibGVJZCUyMiUzQSUyMkRJTlNHJTIyJTJDJTIyaWQlMjIlM0ElMjJmaWx0ZXIuMC4wJTIyJTJDJTIydmFsdWVzSWRzJTIyJTNBJTVCJTIyREclMjIlNUQlMkMlMjJjaGlsZHJlbiUyMiUzQSU1QiU1RCUyQyUyMnNob3dBc0ludGVybGluZSUyMiUzQWZhbHNlJTJDJTIyc2hvd1ZhcmlhYmxlJTIyJTNBZmFsc2UlMkMlMjJzaG93VmFyaWFibGVWYWx1ZSUyMiUzQSU1QiUyMkxBQkVMJTIyJTVEJTJDJTIyc29ydCUyMiUzQSUyMkNvZGVBc2MlMjIlMkMlMjJpc0hpZGRlbiUyMiUzQWZhbHNlJTJDJTIyYmxvY2tDb2RlJTIyJTNBJTIydjElMjIlMkMlMjJwb3NzaWJsZVBsYWNlcyUyMiUzQSU1QiU1RCU3RCU1RCUyQyUyMnNob3dBc0ludGVybGluZSUyMiUzQWZhbHNlJTJDJTIyaXNIaWRkZW4lMjIlM0FmYWxzZSUyQyUyMmJsb2NrQ29kZSUyMiUzQSUyMnMxJTIyJTJDJTIycG9zc2libGVQbGFjZXMlMjIlM0ElNUIlNUQlN0QlNUQlMkMlMjJyb3dIZWFkZXIlMjIlM0ElNUIlN0IlMjJ2YXJpYWJsZUlkJTIyJTNBJTIySkFIUiUyMiUyQyUyMmlkJTIyJTNBJTIycm93VGl0bGUuMCUyMiUyQyUyMnZhbHVlc0lkcyUyMiUzQSU1QiUyMjIwMjQlMjIlMkMlMjIyMDIzJTIyJTVEJTJDJTIyY2hpbGRyZW4lMjIlM0ElNUIlN0IlMjJ2YXJpYWJsZUlkJTIyJTNBJTIyVElFUkcxJTIyJTJDJTIyaWQlMjIlM0ElMjJyb3dUaXRsZS4wLjAlMjIlMkMlMjJ2YWx1ZXNJZHMlMjIlM0ElNUIlMjJUSUVSQVJUNTA4JTIyJTJDJTIyVElFUkFSVDUwNDklMjIlMkMlMjJUSUVSQVJUNTA0JTIyJTJDJTIyVElFUkFSVDUwNDElMjIlMkMlMjJUSUVSQVJUNTA1OSUyMiUyQyUyMlRJRVJBUlQ1MDUlMjIlMkMlMjJUSUVSQVJUNTA1MSUyMiUyQyUyMlRJRVJBUlQ1MDklMjIlMkMlMjJUSUVSQVJUNTEyMSUyMiUyQyUyMlRJRVJBUlQ1MTExJTIyJTJDJTIyVElFUkFSVDUxMzElMjIlMkMlMjJUSUVSQVJUNTE2MSUyMiUyQyUyMiUyNVRPVEFMJTI1JTIyJTVEJTJDJTIyY2hpbGRyZW4lMjIlM0ElNUIlNUQlMkMlMjJzaG93QXNJbnRlcmxpbmUlMjIlM0FmYWxzZSUyQyUyMnNob3dWYXJpYWJsZSUyMiUzQXRydWUlMkMlMjJzaG93VmFyaWFibGVWYWx1ZSUyMiUzQSU1QiUyMkxBQkVMJTIyJTVEJTJDJTIyaXNIaWRkZW4lMjIlM0FmYWxzZSUyQyUyMmJsb2NrQ29kZSUyMiUzQSUyMnYzJTIyJTJDJTIycG9zc2libGVQbGFjZXMlMjIlM0ElNUIlN0IlMjJwcmV2UGFyZW50JTIyJTNBJTdCJTIyYmxvY2tDb2RlJTIyJTNBJTIydjIlMjIlMkMlMjJpZCUyMiUzQSUyMnJvd1RpdGxlLjAlMjIlN0QlMkMlMjJlbGVtZW50QWJvdmUlMjIlM0FudWxsJTJDJTIyZWxlbWVudEJlbG93JTIyJTNBJTdCJTIyYmxvY2tDb2RlJTIyJTNBJTIyYzElMjIlMkMlMjJpZCUyMiUzQSUyMmNvbFRpdGxlLjAlMjIlN0QlMkMlMjJuZXdTaWJsaW5nSW5kZXglMjIlM0EwJTJDJTIyaGFzVHJhbnNwb3NlUGFydCUyMiUzQXRydWUlN0QlNUQlN0QlNUQlMkMlMjJzaG93QXNJbnRlcmxpbmUlMjIlM0F0cnVlJTJDJTIyc2hvd1ZhcmlhYmxlJTIyJTNBdHJ1ZSUyQyUyMnNob3dWYXJpYWJsZVZhbHVlJTIyJTNBJTVCJTIyTEFCRUwlMjIlNUQlMkMlMjJpc0hpZGRlbiUyMiUzQWZhbHNlJTJDJTIyYmxvY2tDb2RlJTIyJTNBJTIydjIlMjIlMkMlMjJwb3NzaWJsZVBsYWNlcyUyMiUzQSU1QiU1RCU3RCU1RCUyQyUyMmNvbHVtbkhlYWRlciUyMiUzQSU1QiU3QiUyMnZhcmlhYmxlSWQlMjIlM0ElMjJCUlQwMDElMjIlMkMlMjJpZCUyMiUzQSUyMmNvbFRpdGxlLjAlMjIlMkMlMjJ2YWx1ZXNJZHMlMjIlM0ElNUIlMjJRTVUlMjIlNUQlMkMlMjJjaGlsZHJlbiUyMiUzQSU1QiU1RCUyQyUyMnNob3dBc0ludGVybGluZSUyMiUzQWZhbHNlJTJDJTIyaXNIaWRkZW4lMjIlM0FmYWxzZSUyQyUyMmJsb2NrQ29kZSUyMiUzQSUyMmMxJTIyJTJDJTIycG9zc2libGVQbGFjZXMlMjIlM0ElNUIlN0IlMjJlbGVtZW50QWJvdmUlMjIlM0ElN0IlMjJibG9ja0NvZGUlMjIlM0ElMjJjMiUyMiUyQyUyMmlkJTIyJTNBJTIyY29sVGl0bGUuMSUyMiU3RCUyQyUyMmVsZW1lbnRCZWxvdyUyMiUzQSU3QiUyMmJsb2NrQ29kZSUyMiUzQSUyMmMzJTIyJTJDJTIyaWQlMjIlM0ElMjJjb2xUaXRsZS4yJTIyJTdEJTJDJTIybmV3U2libGluZ0luZGV4JTIyJTNBMiUyQyUyMmhhc1RyYW5zcG9zZVBhcnQlMjIlM0FmYWxzZSU3RCUyQyU3QiUyMmVsZW1lbnRBYm92ZSUyMiUzQSU3QiUyMmJsb2NrQ29kZSUyMiUzQSUyMmMzJTIyJTJDJTIyaWQlMjIlM0ElMjJjb2xUaXRsZS4yJTIyJTdEJTJDJTIyZWxlbWVudEJlbG93JTIyJTNBJTdCJTIyYmxvY2tDb2RlJTIyJTNBJTIyYzQlMjIlMkMlMjJpZCUyMiUzQSUyMmNvbFRpdGxlLjMlMjIlN0QlMkMlMjJuZXdTaWJsaW5nSW5kZXglMjIlM0EzJTJDJTIyaGFzVHJhbnNwb3NlUGFydCUyMiUzQWZhbHNlJTdEJTJDJTdCJTIyZWxlbWVudEFib3ZlJTIyJTNBJTdCJTIyYmxvY2tDb2RlJTIyJTNBJTIyYzQlMjIlMkMlMjJpZCUyMiUzQSUyMmNvbFRpdGxlLjMlMjIlN0QlMkMlMjJlbGVtZW50QmVsb3clMjIlM0ElN0IlMjJibG9ja0NvZGUlMjIlM0ElMjJjNSUyMiUyQyUyMmlkJTIyJTNBJTIyY29sVGl0bGUuNCUyMiU3RCUyQyUyMm5ld1NpYmxpbmdJbmRleCUyMiUzQTQlMkMlMjJoYXNUcmFuc3Bvc2VQYXJ0JTIyJTNBZmFsc2UlN0QlMkMlN0IlMjJlbGVtZW50QWJvdmUlMjIlM0ElN0IlMjJibG9ja0NvZGUlMjIlM0ElMjJjNSUyMiUyQyUyMmlkJTIyJTNBJTIyY29sVGl0bGUuNCUyMiU3RCUyQyUyMmVsZW1lbnRCZWxvdyUyMiUzQW51bGwlMkMlMjJuZXdTaWJsaW5nSW5kZXglMjIlM0E1JTJDJTIyaGFzVHJhbnNwb3NlUGFydCUyMiUzQWZhbHNlJTdEJTVEJTdEJTJDJTdCJTIydmFyaWFibGVJZCUyMiUzQSUyMkJSVDAwMiUyMiUyQyUyMmlkJTIyJTNBJTIyY29sVGl0bGUuMSUyMiUyQyUyMnZhbHVlc0lkcyUyMiUzQSU1QiUyMlFNVSUyMiU1RCUyQyUyMmNoaWxkcmVuJTIyJTNBJTVCJTVEJTJDJTIyc2hvd0FzSW50ZXJsaW5lJTIyJTNBZmFsc2UlMkMlMjJpc0hpZGRlbiUyMiUzQWZhbHNlJTJDJTIyYmxvY2tDb2RlJTIyJTNBJTIyYzIlMjIlMkMlMjJwb3NzaWJsZVBsYWNlcyUyMiUzQSU1QiU3QiUyMmVsZW1lbnRBYm92ZSUyMiUzQW51bGwlMkMlMjJlbGVtZW50QmVsb3clMjIlM0ElN0IlMjJibG9ja0NvZGUlMjIlM0ElMjJjMSUyMiUyQyUyMmlkJTIyJTNBJTIyY29sVGl0bGUuMCUyMiU3RCUyQyUyMm5ld1NpYmxpbmdJbmRleCUyMiUzQTAlMkMlMjJoYXNUcmFuc3Bvc2VQYXJ0JTIyJTNBZmFsc2UlN0QlMkMlN0IlMjJlbGVtZW50QWJvdmUlMjIlM0ElN0IlMjJibG9ja0NvZGUlMjIlM0ElMjJjMyUyMiUyQyUyMmlkJTIyJTNBJTIyY29sVGl0bGUuMiUyMiU3RCUyQyUyMmVsZW1lbnRCZWxvdyUyMiUzQSU3QiUyMmJsb2NrQ29kZSUyMiUzQSUyMmM0JTIyJTJDJTIyaWQlMjIlM0ElMjJjb2xUaXRsZS4zJTIyJTdEJTJDJTIybmV3U2libGluZ0luZGV4JTIyJTNBMyUyQyUyMmhhc1RyYW5zcG9zZVBhcnQlMjIlM0FmYWxzZSU3RCUyQyU3QiUyMmVsZW1lbnRBYm92ZSUyMiUzQSU3QiUyMmJsb2NrQ29kZSUyMiUzQSUyMmM0JTIyJTJDJTIyaWQlMjIlM0ElMjJjb2xUaXRsZS4zJTIyJTdEJTJDJTIyZWxlbWVudEJlbG93JTIyJTNBJTdCJTIyYmxvY2tDb2RlJTIyJTNBJTIyYzUlMjIlMkMlMjJpZCUyMiUzQSUyMmNvbFRpdGxlLjQlMjIlN0QlMkMlMjJuZXdTaWJsaW5nSW5kZXglMjIlM0E0JTJDJTIyaGFzVHJhbnNwb3NlUGFydCUyMiUzQWZhbHNlJTdEJTJDJTdCJTIyZWxlbWVudEFib3ZlJTIyJTNBJTdCJTIyYmxvY2tDb2RlJTIyJTNBJTIyYzUlMjIlMkMlMjJpZCUyMiUzQSUyMmNvbFRpdGxlLjQlMjIlN0QlMkMlMjJlbGVtZW50QmVsb3clMjIlM0FudWxsJTJDJTIybmV3U2libGluZ0luZGV4JTIyJTNBNSUyQyUyMmhhc1RyYW5zcG9zZVBhcnQlMjIlM0FmYWxzZSU3RCU1RCU3RCUyQyU3QiUyMnZhcmlhYmxlSWQlMjIlM0ElMjJCUlUwMDElMjIlMkMlMjJpZCUyMiUzQSUyMmNvbFRpdGxlLjIlMjIlMkMlMjJ2YWx1ZXNJZHMlMjIlM0ElNUIlMjJRTVUlMjIlNUQlMkMlMjJjaGlsZHJlbiUyMiUzQSU1QiU1RCUyQyUyMnNob3dBc0ludGVybGluZSUyMiUzQWZhbHNlJTJDJTIyaXNIaWRkZW4lMjIlM0FmYWxzZSUyQyUyMmJsb2NrQ29kZSUyMiUzQSUyMmMzJTIyJTJDJTIycG9zc2libGVQbGFjZXMlMjIlM0ElNUIlN0IlMjJlbGVtZW50QWJvdmUlMjIlM0FudWxsJTJDJTIyZWxlbWVudEJlbG93JTIyJTNBJTdCJTIyYmxvY2tDb2RlJTIyJTNBJTIyYzElMjIlMkMlMjJpZCUyMiUzQSUyMmNvbFRpdGxlLjAlMjIlN0QlMkMlMjJuZXdTaWJsaW5nSW5kZXglMjIlM0EwJTJDJTIyaGFzVHJhbnNwb3NlUGFydCUyMiUzQWZhbHNlJTdEJTJDJTdCJTIyZWxlbWVudEFib3ZlJTIyJTNBJTdCJTIyYmxvY2tDb2RlJTIyJTNBJTIyYzElMjIlMkMlMjJpZCUyMiUzQSUyMmNvbFRpdGxlLjAlMjIlN0QlMkMlMjJlbGVtZW50QmVsb3clMjIlM0ElN0IlMjJibG9ja0NvZGUlMjIlM0ElMjJjMiUyMiUyQyUyMmlkJTIyJTNBJTIyY29sVGl0bGUuMSUyMiU3RCUyQyUyMm5ld1NpYmxpbmdJbmRleCUyMiUzQTElMkMlMjJoYXNUcmFuc3Bvc2VQYXJ0JTIyJTNBZmFsc2UlN0QlMkMlN0IlMjJlbGVtZW50QWJvdmUlMjIlM0ElN0IlMjJibG9ja0NvZGUlMjIlM0ElMjJjNCUyMiUyQyUyMmlkJTIyJTNBJTIyY29sVGl0bGUuMyUyMiU3RCUyQyUyMmVsZW1lbnRCZWxvdyUyMiUzQSU3QiUyMmJsb2NrQ29kZSUyMiUzQSUyMmM1JTIyJTJDJTIyaWQlMjIlM0ElMjJjb2xUaXRsZS40JTIyJTdEJTJDJTIybmV3U2libGluZ0luZGV4JTIyJTNBNCUyQyUyMmhhc1RyYW5zcG9zZVBhcnQlMjIlM0FmYWxzZSU3RCUyQyU3QiUyMmVsZW1lbnRBYm92ZSUyMiUzQSU3QiUyMmJsb2NrQ29kZSUyMiUzQSUyMmM1JTIyJTJDJTIyaWQlMjIlM0ElMjJjb2xUaXRsZS40JTIyJTdEJTJDJTIyZWxlbWVudEJlbG93JTIyJTNBbnVsbCUyQyUyMm5ld1NpYmxpbmdJbmRleCUyMiUzQTUlMkMlMjJoYXNUcmFuc3Bvc2VQYXJ0JTIyJTNBZmFsc2UlN0QlNUQlN0QlMkMlN0IlMjJ2YXJpYWJsZUlkJTIyJTNBJTIyQlJUMDAzJTIyJTJDJTIyaWQlMjIlM0ElMjJjb2xUaXRsZS4zJTIyJTJDJTIydmFsdWVzSWRzJTIyJTNBJTVCJTIyUU1VJTIyJTVEJTJDJTIyY2hpbGRyZW4lMjIlM0ElNUIlNUQlMkMlMjJzaG93QXNJbnRlcmxpbmUlMjIlM0FmYWxzZSUyQyUyMmlzSGlkZGVuJTIyJTNBZmFsc2UlMkMlMjJibG9ja0NvZGUlMjIlM0ElMjJjNCUyMiUyQyUyMnBvc3NpYmxlUGxhY2VzJTIyJTNBJTVCJTdCJTIyZWxlbWVudEFib3ZlJTIyJTNBbnVsbCUyQyUyMmVsZW1lbnRCZWxvdyUyMiUzQSU3QiUyMmJsb2NrQ29kZSUyMiUzQSUyMmMxJTIyJTJDJTIyaWQlMjIlM0ElMjJjb2xUaXRsZS4wJTIyJTdEJTJDJTIybmV3U2libGluZ0luZGV4JTIyJTNBMCUyQyUyMmhhc1RyYW5zcG9zZVBhcnQlMjIlM0FmYWxzZSU3RCUyQyU3QiUyMmVsZW1lbnRBYm92ZSUyMiUzQSU3QiUyMmJsb2NrQ29kZSUyMiUzQSUyMmMxJTIyJTJDJTIyaWQlMjIlM0ElMjJjb2xUaXRsZS4wJTIyJTdEJTJDJTIyZWxlbWVudEJlbG93JTIyJTNBJTdCJTIyYmxvY2tDb2RlJTIyJTNBJTIyYzIlMjIlMkMlMjJpZCUyMiUzQSUyMmNvbFRpdGxlLjElMjIlN0QlMkMlMjJuZXdTaWJsaW5nSW5kZXglMjIlM0ExJTJDJTIyaGFzVHJhbnNwb3NlUGFydCUyMiUzQWZhbHNlJTdEJTJDJTdCJTIyZWxlbWVudEFib3ZlJTIyJTNBJTdCJTIyYmxvY2tDb2RlJTIyJTNBJTIyYzIlMjIlMkMlMjJpZCUyMiUzQSUyMmNvbFRpdGxlLjElMjIlN0QlMkMlMjJlbGVtZW50QmVsb3clMjIlM0ElN0IlMjJibG9ja0NvZGUlMjIlM0ElMjJjMyUyMiUyQyUyMmlkJTIyJTNBJTIyY29sVGl0bGUuMiUyMiU3RCUyQyUyMm5ld1NpYmxpbmdJbmRleCUyMiUzQTIlMkMlMjJoYXNUcmFuc3Bvc2VQYXJ0JTIyJTNBZmFsc2UlN0QlMkMlN0IlMjJlbGVtZW50QWJvdmUlMjIlM0ElN0IlMjJibG9ja0NvZGUlMjIlM0ElMjJjNSUyMiUyQyUyMmlkJTIyJTNBJTIyY29sVGl0bGUuNCUyMiU3RCUyQyUyMmVsZW1lbnRCZWxvdyUyMiUzQW51bGwlMkMlMjJuZXdTaWJsaW5nSW5kZXglMjIlM0E1JTJDJTIyaGFzVHJhbnNwb3NlUGFydCUyMiUzQWZhbHNlJTdEJTVEJTdEJTJDJTdCJTIydmFyaWFibGVJZCUyMiUzQSUyMktVRTAwMSUyMiUyQyUyMmlkJTIyJTNBJTIyY29sVGl0bGUuNCUyMiUyQyUyMnZhbHVlc0lkcyUyMiUzQSU1QiUyMlFNVSUyMiU1RCUyQyUyMmNoaWxkcmVuJTIyJTNBJTVCJTVEJTJDJTIyc2hvd0FzSW50ZXJsaW5lJTIyJTNBZmFsc2UlMkMlMjJpc0hpZGRlbiUyMiUzQWZhbHNlJTJDJTIyYmxvY2tDb2RlJTIyJTNBJTIyYzUlMjIlMkMlMjJwb3NzaWJsZVBsYWNlcyUyMiUzQSU1QiU3QiUyMmVsZW1lbnRBYm92ZSUyMiUzQW51bGwlMkMlMjJlbGVtZW50QmVsb3clMjIlM0ElN0IlMjJibG9ja0NvZGUlMjIlM0ElMjJjMSUyMiUyQyUyMmlkJTIyJTNBJTIyY29sVGl0bGUuMCUyMiU3RCUyQyUyMm5ld1NpYmxpbmdJbmRleCUyMiUzQTAlMkMlMjJoYXNUcmFuc3Bvc2VQYXJ0JTIyJTNBZmFsc2UlN0QlMkMlN0IlMjJlbGVtZW50QWJvdmUlMjIlM0ElN0IlMjJibG9ja0NvZGUlMjIlM0ElMjJjMSUyMiUyQyUyMmlkJTIyJTNBJTIyY29sVGl0bGUuMCUyMiU3RCUyQyUyMmVsZW1lbnRCZWxvdyUyMiUzQSU3QiUyMmJsb2NrQ29kZSUyMiUzQSUyMmMyJTIyJTJDJTIyaWQlMjIlM0ElMjJjb2xUaXRsZS4xJTIyJTdEJTJDJTIybmV3U2libGluZ0luZGV4JTIyJTNBMSUyQyUyMmhhc1RyYW5zcG9zZVBhcnQlMjIlM0FmYWxzZSU3RCUyQyU3QiUyMmVsZW1lbnRBYm92ZSUyMiUzQSU3QiUyMmJsb2NrQ29kZSUyMiUzQSUyMmMyJTIyJTJDJTIyaWQlMjIlM0ElMjJjb2xUaXRsZS4xJTIyJTdEJTJDJTIyZWxlbWVudEJlbG93JTIyJTNBJTdCJTIyYmxvY2tDb2RlJTIyJTNBJTIyYzMlMjIlMkMlMjJpZCUyMiUzQSUyMmNvbFRpdGxlLjIlMjIlN0QlMkMlMjJuZXdTaWJsaW5nSW5kZXglMjIlM0EyJTJDJTIyaGFzVHJhbnNwb3NlUGFydCUyMiUzQWZhbHNlJTdEJTJDJTdCJTIyZWxlbWVudEFib3ZlJTIyJTNBJTdCJTIyYmxvY2tDb2RlJTIyJTNBJTIyYzMlMjIlMkMlMjJpZCUyMiUzQSUyMmNvbFRpdGxlLjIlMjIlN0QlMkMlMjJlbGVtZW50QmVsb3clMjIlM0ElN0IlMjJibG9ja0NvZGUlMjIlM0ElMjJjNCUyMiUyQyUyMmlkJTIyJTNBJTIyY29sVGl0bGUuMyUyMiU3RCUyQyUyMm5ld1NpYmxpbmdJbmRleCUyMiUzQTMlMkMlMjJoYXNUcmFuc3Bvc2VQYXJ0JTIyJTNBZmFsc2UlN0QlNUQlN0QlNUQlMkMlMjJmaXhGaXJzdENvbHVtbnMlMjIlM0FmYWxzZSU3RA==)
                """)

