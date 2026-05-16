import streamlit as st

# הגדרות עיצוב - הרבה סגול! 💜
st.markdown("""
<style>
/* רקע כללי של האפליקציה - סגול בהיר מאוד */
.stApp {
    background-color: #f3e8ff; 
}
/* צבע הכותרות והטקסט הרגיל - סגול כהה */
h1, h2, h3, p {
    color: #4c1d95 !important; 
}
/* עיצוב תיבת הטקסט (הסיסמה) */
.stTextInput input {
    border: 2px solid #8b5cf6 !important;
    border-radius: 10px;
    color: #4c1d95 !important;
    background-color: #ffffff;
}
/* עיצוב הכפתור - סגול בוהק */
.stButton>button {
    background-color: #8b5cf6; 
    color: white;
    border-radius: 10px;
    border: none;
    width: 100%;
    font-size: 18px;
    font-weight: bold;
    padding: 10px;
}
/* שינוי צבע הכפתור כשמעבירים עליו את העכבר */
.stButton>button:hover {
    background-color: #7c3aed; 
    color: white;
}
</style>
""", unsafe_allow_html=True)

# מאגר הנתונים - עכשיו המפתח (Key) הוא הסיסמה עצמה
# מבנה: "סיסמה": ["השם של מי שהכניס את הסיסמה", "המטרה שלו"]
targets_db = {
    "1234": ["נועם", "עומר"],
    "5678": ["עומר", "איתמר"],
    "9012": ["איתמר", "נועם"]
}

st.title("💦 משחק המתנקש - שבועות 💦")
st.write("הכנס את הקוד הסודי שלך כדי לגלות את מי אתה הולך להרטיב!")

# תיבת קלט לסיסמה בלבד
password_input = st.text_input("קוד סודי:", type="password")

if st.button("מי המטרה שלי?"):
    if password_input in targets_db:
        user_name = targets_db[password_input][0]
        target_name = targets_db[password_input][1]
        
        st.success(f"היי {user_name}! המטרה שלך היא: **{target_name}**")
        st.warning("הרטבה מקדימה בלבד! בהצלחה 💜")
    elif password_input: # מציג שגיאה רק אם הוכנס משהו
        st.error("קוד סודי שגוי. נסה שוב.")