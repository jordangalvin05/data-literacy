# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 16:29:09 2023

@author: GALVJ
"""
import streamlit as st
import statistics
from PIL import Image


st.title('Descriptive Stats Explorer Log :tent:')
st.header('_Mean, Median & Mode_')
st.caption('10 minute read. For questions contact Jordan @ DataGovernance@perkinscoie.com')
st.subheader('A :blue[Simple] Example	:angel:')

st.text('Let\'''s say your supervisor wants to know how long it takes you to write motion \nso she can plan monthly work allocation. Of course you think, "It depends! Maybe I \nwill just give an average."\n\n'
        '⚠️ Hang on. There are 3 interpretations of the word "average." \nDepending on how you answer, you may find yourself with a lot less time to write \nyour next motion than you actually need.\n\n'
        'So, which do you choose 😕?''\n\n'
        'Suppose you kept track of how many hours you spent drafting each of your \nlast 10 motions.\n\n'
        'Your last 10 motions took you 4, 8, 6, 5, 3, 2, 8, 9, 2, and 5 hours, respectively.\n\n'
        'Notice 👀 there is quite a bit of variability here.\nThis may indicate a true average isn\'''t what we want. Let\'''s try.')

st.subheader(':red[_Mean_]')
st.text('The "Mean" of a dataset is what we typically equate with it\'''s "average."\n'
        'Mathematically, we find the Mean by adding the values of all the observations\n(in this case, our number of hours), and we divide that by the number of\nobservations (in this case, 10).')

data = [4, 8, 6, 5, 3, 2, 8, 9, 2, 5]

#mean = print("Mean:",statistics.mean([4, 8, 6, 5, 3, 2, 8, 9, 2, 5]))
#print("Median:",statistics.median([4, 8, 6, 5, 3, 2, 8, 9, 2, 5]))
#print("Mode(s):",statistics.multimode([4, 8, 6, 5, 3, 2, 8, 9, 2, 5]))
std = statistics.stdev([4, 8, 6, 5, 3, 2, 8, 9, 2, 5])
#print("Standard Deviation:",round(std,2))
col1, col2 = st.columns(2)

with col1:
   st.text("Check it 👇")
   if st.checkbox('Calculate Mean'):
       st.write("Mean:",statistics.mean([4, 8, 6, 5, 3, 2, 8, 9, 2, 5]))
       mean_image = Image.open('mean.png')
       st.image(mean_image, caption='Mean')
       with col2:
           st.text("")
           st.text("")
           st.text("")
           st.text('When would we use a mean? The answer is \nrooted in probability. When we ask for an \n"average", what we usually want is the \nmost frequent result. In other words, if \nI were writing a motion, how long 🕓 will \nit most likely take me?')
           st.text('👈 Look at the graph. Would you be \nwilling to say that a motion will most \nlikely take you 5.2 hours to finish?')
           st.text('Probably not 🙅‍♀️. It looks just as likely \nthat it will take us 2 hours or 8 hours.')
       st.text('But what if our observations were less \nvaried, and our graph looked more like a \nbell curve 🔔?')
       st.text('Here, a mean might be just what we want. \nWhy 🤔? Well, in this case 👉, drafting \na motion took us 5 hours 5 out of 10 times. \nWe only saw other results 1 or 2 times. \nSo, let me ask again: looking at the \nsecond graph, would you be willing to say \nthat a motion will most likely take you \n5.5 hours to finish?')
       with col2:
           st.text("")
           st.text("")
           st.text("")
           st.text("")
           st.text("")
           st.text("")
           hyp_mean_img = Image.open('hypo mean.png')
           st.image(hyp_mean_img, caption='Hypothetical Mean')
    
st.subheader(':red[_Median_]')
st.text('The "Median" of a dataset is found by arranging all observations in a set from \n'
        'smallest to largest and then identifying the middle value.')
st.text("Whenever you're ready 👇")
col3,col4=st.columns(2)
with col3:
    if st.checkbox('Calculate Median'):
        st.write("Median:",statistics.median([4, 8, 6, 5, 3, 2, 8, 9, 2, 5]))
        st.text('In our set,[2,2,3,4,5,5,6,8,8,9], the \nvalue directly in the middle is 5.\n'
                'We can also see, graphically, how this \ncompares to our mean.👉')
        st.text('We now revisit our probability question:\n'
                'would you say that it most typically \ntakes '
                '5 hours to draft a motion? \nStill no 🚫.')
        st.text("")
        st.text("")
        st.text("")
        hyp_med_img = Image.open('hypo median.png')
        st.image(hyp_med_img, caption='Hyptothetical Median')
        with col4:
           median_image = Image.open('median.png')
           st.image(median_image, caption = 'Median')
           st.text('Our mean and median are practically the \nsame. What good is the median? Well, what \nif I changed '
                   'things up again and made our \ndata heavily skewed?\n'
                   '👈 Look at the graph when 6 out of 10 \ntimes we can draft a motion in 2 hours.')
           st.text('Now, the hypothetical mean and median are \n'
                   'still close together, but they are \nfarther '
                   'apart than in the original graph.\nWe only '
                   'have 10 observations, but at \nsufficiently '
                   'large numbers, the mean and \nmedian will move farther '
                   'apart.')
           st.text('When data is skewed in this way, the \n'
                   "median is your best bet. But it doesn't \n"
                   'answer our current question. 😩')

st.subheader(':red[_Mode_]')
st.text('The "Mode" of a dataset is simply the most frequently-observed value in the set.')
st.text("Last one let's go 👇")

col5,col6 = st.columns(2)
with col5:    
    if st.checkbox('Calculate Mode'):
        mode = statistics.multimode([4, 8, 6, 5, 3, 2, 8, 9, 2, 5])
        modes = []
        for i in mode:
            modes.append(i)
        st.write("Mode(s):",str(modes))
        st.text("🤯 Now we see why median and mode weren't\nso helpful: our dataset is multimodal!\nIt has 3 modes.")
        st.text("With the information we have now, \n"
                "It is equally likely that it will take \n"
                "us either 2, 5, or 8 hours to draft a \n"
                "motion. I doubt this answer will satisfy \n"
                "our supervisor 😕.")
        st.text("At this point, we have two options:\n"
                "panic 😭 or ask why we see these 3\n"
                "modes.🕵️‍♀️Could it be that certain motions\n"
                "typically take 2 hours to draft and \n"
                "others typically take 8 hours?")
        st.text("This type of insight would satisfy both\n"
                "your supervisor's need to plan \neffectively"
                " and your need to actually \ncomplete work 😅.")
        with col6:
            st.text("")
            st.text("")
            st.text("")
            mode_image = Image.open('modes.png')
            st.image(mode_image, caption="Mode(s)")

    
#print(modes)
#if st.button('Calculate Standard Deviation'):
    #st.write("Standard Deviation:",round(std,2))
    
#st.subheader('Visualize this Data')

#hist_values = pd.DataFrame((4, 8, 6, 5, 3, 2, 8, 9, 2, 5))
#st.bar_chart(hist_values)

st.subheader(':red[_We Made it_] 💥')
st.text('A sincere thanks to those who took this journey with me. I hope this was a fun \n'
        'and simple introduction to some basic stats. I hope it encourages you to ask \n'
        'questions about data you previously would not have thought to. And if you ever \n'
        'need help deciding whether to use mean, median or mode, the data team is ready \n'
        'to assist! 🦸')
if st.button('Got it!'):
    st.balloons()