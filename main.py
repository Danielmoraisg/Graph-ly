import streamlit as st
from States import _get_state
#paginas
import home
import bar
import line
st.set_page_config(page_title="Graph-ly",page_icon=":fire:",layout="centered",initial_sidebar_state="auto")
state = _get_state()

PAGES = {
	"Homepage":home,
    "Grafico de linhas": line,
    "Grafico de barras": bar
}
st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app(state)
state.sync()