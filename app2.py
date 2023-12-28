import streamlit as st

st.set_page_config(
    page_title="10-year Cancer Prediction App",
    page_icon="favicon.png",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={'About': "This is a 10-year cancer prediction app!"}
)

st.write(":elephant:")

st.image("fight_cancer.png", use_column_width=True, caption="Together we shall win Cancer 🦾🦾🦾")

st.divider()

st.write("### Your predictions will appear below")

with st.sidebar:
  st.write(
  """<p style="text-align:justify">Paste your data and click the <b>Predict</b> button to predict your 10-year Cancer risk</p>
  """, unsafe_allow_html=True
  )
  name = st.text_input("Name (Optional)", placeholder="Name")
  sex = st.text_input("Sex (Required)", placeholder="Male or Female or their initials").lower()
  bmi = st.number_input("BMI (Required)", value=None, placeholder="BMI")
  button = st.button("**Predict**")

def calculate():
  if bmi > 25 and sex in {"male", "m"}:
    return "You have High Risk (> 90%) of Cancer"
  elif bmi > 25 and sex in {"female", "f"}:
    return "You have Medium Risk (> 60%) of Cancer"
  elif bmi < 25 and sex in {"male", "m"}:
    return "You have Low Risk (< 50%) of Cancer"
  elif bmi < 25 and sex in {"female", "f"}:
    return "You have Low Risk (> 40%) of Cancer"
  

try:
  if button:
    result = calculate()
    if result is not None:
      if not name:
        st.write(result)
      else:
        st.write(f"{name}, {result}")
    else:
      st.error("Sex must be `Male` or `Female` or their initials. Note: It is case insensitive")
except:
  st.error("Something went wrong 😡😡😡", icon="🚨")