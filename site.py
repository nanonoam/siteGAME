import streamlit as st

# הגדרת מבנה העמוד 
st.set_page_config(page_title="משחק המתנקש", page_icon="💦", layout="centered")

# עיצוב מטורף - סגול על סגול! 💜
st.markdown("""
<style>
/* רקע העמוד - גרדיאנט של סגול כהה */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #1e0033 0%, #4a0072 50%, #290042 100%);
    color: #e6ccff;
}

/* עיצוב הכותרות */
h1, h2, h3, p, label {
    color: #f3e8ff !important; 
    text-align: center;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

/* עיצוב תיבת הטקסט (הסיסמה) */
.stTextInput input {
    border: 2px solid #b366ff !important;
    border-radius: 15px;
    color: #ffffff !important;
    background-color: rgba(74, 0, 114, 0.5) !important;
    text-align: center;
    font-size: 20px;
    box-shadow: 0 0 10px rgba(179, 102, 255, 0.2);
}

/* עיצוב הכפתור הראשי */
.stButton>button {
    background: linear-gradient(90deg, #9933ff 0%, #cc33ff 100%);
    color: white !important;
    border-radius: 15px;
    border: none;
    width: 100%;
    font-size: 22px;
    font-weight: bold;
    padding: 12px;
    box-shadow: 0 4px 15px rgba(204, 51, 255, 0.4);
    transition: all 0.3s ease;
}

/* אפקט ריחוף על הכפתור */
.stButton>button:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(204, 51, 255, 0.7);
    background: linear-gradient(90deg, #aa44ff 0%, #dd44ff 100%);
}

/* עיצוב חלונית השגיאה וההצלחה */
.stAlert {
    border-radius: 15px;
}
</style>
""", unsafe_allow_html=True)

# מאגר הנתונים המעורבב מחדש (סיסמה: [שם השחקן, המטרה])
targets_db = {
    "4821": ["נועם סגול", "להב"],
    "6390": ["להב", "איתמר הרבסט"],
    "6072": ["איתמר הרבסט", "ניקול"],
    "7014": ["ניקול", "רוי שן"],
    "4091": ["רוי שן", "שלומו זיין"],
    "8263": ["שלומו זיין", "הילה קולטקר"],
    "7160": ["הילה קולטקר", "אלון סטביצקי"],
    "5174": ["אלון סטביצקי", "עומר עידו גרינברג"],
    "9654": ["עומר עידו גרינברג", "שחר גנץ שדמי"],
    "9426": ["שחר גנץ שדמי", "איתן רדובסקי"],
    "1837": ["איתן רדובסקי", "נבו דאי"],
    "1945": ["נבו דאי", "אדם אשטון"],
    "9302": ["אדם אשטון", "אלדר פינטו"],
    "3589": ["אלדר פינטו", "הדר אלוני"],
    "1347": ["הדר אלוני", "אנקין סקיווקר"],
    "8512": ["אנקין סקיווקר", "ליאור בן אור"],
    "5739": ["ליאור בן אור", "אביתר כהן"],
    "3908": ["אביתר כהן", "אופיר גלנץ"],
    "2758": ["אופיר גלנץ", "רועי רז"],
    "2486": ["רועי רז", "אורי מכלוף"],
    "6205": ["אורי מכלוף", "נועם סגול"]
}

# כותרת האתר
st.markdown("<h1>💦 מבצע שבועות 💦</h1>", unsafe_allow_html=True)
st.markdown("<p style='font-size: 18px; margin-bottom: 30px;'>הכנס את הקוד הסודי שלך כדי לגלות מי המטרה שלך</p>", unsafe_allow_html=True)

# אזור הכנסת הסיסמה
password_input = st.text_input("קוד סודי:", type="password", placeholder="הקש את הקוד כאן...")

# רווח לעיצוב
st.write("")

if st.button("חשוף את המטרה שלי 🎯"):
    if password_input in targets_db:
        user_name = targets_db[password_input][0]
        target_name = targets_db[password_input][1]
        
        st.balloons() # מוסיף אנימציה של בלונים בהצלחה!
        st.success(f"היי {user_name}! המטרה שלך היא: **{target_name}** 🤫")
        st.warning("זכור: הרטבה מקדימה ומעל החגורה בלבד. בלי לפגוע בציוד! 💜")
    elif password_input:
        st.error("קוד סודי שגוי. נסה שוב.")

st.write("---")

# חלונית נפתחת עם חוקי המשחק
with st.expander("📜 חוקי המשחק המלאים"):
    st.markdown("""
    * **איך מנצחים?** עליך להרטיב את המטרה שלך. ברגע שהצלחת, אתה לוקח ממנה את השם הבא וממשיך הלאה עד שנשאר מנצח אחד.
    * **פגיעה חוקית:** רק מקדימה, ורק **מעל קו החגורה** (בגלל טלפונים בכיסים!).
    * **אזורים בטוחים (Safe Zones):** אסור בשום אופן להרטיב במקלחות, בבריכה, בזמן הרצאות ותרגולים, וכן בתוך **ספריות, מעבדות, חדרי אוכל וחדרים פרטיים**.
    * **ציוד אלקטרוני:** אם המטרה מחזיקה טאבלט או לפטופ גלוי בחוץ – אסור להרטיב! שמרו על הציוד.
    * **פרישות וסינונים:** שחקן שפורש או מחליט לא לשתף פעולה חייב לדווח למארגן. המטרה שלו תועבר ישירות למי שרדף אחריו.
    * **נזק היקפי:** פגיעה בסטודנט או חבר שלא משתתף במשחק תגרור **פסילה מיידית** של המשפריץ.
    * **חוק המתבצר:** חובה לשמור על שגרת יום רגילה. אסור להסתגר בחדר ימים שלמים רק כדי להימנע מפסילה.
    * **החלטת שופט:** בכל מקרה של ויכוח או ספק לגבי פגיעה, מארגן המשחק הוא הפוסק האחרון והחלטתו סופית.
    """)