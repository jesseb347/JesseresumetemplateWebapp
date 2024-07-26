from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import numpy as np
import time
from PIL import Image


# import pyplot as plt

#import plotly as px
#import plotly.figure_factory as ff

# Draft of Jesse Resume!
"""



"""
#Hi Legacy Scholars, Parents, and Chaperones
"""


"""

st.title('Professional Portfolio of     Jesse Boateng')
st.subheader('Welcome to a look of my professional journey!', divider='rainbow')


#st.balloons()

#st.snow()



"""
# The Beginning of the Trip
"""

video_file = open('images/testclip.mov', 'rb')
video_bytes = video_file.read()

st.video(video_bytes)

#st.audio("Rev.mp3", format="audio/mpeg", loop=True)

#vimeo_url = "https://vimeo.com/837186496"
#st.video(vimeo_url)

#Thank You Legacy Parents!!
"""
whos world is this 
"""

"""
# Fishing Strategy from June 8, 2024 Event
"""

"""
45 lb striper on a private charter with The Legacy Foundation of Hartford kids today. 
We caught like 12 stripers. 7 blue fish and that fish in the picture was 45 pounds times 25 Dollars a pound. 
Its a thousand dollar fish. 45 lbs x 24.99 a lb on a fish market price = $1,125 striped bass. Returned to the ocean for another day. 
How did we do this? 
Some of the Secret is Right people with the know how and resources and gratitude to execute for our future leaders.
"""

"""
Here is some important data points:
"""
"""
June 8, 2024, the Trip
"""
"""
Fishing at "The Race"
"""
"""
Average depth: 140 feet
"""
"""
Near where: Fishers Island NY
"""
"""
Targeted Fish: Striped Bass
"""
"""
Other Fish Caught: Bluefish
"""
"""
Fishing Pole Equipment: Medium to Heavy Rod
"""
"""
Reel Type: Penn Conventional Reel
"""
"""
Fishing Line: 50 LB Monofilament 
"""
"""
Name of Participants: Anglers, Boat Captain, Mate
"""

"""
Method of catching: 
Using 10 ounce Diamond jig lures.
Technique:
"""

"""
On a drift, drop the diamond jig to the bottom on ocean floor, once hitting the floor, Reel up 15 to 30 times and drop the diamond jig back to the ocean floor. Repeat until the Captain instructs the Anglers to Reel up the lines so another drift can be done.
"""

"""
Bucktails and Swimmer lures on a 3 way rig.
"""

"""
Trolling with two umbrella rigs which simulate eels and sand eels in distress.
"""
"""
Thanks
Christopher Enam Franklin, MS
www.franklydatascience.com 
"""


"""
# What We Caught
"""
image6 = Image.open('images/JesseResume.jpeg')
st.image(image6, caption='Jesse Resume')

image7 = Image.open('images/Jesseresume2.jpeg')
st.image(image7, caption='Jesse Resume2')

image8 = Image.open('images/kudosblue.jpg')
new_image = image8.resize((300,200))
st.image(image8, caption='resized image using PIL')

image9 = Image.open('images/kudosblue.jpg')
new_image = image9.resize((100,50))
st.image(image8, caption='resized image using PIL')






st.markdown("Fishing for Striped Bass and Bluefish")

multi = '''We had fun and learned at the same time!'''
st.markdown(multi)

"""



"""
df2 = pd.DataFrame(
    [
        {"Team A": "John", "Role": "Captain", "Fish Caught": 21},
        {"Team A": "Sara", "Role": "Data Wrangler", "Fish Caught": 4},
        {"Team A": "Tony", "Role": "Team Liason", "Fish Caught": 10},
        {"Team A": "Patricia", "Role": "Assistant Captain", "Fish Caught": 6},
        {"Team A": "Tina", "Role": "Statistics Person", "Fish Caught": 30},
    ]
)


st.dataframe(df2, use_container_width=True)

st.bar_chart(df2, y = 'Team A', x='Fish Caught')

# Crypto monthly data
dc = {'Fish Caught':[1,2,3,4,5,6,7,8,9,10,11],
     'Fishing Casts':[477,387,444,462,384,297,192,327,221,193,204]}
     #'Ethereum':[3767,2796,2973,3448,2824,1816,1057,1630,1587,1311,1579]}

fishdata = pd.DataFrame(data = dc)
st.bar_chart(fishdata, y = 'Fish Caught', x='Fishing Casts')



"""
#Demo of Slider
"""

with st.echo(code_location='below'):
    total_points = st.slider("Number of points in spiral", 1, 5000, 2000)
    num_turns = st.slider("Number of turns in spiral", 1, 100, 9)

    Point = namedtuple('Point', 'x y')
    data = []

    points_per_turn = total_points / num_turns

    for curr_point_num in range(total_points):
        curr_turn, i = divmod(curr_point_num, points_per_turn)
        angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
        radius = curr_point_num / total_points
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        data.append(Point(x, y))

    st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
        .mark_circle(color='#0068c9', opacity=0.5)
        .encode(x='x:Q', y='y:Q'))

st.write("Streamlit Play:) creating dataframes and plotly plots")

"""
# June 8, 2024 Fishing Event Scheduling Tracker with Slider Functionality
"""

from datetime import time

appointment = st.slider(
    "Legacy Scholars use the Slider to show when we caught the most fish, its in Military Time, you can do it! :",
    value=(time(11, 30), time(12, 45)))
st.write("Legacy Scholars, you said we caught the most fish between these times:", appointment)

