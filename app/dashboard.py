import requests
import streamlit as st


API_URL = "http://127.0.0.1:8000"


st.set_page_config(
    page_title="StoragePulse",
    page_icon="💾",
    layout="wide"
)


st.title("💾 StoragePulse")
st.caption("Linux Storage & Filesystem Monitoring")


st.header("Disk Inventory")


try:
    response = requests.get(f"{API_URL}/disks")

    if response.status_code == 200:
        data = response.json()

        disks = data.get("blockdevices", [])

        st.write(f"**Total devices:** {len(disks)}")

        for disk in disks:

            st.subheader(f"💿 {disk.get('name')}")

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric(
                    "Size",
                    disk.get("size", "Unknown")
                )

            with col2:
                st.metric(
                    "Type",
                    disk.get("type", "Unknown")
                )

            with col3:
                st.metric(
                    "Filesystem",
                    disk.get("fstype") or "None"
                )

    else:
        st.error(
            f"FastAPI returned HTTP {response.status_code}"
        )

except requests.exceptions.ConnectionError:
    st.error(
        "Cannot connect to StoragePulse API. "
        "Make sure FastAPI is running."
    )