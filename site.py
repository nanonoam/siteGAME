import streamlit as st

# המילון שהגרלת מראש (השם של השחקן: [סיסמה, המטרה שלו])
# דוגמה: נועם מקבל את עומר, עומר מקבל את איתמר וכו'.
targets_db = {
    "נועם": ["1234", "עומר"],
    "עומר": ["5678", "איתמר"],
    "איתמר": ["9012", "נועם"]
}

st.title("💦 משחק המתנקש - שבועות 💦")
st.write("הכנס את השם שלך ואת הקוד הסודי שקיבלת כדי לגלות מי המטרה שלך!")

name_input = st.text_input("שם מלא (כמו שמופיע ברשימה):")
password_input = st.text_input("קוד סודי:", type="password")

if st.button("גלה לי את המטרה"):
    if name_input in targets_db:
        if targets_db[name_input][0] == password_input:
            st.success(f"המטרה שלך היא: **{targets_db[name_input][1]}**")
            st.warning("הרטבה מקדימה בלבד! בהצלחה 😎")
        else:
            st.error("קוד סודי שגוי.")
    else:
        st.error("השם לא נמצא במערכת, ודא שהקלדת נכון.")