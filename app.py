import streamlit as st
import PyPDF2

from agents.career_agent import analyze_career_profile
from agents.skill_gap_agent import analyze_skill_gap
from agents.opportunity_agent import analyze_opportunities
from agents.resume_agent import analyze_resume


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="CareerPath AI",
    page_icon="🎯",
    layout="wide"
)


# =========================================================
# HEADER
# =========================================================

st.title("🎯 CareerPath AI")

st.subheader(
    "Your Agentic AI Career & Employment Assistant"
)

st.write(
    "CareerPath AI helps students and early-career youth "
    "identify skill gaps, analyze resumes, explore opportunities, "
    "and create personalized career action plans."
)

st.divider()


# =========================================================
# PROFILE
# =========================================================

st.header("👤 Tell us about yourself")

col1, col2 = st.columns(2)

with col1:

    name = st.text_input(
        "Your Name",
        placeholder="Example: Gullala Akshaya"
    )

    education = st.text_input(
        "Education",
        placeholder="Example: B.Tech in Artificial Intelligence and Machine Learning"
    )

    year = st.text_input(
        "Graduation Year",
        placeholder="Example: 2028"
    )

with col2:

    career_goal = st.text_input(
        "Your Target Career",
        placeholder="Example: Machine Learning Engineer"
    )

    location = st.text_input(
        "Preferred Location",
        placeholder="Example: Hyderabad / Remote"
    )


skills = st.text_area(
    "Your Current Skills",
    placeholder="Example: Python, SQL, Machine Learning, GitHub"
)


# =========================================================
# RESUME UPLOAD
# =========================================================

st.header("📄 Resume Analyzer")

resume_file = st.file_uploader(
    "Upload your resume",
    type=["pdf", "txt"]
)


# =========================================================
# ANALYZE BUTTON
# =========================================================

if st.button(
    "🚀 Analyze My Career Profile",
    use_container_width=True
):

    if not name or not education or not skills or not career_goal:

        st.warning(
            "Please fill in your name, education, skills, and career goal."
        )

        st.stop()


    # =====================================================
    # PROFILE SUMMARY
    # =====================================================

    st.success("Profile received successfully! 🎉")

    st.header("📋 Your Profile")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.write("**👤 Name**")
        st.write(name)

    with c2:
        st.write("**🎓 Education**")
        st.write(education)

    with c3:
        st.write("**🎯 Career Goal**")
        st.write(career_goal)

    c4, c5, c6 = st.columns(3)

    with c4:
        st.write("**📅 Graduation Year**")
        st.write(year if year else "Not provided")

    with c5:
        st.write("**💻 Skills**")
        st.write(skills)

    with c6:
        st.write("**📍 Location**")
        st.write(location if location else "Not provided")


    # =====================================================
    # STORE REPORT
    # =====================================================

    full_report = f"""
CAREERPATH AI REPORT

Name:
{name}

Education:
{education}

Graduation Year:
{year}

Skills:
{skills}

Target Career:
{career_goal}

Preferred Location:
{location}

"""


    # =====================================================
    # CAREER AGENT
    # =====================================================

    st.divider()

    st.header("🤖 Career Agent")

    with st.spinner(
        "Career Agent is analyzing your career profile..."
    ):

        try:

            career_result = analyze_career_profile(
                name,
                education,
                year,
                skills,
                career_goal,
                location
            )

            st.markdown(career_result)

            full_report += "\n\n===== CAREER ANALYSIS =====\n\n"
            full_report += career_result

        except Exception as e:

            st.error(
                "Career Agent could not complete the analysis."
            )

            st.code(str(e))


    # =====================================================
    # SKILL GAP AGENT
    # =====================================================

    st.divider()

    st.header("📊 Skill Gap Agent")

    with st.spinner(
        "Skill Gap Agent is identifying your skill gaps..."
    ):

        try:

            skill_gap_result = analyze_skill_gap(
                skills,
                career_goal
            )

            st.markdown(skill_gap_result)

            full_report += "\n\n===== SKILL GAP ANALYSIS =====\n\n"
            full_report += skill_gap_result

        except Exception as e:

            st.error(
                "Skill Gap Agent could not complete the analysis."
            )

            st.code(str(e))


    # =====================================================
    # OPPORTUNITY AGENT
    # =====================================================

    st.divider()

    st.header("💼 Opportunity Agent")

    with st.spinner(
        "Opportunity Agent is preparing your opportunity strategy..."
    ):

        try:

            opportunity_result = analyze_opportunities(
                career_goal,
                education,
                skills,
                location
            )

            st.markdown(opportunity_result)

            full_report += "\n\n===== OPPORTUNITY ANALYSIS =====\n\n"
            full_report += opportunity_result

        except Exception as e:

            st.error(
                "Opportunity Agent could not complete the analysis."
            )

            st.code(str(e))


    # =====================================================
    # RESUME AGENT
    # =====================================================

    if resume_file:

        st.divider()

        st.header("📄 Resume Agent")

        with st.spinner(
            "Resume Agent is analyzing your resume..."
        ):

            try:

                resume_text = ""

                if resume_file.name.lower().endswith(".pdf"):

                    pdf_reader = PyPDF2.PdfReader(
                        resume_file
                    )

                    for page in pdf_reader.pages:

                        text = page.extract_text()

                        if text:
                            resume_text += text + "\n"

                else:

                    resume_text = resume_file.read().decode(
                        "utf-8",
                        errors="ignore"
                    )


                if not resume_text.strip():

                    st.warning(
                        "Could not extract readable text from your resume."
                    )

                else:

                    resume_result = analyze_resume(
                        resume_text,
                        career_goal
                    )

                    st.markdown(resume_result)

                    full_report += "\n\n===== RESUME ANALYSIS =====\n\n"
                    full_report += resume_result


            except Exception as e:

                st.error(
                    "Resume Agent could not complete the analysis."
                )

                st.code(str(e))

    else:

        st.info(
            "📄 Upload a PDF or TXT resume to receive "
            "resume-specific recommendations."
        )


    # =====================================================
    # RESUME SCORE
    # =====================================================

    st.divider()

    st.header("📊 Career Readiness Score")

    st.write(
        "This score is an indicative project-based score "
        "generated from the profile information and should "
        "not be considered a professional hiring assessment."
    )

    score = 70

    if resume_file:
        score += 10

    if year:
        score += 5

    if location:
        score += 5

    if len(skills.split(",")) >= 4:
        score += 5

    if len(career_goal.strip()) > 5:
        score += 5

    score = min(score, 100)


    st.metric(
        label="🎯 Overall Career Readiness",
        value=f"{score}/100"
    )

    st.progress(score / 100)


    if score >= 85:

        st.success(
            "Excellent progress! Keep strengthening your projects and experience."
        )

    elif score >= 70:

        st.info(
            "Good foundation! Focus on the recommended skill gaps and projects."
        )

    else:

        st.warning(
            "Build your core skills and strengthen your portfolio step by step."
        )


    full_report += f"""

===== CAREER READINESS SCORE =====

Overall Career Readiness: {score}/100

"""


    # =====================================================
    # FINAL ACTION PLAN
    # =====================================================

    st.divider()

    st.header("🚀 Next Actions")

    st.markdown(
        """
        1. 📚 Learn the high-priority skills identified by the agents.
        2. 🛠️ Build practical portfolio projects.
        3. 📄 Improve your resume based on the Resume Agent.
        4. 💼 Prepare for internships and entry-level opportunities.
        5. 🔗 Keep your GitHub and LinkedIn profiles updated.
        6. 📅 Follow the recommended 30-day learning roadmap.
        """
    )


    full_report += """

===== NEXT ACTIONS =====

1. Learn recommended skills.
2. Build practical portfolio projects.
3. Improve the resume.
4. Prepare for internships and entry-level opportunities.
5. Update GitHub and LinkedIn.
6. Follow the 30-day roadmap.

"""


    # =====================================================
    # DOWNLOAD REPORT
    # =====================================================

    st.divider()

    st.header("📥 Download Your Career Report")

    st.download_button(
        label="📄 Download CareerPath AI Report",
        data=full_report,
        file_name="CareerPath_AI_Report.txt",
        mime="text/plain",
        use_container_width=True
    )


    # =====================================================
    # COMPLETION
    # =====================================================

    st.divider()

    st.success(
        "🎯 CareerPath AI completed your multi-agent analysis!"
    )

    st.markdown(
        """
        ### 🌟 Your Career Journey Starts Here

        Use the recommendations above to:

        - 📚 Build the recommended skills
        - 🛠️ Create portfolio projects
        - 📅 Follow your 30-day roadmap
        - 📄 Improve your resume
        - 💼 Prepare for internships and entry-level roles
        - 📥 Download your personalized career report
        - 🚀 Continue improving your career profile
        """
    )