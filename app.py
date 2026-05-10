import streamlit as st
from datetime import datetime, timedelta

st.markdown(
    "<h1 style='text-align: center;'>Hybrid Work Countdown</h1>",
    unsafe_allow_html=True
)

st.header("Track how many times you still have to show your face in the office before PTO.")

# Holiday date input
holiday_input = st.date_input("Holiday Date")

# Office day selection
office_days = st.multiselect(
    "Onsite Office Days",
    ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
    default=["Monday", "Tuesday"]
)

# Button
if st.button("Calculate Countdown"):

    today = datetime.today().date()
    
    if holiday_input <= today:
        st.error("Please select a future holiday date.")
        
    else:

        on_site_count = 0
        wfh_count = 0

        current_day = today

        office_map = {
            "Monday": 0,
            "Tuesday": 1,
            "Wednesday": 2,
            "Thursday": 3,
            "Friday": 4
        }

        selected_days = [office_map[d] for d in office_days]

        while current_day < holiday_input:

            # Weekdays only
            if current_day.weekday() < 5:

                if current_day.weekday() in selected_days:
                    on_site_count += 1
                else:
                    wfh_count += 1

            current_day += timedelta(days=1)

        total_days = (holiday_input - today).days

        st.success("Countdown Calculated!")

        st.metric("Days Until Holiday", total_days)
        st.metric("Onsite Office Days Left", on_site_count)
        st.metric("WFH Days Left", wfh_count)
        
        st.caption("Days left until your holidays")
        
        progress = on_site_count / (on_site_count + wfh_count)
        st.progress(progress)