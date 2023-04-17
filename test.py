from psychopy import visual, core, event
from psychopy.tools.filetools import fromFile, toFile
import numpy as np
import random

#### Text String Objects ####
# targets
target_self = "You"
target_other = "Next Participant"
targets = [target_self, target_other]
# trial types
offer_reward = "Exert Effort to Win 10 Points for "
offer_punishment = "Exert Effort to Avoid Losing 10 Points for "
offers = [offer_reward, offer_punishment]
# choices
work = "Work"
rest = "Rest"
choices = [work, rest]
# outcomes
win_reward = "+10 Points for "
win_punishment = "-0 Points for "
lose_reward = "-0 Points for "
lose_punishment = "-10 Points for "
outcomes = [win_reward, win_punishment, lose_reward, lose_punishment]
# grip strength effort
go = "SQUEEZE"


win = visual.Window([800,600], monitor="testMonitor", units="deg")

###### Trial Segments #######
# Offer
offer_message = visual.TextStim(win, pos = [0, +3], text = offers[0] + targets[0])
offer_message.draw()
win.flip()
core.wait(3.5)

# Choice
choice_message = visual.TextStim(win, pos = [0, +3], text = 'Press Space to ' + choices[0])
choice_message.draw()
win.flip()
event.waitKeys()

# Grip
grip_message = visual.TextStim(win, pos = [0, +3], text = go)
grip_message.draw()
win.flip()
core.wait(3)

# Feedback
feedback_message = visual.TextStim(win, pos = [0, +3], text = outcomes[0] + targets[0])
feedback_message.draw()
win.flip()
core.wait(0.5)