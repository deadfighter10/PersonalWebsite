import streamlit as st
import datetime

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="David Leonard Nagy | Developer",
    page_icon="👨‍💻", # You can replace with a text icon if you prefer no emojis: "DN"
    layout="wide",
    # initial_sidebar_state="collapsed", # Optional: Collapse sidebar by default
)

# --- CUSTOM CSS ---
# Inject CSS for visual enhancements like section backgrounds, padding, and fonts.
# Note: Streamlit class names might change in future versions. Inspect elements if needed.
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');

    /* Apply base font */
    html, body, [class*="st-"], .stApp {
        font-family: 'Inter', sans-serif;
    }

    /* Style the main containers for sections */
    /* Targeting a common parent class for containers - adjust if needed after inspection */
    .st-emotion-cache-z5fcl4 { /* This selector might need updating in future Streamlit versions */
        background-color: #f8f9fa; /* Light grey background for sections */
        padding: 1.5rem;          /* Add padding inside sections */
        border-radius: 0.5rem;     /* Rounded corners */
        margin-bottom: 1.5rem;    /* Space between sections */
        border: 1px solid #e9ecef; /* Subtle border */
    }

    /* Improve header spacing and alignment */
    .st-emotion-cache-18ni7ap { /* Target title container - adjust if needed */
         margin-bottom: 0.5rem;
    }

    /* Style headers within sections */
    h1, h2, h3 {
        color: #212529; /* Darker color for headers */
    }
    h1 {
        font-weight: 700;
    }
     h2 {
        font-weight: 600;
        border-bottom: 2px solid #dee2e6; /* Underline for H2 headers */
        padding-bottom: 0.3rem;
        margin-bottom: 1rem;
    }
     h3 {
        font-weight: 600;
        color: #495057; /* Slightly lighter color for H3 */
        margin-bottom: 0.5rem;
     }

    /* Style buttons */
    .stButton>button, .stDownloadButton>button, .stLinkButton>a {
        border-radius: 0.3rem;
        padding: 0.5rem 1rem;
        font-weight: 600;
        border: none; /* Remove default border */
        /* Add transition for hover effects */
        transition: background-color 0.2s ease-in-out, color 0.2s ease-in-out;
    }
    /* Primary button style for form submit */
    .stForm .stButton>button {
         background-color: #0d6efd; /* Bootstrap primary blue */
         color: white;
    }
     .stForm .stButton>button:hover {
         background-color: #0b5ed7;
         color: white;
     }

    /* Style link buttons */
    .stLinkButton>a {
        background-color: #6c757d; /* Bootstrap secondary grey */
        color: white;
        text-decoration: none; /* Remove underline */
    }
    .stLinkButton>a:hover {
         background-color: #5c636a;
         color: white;
         text-decoration: none;
     }

     /* Style expander */
    .stExpander {
        border: 1px solid #dee2e6 !important; /* Override default border */
        border-radius: 0.5rem;
        background-color: #ffffff; /* White background for expander content */
    }
    .stExpander header {
        font-weight: 600;
        color: #0d6efd; /* Use primary color for expander header */
    }

    /* Style form inputs */
    .stTextInput input, .stTextArea textarea {
        border-radius: 0.3rem;
        border: 1px solid #ced4da;
    }
    .stTextInput input:focus, .stTextArea textarea:focus {
        border-color: #86b7fe; /* Highlight on focus */
        box-shadow: 0 0 0 0.25rem rgba(13, 110, 253, 0.25); /* Focus shadow */
    }

</style>
""", unsafe_allow_html=True)

# --- HEADER SECTION ---
# Removed the first column previously used for the picture
with st.container():
    # Center the title and subheader
    st.title("David Leonard Nagy")
    st.subheader("Full-Stack Developer & Machine Learning Engineer")
    st.write("📍 Budapest, Hungary")
    # Optional: Add a brief tagline or status
    # st.write("🚀 Open to new opportunities and collaborations.")
    st.divider() # Use st.divider for a cleaner look

# --- ABOUT ME & SKILLS SECTION (Combined Layout) ---
with st.container(): # This container will get the background/padding from CSS
    col1, col2 = st.columns([2, 1], gap="large") # 2/3 width for About, 1/3 for Skills

    with col1:
        st.header("👤 About Me")
        st.write(
            """
            Hi! I'm David, an 18-year-old developer from Hungary with a passion for building robust applications and exploring the frontiers of Machine Learning.

            My expertise spans **Full-Stack Development** and **Machine Learning Engineering**, with a particular focus on **Natural Language Processing (NLP)** and **Kernel Methods**. I also have experience in **Game Development** and **Mobile App Development**.

            I'm comfortable working across the entire development lifecycle, proficient with Git and Docker, and enjoy tackling diverse challenges using technologies like MERN, Python frameworks, and cloud platforms.
            """
        )

    with col2:
        st.header("🛠️ Key Skills")
        st.subheader("Languages")
        st.markdown("""
        - Python, C#, JavaScript, SQL, HTML/CSS
        """)
        st.subheader("Frameworks")
        st.markdown("""
        - Node.js/Express, Flask
        - React/React Native
        - PyTorch, Scikit-learn
        """)
        st.subheader("Tools & Platforms")
        st.markdown("""
        - Git/GitHub, Docker
        - Firebase, GCP
        - Unity, Blender, Ollama
        """)
    # st.write("") # Add vertical space if needed after the container

# --- PROJECTS SECTION (Using Expanders) ---
with st.container(): # This container will get the background/padding from CSS
    st.header("🚀 Projects")
    st.write("Here's a highlight of my work (click to expand):")
    # st.divider() # Divider within the section if needed

    # Project 1: RAG Research Tool (Inside an Expander)
    # The expander itself is styled via CSS
    with st.expander("Local RAG Research Helper (Offline NLP Tool)", expanded=False):
        # Removed the first column previously used for the icon
        # Content now takes full width within the expander
        st.write(
            """
            **Description:** Developed a fully offline and local Retrieval-Augmented Generation (RAG) tool leveraging Ollama. This application allows users to upload documents or fetch papers directly from arXiv.org. It processes and indexes the content locally, enabling users to perform semantic searches and ask questions answered *solely* based on the provided document corpus.

            **Technologies:** Python, Ollama, Streamlit, NLP techniques.
            """
        )
        st.link_button("View Code on GitHub", "https://github.com/deadfighter10/RAGResearchHelper")

    # Add more projects using st.expander similarly
    # with st.expander("Project Title 2", expanded=False):
    #     st.write("**Description:** ...")
    #     st.write("**Technologies:** ...")
    #     st.link_button("View Project/Code", "your-link-here")

    # st.write("") # Add vertical space if needed

# --- CONTACT SECTION ---
with st.container(): # This container will get the background/padding from CSS
    st.header("📬 Get In Touch")
    st.write(
        """
        I'm always open to new opportunities, collaborations, or just a chat about technology!
        Feel free to reach out directly or use the form below:
        """
    )
    st.write("") # Add a bit of space before the buttons

    # Links using styled link_buttons
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.link_button("📧 Email", "mailto:nagy.david.leonard@gmail.com", use_container_width=True)
    with col2:
        st.link_button("🔗 LinkedIn", "https://www.linkedin.com/in/david-leonard-nagy-215722355/", use_container_width=True)
    with col3:
        st.link_button("🐙 GitHub", "https://github.com/deadfighter10/", use_container_width=True)
    with col4:
        st.link_button("📸 Instagram", "https://www.instagram.com/leo.nagy.2/", use_container_width=True)

    st.divider() # Separator before the form

    # --- CONTACT FORM ---
    st.subheader("Send me a message:")
    # Form styled via CSS
    with st.form(key="contact_form"):
        name = st.text_input("Your Name", placeholder="Enter your name")
        email = st.text_input("Your Email", placeholder="Enter your email address")
        message = st.text_area("Message", placeholder="Your message here...", height=150) # Increased height
        submit_button = st.form_submit_button(label="Send Inquiry")

        if submit_button:
            if name and email and message:
                st.success(f"Thank you, {name}! Your message has been received.")
                st.balloons()
            else:
                st.error("Please fill out all fields before sending.")

    # st.write("") # Add vertical space if needed

# --- FOOTER ---
st.divider() # Use divider before footer
st.write(f"© {datetime.date.today().year} David Leonard Nagy | Built with Streamlit")
st.write("") # Extra space at the bottom
