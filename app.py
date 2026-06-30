import streamlit as st
from db import (
    get_user,
    get_user_skills,
    get_missing_skills,
    get_progress,
    add_user_skill,
    get_next_skill,
    create_user,
    login_user,
    get_goals,
    get_skills,
    email_exists
)


st.set_page_config(
    page_title="Learning Recommendation System",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>

/* ---------- Hide Streamlit Default UI ---------- */

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}

/* ---------- Reduce Top Padding ---------- */

.block-container{
    padding-top:2rem;
    padding-bottom:2rem;
}

/* ---------- Button Style ---------- */

.stButton > button{
    width:100%;
    background:linear-gradient(135deg,#ff4b4b,#ff6b6b);
    color:white;
    border:none;
    border-radius:12px;
    padding:12px 20px;
    font-size:15px;
    font-weight:600;
    transition:all 0.3s ease;
    box-shadow:0 4px 12px rgba(255,75,75,0.25);
}

.stButton > button:hover{
    transform:translateY(-3px);
    box-shadow:0 8px 20px rgba(255,75,75,0.45);
}

.stButton > button:active{
    transform:scale(0.98);
}

/* ---------- Progress Bar ---------- */

.stProgress > div > div > div{
    border-radius:10px;
}

/* ---------- Metric Cards ---------- */

.metric-card{
    padding:25px;
    border-radius:15px;
    color:white;
    margin-bottom:15px;
    transition: all 0.3s ease;
    cursor:pointer;
}

.metric-card:hover{
    transform: translateY(-6px);
    box-shadow: 0 10px 25px rgba(0,0,0,0.35);
}

.goal-card{
    background:#1f3b57;
}

.progress-card{
    background:#1f5c39;
}

.skill-card{
    background:#5c571f;
}

.metric-title{
    font-size:20px;
    font-weight:600;
}

.metric-value{
    font-size:45px;
    font-weight:bold;
    margin-top:15px;
}

</style>
""", unsafe_allow_html=True)


st.markdown("""
<h1 style='
text-align:center;
font-size:55px;
margin-bottom:0px;
'>
🎯 Learning Recommendation System
</h1>
""", unsafe_allow_html=True)


st.markdown("""
<p style='
text-align:center;
font-size:20px;
color:gray;
margin-top:0px;
'>
Your Personalized Roadmap to Master New Skills
</p>
""", unsafe_allow_html=True)
# -----------------------------
# Session State
# -----------------------------

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "user_id" not in st.session_state:
    st.session_state.user_id = None

if not st.session_state.logged_in:

        page = st.radio(
        "Choose an option",
        ["Login", "Sign Up"],
        horizontal=True
        )

        if page == "Login":
            email = st.text_input("Enter your email")
            password = st.text_input("Enter your password", type="password")
            if st.button("Login"):
                user = login_user(email, password)

                if user:
                    st.session_state.logged_in = True
                    st.session_state.user_id = user[0]
                    st.rerun()
                else:
                    st.error("❌ Invalid email or password.")
    

        else:
            goals = get_goals()     
            selected_goal = st.selectbox(
            "Choose your career goal",
            goals,
            format_func=lambda goal: goal[1]
            )    
            skills = get_skills()

            selected_skills = st.multiselect(
            "Select the skills you already know",
            skills,
            format_func=lambda skill: skill[1]
            )
            name = st.text_input("Enter your name")
            email = st.text_input("Enter your email")
            password = st.text_input("Enter your password", type="password")
            if st.button("Create Account"):

                if name and email and password:

                    if email_exists(email):
                        st.error("❌ Email already exists.")

                    else:
                        create_user(name, email, password, selected_goal[0])

                        user = login_user(email, password)

                        for skill in selected_skills:
                            add_user_skill(user[0], skill[0])

                        st.success("✅ Account created successfully!")

                else:
                    st.error("Please fill in all the fields.")
        
if st.session_state.logged_in:

    user = get_user(st.session_state.user_id)

    if user:

            skills = get_user_skills(st.session_state.user_id)
            missing_skills = get_missing_skills(st.session_state.user_id)
            skill_icons = {
                "Python": "🐍",
                "SQL": "🗄️",
                "PostgreSQL": "🐘",
                "NumPy": "🔢",
                "Pandas": "🐼",
                "Statistics": "📈",
                "Data Visualization": "📊",
                "Excel": "📗",
                "Feature Engineering": "⚙️",
                "Machine Learning": "🤖",
                "Power BI": "💼"
            }
            current_skills, total_skills, progress = get_progress(st.session_state.user_id)
            skill_name, reason = get_next_skill(st.session_state.user_id)

            header_left, header_right = st.columns([8, 1])

            with header_left:
                st.markdown(f"# 👋 Welcome, {user[0]}")

            with header_right:
                if st.button("Logout", use_container_width=True):
                    st.session_state.clear()

                    st.rerun()

            if progress >= 80:
                status = "🏆 Expert"
            elif progress >= 60:
                status = "🚀 Advanced"
            elif progress >= 40:
                status = "📘 Intermediate"
            else:
                status = "🌱 Beginner"

            col1, col2, col3, col4 = st.columns(4)

            with col1:
                st.markdown(f"""
                <div class="metric-card goal-card">
                    <div class="metric-title">🎯 Career Goal</div>
                    <div class="metric-value">{user[2]}</div>
                </div>
                """, unsafe_allow_html=True)

            with col2:
                st.markdown(f"""
                <div class="metric-card progress-card">
                    <div class="metric-title">📈 Progress</div>
                    <div class="metric-value">{progress}%</div>
                </div>
                """, unsafe_allow_html=True)

            with col3:
                st.markdown(f"""
                <div class="metric-card skill-card">
                    <div class="metric-title">✅ Skills Completed</div>
                    <div class="metric-value">{current_skills}/{total_skills}</div>
                </div>
                """, unsafe_allow_html=True)
            with col4:
                st.markdown(f"""
                <div class="metric-card progress-card">
                    <div class="metric-title">🏆 Status</div>
                    <div class="metric-value">{status}</div>
                </div>
                """, unsafe_allow_html=True)

            left, right = st.columns(2)

            with left:

                st.subheader("✅ Current Skills")

                skill_col1, skill_col2 = st.columns(2)

                for i, skill in enumerate(skills):

                    icon = skill_icons.get(skill[0], "✅")

                    if i % 2 == 0:
                        with skill_col1:
                            st.markdown(f"""
                            <div style="
                            background:#1f5c39;
                            padding:10px 15px;
                            border-radius:10px;
                            margin-bottom:8px;
                            font-size:15px;
                            font-weight:500;
                            color:white;
                            ">
                            {icon} {skill[0]}
                            </div>
                            """, unsafe_allow_html=True)

                    else:
                        with skill_col2:
                            st.markdown(f"""
                            <div style="
                            background:#1f5c39;
                            padding:10px 15px;
                            border-radius:10px;
                            margin-bottom:8px;
                            font-size:15px;
                            font-weight:500;
                            color:white;
                            ">
                            {icon} {skill[0]}
                            </div>
                            """, unsafe_allow_html=True)
            with right:
             if progress < 100:
                    st.subheader("❌ Missing Skills")

                    for skill in missing_skills:

                        icon = skill_icons.get(skill[1], "❌")

                        col1, col2 = st.columns([4,1])

                        with col1:
                            st.markdown(f"""
                            <div style="
                            background:#5b2c2c;
                            padding:10px 15px;
                            border-radius:10px;
                            margin-bottom:8px;
                            font-size:15px;
                            font-weight:500;
                            color:white;
                            border-left:5px solid #ff4b4b;
                            ">
                            {icon} {skill[1]}
                            </div>
                            """, unsafe_allow_html=True)

                        with col2:
                            if st.button("✓ Complete", key=skill[0]):
                                add_user_skill(st.session_state.user_id, skill[0])
                                st.rerun()

            st.divider()
             
            if skill_name:

                st.subheader("💡 Your Next Learning Recommendation")

                st.markdown(f"""
                        <div style="
                            background:#1f3b57;
                            padding:22px;
                            border-radius:15px;
                            border-left:6px solid #4da3ff;
                        ">

                        <h2 style="margin:0;">📘 {skill_name}</h2>

                        <p style="color:#bbbbbb; margin-top:12px;">
                        <b>Why learn this?</b>
                        </p>

                        <p style="font-size:17px;">
                        {reason}
                        </p>

                        </div>
                        """, unsafe_allow_html=True)
            else:
                st.balloons()

                st.success("""
                ## 🎉 Congratulations!

                You have completed your learning roadmap.

                Start building real-world projects and strengthen your portfolio.
                """)