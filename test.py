from psychopy import visual, core, event
from psychopy.tools.filetools import fromFile, toFile
import numpy as np
import random

#### Text String Objects ####
# targets
target_self = "You"
target_other = "Next Participant"
# trial types
offer_reward = "Exert Effort to Win 10 Points for "
offer_punishment = "Exert Effort to Avoid Losing 10 Points for "
# choices
work = "Work"
rest = "Rest"
# outcomes
win_reward = "+10 Points for "
win_punishment = "-0 Points for "
lose_reward = "-0 Points for "
lose_punishment = "-10 Points for "
# grip strength effort
go = "SQUEEZE"


win = visual.Window([800,600], monitor="testMonitor", units="deg")

###### Trial Segments #######
# Offer
offers = [offer_reward, offer_punishment]
targets = [target_self, target_other]
offer_message = visual.TextStim(win, pos = [0, +3], text = 'Press Space')
offer_message.draw()
win.flip()

event.waitKeys()

message2 = visual.TextStim(win, pos = [0, +3], text = 'Press Space Again')
message2.draw()
win.flip()

event.waitKeys()