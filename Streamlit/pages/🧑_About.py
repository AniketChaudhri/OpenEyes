import streamlit as st


st.set_page_config(
    page_title="About OpenEyes",
    page_icon="👀",
)

TeamMember1 = {
    "Name": "Adarsh Anand",
    "image": "https://avatars.githubusercontent.com/u/73928744?v=4",
    "Role": "DSC Lead '22 | Foss Overflow Mentor | Postman Leader | MERN | 4⭐CC | IIT Goa CSE '24",
    "LinkedIn": "https://www.linkedin.com/in/adarsh-anand-iitgoa/",
    "GitHub": "https://github.com/adarshanand67",
    "description": "I am a Full-stack developer with a passion for problem-solving. I love working on backend and frontend projects, but my true love is React.js. I enjoy working on projects that are challenging and have the potential to make a positive impact on people's lives.",
}

TeamMember2 = {
    "Name": "Aniket Akshay Chaudhri",
    "image": "https://avatars.githubusercontent.com/u/79798301?v=4",
    "Role": "Head @ Coding Club IIT Goa | Competitive Programmer | Web Developer | Android Developer | CSE @ IIT Goa",
    "LinkedIn": "https://www.linkedin.com/in/aniketchaudhri/",
    "GitHub": "https://github.com/AniketChaudhri/",
    "description": "I am a CSE pre-final year Undergrad at IIT Goa. I have experience in various Tech Domains such as Web Development, App Development, Deep Learning.",
}

# adarsh = Image.open("/Streamlit/adarsh.jpg")
# aniket = Image.open("/Streamlit/aniket.jpg")

# layout 2 cols
st.title("About OpenEyes")
col1, col2, col3 = st.columns([3,1,3])

# center text
# st.markdown("<h1 style='text-align: center; color: black;'>Meet the Team</h1>", unsafe_allow_html=True)

# create 2 cards showing the details

def show_details(TeamMember):
    st.image(TeamMember["image"], width=200)
    st.header(TeamMember["Name"])
    st.markdown(TeamMember["Role"])
    st.subheader(f"[LinkedIn]({TeamMember['LinkedIn']})")
    st.subheader(f"[GitHub]({TeamMember['GitHub']})")
    st.write(TeamMember["description"])

# add border
with col1:
    show_details(TeamMember1)

with col3:
    show_details(TeamMember2)
