import streamlit as st

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
        
    uploaded_file = st.file_uploader("UPLOAD LESSON EXEMPLAR / NOTES (Optional)", type=["txt", "pdf", "docx"])
    
    # Submit Button
    submitted = st.form_submit_button("Generate Lesson Plan")

# Output Section after submission
if submitted:
    st.success("Form submitted successfully! Here is your generated ILAW Lesson Plan:")
    
    # You can connect this section to an AI API (like OpenAI or Google Gemini API) 
    # to automatically generate the lesson plan based on the inputs above.
    st.markdown(f"""
    ### I-L-A-W Framework Output Preview:
    * *Language:* {target_language}
    * *Subject:* {learning_area} ({term_week} - {session_number})
    * *Prepared By:* {prepared_by} | *Checked By:* {checked_by}
    
    1. *I - INTENTIONS:*
       * Grade 3: {g3_competency}
       * Grade 4: {g4_competency}
       
    2. *L - LEARNING EXPERIENCE:*
       * (Multigrade methodology with alternating direct teaching and independent activities goes here...)
       
    3. *A - ASSESSMENT:*
       * (Tailored formative assessments for G3 and G4...)
       
    4. *W - WAYS FORWARD:*
       * (Remediation and enrichment steps...)
