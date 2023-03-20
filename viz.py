import streamlit as st
from main import HanoiTower

st.set_page_config(page_title="Towers of Hanoi Game", layout="wide")
st.write("""# Towers of Hanoi Game""")

col1, col2 = st.columns(2)

with col1:
    subcol1, subcol2 = st.columns(2)

    with subcol1:
        disks = st.slider("Number of disks", 1, 7)

    with subcol2:
        towers = st.slider("Number of towers", 3, 5)
        st.write("""# Ending State""")
        disk_ends = []
        for disk in range(disks):
            curr_disk = disk + 1
            disk_ends.append(st.selectbox(f"Disk {curr_disk} end place", range(1, towers + 1)))

    with subcol1:
        st.write("""# Starting State""")
        disk_starts = []
        for disk in range(disks):
            curr_disk = disk + 1
            disk_starts.append(st.selectbox(f"Disk {curr_disk} start place", range(1, towers + 1)))

    disk_start = ''.join([str(elem) for elem in disk_starts])
    disk_end = ''.join([str(elem) for elem in disk_ends])

with col2:
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;justify-content: center;} </style>',
             unsafe_allow_html=True)

    st.write('<style>div.st-bf{flex-direction:column;} div.st-ag{font-weight:bold;padding-left:2px;}</style>',
             unsafe_allow_html=True)

    layout = st.radio("", ('circular', 'kamada-kawai', 'planar', 'random', 'shell', 'spring', 'spectral', 'spiral'))

    st.set_option('deprecation.showPyplotGlobalUse', False)

    hanoi_tower = HanoiTower(disks, towers, layout)
    hanoi_plot = hanoi_tower.create_tower(shortest_path=True, plot_diagram=True, start=disk_start, end=disk_end)

    st.pyplot(hanoi_plot)

    path = hanoi_tower.get_shortest_path()

with subcol1: st.write(f"""Number of Shortest Paths \n ## {hanoi_tower.num_short_paths}""")
with subcol2: st.write(f"""Shortest Path Length (number of nodes) \n ## {path}""")

