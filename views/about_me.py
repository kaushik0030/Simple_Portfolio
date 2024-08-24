import streamlit as st

def about_me():
    st.title("About Me")
    
    # --- HERO SECTION ---
    col1, col2 = st.columns([1, 2], gap="small")  # Adjust column ratios to balance the layout
    
    with col1:
        # Contact Me Button
        st.markdown(
            """
            <style>
            .contact-button {
                display: inline-block;
                padding: 10px 20px;
                background-color: #B16100; /* LinkedIn color */
                color: white;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                text-align: center;
                text-decoration: none;
            }
            .contact-button:hover {
                background-color: #007782;
            }
            </style>
            <a href="mailto:pallavikaushik0030@gmail.com" class="contact-button">Contact Me</a>
            """,
            unsafe_allow_html=True
        )
        st.image("./assets/profile_pic.jpg", width=230)
    
    with col2:
        st.title("Pallavi Kaushik")
        st.write("Aspiring Data Scientist | Ex-Machine Learning Intern @ DRDO")
    
    # --- EXPERIENCE & QUALIFICATIONS ---
    st.write("\n")  # Add a line break for spacing
    st.subheader("Experience & Qualifications")
    st.write(
        """
        - 2 years of experience as an ML engineer, working on data science projects.
        - 3 years of experience extracting actionable insights from data.
        - Strong hands-on experience and knowledge in Python and Excel.
        - Good understanding of statistical principles and their applications.
        - Excellent team player with a strong sense of initiative on tasks.
        """
    )
    
    # --- SKILLS ---
    st.write("\n")  # Add a line break for spacing
    st.subheader("Hard Skills")
    st.write(
        """
        - **Programming**: Python (Scikit-learn, Pandas), SQL, VBA
        - **Data Visualization**: Power BI, MS Excel, Plotly
        - **Data Science**: Machine Learning, Deep Learning, NLP
        - **Frameworks**: Flask, Streamlit, Django
        """
    )

    # --- PROJECTS ---
    st.write("\n")  # Add a line break for spacing

    # Add LinkedIn and GitHub links below the button
    st.markdown(
        """
        <style>
        .social-links {
            margin-top: 10px;
            display: flex;
            flex-direction: column;
        }
        .social-links a {
            color: #0073b1; /* LinkedIn color */
            text-decoration: none;
            margin-bottom: 5px;
            font-size: 16px;
        }
        .social-links a:hover {
            text-decoration: underline;
        }
        </style>
        <div class="social-links">
            <a href="https://www.linkedin.com/in/pallavi-kaushik03/" target="_blank">LinkedIn</a>
            <a href="https://github.com/kaushik0030" target="_blank">GitHub</a>
        </div>
        """,
        unsafe_allow_html=True
    )
