import streamlit as st
from pathlib import Path

st.set_page_config(layout="wide", page_title="The Costs of Industrialization")

# -----------------------------
# Custom CSS for UI/UX
# -----------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap');

body {
    font-family: 'Roboto', sans-serif;
}

h1, h2, h3, h4 {
    font-weight: 700;
    color: #1f3552;
}

.stApp {
    background-color: #f4f7fb;
}

.card {
    background-color: #ffffff;
    border-radius: 15px;
    padding: 20px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    margin-bottom: 25px;
}

.section-header {
    background-color: #1f3552;
    color: #ffffff;
    padding: 10px 20px;
    border-radius: 10px;
    margin-bottom: 20px;
}

.selectbox, .stSlider, .stSegmentedControl, .stPills {
    color: #1f3552;
    font-weight: 500;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Intro
# -----------------------------
st.markdown(
    """
    <div style="text-align:justify; margin-bottom:30px;">
        <h1 style="text-align: center; color:#1f3552;">The Costs of Industrialization in Vietnam</h1>
        <p style="font-size:20px; line-height:1.5; color:#333;">
            Vietnam is a small country located in the South East Asia region.
            Its government and companies have had constant efforts in developing the national situation, both economically and politically.
            Many buildings and attractions are constructed, the living standard has been raised substantially, people have gained access to many more information and facilities.
            At the same time, this does not come without any cost. Materials and resources do not spawn free.
            Let's look at how the energy and environment have changed throughout the last decades in accompany with the development of Vietnam.
            This interactive dashboard explores multiple aspects over time, highlighting the changes whether it is good or bad.
            We first observe the development index of Vietnam compared to other regions, then moving to the energy and environmental factors, and lastly how Vietnam decided to improve the situation with SGDS goals.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)
st.divider()


# -----------------------------
# Development Index
# -----------------------------
st.markdown('<div class="section-header"><h2>Development Index</h2></div>', unsafe_allow_html=True)

with st.container():
    col1, col2 = st.columns([2, 1], vertical_alignment="center")
    with col1:
        o1_map = {
            "Access to clean fuels and technologies for cooking (% of population)": 1,
            "Access to electricity (% of population)": 2,
            "Adjusted net national income per capita (current US$)": 3,
            "Energy use (kg of oil equivalent per capita)": 4
        }
        o1 = st.selectbox("Choose an index:", list(o1_map.keys()))
        html_path = Path(f'gfx/dev_idx_{o1_map[o1]}.html')
        if html_path.exists():
            with open(html_path, "r", encoding="utf-8") as f:
                html_data = f.read()
            st.components.v1.html(html_data, height=450)

    with col2:
        st.markdown(
            f"""
            <div class="card" style="height:450px; display:flex; align-items:center; justify-content:center; text-align:center;">
                <div>
                    <h3>Vietnam in terms of development</h3>
                    <p style="text-align:justify">
                    Explore Vietnam's development trajectory across key socioeconomic indicators.
                    We can easily see that Vietnam has been working hard to provide its citizens access to electricity and technology.
                    The percentage of people having access to those has increased fundamentally, matching with the bigger region and the world.
                    Though the income remains humble, but at least it is rising up, promising a great potential in the future.
                    Another indicator that shows how fast we have been developing is the energy use, which has a high rise during the last 15 years. 
                    </p>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

st.divider()

# -----------------------------
# Energy Section
# -----------------------------
st.markdown('<div class="section-header"><h2>Energy</h2></div>', unsafe_allow_html=True)

# --- Energy Trade ---
with st.container():
    col1, col2 = st.columns([1, 2], vertical_alignment="center")
    with col1:
        st.markdown(
            """
            <div class="card" style="height:450px; display:flex; align-items:center; justify-content:center; text-align:center;">
                <div>
                    <h3>Energy Imports and Supply</h3>
                    <p style="text-align:justify">
                    The need for energy has been in a constant rising status since the beginning as seen in the supply amount.
                    There used to be some time before 2015 where Vietnam was capable of self-supplying for energy, while having some to export.
                    We can see this in the graph as the import amount stayed negative during that period.
                    However, in the last 10 years, the demand for energy has risen together with the development of technology and facilities, leading to a lack in energy supply.
                    This only stopped when the pandemic appeared, resulting in a halt of everything in the country.
                    </p>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
    with col2:
        with open("gfx/energy_trade.html", "r", encoding="utf-8") as f:
            html_data = f.read()
        st.components.v1.html(html_data, height=450)

# --- Energy Type ---
with st.container():
    col1, col2 = st.columns([2, 1], vertical_alignment="center")
    with col1:
        with open("gfx/energy_type.html", "r", encoding="utf-8") as f:
            html_data = f.read()
        st.components.v1.html(html_data, height=450)
    with col2:
        st.markdown(
            """
            <div class="card" style="height:450px; display:flex; align-items:center; justify-content:center; text-align:center;">
                <div>
                    <h3>Energy Composition</h3>
                    <p style="text-align:justify">
                    While renewable energy is good for the environment, it is understandable that fossil fuels provide us with a lot of energy need for power indutries and heavy machines.
                    In the start, Vietnam also made use of a lot renewable energy. However, this trend has shifted towards fossil fuels gradually, with approximately 80% of energy consumed were fossils at peak.
                    </p>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

st.divider()

# --- CO₂ by Sector ---
with st.container():
    col1, col2 = st.columns([1, 2], vertical_alignment="center")
    with col1:
        st.markdown(
            """
            <div class="card" style="height:450px; display:flex; align-items:center; justify-content:center; text-align:center;">
                <div>
                    <h3>CO₂ Emissions by Sector</h3>
                    <p style="text-align:justify">
                    High energy output and rapid development also mean big CO₂ emissions. Industrial processes and energy has been dominating the emissions in Vietnam for all the time.
                    At first, we had forestry to balance out this amount, but this did not prove to last long for more than 10 years.
                    During 2001-2010, there had only been positive emissions amount from all the sectors.
                    Nevertheless, we witnessed a change in the forestry industry growing back in the last decade. However, this is very small compared to how much CO₂ the energy and industry produced.
                    </p>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
    with col2:
        with open("gfx/co2_sector.html", "r", encoding="utf-8") as f:
            html_data = f.read()
        st.components.v1.html(html_data, height=450)

st.divider()

# -----------------------------
# Environment Section
# -----------------------------
st.markdown('<div class="section-header"><h2>Environment</h2></div>', unsafe_allow_html=True)

# --- Land Use ---
with st.container():
    col1, col2 = st.columns([2, 1], vertical_alignment="center")
    with col1:
        o2_map = {"Absolute": "abs", "Percentage": "per"}
        o2 = st.segmented_control("Display Mode", options=o2_map.keys(), default="Absolute")
        with open(f'gfx/land_use_{o2_map[o2]}.html', "r", encoding="utf-8") as f:
            html_data = f.read()
        st.components.v1.html(html_data, height=450)
    with col2:
        st.markdown(
            """
            <div class="card" style="height:450px; display:flex; align-items:center; justify-content:center; text-align:center;">
                <div>
                    <h3>Land Use Changes</h3>
                    <p style="text-align:justify">
                    Toggle between absolute and percentage views to explore how land distribution across agricultural, forest, and urban sectors has evolved.
                    The aspect has remained quite stable throughout the years, with the same amount of land area usable.
                    In general, there has not been a big change withing arable land and forest cover, but we can observe the rise of land for permanent crops with almost a double in hectares within 16 years.
                    Agriculture is a big strong point of Vietnam and we are exploting that to push the economy forward, as well as to balance with the heavy industries.
                    </p>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

st.divider()

# --- Species ---
with st.container():
    col1, col2 = st.columns([1, 2], vertical_alignment="center")
    with col1:
        st.markdown(
            """
            <div class="card" style="height:450px; display:flex; align-items:center; justify-content:center; text-align:center;">
                <div>
                    <h3>Species at Risk</h3>
                    <p style="text-align:justify">
                    Unfortunately, the species cannot stay as constant as the lands.
                    There have been clear trends in biodiversity and species decline, and this is a major consequence of rapid land and resource use.
                    The numbers do not seem to stop any time soon, with even more species being considered threatened in the last 5 years.
                    </p>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
    with col2:
        with open("gfx/species.html", "r", encoding="utf-8") as f:
            html_data = f.read()
        st.components.v1.html(html_data, height=450)

st.divider()

# --- Weather ---
with st.container():
    col1, col2 = st.columns([2, 1], vertical_alignment="center")
    with col1:
        o3_map = {"1901-1930": "0130", "1931-1960": "3160", "1961-1990": "6190", "1991-2020": "9120"}
        o3 = st.pills("Year Range", options=o3_map.keys(), selection_mode="single", default="1901-1930")
        with open(f'gfx/weather_{o3_map[o3]}.html', "r", encoding="utf-8") as f:
            html_data = f.read()
        st.components.v1.html(html_data, height=450)
    with col2:
        st.markdown(
            """
            <div class="card" style="height:450px; display:flex; align-items:center; justify-content:center; text-align:center;">
                <div>
                    <h3>Temperature and Precipitation</h3>
                    <p style="text-align:justify">
                    Select a period to examine Vietnam's changing climate patterns across decades.  
                    Despite global warming, the temperature in Vietnam has been stable throuhgout the century.
                    The minimum, average, and maximum points are hardly any different, indicating a constant climate in the country.
                    Regarding the rainfall, Vietnam often suffers from many small floods to big typhoons around the later half of the year,
                    hence we are seeing the sudden rise in precipitation.
                    Especially in more recent years, we have experienced more severe and fatal natural disasters which could even reset our development progress to decades ago.
                    </p>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

st.divider()

# --- Temperature by Cities ---
st.markdown(
    """
    <div style="margin-bottom:10px;">
        <strong style="text-align:justify; font-size:20px;">Depending on the location and height, cities in Vietnam experience different kinds of weather and temperature.
        We can observe that there is a seasonal effect on how the temperature changes, with peak heat during summer and autumn and gradual descrease towards winter.
        And even though the overall temperature seems to increase over the years, the change has not been too drastic.
        This matches with our findings from the previous visualization that the temperature has been stable throughout the years, even when we look at a smaller scale of a city.</strong>
        <p></p>
        <p>Select the month and year to view temperature trends in cities across Vietnam:</p>
    </div>
    """,
    unsafe_allow_html=True
)

col1, col2 = st.columns([2, 1])
with col1:
    o4 = st.select_slider("Month:", 
                             ['January', 'February', 'March', 'April', 'May', 'June', 
                              'July', 'August', 'September', 'October', 'November', 'December'])
with col2:
    o5 = st.selectbox("Year:", range(2002, 2018))
with open(f'gfx/temp_cities/temp_cities_{o4}_{o5}.html', "r", encoding="utf-8") as f:
    html_data = f.read()
st.components.v1.html(html_data, height=700)

st.divider()

# -----------------------------
# Policies Section
# -----------------------------
st.markdown('<div class="section-header"><h2>Policies Timeline</h2></div>', unsafe_allow_html=True)
st.markdown(
    """
    <div style="margin-bottom:10px;">
        <strong style="text-align:justify; font-size:20px">Knowing that environmental impacts are inevitable along with urban development, 
        Vietnam has signed multiple Policies and Decisions regarding Climate Actions to match with global goals.
        The following summarizes some important milestones where Vietnam has set its own national goals while keeping up with the international standards:</strong>
    </div>
    """,
    unsafe_allow_html=True
)
with open(f'gfx/policies_timeline.html', "r", encoding="utf-8") as f:
    html_data = f.read()
st.components.v1.html(html_data, height=450)
st.divider()

# -----------------------------
# Conclusion
# -----------------------------
st.markdown('<div class="section-header"><h2>Summary</h2></div>', unsafe_allow_html=True)
st.markdown(
    """
    <div style="text-align:justify; margin-bottom:30px;">
        <p style="font-size:20px; line-height:1.5; color:#333;">
            Vietnam has been developing the country over the last 30 years, focusing on many aspects such as increasing access to more facilities and electricity.
            The efforts is shown as now it is catching up with neighboring countries and regions as well as with the world when we explore the development indicators.
            At the same time, the environment and energy has been drastically changing.
            Even though the climate seems stable, the species and precipitation are going in a bad direction without proper actions.
            The industries are going strong, with the costs of enormous gas emissions and the reliance on fossil fuels.
            To better improve the situation, Vietnam has been aware of the global goals for climate actions and actively participated in such actions, with more policies and decisions made during the last 10 years.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)