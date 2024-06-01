import streamlit as st

def get_ent_information(case):
    case = case.strip().lower()
    if "epistaxis" in case:
        return (
            "EPISTAXIS.\n"
            "- If elderly patient then admit for 24 hours to monitor.\n"
            "- CAN PROVIDE NASEPTIN CREAM QDS BUT CHECK FOR NUT ALLERGY.\n"
            "- If they do start mupirocin as alternative."
        )
    elif "nasal bone fracture" in case or "fracture" in case:
        return (
            "NASAL BONE FRCATURE.\n"
            "- IF NO ONGOING BLEEDING/SEPTAL HAEMATOMA À ED TO DISCHARGE WITH ANALGESIA – CAS CLINIC IN 1 WEEK.\n"
        )
    elif "dizziness" in case:
        return (
            "DIZZINESS.\n"
            "- ED to r/o central causes.\n"
            "- F/u à balance clinic.\n"
            "- If unable to mobilise then admit under medics."
        )
    elif "ear laceration" in case or "laceration" in case:
        return (
            "EAR/ NOSE LACERATION.\n"
            "- DURING OUT OF HOURS IN NIGHT --> NEXT DAY SEAU OR ELSE SAME DAY SEAU AND REPAIR.\n"
            "- Complex laceration may need plastic referral.\n"
        )
    elif "foreign body" in case or "body" in case:
        return (
            "FOREIGN BODY.\n"
            "- If airway --> call ENT reg.\n"
            "- If oropharynx and ABC stable --> SEAU for FNE.\n"
            "- If oesophagus/ cricopharynx and not able to swallow --> admit.\n"
            "- Veg Ear or nose  - LG NBM for children.\n"
            "- Non vegetative Ear or nose -  CAS clinic if no infective signs present.\n"
            "- BATTERY – EMERGENCY – NEEDS REMOVAL IN 1-2 HOURS."
        )
    elif "neck abscess" in case or "abscess" in case:
        return (
            "NECK ABSCESS.\n"
            "- Check ABC.\n"
            "- Bloods and IV abx. If airway concern = call ENT reg and may need FNE.\n"
            "- May need CT neck with contrast."
        )
    elif "ludwig's angina" in case or "angina" in case:
        return (
            "LUDWIG ANGINA.\n"
            "- Involvement of submental and submandibular space.\n"
            "- Airway concern = FNE.\n"
            "- ED to refer to Max Fax."
        )
    elif "post tonsillectomy bleed" in case or "tonsillectomy" in case or "bleed" in case:
        return (
            "POST TONSILLECTOMY BLEED.\n"
            "- If active bleeding call on call SpR Immediately.\n"
            "- Do below if has active bleeding or past bleed: Need bloods FBC, U+E, clotting and CRP and G+S.\n"
            "- NBM.\n"
            "- Start H2O2 gargles.\n"
            "- Must admit all post tonsillectomy/adenotonsillectomy bleeds."
        )
    elif "otitis externa/MEDIA/MASTOIDITS" in case or "media" in case or "mastoiditis" in case:
        return (
            "OTITS EXTERNA/MEDIA/ OTOMASTOIDITIS.\n"
            "- Ask NS in SEAU to do bloods on arrival.\n"
            "- Severe otitis externa will include tragal tenderness, swollen ear canals – may need pope wick.\n"
            "- If unable to insert speak to SpR regarding admission/come back.\n"
            "- If not severe can be managed with cipro drops regardless of perforation.\n"
            "- Gent drops not given if there is a perforation.\n"
            "- White discharge with black dots – fungal – given cotrimazole 1% solution."
        )
    else:
        return "No prompt found. Please provide correct prompt."

st.title("ENT on Call Assistant")

st.write("Welcome to ENT on call. How can I help? Please enter the topic you want to know about.")
case = st.text_input("Enter the topic:")

if case:
    result = get_ent_information(case)
    st.text_area("Result:", value=result, height=200)
