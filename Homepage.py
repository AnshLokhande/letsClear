import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Lets Clear",
    page_icon="🌐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown(
    """
    <style>
        .st-eb {
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 0px 20px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
        }
        .st-eb img {
            width: 100%;
            border-radius: 10px;
        }
        .st-eb a {
            text-decoration: none;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Title and image
st.title(""" Lets Clear
[![](https://private-user-images.githubusercontent.com/91942072/241233617-852ecf78-e684-438e-b53a-5944261b9aa3.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXkiOiJrZXkxIiwiZXhwIjoxNjg1MTA4MzI1LCJuYmYiOjE2ODUxMDgwMjUsInBhdGgiOiIvOTE5NDIwNzIvMjQxMjMzNjE3LTg1MmVjZjc4LWU2ODQtNDM4ZS1iNTNhLTU5NDQyNjFiOWFhMy5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBSVdOSllBWDRDU1ZFSDUzQSUyRjIwMjMwNTI2JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDIzMDUyNlQxMzMzNDVaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT03ODU4MWJlOTRmNzM0YTFiZGJmZThjMTcxMzJjYzJjNDgzY2QwMTgzNjM1MGQyNjgyOTBiNTZkNjgzZmNiZDA1JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.q6-S0rDvqITNe7_xFLI3OcgzQsGc3wro53Ihy8fY3vw)](https://github.com/parmishh)""")

# Problem identified
st.subheader("Problem Identified:")
st.write(""" **Haze & Fog causes several Road and Plane accidents.** Survey By Times of INDIA Shows about **11000 people died** because of accidents met due to Fog/Haze during the year 2017 and the number keeps on increasing
every year. Article By TOI: [LINK ](https://timesofindia.indiatimes.com/india/over-10000-lives-lost-in-fog-related-road-crashes/articleshow/67391588.cms)""")

st.image("tiananmen1 (1).png", caption="Foggy Road")
st.write("""Several Plane and Chopper crashes has been reported due to low visibility caused by Fog and Haze. In 2019 we lost Chief of Defence Staff, General Bipin Rawat during a chopper crash caused by low visibility caused by haze. Another accident in which **234 people died** during an Indonesian Jet crash due to reduced visibility caused by Fog and Haze Article By NewYork Times: [LINK ](https://www.nytimes.com/1997/09/27/world/indonesia-jet-crash-kills-all-234-aboard-haze-was-a-possible-cause.html)""")
st.write("""We now have a solution thanks to the breakthroughs in **Image processing Algorithms and Deep Learning techniques**. With this project we hope to come one step closer to Prevent **Accidents due to reduced visibility caused by Fog and Haze** for good!""")

# Solution
st.subheader("Solution:")
st.image("fixed.png", caption="Improved Visibility")
st.write("We have used the Efficient Image Dehazing with Boundary Constraint and Contextual Regularization Research papers as our base thanks to Gaofeng MENG, Ying WANG, Jiangyong DUAN, Shiming XIANG, Chunhong which helped to produce an image Dehazer Algorithm. The next step I took is to take an input video and split it into frames and apply image Dehazing on each frame and merge them back to produce our output video.")
