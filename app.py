import streamlit as st
from PIL import Image

def main_page():
    st.title("Curriculum Vitae")

    # Foto
    st.subheader("Foto")
    image = Image.open("assets/profile.png")
    st.image(image, caption="Muhammad Raditya Prakoso", use_column_width=True)

    # Biodata
    st.subheader("Biodata")
    st.write(
        """
        **Nama:** Muhammad Raditya Prakoso
        **Email:** raditya.prakos@.com
        **LinkedIn:** https://www.linkedin.com/in/radityaprakoso/
        **GitHub:** github.com/radityaprakoso
        """
    )

    # Pendidikan
    st.subheader("Education Level")
    st.write(
        """
        - **Universitas Indonesia** - Undergraduate in Mechanical Engineering (2020-2024)
          • Assistant Lecturer for Health, Safety, and Environment (HSE) class for Odd Semester 2021/2022, Even Semester 2021/2022, Odd Semester
            2022/2023, and Even Semester 2022/2023
          • Assistant Lecturer for Mechanical Vibration class for Odd Semester 2023/2024
          • Laboratory Assistant for Metrology and Measurement Lab for Even Semester 2022/2023
          • Laboratory Coordinator for Metrology and Measurement Lab for Odd Semester 2023/2024 and Even Semester 2023/2024
        - **SMA Negeri 8 Jakarta** - High School Diploma in Natural Science Program (2017-2020)
        """
    )

    # Pengalaman Kerja
    st.subheader("Work Experiences")
    st.write(
        """
        - **Direktorat Pengembangan Karir Lulusan dan Hubungan Alumni (DPKHA) Universitas Indonesia** - Data Analyst (February 2024 - Augustus 2024)
          • Designed and implemented surveys and questionnaires to gather data on alumni employment outcomes, career progression, and educational
            experiences for Tracer Study (TS) and Employeer Study (ES) for Universitas Indonesia.
          • Coordinated and administered online and offline surveys to a diverse alumni population, ensuring high response rates through effective follow-up
            and engagement strategies.
          • Analyzed quantitative and qualitative data to assess employment trends, skill utilization, and overall satisfaction among graduates, producing
            comprehensive reports for stakeholders.
          • Compiled and presented findings to university administration and academic departments, providing actionable insights to enhan ce
            curriculum development and student support services.
        - **NOICE** - User Experience Researcher (February 2023 - Augustus 2023)
          • Developed and implemented comprehensive research workflows utilizing quantitative and qualitative methodologies, with a focus
            on behavioral and attitudinal analysis.
          • Conducted thorough desk research to support primary research initiatives and performed benchmarking and competitor analysis to identify
            strategic gaps in products and services.
          • Led market research and usability testing efforts to evaluate product trends, market viability, and user experience.
          • Managed and analyzed Customer Satisfaction Surveys (CSAT) and Net Promoter Scores (NPS) to inform product development and assess
            customer satisfaction levels.
          • Facilitated Focus Group Discussions (FGD) and In-Depth Interviews (IDI) to gather in-depth qualitative insights.
          • Designed survey instruments and conducted advanced data analysis using Microsoft Excel and SPSS.
        """
    )

    # Pengalaman Organisasi
    st.subheader("Organisational Experience")
    st.write(
        """
        - **BebanBerganda** - Think Tank Caretakers – Head of Research and Marketing Strategy (May 2024 - Present)
          Initiating research process and developing the marketing strategy for BebanBerganda, a youth-led community nurturing young leaders with a strong
          commitment to social inclusivity by addressing structural issues and creating systemic impact. BebanBerganda is incubated by Young Leaders for
          Indonesia, an initiative of McKinsey & Company Indonesia
        - **Badan Eksekutif Mahasiswa (BEM) FTUI** - Coordinator of Internal Corridor (January 2023 - February 2024)
          • Supervised three key divisions—Secretary, Organizational Research and Development, and Human Resources Research and Development—
            overseeing 10 division heads and a team of 35 staff members.
          • Managed the execution of 15 primary programs and 16 secondary events, driving continuous organizational improvement.
          • Actively participated on the deliberative board alongside the Chair and Deputy Chair, contributing to all major decisions impacting BEM FTUI.
          • Designed and implemented a strategic long-term development plan to guide the ongoing enhancement of BEM FTUI.
          • Established a Data Center to monitor and evaluate organizational progress effectively.
        """
    )

    # Skill
    st.subheader("Skill")
    st.write(
        """
        - 👩‍💻 Programming: Python (Scikit-learn, Pandas), SQL, VBA
        - 📊 Data Visulization: PowerBi, MS Excel, Plotly
        - 📚 Modeling: Logistic regression, linear regression, decision trees
        - 🗄️ Databases: Postgres, MongoDB, MySQL
        """
    )

def about_page():
    st.title("Tentang Aplikasi")
    st.write(
        """
        Aplikasi ini dibuat dengan Streamlit untuk menampilkan informasi Curriculum Vitae.
        """
    )

# Navigasi multipage
st.sidebar.title("Navigasi")
page = st.sidebar.radio("Pilih Halaman", ["Curriculum Vitae", "Tentang Aplikasi"])

if page == "Curriculum Vitae":
    main_page()
elif page == "Tentang Aplikasi":
    about_page()
