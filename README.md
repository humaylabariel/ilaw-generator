mport streamlit as st
from google import genai
from google.genai import types

# Page Configuration
st.set_page_config(
    page_title="ILAW Multigrade Lesson Plan Generator",
    page_icon="📖",
    layout="centered"
)

# App Header
st.markdown("## 📖 ILAW Multigrade Lesson Plan Generator")
st.markdown("by Wynner B. Elba")
st.markdown("---")

# Retrieve Gemini API Key from Streamlit Secrets
# (You will add your API key safely in your Streamlit Cloud settings)
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    client = genai.Client(api_key=api_key)
except Exception:
    client = None

# Form Inputs
with st.form("ilaw_form"):
    target_language = st.selectbox(
        "TARGET LANGUAGE",
        ["English", "Filipino"]
    )
    
    learning_area = st.text_input(
        "LEARNING AREA / SUBJECT",
        placeholder="e.g., Mathematics, Science"
    )
    
    col1, col2 = st.columns(2)
    with col1:
        grade_section = st.text_input(
            "GRADE & SECTION",
            placeholder="e.g., Grade 3 & 4 - Rizal"
        )
    with col2:
        term_week = st.text_input(
            "TERM & WEEK",
            placeholder="e.g., Term 1, Week 1"
        )
        
    session_number = st.selectbox(
        "SESSION NUMBER",
        ["Session 1 of 5", "Session 2 of 5", "Session 3 of 5", "Session 4 of 5", "Session 5 of 5"]
    )
    
    g3_competency = st.text_area(
        "GRADE 3 COMPETENCY / MELC",
        placeholder="Type Grade 3 learning competency here..."
    )
    
    g4_competency = st.text_area(
        "GRADE 4 COMPETENCY / MELC",
        placeholder="Type Grade 4 learning competency here..."
    )
    
    col3, col4 = st.columns(2)
    with col3:
        prepared_by = st.text_input("PREPARED BY", value="Wynner B. Elba")
    with col4:
        checked_by = st.text_input("CHECKED BY", value="Juan Dela Cruz")
        
    uploaded_notes = st.text_area("UPLOAD LESSON EXEMPLAR / NOTES (Optional)", placeholder="Paste any extra notes or text material here...")
    
    submitted = st.form_submit_button("Generate Lesson Plan")

# Handle Generation
if submitted:
    if not client:
        st.error("Gemini API Key is missing! Please configure 'GEMINI_API_KEY' in your Streamlit Secrets.")
    elif not learning_area or not g3_competency or not g4_competency:
        st.warning("Please fill out the Learning Area and both Grade 3 & Grade 4 Competencies before generating.")
    else:
        with st.spinner("Generating your professional I-L-A-W Multigrade Lesson Plan... Please wait."):
            
            # Construct the prompt based on your ILAW framework rules
            prompt = f"""
            You are the ILAW Multigrade Lesson Plan Generator created by Wynner B. Elba. 
            Generate a professional multigrade lesson plan for Grade 3 and Grade 4 based on the following details:
            
            - Target Language: {target_language}
            - Learning Area / Subject: {learning_area}
            - Grade & Section: {grade_section}
            - Term & Week: {term_week}
            - Session Number: {session_number}
            - Grade 3 Competency / MELC: {g3_competency}
            - Grade 4 Competency / MELC: {g4_competency}
            - Prepared By: {prepared_by}
            - Checked By: {checked_by}
            - Additional Notes/Exemplar: {uploaded_notes}
            
            Strictly follow the I-L-A-W Framework layout:
            1. *I - INTENTIONS:* (Separate learning objectives, targets, and competencies for Grade 3 and Grade 4)
            2. *L - LEARNING EXPERIENCE:* (Subject matter, references, materials, and multigrade methodology using alternating Direct Teaching and Independent Activities for G3 and G4)
            3. *A - ASSESSMENT:* (Formative assessments, quizzes, or performance tasks tailored to each grade)
            4. *W - WAYS FORWARD:* (Remediation, enrichment, and next steps)
            """
            
            try:
                response = client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=prompt
                )
                st.success("Lesson Plan Generated Successfully!")
                st.markdown("---")
                st.markdown(response.text)
            except Exception as e:
                st.error(f"An error occurred while communicating with Gemini: {e}")
