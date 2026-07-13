import streamlit as st

from services.dashboard_service import DashboardService


from config.settings import APP_NAME

st.title(APP_NAME)

# ==========================================
# CONFIGURAÇÃO
# ==========================================

st.set_page_config(
    page_title="StudyOS AI",
    page_icon="🚀",
    layout="wide"
)

# ==========================================
# DADOS (TEMPORÁRIOS)
# ==========================================

TRILHAS = {
    "🐍 Python": 90,
    "🗄 SQL": 80,
    "⚙ Engenharia de Dados": 40,
    "🌐 Backend": 20,
    "☁ AWS": 15,
    "🐳 DevOps": 5,
    "🤖 IA": 15
}

PROJETOS = [
    ("✅", "Monitoramento Vivaz"),
    ("✅", "Monitoramento BPO"),
    ("🟡", "Central de Inteligência"),
    ("⬜", "StudyOS AI"),
]

CERTIFICACOES = [
    ("⬜", "AWS Solutions Architect Associate"),
    ("⬜", "Google Professional Data Engineer"),
    ("⬜", "Terraform Associate"),
    ("⬜", "CKA Kubernetes"),
]

# ==========================================
# SIDEBAR
# ==========================================

st.sidebar.title("🚀 StudyOS AI")

menu = st.sidebar.radio(
    "Menu",
    [
        "Dashboard",
        "Trilhas",
        "Projetos",
        "Certificações",
        "Mentor IA"
    ]
)

# ==========================================
# DASHBOARD
# ==========================================

if menu == "Dashboard":

    st.title("🚀 StudyOS AI")

    st.caption("Sua plataforma de evolução profissional")    

    service = DashboardService()

    usuario = service.obter_usuario()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Progresso", "32%")

    with col2:
        st.metric("Projetos", "4")

    with col3:

        if usuario:

            st.metric(
                "Horas Estudadas",
                f"{usuario.horas_estudadas}h"
            )

    st.divider()

    st.subheader("📚 Progresso das Trilhas")

    for nome, progresso in TRILHAS.items():
        st.write(nome)
        st.progress(progresso / 100)

    st.divider()

    st.subheader("🎯 Objetivo")

    st.success(
        """
        Tornar-se:

        • Engenheiro de Dados

        • Backend Python

        • AWS

        • DevOps

        • IA Generativa
        """
    )

# ==========================================
# TRILHAS
# ==========================================

elif menu == "Trilhas":

    st.title("📚 Trilhas")

    for nome, progresso in TRILHAS.items():

        with st.container():

            col1, col2 = st.columns([4,1])

            with col1:
                st.write(nome)
                st.progress(progresso/100)

            with col2:
                st.write(f"**{progresso}%**")

# ==========================================
# PROJETOS
# ==========================================

elif menu == "Projetos":

    st.title("💼 Projetos")

    for status, projeto in PROJETOS:

        st.write(f"{status} {projeto}")

# ==========================================
# CERTIFICAÇÕES
# ==========================================

elif menu == "Certificações":

    st.title("🏆 Certificações")

    for status, cert in CERTIFICACOES:

        st.write(f"{status} {cert}")

# ==========================================
# MENTOR IA
# ==========================================

elif menu == "Mentor IA":

    st.title("🤖 Mentor IA")

    st.info(
        """
### Bom dia, Carlos!

Hoje eu faria:

✅ Python (45 min)

✅ SQL (30 min)

✅ IA Generativa (30 min)

---

🎯 Próximo objetivo

Finalizar Git/GitHub para iniciar Docker.

---

📌 Projeto recomendado

Central de Inteligência

---

🏆 Próxima certificação

AWS Solutions Architect Associate
        """
    )

    pergunta = st.text_input(
        "Pergunte ao Mentor"
    )

    if pergunta:

        st.success(
            f"""
Você perguntou:

> {pergunta}

Resposta (V1):

Essa funcionalidade será integrada à IA nas próximas versões.

Por enquanto, o Mentor utiliza regras de negócio para recomendar sua próxima etapa de estudos.
            """
        )