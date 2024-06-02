import os
import sys
import streamlit as st
st.image("TOP.jpg", caption="ENT on call", use_column_width=True)
def get_ent_information(case):
    case = case.strip().lower()
    st.write(f"Debug: Case input - {case}")
    if "epistaxis" in case:
        st.image("EPIS.jpg", caption="Epistaxis")  # Add image
        return (
            "EPISTAXIS.\n"
            "- If elderly patient then admit for 24 hours to monitor.\n"
            "- CAN PROVIDE NASEPTIN CREAM QDS BUT CHECK FOR NUT ALLERGY.\n"
            "- If they do start mupirocin as alternative."
        )
    elif "nasal bone fracture" in case or in case "nasal" or in case "bone" or in case "fracture" in case:
        st.image("NBF.png", caption="Nasal fracture")  # Add image
        return (
            "NASAL BONE FRACTURE.\n"
            "- IF NO ONGOING BLEEDING/SEPTAL HAEMATOMA À ED TO DISCHARGE WITH ANALGESIA – CAS CLINIC IN 1 WEEK.\n"
        )
    elif "dizziness" in case:
        st.image("DIZ.jpeg", caption="Dizziness")  # Add image
        return (
            "DIZZINESS.\n"
            "- ED to r/o central causes.\n"
            "- F/u à balance clinic.\n"
            "- If unable to mobilise then admit under medics."
        )
    elif "ear/nose laceration" in case or in case "ear" or in case "laceration" in case:
        st.image("LAC.jpeg", caption="Laceration")  # Add image
        return (
            "EAR/ NOSE LACERATION.\n"
            "- DURING OUT OF HOURS IN NIGHT --> NEXT DAY SEAU OR ELSE SAME DAY SEAU AND REPAIR.\n"
            "- Complex laceration may need plastic referral.\n"
        )
    elif "foreign body" in case or in case "foreing" or in case "body" in case:
        st.image("FB.jpg", caption="FB")  # Add image
        return (
            "FOREIGN BODY.\n"
            "- If airway --> call ENT reg.\n"
            "- If oropharynx and ABC stable --> SEAU for FNE.\n"
            "- If oesophagus/ cricopharynx and not able to swallow --> admit.\n"
            "- Veg Ear or nose  - LG NBM for children.\n"
            "- Non vegetative Ear or nose -  CAS clinic if no infective signs present.\n"
            "- BATTERY – EMERGENCY – NEEDS REMOVAL IN 1-2 HOURS."
        )
    elif "neck abscess" in case or in case "neck" or in case "abscess" in case:
        st.image("NA.jpg", caption="Neck abscess")  # Add image
        return (
            "NECK ABSCESS.\n"
            "- Check ABC.\n"
            "- Bloods and IV abx. If airway concern = call ENT reg and may need FNE.\n"
            "- May need CT neck with contrast."
        )
    elif "ludwig's angina" in case or in case "ludwig" or in case "angina" in case:
        st.image("LA.jpeg", caption="Ludwig's Angina")  # Add image
        return (
            "LUDWIG ANGINA.\n"
            "- Involvement of submental and submandibular space.\n"
            "- Airway concern = FNE.\n"
            "- ED to refer to Max Fax."
        )
    elif "post tonsillectomy bleed" in case or in case "tonsillectomy" or in case "bleed" in case:
        st.image("TONS.jpeg", caption="Post tonsillectomy bleed")  # Add image
        return (
            "POST TONSILLECTOMY BLEED.\n"
            "- If active bleeding call on call SpR Immediately.\n"
            "- Do below if has active bleeding or past bleed: Need bloods FBC, U+E, clotting and CRP and G+S.\n"
            "- NBM.\n"
            "- Start H2O2 gargles.\n"
            "- Must admit all post tonsillectomy/adenotonsillectomy bleeds."
       )
    elif "otitis externa/media/MASTOIDITS" in case or in case "otitis" or in case "media" or in case "mastoiditis" in case:
        st.image("MAST.jpeg", caption="Ear infection")  # Add image
        return (
            "OTITIS EXTERNA/MEDIA/ OTOMASTOIDITIS.\n"
            "- Ask NS in SEAU to do bloods on arrival.\n"
            "- Severe otitis externa will include tragal tenderness, swollen ear canals – may need pope wick.\n"
            "- If unable to insert speak to SpR regarding admission/come back.\n"
            "- If not severe can be managed with cipro drops regardless of perforation.\n"
            "- Gent drops not given if there is a perforation.\n"
            "- White discharge with black dots – fungal – given cotrimazole 1% solution."
        )
    else:
        return "No prompt found. Please provide correct prompt."

st.title("ENT on Call Assistant SWBH -  by Mr Shiraz Syed (ENT Reg)")

st.write("Welcome to ENT on call. How can I help? Please enter the topic you want to know about.")
case = st.text_input("Enter the topic:")

if case:
    result = get_ent_information(case)
    st.write(result)
