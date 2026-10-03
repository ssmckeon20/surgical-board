import os
from mcp.server.fastmcp import FastMCP
from mcp.server.transport_security import TransportSecuritySettings

mcp = FastMCP(
    "East Texas AM Surgical Center",
    host="0.0.0.0",
    port=int(os.environ.get("PORT", "8000")),
    stateless_http=True,
    json_response=True,
    transport_security=TransportSecuritySettings(enable_dns_rebinding_protection=False),
)

CASES = [
    {
        "id": "C-1041",
        "time": "6:15 a.m.",
        "room": "OR 2",
        "patient": "Elena Vargas",
        "mrn": "448210",
        "procedure": "Laparoscopic cholecystectomy",
        "surgeon": "A. Shah, MD",
        "anesthesia": "L. Ellison, MD",
        "patient_confirmation": "Arrival text Sunday 4:10 p.m. Reply: ok. No second confirmation this morning.",
        "anesthesia_confirmation": "Anesthesia assignment posted. Pre-anesthesia evaluation not signed.",
        "consent": "Procedure consent signed 10/04. Blood consent signed. Witness name blank.",
        "chart": "H&P signed 10/05. NKDA. BMI 31. Nurse line call logged today 5:52 a.m.: patient reported toast and coffee at 5:40 a.m. because she felt dizzy. Booking instruction was nothing by mouth after midnight. Arrival remains 6:15 a.m.",
        "orders": "CBC and BMP 10/05, within reference range. Urine pregnancy negative.",
        "messages": "Sun 4:22 p.m. patient replied ok. Mon 5:52 a.m. nurse line: toast and coffee at 5:40 a.m., still planning to come.",
    },
    {
        "id": "C-1042",
        "time": "7:00 a.m.",
        "room": "OR 1",
        "patient": "Marcus Hale",
        "mrn": "339184",
        "procedure": "Right knee arthroscopy",
        "surgeon": "I. Okonkwo, MD",
        "anesthesia": "S. Patel, CRNA",
        "patient_confirmation": "Confirmed arrival by phone Sunday 6:40 p.m.",
        "anesthesia_confirmation": "CRNA Patel reviewed the chart Sunday. Note says med rec incomplete.",
        "consent": "Procedure consent signed 10/03. Anesthesia consent signed 10/03.",
        "chart": "Hypertension. Med list includes Eliquis 5 mg twice daily. Booking note: stop 48 hours before surgery. MAR free-text entry today 6:10 a.m. documents the usual morning dose taken at home.",
        "orders": "CBC resulted. Type and screen current.",
        "messages": "Sun 7:05 p.m. patient: Took my usual blood thinner this morning, was that right? No staff reply documented.",
    },
    {
        "id": "C-1043",
        "time": "8:30 a.m.",
        "room": "OR 3",
        "patient": "Priya Nair",
        "mrn": "550912",
        "procedure": "Carpal tunnel release",
        "surgeon": "A. Shah, MD",
        "anesthesia": "L. Ellison, MD",
        "patient_confirmation": "NPO and arrival confirmed by text Sun 8:40 p.m.",
        "anesthesia_confirmation": "Anesthesia assigned. No pre-anesthesia note on the chart.",
        "consent": "Procedure consent signed 10/02. Anesthesia consent not scanned.",
        "chart": "Type 2 diabetes, metformin and lisinopril. Son listed as ride. Booking does not require cardiology clearance.",
        "orders": "CBC final. BMP ordered Friday, status not collected. Prior EKG from September on file.",
        "messages": "Fri 11:20 a.m. lab desk: patient left before the BMP tube was filled. Redraw not booked.",
    },
    {
        "id": "C-1044",
        "time": "9:45 a.m.",
        "room": "OR 2",
        "patient": "James Whitaker",
        "mrn": "221765",
        "procedure": "Inguinal hernia repair",
        "surgeon": "M. Cole, MD",
        "anesthesia": "L. Ellison, MD",
        "patient_confirmation": "Arrival confirmed by his wife Sunday evening.",
        "anesthesia_confirmation": "Anesthesia note 10/05: stents in 2022, holding evaluation until clearance is on the chart.",
        "consent": "Procedure and anesthesia consents signed 10/01.",
        "chart": "Coronary stents placed 2022. Face sheet says cardiology clearance within 30 days when stent history is marked. Clearance requested Sept 18. No clearance document in media. NPO confirmed.",
        "orders": "CBC, BMP, and EKG resulted and filed.",
        "messages": "Fri 3:15 p.m. scheduler left voicemail with cardiology. No return call documented.",
    },
    {
        "id": "C-1045",
        "time": "11:00 a.m.",
        "room": "OR 1",
        "patient": "Sofia Alvarez",
        "mrn": "618330",
        "procedure": "Umbilical hernia repair",
        "surgeon": "M. Cole, MD",
        "anesthesia": "S. Patel, CRNA",
        "patient_confirmation": "No arrival confirmation logged.",
        "anesthesia_confirmation": "CRNA assignment posted. Pre-anesthesia screen completed 10/04, no concerns listed.",
        "consent": "Procedure consent signed. Anesthesia consent signed. Ride field blank.",
        "chart": "Registration note: sister might come after work. No name or phone entered. NPO instruction sent. No reply.",
        "orders": "Labs required for this booking are resulted. Auth approved.",
        "messages": "Sat 1:10 p.m. scheduler note: ask again about driver. No second call logged.",
    },
    {
        "id": "C-1046",
        "time": "12:30 p.m.",
        "room": "OR 3",
        "patient": "Noah Bennett",
        "mrn": "774521",
        "procedure": "Shoulder arthroscopy",
        "surgeon": "I. Okonkwo, MD",
        "anesthesia": "S. Patel, CRNA",
        "patient_confirmation": "Arrival and NPO confirmed Sun 5:15 p.m. Ride confirmed.",
        "anesthesia_confirmation": "CRNA Patel confirmed the assignment Sunday.",
        "consent": "Procedure and anesthesia consents signed 10/04.",
        "chart": "Nursing checklist otherwise complete. No anticoagulant. No cardiac history.",
        "orders": "Labs current. Face sheet auth status: pending, requested Oct 1.",
        "messages": "Mon 7:05 a.m. billing: payer portal still pending.",
    },
    {
        "id": "C-1047",
        "time": "1:45 p.m.",
        "room": "OR 2",
        "patient": "Hannah Brooks",
        "mrn": "190442",
        "procedure": "Trigger finger release",
        "surgeon": "A. Shah, MD",
        "anesthesia": "L. Ellison, MD",
        "patient_confirmation": "Phone confirmation last night. Husband driving. NPO confirmed.",
        "anesthesia_confirmation": "Pre-anesthesia evaluation signed 10/05.",
        "consent": "Procedure and anesthesia consents signed. Witness recorded.",
        "chart": "No blood thinners. No cardiac history. Arrival text confirmed.",
        "orders": "CBC resulted. No other pre-op tests required. Auth approved.",
        "messages": "Sun 8:05 p.m. patient confirmed. Husband will drive.",
    },
    {
        "id": "C-1048",
        "time": "2:30 p.m.",
        "room": "OR 1",
        "patient": "Owen Patel",
        "mrn": "263778",
        "procedure": "Excision of back cyst",
        "surgeon": "M. Cole, MD",
        "anesthesia": "S. Patel, CRNA",
        "patient_confirmation": "Arrival text confirmed Sunday.",
        "anesthesia_confirmation": "Pre-anesthesia screen signed. No concerns.",
        "consent": "Consents signed and witnessed.",
        "chart": "No blood thinners. No cardiac history. Ride confirmed.",
        "orders": "No labs required for this booking. Auth approved.",
        "messages": "Sun 3:40 p.m. patient confirmed.",
    },
]

OPENINGS = [
    {"time": "3:15 p.m.", "room": "OR 2", "block": "Shah", "open": True},
    {"time": "4:00 p.m.", "room": "OR 1", "block": "Cole", "open": True},
]

CONTACTS = [
    "Pre-op nurse line · Desk · office 2140 · pager none · on call 2140",
    "OR charge nurse · Board desk · office 2144 · pager 3221 · on call 3221",
    "Scheduler · Renee Cho · office 2102 · pager none · on call 2102",
    "Lab · Outpatient draw · office 2188 · pager 4410 · on call 4419",
    "Cardiology · Clinic desk · office 555-0148 · pager 5502 · on call 5500",
    "Anesthesia · Dr. L. Ellison · office 2160 · pager 6174 · on call 6100",
    "Anesthesia · S. Patel, CRNA · office 2162 · pager 6188 · on call 6100",
    "Surgery · A. Shah, MD · office 555-0172 · pager 2044 · on call 2001",
    "Surgery · I. Okonkwo, MD · office 555-0194 · pager 2081 · on call 2001",
    "Surgery · M. Cole, MD · office 555-0116 · pager 2036 · on call 2001",
    "Surgery on call · Attending on call · pager 2001 · on call 2001",
    "House supervisor · Nursing supervisor · office 2000 · pager 2008 · on call 2008",
    "Billing / auth · Mara Velez · office 2119 · on call 2119",
    "Patient",
]

DRAFTS = []
MOVES = []
NEXT_ID = 1


def case_by_id(case_id: str):
    return next((case for case in CASES if case["id"].lower() == case_id.strip().lower()), None)


@mcp.tool()
def list_cases() -> str:
    """List the Monday Oct 6 board, including any approved moves."""
    lines = ["Booked cases:"]
    for case in CASES:
        lines.append(f"{case['id']} {case['time']} {case['room']} {case['patient']} — {case['procedure']} — {case['surgeon']} / {case['anesthesia']}")
    lines.append("Open later today:")
    for slot in OPENINGS:
        state = "open" if slot["open"] else "taken"
        lines.append(f"{slot['time']} {slot['room']} {slot['block']} block · {state}")
    return "\n".join(lines)


@mcp.tool()
def get_case(case_id: str) -> str:
    """Read one chart: notes, orders, consents, confirmations, and messages."""
    found = case_by_id(case_id)
    if not found:
        return "No case with that id."
    return "\n".join(f"{key}: {value}" for key, value in found.items())


@mcp.tool()
def list_contacts() -> str:
    """List the same contacts as the chart directory. Use one of these names in draft_message."""
    return "\n".join(CONTACTS)


@mcp.tool()
def draft_message(case_id: str, contact: str, message: str) -> str:
    """Save a message to a directory contact or the patient. Does not call, page, or send."""
    if not case_by_id(case_id):
        return "No case with that id."
    if not any(contact.lower() in item.lower() for item in CONTACTS):
        return "That contact is not in the directory. Call list_contacts and use one of those."
    DRAFTS.append({"case_id": case_id.upper(), "contact": contact, "message": message, "status": "Saved, not sent"})
    return f"Saved, not sent. {case_id} to {contact}."


@mcp.tool()
def list_drafts() -> str:
    """Show saved messages. None of these have been sent."""
    if not DRAFTS:
        return "No messages saved."
    return "\n".join(f"{item['status']} · {item['case_id']} · {item['contact']} · {item['message']}" for item in DRAFTS)


@mcp.tool()
def request_move(case_id: str, new_time: str, reason: str) -> str:
    """Ask to move a case. This does not change the board. The user must approve it in chat before approve_move is called."""
    global NEXT_ID
    found = case_by_id(case_id)
    if not found:
        return "No case with that id."
    slot = next((item for item in OPENINGS if item["time"].lower() == new_time.strip().lower()), None)
    if not slot:
        return "That time is not an open slot. Open times are 3:15 p.m. and 4:00 p.m."
    if not slot["open"]:
        return "That slot is already taken."
    move_id = f"M-{NEXT_ID}"
    NEXT_ID += 1
    MOVES.append({
        "id": move_id,
        "case_id": found["id"],
        "patient": found["patient"],
        "from_time": found["time"],
        "new_time": slot["time"],
        "reason": reason,
        "status": "Waiting for user approval",
    })
    return f"{move_id} is waiting for user approval. Ask the user before doing anything else. Do not call approve_move unless the user says yes."


@mcp.tool()
def approve_move(move_id: str) -> str:
    """Move the case only after the user has explicitly said yes in the chat. Refuse if they have not."""
    move = next((item for item in MOVES if item["id"].lower() == move_id.strip().lower()), None)
    if not move:
        return "No request with that id."
    if move["status"] == "Approved":
        return "Already approved."
    slot = next(item for item in OPENINGS if item["time"] == move["new_time"])
    if not slot["open"]:
        return "That slot was taken. Request a different time."
    found = case_by_id(move["case_id"])
    old = found["time"]
    found["time"] = slot["time"]
    found["room"] = slot["room"]
    slot["open"] = False
    move["status"] = "Approved"
    return f"Approved. {found['patient']} moved from {old} to {slot['time']} {slot['room']}."


@mcp.tool()
def list_move_requests() -> str:
    """Show move requests and whether the user has approved them."""
    if not MOVES:
        return "No move requests."
    return "\n".join(
        f"{item['id']} · {item['status']} · {item['patient']} · {item['from_time']} to {item['new_time']} · {item['reason']}"
        for item in MOVES
    )


if __name__ == "__main__":
    mcp.run(transport="streamable-http")
