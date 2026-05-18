import streamlit as st
from datetime import datetime, timedelta

on_site_count = 0
wfh_count = 0

office_map = {
            "Monday": 0,
            "Tuesday": 1,
            "Wednesday": 2,
            "Thursday": 3,
            "Friday": 4
        }

st.markdown(
    "<h1 style='text-align: center;'>Hybrid Work Countdown</h1>",
    unsafe_allow_html=True
)

st.header("Track how many onsite visits you have to make before your holidays.")

# Holiday date input
holiday_input = st.date_input("Holiday Date",format="DD/MM/YYYY")

# Office day selection
office_days = st.multiselect(
    "Onsite Office Days",
    ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
    default=["Monday", "Tuesday"]
)

# Button
if st.button("Calculate Countdown"):
    
    # Reset the counter
    on_site_count = 0
    wfh_count = 0

    today = datetime.today().date()
    
    if holiday_input <= today:
        st.error("Please select a future holiday date.")
        
    else:
        current_day = today

        # Convert office days into numbers
        selected_days = [office_map[d] for d in office_days]

        # Loop day by day until the date of holiday.
        while current_day < holiday_input:

            # Weekdays only
            if current_day.weekday() < 5:

                if current_day.weekday() in selected_days:
                    on_site_count += 1
                else:
                    wfh_count += 1

            # Move to the next day
            current_day += timedelta(days=1)

        total_days = (holiday_input - today).days

        st.success("Countdown Calculated!")

        st.metric("Days Until Holiday", total_days)
        st.metric("Onsite Office Days Left", on_site_count)
        st.metric("WFH Days Left", wfh_count)
        
        st.caption("Days left until your holidays")
        
        # Progress toward holiday
        # This is needed as the progress bar needs a starting date, in this case, the start of the year.
        start_of_year = datetime(today.year, 1, 1).date()\

        # This calculates the time from start of year to holiday date
        total_duration = (holiday_input - start_of_year).days
        # This then calculates the from the start of year to today.
        elapsed = (today - start_of_year).days

        
        progress = elapsed / total_duration

        st.progress(progress)