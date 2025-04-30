# Import the Streamlit library
import streamlit as st
import datetime

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="David Leonard Nagy | Developer",
    page_icon="✨", # Simple, clean icon
    layout="wide",
)

# --- HEADER ---
with st.container():
    # Reverted to 3-column layout for centering text now that image is removed
    col1, col2, col3 = st.columns([1, 3, 1])
    with col2:
        st.title("David Leonard Nagy")
        st.subheader("Full-Stack Developer & Machine Learning Engineer")
        st.caption("📍 Budapest, Hungary | Building digital experiences") # Combined location & tagline

st.divider() # Visual separator

# --- MAIN CONTENT AREA (Using Columns for Layout) ---
col_main_left, col_main_right = st.columns([2, 1], gap="large") # Left column wider

with col_main_left:
    # --- ABOUT ME ---
    with st.container():
        st.header("👤 About Me")
        st.markdown( # Using markdown for slightly richer formatting
            """
            Hi! I'm Leo, an 18-year-old developer from Hungary with a passion for building robust applications and exploring the frontiers of Artificial Intelligence.

            My expertise spans **Full-Stack Development** and **Machine Learning Engineering**, with a particular focus on **Natural Language Processing (NLP)** and **Kernel Methods**. I also have experience in **Game Development** and **Mobile App Development**.

            I'm comfortable working across the entire development lifecycle, proficient with Git and Docker, and enjoy tackling diverse challenges using technologies like MERN, Python frameworks, and cloud platforms.
            """
        )
        st.write("") # Add some vertical space

    # --- PROJECTS ---
    with st.container():
        st.header("🚀 Projects")
        st.write("A selection of my work:")

        # Project 1: RAG Research Tool
        with st.expander("Local RAG Research Helper (Offline NLP Tool)", expanded=True): # Keep first one collapsed by default now
            st.markdown(
                """
                **Description:** Developed a fully offline and local Retrieval-Augmented Generation (RAG) tool leveraging Ollama. This application allows users to upload documents or fetch papers directly from arXiv.org. It processes and indexes the content locally, enabling users to perform semantic searches and ask questions answered *solely* based on the provided document corpus.

                **Technologies:** Python, Ollama, Streamlit, NLP techniques.
                """
            )
            # Use columns for the button to control its width/alignment if needed
            btn_col1, btn_col2, btn_col3 = st.columns([1,2,1])
            with btn_col2: # Center the button somewhat
                 st.link_button("View Code on GitHub", "https://github.com/deadfighter10/RAGResearchHelper")

        # Project 2: Bike Rental Demand Prediction
        with st.expander("Bike Rental Demand Prediction App", expanded=True): # Expand the new one by default
            st.markdown(
                """
                **Description:** An interactive web application built with Python (Streamlit, Pandas, Scikit-learn) that predicts the total number of daily bike rentals based on the historical Washington D.C. dataset (2011-2012). Users input daily conditions (month, day, holiday, weather metrics), and the app determines season/working day automatically. A pre-trained Gradient Boosting Regressor model forecasts the rental count instantly.

                **Technologies:** Python, Streamlit, Pandas, Scikit-learn, Gradient Boosting.
                """
            )
            # Use columns for the buttons for better layout
            btn_col_1, btn_col_2 = st.columns(2)
            with btn_col_1:
                 st.link_button("View Live App", "https://predictbikerent.streamlit.app/")
            with btn_col_2:
                 st.link_button("View Code on GitHub", "https://github.com/deadfighter10/BikeRentDemand")


        st.write("") # Add space after projects

with col_main_right:
    # --- KEY SKILLS ---
    # This column starts with Skills
    with st.container():
        st.header("🛠️ Key Skills")

        st.subheader("Languages")
        st.markdown("- Python, C#, JavaScript, SQL, HTML/CSS")

        st.subheader("Frameworks & Libraries")
        st.markdown("- Node.js/Express, Flask\n- React/React Native\n- PyTorch, Scikit-learn")

        st.subheader("Tools & Platforms")
        st.markdown("- Git/GitHub, Docker\n- Firebase, GCP\n- Unity, Blender, Ollama")
        st.write("") # Add space

    # --- CONTACT ---
    with st.container():
        st.header("📬 Get In Touch")
        st.write("Open to opportunities & collaborations. Reach out!")

        # Using columns for button layout
        contact_col1, contact_col2 = st.columns(2)
        with contact_col1:
            st.link_button("📧 Email Me", "mailto:nagy.david.leonard@gmail.com", use_container_width=True)
            st.link_button("🐙 GitHub", "https://github.com/deadfighter10/", use_container_width=True)
        with contact_col2:
            st.link_button("🔗 LinkedIn", "https://www.linkedin.com/in/david-leonard-nagy-215722355/", use_container_width=True)
            st.link_button("📸 Instagram", "https://www.instagram.com/leo.nagy.2/", use_container_width=True)

        st.write("") # Add space

        # --- Simple Inquiry Note (No Form) ---
        st.subheader("Quick Inquiry?")
        st.caption(f"Just drop me an email at: nagy.david.leonard@gmail.com")


st.divider() # Visual separator before footer

# --- FOOTER ---
st.markdown(
    f"<div style='text-align: center; color: #6c757d;'>© {datetime.date.today().year} David Leonard Nagy | Built with Streamlit</div>",
    unsafe_allow_html=True
)
st.write("") # Final bit of space
