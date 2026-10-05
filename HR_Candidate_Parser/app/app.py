import json
import html

import streamlit as st
import requests

API_URL = "https://private-barstool-refueling.ngrok-free.dev/parse-cv"

st.set_page_config(
    page_title="HR Candidate Profile Parser",
    page_icon="📄",
    layout="wide",
)

# ----------------------------------------------------------------------
# Styling
# ----------------------------------------------------------------------
st.markdown(
    """
<style>
header[data-testid="stHeader"], #MainMenu, footer {display: none;}

.stApp {background: #f6f8fc;}
.block-container {
    padding: 0 1.5rem 2rem 1.5rem !important;
    max-width: 100% !important;
}

/* ---------- Top banner ---------- */
.hero {
    margin: 0 -1.5rem 1.5rem -1.5rem;
    padding: 1.6rem 2.5rem;
    background: linear-gradient(100deg, #1b2a52 0%, #243a6e 55%, #1b2a52 100%);
    display: flex; align-items: center; justify-content: space-between;
    color: #fff;
}
.hero-left {display: flex; align-items: center; gap: 1.1rem;}
.hero-icon {
    width: 58px; height: 58px; border-radius: 14px;
    background: #2f6df0; display: flex; align-items: center; justify-content: center;
}
.hero h1 {
    margin: 0; padding: 0; font-size: 2.1rem; font-weight: 700;
    color: #fff; line-height: 1.15;
}
.hero p {margin: .25rem 0 0 0; color: #dbe4fb; font-size: 1.02rem;}
.hero-right {
    display: flex; align-items: center; gap: .7rem;
    color: #dbe4fb; font-size: .85rem; line-height: 1.4;
}

/* ---------- Cards (bordered containers) ---------- */
div[data-testid="stVerticalBlockBorderWrapper"] {
    background: #ffffff;
    border: 1px solid #e3e8f2 !important;
    border-radius: 12px !important;
    box-shadow: 0 1px 3px rgba(20, 40, 90, .04);
}

.card-title {
    display: flex; align-items: center; gap: .6rem;
    font-size: 1.25rem; font-weight: 700; color: #1b2a52;
    margin-bottom: .6rem;
}
.card-title svg {flex-shrink: 0;}

/* ---------- Upload card ---------- */
.upload-top {text-align: center; padding-top: .8rem;}
.upload-circle {
    width: 84px; height: 84px; border-radius: 50%; background: #eaf0fe;
    margin: 0 auto .7rem auto; display: flex;
    align-items: center; justify-content: center;
}
.upload-top h3 {margin: 0; font-size: 1.45rem; color: #1b2a52; font-weight: 700;}
.upload-top p {margin: .3rem 0 1rem 0; color: #6b7a99; font-size: .88rem;}

[data-testid="stFileUploaderDropzone"] {
    border: 1.5px dashed #b9c6e4 !important;
    background: #fafbfe !important;
    border-radius: 10px !important;
    flex-direction: column !important;
    align-items: center !important;
    justify-content: center !important;
    padding: 1.6rem 1rem !important;
    gap: .6rem;
}
[data-testid="stFileUploaderDropzoneInstructions"] {display: none !important;}
[data-testid="stFileUploaderDropzone"]::before {
    content: "📄\A Drag and drop your CV here\A or";
    white-space: pre-line; text-align: center;
    color: #44516f; font-size: .88rem; line-height: 1.9;
}
/* keep everything inside the dashed box */
[data-testid="stFileUploaderDropzone"] {
    box-sizing: border-box !important;
    width: 100% !important;
    min-width: 0 !important;
    overflow: hidden !important;
}
[data-testid="stFileUploaderDropzone"] > *,
[data-testid="stFileUploaderDropzone"] [data-testid="stFileUploaderFile"] {
    max-width: 100% !important;
    box-sizing: border-box !important;
}

/* Browse files / "+" (add) button: blue, centered, inside the box */
[data-testid="stFileUploaderDropzone"] > button,
[data-testid="stFileUploaderDropzone"] [data-testid="stBaseButton-secondary"] {
    background: #2f6df0 !important; color: #fff !important;
    border: none !important; border-radius: 6px !important;
    padding: .45rem 1.6rem !important; font-weight: 600;
    width: auto !important; min-width: 0 !important;
    margin: 0 auto !important;
}
[data-testid="stFileUploaderDropzone"] > button:hover,
[data-testid="stFileUploaderDropzone"] [data-testid="stBaseButton-secondary"]:hover {
    background: #2559c8 !important;
}

/* file chip */
[data-testid="stFileUploaderFile"] {
    display: flex !important;
    align-items: center !important;
    width: 100% !important;
    margin: 0 !important;
    padding: .4rem .6rem !important;
    background: #fff; border: 1px solid #e3e8f2; border-radius: 8px;
    box-sizing: border-box !important;
}
[data-testid="stFileUploaderFileName"] {
    overflow: hidden; text-overflow: ellipsis; white-space: nowrap;
}

/* remove (x) button: small, transparent, NOT the blue style */
[data-testid="stFileUploaderDeleteBtn"],
[data-testid="stFileUploaderDeleteBtn"] button,
[data-testid="stFileUploaderFile"] button {
    background: transparent !important;
    color: #6b7a99 !important;
    border: none !important;
    box-shadow: none !important;
    width: auto !important;
    min-width: 0 !important;
    padding: .25rem !important;
    margin-left: auto !important;
}
[data-testid="stFileUploaderDeleteBtn"] button:hover,
[data-testid="stFileUploaderFile"] button:hover {
    background: #eef2fb !important;
    color: #e5484d !important;
}

/* ---------- Buttons ---------- */
div[data-testid="stButton"] button {
    width: 100%; background: #2f6df0; color: #fff; border: none;
    border-radius: 8px; padding: .7rem 1rem; font-weight: 600; font-size: 1rem;
}
div[data-testid="stButton"] button:hover {background: #2559c8; color: #fff;}
div[data-testid="stButton"] button p::before {content: "▶  "; font-size: .85rem;}

/* ---------- Alerts ---------- */
div[data-testid="stAlert"]:has([data-testid="stAlertContentSuccess"]),
div[data-testid="stAlertContainer"]:has([data-testid="stAlertContentSuccess"]) {
    background: #e8f6ee !important; border-radius: 8px;
}
[data-testid="stAlertContentSuccess"] {color: #1f6f43 !important;}

/* ---------- Candidate info ---------- */
.label {color: #5c6b8c; font-weight: 600; font-size: .85rem; margin-bottom: .2rem;}
.value {color: #1b2a52; font-size: 1.05rem;}

/* ---------- Rows (education / experience) ---------- */
.row {
    display: flex; justify-content: space-between; align-items: flex-start;
    padding: .8rem 0; border-bottom: 1px solid #edf0f6;
}
.row:last-child {border-bottom: none;}
.row .main {color: #1b2a52; font-weight: 600; font-size: 1.02rem;}
.row .sub {color: #6b7a99; font-size: .92rem; margin-top: .25rem;}
.row .meta {color: #5c6b8c; font-size: .9rem; white-space: nowrap;}

/* ---------- Skills ---------- */
.pills {display: flex; flex-wrap: wrap; gap: .6rem;}
.pill {
    background: #eaf0fe; color: #2f4f9f; border-radius: 999px;
    padding: .4rem 1rem; font-size: .9rem;
}

/* ---------- Raw JSON ---------- */
[data-testid="stCode"] pre, [data-testid="stCode"] {
    background: #0f1b33 !important; border-radius: 8px;
}
[data-testid="stCode"] pre {max-height: 330px; overflow: auto;}
[data-testid="stCode"] code {font-size: .78rem !important; color: #cfe3ff !important;}
</style>
""",
    unsafe_allow_html=True,
)

# ----------------------------------------------------------------------
# Icons
# ----------------------------------------------------------------------
ICON_USER = '<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#2f6df0" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="4"/><path d="M4 21c0-4 4-6 8-6s8 2 8 6"/></svg>'
ICON_EDU = '<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#2f6df0" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 10 12 5 2 10l10 5 10-5z"/><path d="M6 12v5c3 2 9 2 12 0v-5"/></svg>'
ICON_JOB = '<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#2f6df0" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="7" width="18" height="13" rx="2"/><path d="M9 7V5a2 2 0 0 1 2-2h2a2 2 0 0 1 2 2v2M3 13h18"/></svg>'
ICON_SKILL = '<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#2f6df0" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="3"/><path d="M19 12a7 7 0 0 0-.1-1.2l2-1.5-2-3.4-2.3 1a7 7 0 0 0-2-1.2L14.3 3h-4l-.4 2.7a7 7 0 0 0-2 1.2l-2.3-1-2 3.4 2 1.5A7 7 0 0 0 5 12a7 7 0 0 0 .1 1.2l-2 1.5 2 3.4 2.3-1a7 7 0 0 0 2 1.2l.4 2.7h4l.4-2.7a7 7 0 0 0 2-1.2l2.3 1 2-3.4-2-1.5c.1-.4.1-.8.1-1.2z"/></svg>'
ICON_CODE = '<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#2f6df0" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m16 18 6-6-6-6M8 6l-6 6 6 6M14 4l-4 16"/></svg>'


def card_title(icon, text):
    st.markdown(
        f'<div class="card-title">{icon}<span>{text}</span></div>',
        unsafe_allow_html=True,
    )


def esc(value):
    return html.escape(str(value))


# ----------------------------------------------------------------------
# Header banner
# ----------------------------------------------------------------------
st.markdown(
    """
<div class="hero">
  <div class="hero-left">
    <div class="hero-icon">
      <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="3" width="16" height="18" rx="3"/><circle cx="12" cy="10" r="3"/><path d="M7 18c1-3 9-3 10 0"/></svg>
    </div>
    <div>
      <h1>HR Candidate Profile Parser</h1>
      <p>Upload a CV and automatically extract structured candidate information.</p>
    </div>
  </div>
  <div class="hero-right">
    <svg width="34" height="34" viewBox="0 0 24 24" fill="none" stroke="#8fb2ff" stroke-width="1.6" stroke-linejoin="round"><path d="M12 2c.7 5.5 4.5 9.3 10 10-5.5.7-9.3 4.5-10 10-.7-5.5-4.5-9.3-10-10 5.5-.7 9.3-4.5 10-10z"/></svg>
    <div>Smarter Hiring<br>with Better Data</div>
  </div>
</div>
""",
    unsafe_allow_html=True,
)

left_col, right_col = st.columns([1, 3.2], gap="large")

# ----------------------------------------------------------------------
# Left: upload panel
# ----------------------------------------------------------------------
with left_col:
    with st.container(border=True):
        st.markdown(
            """
<div class="upload-top">
  <div class="upload-circle">
    <svg width="44" height="44" viewBox="0 0 24 24" fill="none" stroke="#2f6df0" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M7 18a4.5 4.5 0 0 1-.6-8.96A6 6 0 0 1 18 8.5a4 4 0 0 1-.5 9.5"/><path d="M12 21v-8M9 15.5l3-3 3 3"/></svg>
  </div>
  <h3>Upload CV</h3>
  <p>Supported format: PDF</p>
</div>
""",
            unsafe_allow_html=True,
        )

        uploaded_file = st.file_uploader(
            "Upload CV",
            type=["pdf"],
            label_visibility="collapsed",
        )

        if uploaded_file is not None:

            parse_clicked = st.button("Parse CV")

            st.success("CV uploaded successfully!")

# ----------------------------------------------------------------------
# Right: results panel
# ----------------------------------------------------------------------
with right_col:

    if uploaded_file is not None:

        if parse_clicked:

            with st.spinner("Parsing CV..."):

                files = {
                    "file": (
                        uploaded_file.name,
                        uploaded_file.getvalue(),
                        "application/pdf"
                    )
                }

                response = requests.post(
                    API_URL,
                    files=files
                )

            if response.status_code == 200:

                result = response.json()

                st.success("CV parsed successfully!")

                # ---------------- Candidate information ----------------
                with st.container(border=True):
                    card_title(ICON_USER, "Candidate Information")
                    c1, c2 = st.columns(2)
                    with c1:
                        st.markdown(
                            f'<div class="label">Name</div>'
                            f'<div class="value">{esc(result.get("full_name", "N/A"))}</div>',
                            unsafe_allow_html=True,
                        )
                    with c2:
                        st.markdown(
                            f'<div class="label">Email</div>'
                            f'<div class="value">{esc(result.get("email", "N/A"))}</div>',
                            unsafe_allow_html=True,
                        )

                main_col, side_col = st.columns([1.9, 1.1], gap="medium")

                with main_col:

                    # ---------------- Education ----------------
                    with st.container(border=True):
                        card_title(ICON_EDU, "Education")

                        rows = ""
                        for education in result.get("education", []):
                            rows += (
                                '<div class="row">'
                                '<div>'
                                f'<div class="main">{esc(education.get("degree", "N/A"))}</div>'
                                f'<div class="sub">{esc(education.get("institution", "N/A"))}</div>'
                                '</div>'
                                f'<div class="meta">{esc(education.get("year", "N/A"))}</div>'
                                '</div>'
                            )
                        st.markdown(rows, unsafe_allow_html=True)

                    # ---------------- Experience ----------------
                    with st.container(border=True):
                        card_title(ICON_JOB, "Experience")

                        rows = ""
                        for experience in result.get("experience", []):
                            rows += (
                                '<div class="row">'
                                '<div>'
                                f'<div class="main">{esc(experience.get("role", "N/A"))}</div>'
                                f'<div class="sub">{esc(experience.get("company", "N/A"))}</div>'
                                '</div>'
                                f'<div class="meta">{esc(experience.get("years", "N/A"))}</div>'
                                '</div>'
                            )
                        st.markdown(rows, unsafe_allow_html=True)

                with side_col:

                    # ---------------- Skills ----------------
                    with st.container(border=True):
                        card_title(ICON_SKILL, "Skills")

                        skills = result.get("skills", [])

                        if isinstance(skills, list):
                            pills = "".join(
                                f'<span class="pill">{esc(s)}</span>' for s in skills
                            )
                        else:
                            pills = f'<span class="pill">{esc(skills)}</span>'

                        st.markdown(
                            f'<div class="pills">{pills}</div>',
                            unsafe_allow_html=True,
                        )

                    # ---------------- Raw JSON ----------------
                    with st.container(border=True):
                        card_title(ICON_CODE, "Raw JSON")
                        st.code(
                            json.dumps(result, indent=2, ensure_ascii=False),
                            language="json",
                        )

            else:

                st.error(
                    f"Error {response.status_code}: {response.text}"
                )