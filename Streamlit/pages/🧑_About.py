import streamlit as st
from PIL import Image


st.set_page_config(
    page_title="About OpenEyes",
    page_icon="👀",
)

TeamMember1 = {
    "Name": "Adarsh Anand",
    "Role": "DSC Lead '22 | Foss Overflow Mentor | Postman Leader | MERN | 4⭐CC | IIT Goa CSE '24",
    "LinkedIn": "https://www.linkedin.com/in/adarsh-anand-iitgoa/",
    "GitHub": "https://github.com/adarshanand67",
    "description": "I am a Full-stack developer with a passion for problem-solving. I love working on backend and frontend projects, but my true love is React.js. I enjoy working on projects that are challenging and have the potential to make a positive impact on people's lives.",
}

TeamMember2 = {
    "Name": "Aniket Akshay Chaudhri",
    "Role": "Head @ Coding Club IIT Goa | Competitive Programmer | Web Developer | Android Developer | CSE @ IIT Goa",
    "LinkedIn": "https://www.linkedin.com/in/aniketchaudhri/",
    "GitHub": "https://github.com/AniketChaudhri/",
    "description": "I am a CSE pre-final year Undergrad at IIT Goa. I have experience in various Tech Domains such as Web Development, App Development, Deep Learning.",
}

# adarsh = Image.open("/Streamlit/adarsh.jpg")
# aniket = Image.open("/Streamlit/aniket.jpg")

# layout 2 cols
st.title("About OpenEyes")
col1, col2 = st.columns(2)

# create 2 cards showing the details
with col1:
    # display image located at ../adarsh.jpg
    # st.image(adarsh, width=200,caption="Adarsh Anand")
    st.header(TeamMember1["Name"])
    st.markdown(TeamMember1["Role"])
    st.markdown(f"[LinkedIn]({TeamMember1['LinkedIn']})")
    st.markdown(f"[GitHub]({TeamMember1['GitHub']})")
    st.write(TeamMember1["description"])

with col2:
    # st.image(TeamMember2["image"], width=200)
    # st.image(aniket, width=200,caption="Aniket Akshay Chaudhri")
    st.header(TeamMember2["Name"])
    st.markdown(TeamMember2["Role"])
    st.markdown(f"[LinkedIn]({TeamMember2['LinkedIn']})")
    st.markdown(f"[GitHub]({TeamMember2['GitHub']})")
    st.write(TeamMember2["description"])
