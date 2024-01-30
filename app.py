import streamlit as st
import pandas as pd
import random


# Function to generate example data
def generate_example_data(num_entries=10):
    return pd.DataFrame({
        'Room': [f'Room {i+1}' for i in range(num_entries)],
        'Status': [random.choice(['On', 'Off']) for _ in range(num_entries)],
        'Brightness': [random.randint(0, 100) for _ in range(num_entries)],
        'Temperature': [random.uniform(18.0, 30.0) for _ in range(num_entries)],
        'Motion Detected': [random.choice([True, False]) for _ in range(num_entries)],
        'Command': [''] * num_entries
    })

# Title
st.title("Fine Arts Flooring Smart Home Control")

# Sidebar for Navigation
navigation_option = st.sidebar.radio("Navigation", ["LED Lights", "Voice Control", "Smoke Monitor", "Alarm System", "Settings"])

# LED Lights Section
if navigation_option == "LED Lights":
    st.header("LED Lights Control")
    led_data = generate_example_data()
    st.dataframe(led_data)

    # Interactive Control
    selected_room = st.selectbox("Select Room:", led_data['Room'])
    brightness_slider = st.slider("Adjust Brightness:", 0, 100, led_data.loc[led_data['Room'] == selected_room, 'Brightness'].values[0])
    st.write(f"Command Sent: Adjust brightness of {selected_room} to {brightness_slider}")

    # Real-time Brightness Visualization
    fig_brightness = px.bar(led_data, x='Room', y='Brightness', color='Status', title='Real-time Brightness Status')
    st.plotly_chart(fig_brightness)

    # Real-time Motion Detection Visualization
    fig_motion = px.bar(led_data, x='Room', y='Motion Detected', color='Status', title='Motion Detection Status')
    st.plotly_chart(fig_motion)

# Voice Control Section
elif navigation_option == "Voice Control":
    st.header("Voice Control")
    voice_data = generate_example_data()
    st.dataframe(voice_data)

    # Interactive Control
    selected_room = st.selectbox("Select Room:", voice_data['Room'])
    command_input = st.text_input("Enter Voice Command:")
    st.write(f"Command Sent: '{command_input}' in {selected_room}")

# Smoke Monitor Section
elif navigation_option == "Smoke Monitor":
    st.header("Smoke Monitor")
    smoke_data = generate_example_data()
    st.dataframe(smoke_data)

    # Real-time Temperature Visualization
    fig_temperature = px.line(smoke_data, x='Room', y='Temperature', title='Real-time Temperature Status')
    st.plotly_chart(fig_temperature)

    # Notifications
    high_temp_rooms = smoke_data.loc[smoke_data['Temperature'] > 25, 'Room'].tolist()
    if high_temp_rooms:
        st.warning(f"High temperature detected in {', '.join(high_temp_rooms)}!")

# Alarm System Section
elif navigation_option == "Alarm System":
    st.header("Alarm System")
    alarm_data = generate_example_data()
    st.dataframe(alarm_data)

    # Notifications
    activated_rooms = alarm_data.loc[alarm_data['Status'] == 'On', 'Room'].tolist()
    if activated_rooms:
        st.error(f"Alarm activated! Security breach detected in {', '.join(activated_rooms)}!")

# Settings Section
elif navigation_option == "Settings":
    st.header("Settings")
    
    # Adjustable Security Threshold
    security_threshold = st.slider("Set Security Threshold:", 0, 100, 50)
    st.write(f"Security Threshold set to {security_threshold}")

    # Enable/Disable Notifications
    enable_notifications = st.checkbox("Enable Notifications", value=True)
    st.write(f"Notifications {'Enabled' if enable_notifications else 'Disabled'}")

    # Other settings...

# Footer
st.sidebar.markdown("---")
st.sidebar.info("Fine Arts Flooring Smart Home Control Dashboard")

# Run the app
if __name__ == "__main__":
    st.sidebar.success("To run the app, use the command: `streamlit run your_app_file.py`.")
