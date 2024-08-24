import streamlit as st
from views.about_me import about_me  # Import the about_me function from the about_me.py file

# --- PAGE SETUP ---


def view_resume():
    st.title("Resume")
    st.write("Click the button below to view my resume:")
    
    # Resume button that redirects to your Google Drive link
    st.markdown(
        """
        <a href="https://drive.google.com/file/d/1U0GjCdDuDsG329b1hbdzPS6wmlIYwnir/view?usp=sharing" target="_blank">
            <button style="padding: 10px 20px; background-color: #4CAF50; color: white; border: none; border-radius: 5px; cursor: pointer;">
                View My Resume
            </button>
        </a>
        """,
        unsafe_allow_html=True,
    )

# --- NAVIGATION SETUP ---
def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["About Me", "Resume"])

    if page == "About Me":
        about_me()  # Call the about_me function from the imported file
    elif page == "Resume":
        view_resume()

# --- SHARED ON ALL PAGES ---
st.sidebar.image("assets/image.png", use_column_width=True)
st.sidebar.markdown("Made with ❤️ by [Pallavi Kaushik]")

# --- RUN NAVIGATION ---
if __name__ == "__main__":
    main()
