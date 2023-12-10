#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.1.0),
    on Thu Oct  5 16:16:29 2023
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

import psychopy
psychopy.useVersion('2023.1.0')


# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2023.1.0'
expName = 'Gen_Run1_Tone'  # from the Builder filename that created this script
expInfo = {
    'participant': '',
    'run': '001',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/stashjian/Documents/Melbourne/Adolescent_Safety/GeneralizationTask_windows/Run1/Gen_Run1_Tone.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.DATA)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1512, 982], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='mri_monitor', color=[1,1,1], colorSpace='rgb',
    backgroundImage='', backgroundFit='none',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
#ioConfig = {}

# Setup iohub keyboard
#ioConfig['Keyboard'] = dict(use_keymap='psychopy')

#ioSession = '1'
#if 'session' in expInfo:
#    ioSession = str(expInfo['session'])
#ioServer = io.launchHubServer(window=win, **ioConfig)
#eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# --- Initialize components for Routine "Trigger" ---
trigger_image = visual.ImageStim(
    win=win,
    name='trigger_image', 
    image='img/runstart.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(.75, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
trigger_resp = keyboard.Keyboard()

# --- Initialize components for Routine "Wait" ---
wait = visual.TextStim(win=win, name='wait',
    text='The game will start in 5 seconds.\n\nRemember to hold still in the scanner...',
    font='Arial',
    pos=(0, 0), height=0.08, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "Block_L" ---
Block_L_ITI = visual.TextStim(win=win, name='Block_L_ITI',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.3, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Block_L_Context = visual.ImageStim(
    win=win,
    name='Block_L_Context', 
    image='img/context_lion.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.75, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
Block_L_Confidence = visual.ImageStim(
    win=win,
    name='Block_L_Confidence', 
    image='img/confidence.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.7, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
Block_L_Confidence_Resp = keyboard.Keyboard()

# --- Initialize components for Routine "firststim_loop1" ---
firststim_img_loop1 = visual.ImageStim(
    win=win,
    name='firststim_img_loop1', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.75, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# --- Initialize components for Routine "ISI_conf_stim1_loop1" ---
isi_conf_stim1_loop1 = visual.TextStim(win=win, name='isi_conf_stim1_loop1',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "conf_stim1_loop1" ---
conf_img_stim1_loop1 = visual.ImageStim(
    win=win,
    name='conf_img_stim1_loop1', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.72, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
conf_resp_stim1_loop1 = keyboard.Keyboard()

# --- Initialize components for Routine "ISI_stim_loop1" ---
isi_stim_loop1 = visual.TextStim(win=win, name='isi_stim_loop1',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "secondstim_loop1" ---
secondstim_img_loop1 = visual.ImageStim(
    win=win,
    name='secondstim_img_loop1', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.75, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# --- Initialize components for Routine "ISI_conf_stim2_loop1" ---
isi_conf_stim2_loop1 = visual.TextStim(win=win, name='isi_conf_stim2_loop1',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "conf_stim2_loop1" ---
conf_img_stim2_loop1 = visual.ImageStim(
    win=win,
    name='conf_img_stim2_loop1', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.72, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
conf_resp_stim2_loop1 = keyboard.Keyboard()

# --- Initialize components for Routine "ISI_outcome" ---
isi_outcome = visual.TextStim(win=win, name='isi_outcome',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "outcome_loop1" ---
outcome_img_loop1 = visual.ImageStim(
    win=win,
    name='outcome_img_loop1', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.75, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
Tone_loop1 = sound.Sound('A', secs=1.3, stereo=True, hamming=True,
    name='Tone_loop1')
Tone_loop1.setVolume(1.0)

# --- Initialize components for Routine "jitter_ITI_loop1" ---
iti_loop1 = visual.TextStim(win=win, name='iti_loop1',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.3, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "Block_A" ---
Block_A_ITI = visual.TextStim(win=win, name='Block_A_ITI',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.3, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Block_A_Context = visual.ImageStim(
    win=win,
    name='Block_A_Context', 
    image='img/context_antelope.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.7, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
Block_A_Confidence = visual.ImageStim(
    win=win,
    name='Block_A_Confidence', 
    image='img/confidence.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.7, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
Block_A_Resp = keyboard.Keyboard()

# --- Initialize components for Routine "firststim_loop2" ---
firststim_img_loop2 = visual.ImageStim(
    win=win,
    name='firststim_img_loop2', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.75, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# --- Initialize components for Routine "ISI_conf_stim1_loop2" ---
isi_conf_stim1_loop2 = visual.TextStim(win=win, name='isi_conf_stim1_loop2',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "conf_stim1_loop2" ---
conf_img_stim1_loop2 = visual.ImageStim(
    win=win,
    name='conf_img_stim1_loop2', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.72, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
conf_resp_stim1_loop2 = keyboard.Keyboard()

# --- Initialize components for Routine "ISI_stim_loop2" ---
isi_stim_loop2 = visual.TextStim(win=win, name='isi_stim_loop2',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "secondstim_loop2" ---
secondstim_img_loop2 = visual.ImageStim(
    win=win,
    name='secondstim_img_loop2', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.75, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# --- Initialize components for Routine "ISI_conf_stim2_loop2" ---
isi_conf_loop2 = visual.TextStim(win=win, name='isi_conf_loop2',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "conf_stim2_loop2" ---
conf_img_stim2_loop2 = visual.ImageStim(
    win=win,
    name='conf_img_stim2_loop2', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.72, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
conf_resp_stim2_loop2 = keyboard.Keyboard()

# --- Initialize components for Routine "ISI_outcome" ---
isi_outcome = visual.TextStim(win=win, name='isi_outcome',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "outcome_loop2" ---
outcome_image_loop2 = visual.ImageStim(
    win=win,
    name='outcome_image_loop2', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.75, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
Tone_loop2 = sound.Sound('A', secs=1.3, stereo=True, hamming=True,
    name='Tone_loop2')
Tone_loop2.setVolume(1.0)

# --- Initialize components for Routine "jitter_ITI_loop2" ---
iti_loop2 = visual.TextStim(win=win, name='iti_loop2',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.3, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "Block_H" ---
Block_H_ITI = visual.TextStim(win=win, name='Block_H_ITI',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.3, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Block_H_Context = visual.ImageStim(
    win=win,
    name='Block_H_Context', 
    image='img/context_hyena.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.7, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
Block_H_Confidence = visual.ImageStim(
    win=win,
    name='Block_H_Confidence', 
    image='img/confidence.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.7, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
Block_H_Resp = keyboard.Keyboard()

# --- Initialize components for Routine "firststim_loop3" ---
firststim_img_loop3 = visual.ImageStim(
    win=win,
    name='firststim_img_loop3', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.75, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# --- Initialize components for Routine "ISI_conf_stim1_loop3" ---
isi_conf_stim1_loop3 = visual.TextStim(win=win, name='isi_conf_stim1_loop3',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "conf_stim1_loop3" ---
conf_img_stim1_loop3 = visual.ImageStim(
    win=win,
    name='conf_img_stim1_loop3', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.72, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
conf_resp_stim1_loop3 = keyboard.Keyboard()

# --- Initialize components for Routine "ISI_stim_loop3" ---
isi_stim_loop3 = visual.TextStim(win=win, name='isi_stim_loop3',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "secondstim_loop3" ---
secondstim_img_loop3 = visual.ImageStim(
    win=win,
    name='secondstim_img_loop3', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.75, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# --- Initialize components for Routine "ISI_conf_stim2_loop3" ---
isi_conf_stim2_loop3 = visual.TextStim(win=win, name='isi_conf_stim2_loop3',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "conf_stim2_loop3" ---
conf_img_stim2_loop3 = visual.ImageStim(
    win=win,
    name='conf_img_stim2_loop3', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.72, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
conf_resp_stim2_loop3 = keyboard.Keyboard()

# --- Initialize components for Routine "ISI_outcome" ---
isi_outcome = visual.TextStim(win=win, name='isi_outcome',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "outcome_loop3" ---
outcome_img_loop3 = visual.ImageStim(
    win=win,
    name='outcome_img_loop3', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.75, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
Tone_loop3 = sound.Sound('A', secs=1.3, stereo=True, hamming=True,
    name='Tone_loop3')
Tone_loop3.setVolume(1.0)

# --- Initialize components for Routine "jitter_ITI_loop3" ---
iti_loop3 = visual.TextStim(win=win, name='iti_loop3',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "Completion" ---
completion_prompt = visual.TextStim(win=win, name='completion_prompt',
    text='You are finished with this scan!\n\nPlease press 1 to end.',
    font='Arial',
    pos=(0, 0), height=0.08, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
completion_prompt_resp = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "Trigger" ---
continueRoutine = True
# update component parameters for each repeat
trigger_resp.keys = []
trigger_resp.rt = []
_trigger_resp_allKeys = []
# keep track of which components have finished
TriggerComponents = [trigger_image, trigger_resp]
for thisComponent in TriggerComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Trigger" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *trigger_image* updates
    
    # if trigger_image is starting this frame...
    if trigger_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        trigger_image.frameNStart = frameN  # exact frame index
        trigger_image.tStart = t  # local t and not account for scr refresh
        trigger_image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(trigger_image, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'trigger_image.started')
        # update status
        trigger_image.status = STARTED
        trigger_image.setAutoDraw(True)
    
    # if trigger_image is active this frame...
    if trigger_image.status == STARTED:
        # update params
        pass
    
    # *trigger_resp* updates
    waitOnFlip = False
    
    # if trigger_resp is starting this frame...
    if trigger_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        trigger_resp.frameNStart = frameN  # exact frame index
        trigger_resp.tStart = t  # local t and not account for scr refresh
        trigger_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(trigger_resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'trigger_resp.started')
        # update status
        trigger_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(trigger_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(trigger_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if trigger_resp.status == STARTED and not waitOnFlip:
        theseKeys = trigger_resp.getKeys(keyList=['t'], waitRelease=False)
        _trigger_resp_allKeys.extend(theseKeys)
        if len(_trigger_resp_allKeys):
            trigger_resp.keys = _trigger_resp_allKeys[-1].name  # just the last key pressed
            trigger_resp.rt = _trigger_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in TriggerComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Trigger" ---
for thisComponent in TriggerComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if trigger_resp.keys in ['', [], None]:  # No response was made
    trigger_resp.keys = None
thisExp.addData('trigger_resp.keys',trigger_resp.keys)
if trigger_resp.keys != None:  # we had a response
    thisExp.addData('trigger_resp.rt', trigger_resp.rt)
thisExp.nextEntry()
# the Routine "Trigger" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Wait" ---
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
WaitComponents = [wait]
for thisComponent in WaitComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Wait" ---
routineForceEnded = not continueRoutine
while continueRoutine and routineTimer.getTime() < 5.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *wait* updates
    
    # if wait is starting this frame...
    if wait.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        wait.frameNStart = frameN  # exact frame index
        wait.tStart = t  # local t and not account for scr refresh
        wait.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(wait, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'wait.started')
        # update status
        wait.status = STARTED
        wait.setAutoDraw(True)
    
    # if wait is active this frame...
    if wait.status == STARTED:
        # update params
        pass
    
    # if wait is stopping this frame...
    if wait.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > wait.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            wait.tStop = t  # not accounting for scr refresh
            wait.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'wait.stopped')
            # update status
            wait.status = FINISHED
            wait.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in WaitComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Wait" ---
for thisComponent in WaitComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-5.000000)

# set up handler to look after randomisation of conditions etc
FullLoop = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='FullLoop')
thisExp.addLoop(FullLoop)  # add the loop to the experiment
thisFullLoop = FullLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisFullLoop.rgb)
if thisFullLoop != None:
    for paramName in thisFullLoop:
        exec('{} = thisFullLoop[paramName]'.format(paramName))

for thisFullLoop in FullLoop:
    currentLoop = FullLoop
    # abbreviate parameter names if possible (e.g. rgb = thisFullLoop.rgb)
    if thisFullLoop != None:
        for paramName in thisFullLoop:
            exec('{} = thisFullLoop[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    loopL = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='loopL')
    thisExp.addLoop(loopL)  # add the loop to the experiment
    thisLoopL = loopL.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisLoopL.rgb)
    if thisLoopL != None:
        for paramName in thisLoopL:
            exec('{} = thisLoopL[paramName]'.format(paramName))
    
    for thisLoopL in loopL:
        currentLoop = loopL
        # abbreviate parameter names if possible (e.g. rgb = thisLoopL.rgb)
        if thisLoopL != None:
            for paramName in thisLoopL:
                exec('{} = thisLoopL[paramName]'.format(paramName))
        
        # # --- Prepare to start Routine "Block_L" ---
        # continueRoutine = True
        # # update component parameters for each repeat
        # # Block_L_Confidence_Resp.keys = []
        # # Block_L_Confidence_Resp.rt = []
        # # _Block_L_Confidence_Resp_allKeys = []
        # # keep track of which components have finished
        # # Block_LComponents = [Block_L_ITI, Block_L_Context, Block_L_Confidence, Block_L_Confidence_Resp]
        # Block_LComponents = [Block_L_ITI, Block_L_Context]
        # for thisComponent in Block_LComponents:
        #     thisComponent.tStart = None
        #     thisComponent.tStop = None
        #     thisComponent.tStartRefresh = None
        #     thisComponent.tStopRefresh = None
        #     if hasattr(thisComponent, 'status'):
        #         thisComponent.status = NOT_STARTED
        # # reset timers
        # t = 0
        # _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        # frameN = -1
        
        # # --- Run Routine "Block_L" ---
        # routineForceEnded = not continueRoutine
        # while continueRoutine and routineTimer.getTime() < 10.5:
        #     # get current time
        #     t = routineTimer.getTime()
        #     tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        #     tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        #     frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        #     # update/draw components on each frame
            
        #     # *Block_L_ITI* updates
            
        #     # if Block_L_ITI is starting this frame...
        #     if Block_L_ITI.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        #         # keep track of start time/frame for later
        #         Block_L_ITI.frameNStart = frameN  # exact frame index
        #         Block_L_ITI.tStart = t  # local t and not account for scr refresh
        #         Block_L_ITI.tStartRefresh = tThisFlipGlobal  # on global time
        #         win.timeOnFlip(Block_L_ITI, 'tStartRefresh')  # time at next scr refresh
        #         # add timestamp to datafile
        #         thisExp.timestampOnFlip(win, 'Block_L_ITI.started')
        #         # update status
        #         Block_L_ITI.status = STARTED
        #         Block_L_ITI.setAutoDraw(True)
            
        #     # if Block_L_ITI is active this frame...
        #     if Block_L_ITI.status == STARTED:
        #         # update params
        #         pass
            
        #     # if Block_L_ITI is stopping this frame...
        #     if Block_L_ITI.status == STARTED:
        #         # is it time to stop? (based on global clock, using actual start)
        #         if tThisFlipGlobal > Block_L_ITI.tStartRefresh + .5-frameTolerance:
        #             # keep track of stop time/frame for later
        #             Block_L_ITI.tStop = t  # not accounting for scr refresh
        #             Block_L_ITI.frameNStop = frameN  # exact frame index
        #             # add timestamp to datafile
        #             thisExp.timestampOnFlip(win, 'Block_L_ITI.stopped')
        #             # update status
        #             Block_L_ITI.status = FINISHED
        #             Block_L_ITI.setAutoDraw(False)
            
        #     # *Block_L_Context* updates
            
        #     # if Block_L_Context is starting this frame...
        #     if Block_L_Context.status == NOT_STARTED and tThisFlip >= .5-frameTolerance:
        #         # keep track of start time/frame for later
        #         Block_L_Context.frameNStart = frameN  # exact frame index
        #         Block_L_Context.tStart = t  # local t and not account for scr refresh
        #         Block_L_Context.tStartRefresh = tThisFlipGlobal  # on global time
        #         win.timeOnFlip(Block_L_Context, 'tStartRefresh')  # time at next scr refresh
        #         # add timestamp to datafile
        #         thisExp.timestampOnFlip(win, 'Block_L_Context.started')
        #         # update status
        #         Block_L_Context.status = STARTED
        #         Block_L_Context.setAutoDraw(True)
            
        #     # if Block_L_Context is active this frame...
        #     if Block_L_Context.status == STARTED:
        #         # update params
        #         pass
            
        #     # if Block_L_Context is stopping this frame...
        #     if Block_L_Context.status == STARTED:
        #         # is it time to stop? (based on global clock, using actual start)
        #         if tThisFlipGlobal > Block_L_Context.tStartRefresh + 5.0-frameTolerance:
        #             # keep track of stop time/frame for later
        #             Block_L_Context.tStop = t  # not accounting for scr refresh
        #             Block_L_Context.frameNStop = frameN  # exact frame index
        #             # add timestamp to datafile
        #             thisExp.timestampOnFlip(win, 'Block_L_Context.stopped')
        #             # update status
        #             Block_L_Context.status = FINISHED
        #             Block_L_Context.setAutoDraw(False)
            
        #     # # *Block_L_Confidence* updates
            
        #     # # if Block_L_Confidence is starting this frame...
        #     # if Block_L_Confidence.status == NOT_STARTED and tThisFlip >= 5.5-frameTolerance:
        #     #     # keep track of start time/frame for later
        #     #     Block_L_Confidence.frameNStart = frameN  # exact frame index
        #     #     Block_L_Confidence.tStart = t  # local t and not account for scr refresh
        #     #     Block_L_Confidence.tStartRefresh = tThisFlipGlobal  # on global time
        #     #     win.timeOnFlip(Block_L_Confidence, 'tStartRefresh')  # time at next scr refresh
        #     #     # add timestamp to datafile
        #     #     thisExp.timestampOnFlip(win, 'Block_L_Confidence.started')
        #     #     # update status
        #     #     Block_L_Confidence.status = STARTED
        #     #     Block_L_Confidence.setAutoDraw(True)
            
        #     # # if Block_L_Confidence is active this frame...
        #     # if Block_L_Confidence.status == STARTED:
        #     #     # update params
        #     #     pass
            
        #     # # if Block_L_Confidence is stopping this frame...
        #     # if Block_L_Confidence.status == STARTED:
        #     #     # is it time to stop? (based on global clock, using actual start)
        #     #     if tThisFlipGlobal > Block_L_Confidence.tStartRefresh + 7-frameTolerance:
        #     #         # keep track of stop time/frame for later
        #     #         Block_L_Confidence.tStop = t  # not accounting for scr refresh
        #     #         Block_L_Confidence.frameNStop = frameN  # exact frame index
        #     #         # add timestamp to datafile
        #     #         thisExp.timestampOnFlip(win, 'Block_L_Confidence.stopped')
        #     #         # update status
        #     #         Block_L_Confidence.status = FINISHED
        #     #         Block_L_Confidence.setAutoDraw(False)
            
        #     # # *Block_L_Confidence_Resp* updates
        #     # waitOnFlip = False
            
        #     # # if Block_L_Confidence_Resp is starting this frame...
        #     # if Block_L_Confidence_Resp.status == NOT_STARTED and tThisFlip >= 5.5-frameTolerance:
        #     #     # keep track of start time/frame for later
        #     #     Block_L_Confidence_Resp.frameNStart = frameN  # exact frame index
        #     #     Block_L_Confidence_Resp.tStart = t  # local t and not account for scr refresh
        #     #     Block_L_Confidence_Resp.tStartRefresh = tThisFlipGlobal  # on global time
        #     #     win.timeOnFlip(Block_L_Confidence_Resp, 'tStartRefresh')  # time at next scr refresh
        #     #     # add timestamp to datafile
        #     #     thisExp.timestampOnFlip(win, 'Block_L_Confidence_Resp.started')
        #     #     # update status
        #     #     Block_L_Confidence_Resp.status = STARTED
        #     #     # keyboard checking is just starting
        #     #     waitOnFlip = True
        #     #     win.callOnFlip(Block_L_Confidence_Resp.clock.reset)  # t=0 on next screen flip
        #     #     win.callOnFlip(Block_L_Confidence_Resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            
        #     # # if Block_L_Confidence_Resp is stopping this frame...
        #     # if Block_L_Confidence_Resp.status == STARTED:
        #     #     # is it time to stop? (based on global clock, using actual start)
        #     #     if tThisFlipGlobal > Block_L_Confidence_Resp.tStartRefresh + 7-frameTolerance:
        #     #         # keep track of stop time/frame for later
        #     #         Block_L_Confidence_Resp.tStop = t  # not accounting for scr refresh
        #     #         Block_L_Confidence_Resp.frameNStop = frameN  # exact frame index
        #     #         # add timestamp to datafile
        #     #         thisExp.timestampOnFlip(win, 'Block_L_Confidence_Resp.stopped')
        #     #         # update status
        #     #         Block_L_Confidence_Resp.status = FINISHED
        #     #         Block_L_Confidence_Resp.status = FINISHED
        #     # if Block_L_Confidence_Resp.status == STARTED and not waitOnFlip:
        #     #     theseKeys = Block_L_Confidence_Resp.getKeys(keyList=['a','b','c','d', 'A', 'B', 'C', 'D'], waitRelease=False)
        #     #     _Block_L_Confidence_Resp_allKeys.extend(theseKeys)
        #     #     if len(_Block_L_Confidence_Resp_allKeys):
        #     #         Block_L_Confidence_Resp.keys = [key.name for key in _Block_L_Confidence_Resp_allKeys]  # storing all keys
        #     #         Block_L_Confidence_Resp.rt = [key.rt for key in _Block_L_Confidence_Resp_allKeys]
        #     #         # a response ends the routine
        #     #         continueRoutine = False
            
        #     # check for quit (typically the Esc key)
        #     if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        #         core.quit()
            
        #     # check if all components have finished
        #     if not continueRoutine:  # a component has requested a forced-end of Routine
        #         routineForceEnded = True
        #         break
        #     continueRoutine = False  # will revert to True if at least one component still running
        #     for thisComponent in Block_LComponents:
        #         if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
        #             continueRoutine = True
        #             break  # at least one component has not yet finished
            
        #     # refresh the screen
        #     if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        #         win.flip()
        
        # # --- Ending Routine "Block_L" ---
        # for thisComponent in Block_LComponents:
        #     if hasattr(thisComponent, "setAutoDraw"):
        #         thisComponent.setAutoDraw(False)
        # # # check responses
        # # if Block_L_Confidence_Resp.keys in ['', [], None]:  # No response was made
        # #     Block_L_Confidence_Resp.keys = None
        # # loopL.addData('Block_L_Confidence_Resp.keys',Block_L_Confidence_Resp.keys)
        # # if Block_L_Confidence_Resp.keys != None:  # we had a response
        # #     loopL.addData('Block_L_Confidence_Resp.rt', Block_L_Confidence_Resp.rt)
        # # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        # if routineForceEnded:
        #     routineTimer.reset()
        # else:
        #     routineTimer.addTime(-10.500000)
        
        # set up handler to look after randomisation of conditions etc
        loop1 = data.TrialHandler(nReps=1.0, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('Battles_Run1_L.xlsx'),
            seed=None, name='loop1')
        thisExp.addLoop(loop1)  # add the loop to the experiment
        thisLoop1 = loop1.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisLoop1.rgb)
        if thisLoop1 != None:
            for paramName in thisLoop1:
                exec('{} = thisLoop1[paramName]'.format(paramName))
        
        for thisLoop1 in loop1:
            currentLoop = loop1
            # abbreviate parameter names if possible (e.g. rgb = thisLoop1.rgb)
            if thisLoop1 != None:
                for paramName in thisLoop1:
                    exec('{} = thisLoop1[paramName]'.format(paramName))
            
            # --- Prepare to start Routine "firststim_loop1" ---
            continueRoutine = True
            # update component parameters for each repeat
            firststim_img_loop1.setImage(FirstStimL)
            # keep track of which components have finished
            firststim_loop1Components = [firststim_img_loop1]
            for thisComponent in firststim_loop1Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "firststim_loop1" ---
            routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 1.0:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *firststim_img_loop1* updates
                
                # if firststim_img_loop1 is starting this frame...
                if firststim_img_loop1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    firststim_img_loop1.frameNStart = frameN  # exact frame index
                    firststim_img_loop1.tStart = t  # local t and not account for scr refresh
                    firststim_img_loop1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(firststim_img_loop1, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'firststim_img_loop1.started')
                    # update status
                    firststim_img_loop1.status = STARTED
                    firststim_img_loop1.setAutoDraw(True)
                
                # if firststim_img_loop1 is active this frame...
                if firststim_img_loop1.status == STARTED:
                    # update params
                    pass
                
                # if firststim_img_loop1 is stopping this frame...
                if firststim_img_loop1.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > firststim_img_loop1.tStartRefresh + 1-frameTolerance:
                        # keep track of stop time/frame for later
                        firststim_img_loop1.tStop = t  # not accounting for scr refresh
                        firststim_img_loop1.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'firststim_img_loop1.stopped')
                        # update status
                        firststim_img_loop1.status = FINISHED
                        firststim_img_loop1.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in firststim_loop1Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "firststim_loop1" ---
            for thisComponent in firststim_loop1Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-1.000000)
            
            # --- Prepare to start Routine "ISI_conf_stim1_loop1" ---
            continueRoutine = True
            # update component parameters for each repeat
            # keep track of which components have finished
            ISI_conf_stim1_loop1Components = [isi_conf_stim1_loop1]
            for thisComponent in ISI_conf_stim1_loop1Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "ISI_conf_stim1_loop1" ---
            routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 0.25:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *isi_conf_stim1_loop1* updates
                
                # if isi_conf_stim1_loop1 is starting this frame...
                if isi_conf_stim1_loop1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    isi_conf_stim1_loop1.frameNStart = frameN  # exact frame index
                    isi_conf_stim1_loop1.tStart = t  # local t and not account for scr refresh
                    isi_conf_stim1_loop1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(isi_conf_stim1_loop1, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'isi_conf_stim1_loop1.started')
                    # update status
                    isi_conf_stim1_loop1.status = STARTED
                    isi_conf_stim1_loop1.setAutoDraw(True)
                
                # if isi_conf_stim1_loop1 is active this frame...
                if isi_conf_stim1_loop1.status == STARTED:
                    # update params
                    pass
                
                # if isi_conf_stim1_loop1 is stopping this frame...
                if isi_conf_stim1_loop1.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > isi_conf_stim1_loop1.tStartRefresh + .3-frameTolerance:
                        # keep track of stop time/frame for later
                        isi_conf_stim1_loop1.tStop = t  # not accounting for scr refresh
                        isi_conf_stim1_loop1.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'isi_conf_stim1_loop1.stopped')
                        # update status
                        isi_conf_stim1_loop1.status = FINISHED
                        isi_conf_stim1_loop1.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in ISI_conf_stim1_loop1Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "ISI_conf_stim1_loop1" ---
            for thisComponent in ISI_conf_stim1_loop1Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-0.250000)
            
            # --- Prepare to start Routine "conf_stim1_loop1" ---
            continueRoutine = True
            # update component parameters for each repeat
            conf_img_stim1_loop1.setImage(ConfidenceL)
            conf_resp_stim1_loop1.keys = []
            conf_resp_stim1_loop1.rt = []
            _conf_resp_stim1_loop1_allKeys = []
            # keep track of which components have finished
            conf_stim1_loop1Components = [conf_img_stim1_loop1, conf_resp_stim1_loop1]
            for thisComponent in conf_stim1_loop1Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "conf_stim1_loop1" ---
            routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 5.0:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *conf_img_stim1_loop1* updates
                
                # if conf_img_stim1_loop1 is starting this frame...
                if conf_img_stim1_loop1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    conf_img_stim1_loop1.frameNStart = frameN  # exact frame index
                    conf_img_stim1_loop1.tStart = t  # local t and not account for scr refresh
                    conf_img_stim1_loop1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(conf_img_stim1_loop1, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'conf_img_stim1_loop1.started')
                    # update status
                    conf_img_stim1_loop1.status = STARTED
                    conf_img_stim1_loop1.setAutoDraw(True)
                
                # if conf_img_stim1_loop1 is active this frame...
                if conf_img_stim1_loop1.status == STARTED:
                    # update params
                    pass
                
                # if conf_img_stim1_loop1 is stopping this frame...
                if conf_img_stim1_loop1.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > conf_img_stim1_loop1.tStartRefresh + 5-frameTolerance:
                        # keep track of stop time/frame for later
                        conf_img_stim1_loop1.tStop = t  # not accounting for scr refresh
                        conf_img_stim1_loop1.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'conf_img_stim1_loop1.stopped')
                        # update status
                        conf_img_stim1_loop1.status = FINISHED
                        conf_img_stim1_loop1.setAutoDraw(False)
                
                # *conf_resp_stim1_loop1* updates
                waitOnFlip = False
                
                # if conf_resp_stim1_loop1 is starting this frame...
                if conf_resp_stim1_loop1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    conf_resp_stim1_loop1.frameNStart = frameN  # exact frame index
                    conf_resp_stim1_loop1.tStart = t  # local t and not account for scr refresh
                    conf_resp_stim1_loop1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(conf_resp_stim1_loop1, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'conf_resp_stim1_loop1.started')
                    # update status
                    conf_resp_stim1_loop1.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(conf_resp_stim1_loop1.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(conf_resp_stim1_loop1.clearEvents, eventType='keyboard')  # clear events on next screen flip
                
                # if conf_resp_stim1_loop1 is stopping this frame...
                if conf_resp_stim1_loop1.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > conf_resp_stim1_loop1.tStartRefresh + 5-frameTolerance:
                        # keep track of stop time/frame for later
                        conf_resp_stim1_loop1.tStop = t  # not accounting for scr refresh
                        conf_resp_stim1_loop1.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'conf_resp_stim1_loop1.stopped')
                        # update status
                        conf_resp_stim1_loop1.status = FINISHED
                        conf_resp_stim1_loop1.status = FINISHED
                if conf_resp_stim1_loop1.status == STARTED and not waitOnFlip:
                    theseKeys = conf_resp_stim1_loop1.getKeys(keyList=['a','b','c','d','A', 'B', 'C', 'D'], waitRelease=False)
                    _conf_resp_stim1_loop1_allKeys.extend(theseKeys)
                    if len(_conf_resp_stim1_loop1_allKeys):
                        conf_resp_stim1_loop1.keys = [key.name for key in _conf_resp_stim1_loop1_allKeys]  # storing all keys
                        conf_resp_stim1_loop1.rt = [key.rt for key in _conf_resp_stim1_loop1_allKeys]
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in conf_stim1_loop1Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "conf_stim1_loop1" ---
            for thisComponent in conf_stim1_loop1Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # check responses
            if conf_resp_stim1_loop1.keys in ['', [], None]:  # No response was made
                conf_resp_stim1_loop1.keys = None
            loop1.addData('conf_resp_stim1_loop1.keys',conf_resp_stim1_loop1.keys)
            if conf_resp_stim1_loop1.keys != None:  # we had a response
                loop1.addData('conf_resp_stim1_loop1.rt', conf_resp_stim1_loop1.rt)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-5.000000)
            
            # --- Prepare to start Routine "ISI_stim_loop1" ---
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from isi_stim_code_loop1
            import random as rand
            
            jitter_isi_1 = rand.choices([0.5, 0.5, 0.5, 1.0, 1.0, 1.5, 2.0], k=54) # create the list
            
            
            if loop1.thisN == 0: # only on the first trial
                shuffle(jitter_isi_1) # randomise its order
            
            current_isi_1 = jitter_isi_1.pop() # extract one entry on each trial
            thisExp.addData('isi_stim_1', current_isi_1) # record in the data for this trial
            # keep track of which components have finished
            ISI_stim_loop1Components = [isi_stim_loop1]
            for thisComponent in ISI_stim_loop1Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "ISI_stim_loop1" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *isi_stim_loop1* updates
                
                # if isi_stim_loop1 is starting this frame...
                if isi_stim_loop1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    isi_stim_loop1.frameNStart = frameN  # exact frame index
                    isi_stim_loop1.tStart = t  # local t and not account for scr refresh
                    isi_stim_loop1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(isi_stim_loop1, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'isi_stim_loop1.started')
                    # update status
                    isi_stim_loop1.status = STARTED
                    isi_stim_loop1.setAutoDraw(True)
                
                # if isi_stim_loop1 is active this frame...
                if isi_stim_loop1.status == STARTED:
                    # update params
                    pass
                
                # if isi_stim_loop1 is stopping this frame...
                if isi_stim_loop1.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > isi_stim_loop1.tStartRefresh + current_isi_1-frameTolerance:
                        # keep track of stop time/frame for later
                        isi_stim_loop1.tStop = t  # not accounting for scr refresh
                        isi_stim_loop1.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'isi_stim_loop1.stopped')
                        # update status
                        isi_stim_loop1.status = FINISHED
                        isi_stim_loop1.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in ISI_stim_loop1Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "ISI_stim_loop1" ---
            for thisComponent in ISI_stim_loop1Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # the Routine "ISI_stim_loop1" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "secondstim_loop1" ---
            continueRoutine = True
            # update component parameters for each repeat
            secondstim_img_loop1.setImage(SecondStimL)
            # keep track of which components have finished
            secondstim_loop1Components = [secondstim_img_loop1]
            for thisComponent in secondstim_loop1Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "secondstim_loop1" ---
            routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 1.0:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *secondstim_img_loop1* updates
                
                # if secondstim_img_loop1 is starting this frame...
                if secondstim_img_loop1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    secondstim_img_loop1.frameNStart = frameN  # exact frame index
                    secondstim_img_loop1.tStart = t  # local t and not account for scr refresh
                    secondstim_img_loop1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(secondstim_img_loop1, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'secondstim_img_loop1.started')
                    # update status
                    secondstim_img_loop1.status = STARTED
                    secondstim_img_loop1.setAutoDraw(True)
                
                # if secondstim_img_loop1 is active this frame...
                if secondstim_img_loop1.status == STARTED:
                    # update params
                    pass
                
                # if secondstim_img_loop1 is stopping this frame...
                if secondstim_img_loop1.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > secondstim_img_loop1.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        secondstim_img_loop1.tStop = t  # not accounting for scr refresh
                        secondstim_img_loop1.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'secondstim_img_loop1.stopped')
                        # update status
                        secondstim_img_loop1.status = FINISHED
                        secondstim_img_loop1.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in secondstim_loop1Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "secondstim_loop1" ---
            for thisComponent in secondstim_loop1Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-1.000000)
            
            # --- Prepare to start Routine "ISI_conf_stim2_loop1" ---
            continueRoutine = True
            # update component parameters for each repeat
            # keep track of which components have finished
            ISI_conf_stim2_loop1Components = [isi_conf_stim2_loop1]
            for thisComponent in ISI_conf_stim2_loop1Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "ISI_conf_stim2_loop1" ---
            routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 0.25:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *isi_conf_stim2_loop1* updates
                
                # if isi_conf_stim2_loop1 is starting this frame...
                if isi_conf_stim2_loop1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    isi_conf_stim2_loop1.frameNStart = frameN  # exact frame index
                    isi_conf_stim2_loop1.tStart = t  # local t and not account for scr refresh
                    isi_conf_stim2_loop1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(isi_conf_stim2_loop1, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'isi_conf_stim2_loop1.started')
                    # update status
                    isi_conf_stim2_loop1.status = STARTED
                    isi_conf_stim2_loop1.setAutoDraw(True)
                
                # if isi_conf_stim2_loop1 is active this frame...
                if isi_conf_stim2_loop1.status == STARTED:
                    # update params
                    pass
                
                # if isi_conf_stim2_loop1 is stopping this frame...
                if isi_conf_stim2_loop1.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > isi_conf_stim2_loop1.tStartRefresh + .3-frameTolerance:
                        # keep track of stop time/frame for later
                        isi_conf_stim2_loop1.tStop = t  # not accounting for scr refresh
                        isi_conf_stim2_loop1.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'isi_conf_stim2_loop1.stopped')
                        # update status
                        isi_conf_stim2_loop1.status = FINISHED
                        isi_conf_stim2_loop1.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in ISI_conf_stim2_loop1Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "ISI_conf_stim2_loop1" ---
            for thisComponent in ISI_conf_stim2_loop1Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-0.250000)
            
            # --- Prepare to start Routine "conf_stim2_loop1" ---
            continueRoutine = True
            # update component parameters for each repeat
            conf_img_stim2_loop1.setImage(ConfidenceL)
            conf_resp_stim2_loop1.keys = []
            conf_resp_stim2_loop1.rt = []
            _conf_resp_stim2_loop1_allKeys = []
            # keep track of which components have finished
            conf_stim2_loop1Components = [conf_img_stim2_loop1, conf_resp_stim2_loop1]
            for thisComponent in conf_stim2_loop1Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "conf_stim2_loop1" ---
            routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 5.0:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *conf_img_stim2_loop1* updates
                
                # if conf_img_stim2_loop1 is starting this frame...
                if conf_img_stim2_loop1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    conf_img_stim2_loop1.frameNStart = frameN  # exact frame index
                    conf_img_stim2_loop1.tStart = t  # local t and not account for scr refresh
                    conf_img_stim2_loop1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(conf_img_stim2_loop1, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'conf_img_stim2_loop1.started')
                    # update status
                    conf_img_stim2_loop1.status = STARTED
                    conf_img_stim2_loop1.setAutoDraw(True)
                
                # if conf_img_stim2_loop1 is active this frame...
                if conf_img_stim2_loop1.status == STARTED:
                    # update params
                    pass
                
                # if conf_img_stim2_loop1 is stopping this frame...
                if conf_img_stim2_loop1.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > conf_img_stim2_loop1.tStartRefresh + 5-frameTolerance:
                        # keep track of stop time/frame for later
                        conf_img_stim2_loop1.tStop = t  # not accounting for scr refresh
                        conf_img_stim2_loop1.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'conf_img_stim2_loop1.stopped')
                        # update status
                        conf_img_stim2_loop1.status = FINISHED
                        conf_img_stim2_loop1.setAutoDraw(False)
                
                # *conf_resp_stim2_loop1* updates
                waitOnFlip = False
                
                # if conf_resp_stim2_loop1 is starting this frame...
                if conf_resp_stim2_loop1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    conf_resp_stim2_loop1.frameNStart = frameN  # exact frame index
                    conf_resp_stim2_loop1.tStart = t  # local t and not account for scr refresh
                    conf_resp_stim2_loop1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(conf_resp_stim2_loop1, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'conf_resp_stim2_loop1.started')
                    # update status
                    conf_resp_stim2_loop1.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(conf_resp_stim2_loop1.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(conf_resp_stim2_loop1.clearEvents, eventType='keyboard')  # clear events on next screen flip
                
                # if conf_resp_stim2_loop1 is stopping this frame...
                if conf_resp_stim2_loop1.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > conf_resp_stim2_loop1.tStartRefresh + 5-frameTolerance:
                        # keep track of stop time/frame for later
                        conf_resp_stim2_loop1.tStop = t  # not accounting for scr refresh
                        conf_resp_stim2_loop1.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'conf_resp_stim2_loop1.stopped')
                        # update status
                        conf_resp_stim2_loop1.status = FINISHED
                        conf_resp_stim2_loop1.status = FINISHED
                if conf_resp_stim2_loop1.status == STARTED and not waitOnFlip:
                    theseKeys = conf_resp_stim2_loop1.getKeys(keyList=['a','b','c','d', 'A', 'B', 'C', 'D'], waitRelease=False)
                    _conf_resp_stim2_loop1_allKeys.extend(theseKeys)
                    if len(_conf_resp_stim2_loop1_allKeys):
                        conf_resp_stim2_loop1.keys = [key.name for key in _conf_resp_stim2_loop1_allKeys]  # storing all keys
                        conf_resp_stim2_loop1.rt = [key.rt for key in _conf_resp_stim2_loop1_allKeys]
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in conf_stim2_loop1Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "conf_stim2_loop1" ---
            for thisComponent in conf_stim2_loop1Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # check responses
            if conf_resp_stim2_loop1.keys in ['', [], None]:  # No response was made
                conf_resp_stim2_loop1.keys = None
            loop1.addData('conf_resp_stim2_loop1.keys',conf_resp_stim2_loop1.keys)
            if conf_resp_stim2_loop1.keys != None:  # we had a response
                loop1.addData('conf_resp_stim2_loop1.rt', conf_resp_stim2_loop1.rt)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-5.000000)
            
            # --- Prepare to start Routine "ISI_outcome" ---
            continueRoutine = True
            # update component parameters for each repeat
            # keep track of which components have finished
            ISI_outcomeComponents = [isi_outcome]
            for thisComponent in ISI_outcomeComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "ISI_outcome" ---
            routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < .25:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *isi_outcome* updates
                
                # if isi_outcome is starting this frame...
                if isi_outcome.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    isi_outcome.frameNStart = frameN  # exact frame index
                    isi_outcome.tStart = t  # local t and not account for scr refresh
                    isi_outcome.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(isi_outcome, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'isi_outcome.started')
                    # update status
                    isi_outcome.status = STARTED
                    isi_outcome.setAutoDraw(True)
                
                # if isi_outcome is active this frame...
                if isi_outcome.status == STARTED:
                    # update params
                    pass
                
                # if isi_outcome is stopping this frame...
                if isi_outcome.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > isi_outcome.tStartRefresh + 0.5-frameTolerance:
                        # keep track of stop time/frame for later
                        isi_outcome.tStop = t  # not accounting for scr refresh
                        isi_outcome.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'isi_outcome.stopped')
                        # update status
                        isi_outcome.status = FINISHED
                        isi_outcome.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in ISI_outcomeComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "ISI_outcome" ---
            for thisComponent in ISI_outcomeComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-0.2500000)
            
            # --- Prepare to start Routine "outcome_loop1" ---
            continueRoutine = True
            # update component parameters for each repeat
            outcome_img_loop1.setImage(OutcomeL)
            Tone_loop1.setSound(ToneL, secs=1.3, hamming=True)
            Tone_loop1.setVolume(1.0, log=False)
            # keep track of which components have finished
            outcome_loop1Components = [outcome_img_loop1, Tone_loop1]
            for thisComponent in outcome_loop1Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "outcome_loop1" ---
            routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 1.5:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *outcome_img_loop1* updates
                
                # if outcome_img_loop1 is starting this frame...
                if outcome_img_loop1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    outcome_img_loop1.frameNStart = frameN  # exact frame index
                    outcome_img_loop1.tStart = t  # local t and not account for scr refresh
                    outcome_img_loop1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(outcome_img_loop1, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'outcome_img_loop1.started')
                    # update status
                    outcome_img_loop1.status = STARTED
                    outcome_img_loop1.setAutoDraw(True)
                
                # if outcome_img_loop1 is active this frame...
                if outcome_img_loop1.status == STARTED:
                    # update params
                    pass
                
                # if outcome_img_loop1 is stopping this frame...
                if outcome_img_loop1.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > outcome_img_loop1.tStartRefresh + 1.5-frameTolerance:
                        # keep track of stop time/frame for later
                        outcome_img_loop1.tStop = t  # not accounting for scr refresh
                        outcome_img_loop1.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'outcome_img_loop1.stopped')
                        # update status
                        outcome_img_loop1.status = FINISHED
                        outcome_img_loop1.setAutoDraw(False)
                # start/stop Tone_loop1
                
                # if Tone_loop1 is starting this frame...
                if Tone_loop1.status == NOT_STARTED and tThisFlip >= .2-frameTolerance:
                    # keep track of start time/frame for later
                    Tone_loop1.frameNStart = frameN  # exact frame index
                    Tone_loop1.tStart = t  # local t and not account for scr refresh
                    Tone_loop1.tStartRefresh = tThisFlipGlobal  # on global time
                    # add timestamp to datafile
                    thisExp.addData('Tone_loop1.started', tThisFlipGlobal)
                    # update status
                    Tone_loop1.status = STARTED
                    Tone_loop1.play(when=win)  # sync with win flip
                
                # if Tone_loop1 is stopping this frame...
                if Tone_loop1.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Tone_loop1.tStartRefresh + 1.3-frameTolerance:
                        # keep track of stop time/frame for later
                        Tone_loop1.tStop = t  # not accounting for scr refresh
                        Tone_loop1.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'Tone_loop1.stopped')
                        # update status
                        Tone_loop1.status = FINISHED
                        Tone_loop1.stop()
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in outcome_loop1Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "outcome_loop1" ---
            for thisComponent in outcome_loop1Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            Tone_loop1.stop()  # ensure sound has stopped at end of routine
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-1.500000)
            
            # --- Prepare to start Routine "jitter_ITI_loop1" ---
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from iti_code_loop1
            import random as rand
            
            jitter_iti_1 = rand.choices([.5, 1.0, 1.5, 2.0], k=54) # create the list
            
            if loop1.thisN == 0: # only on the first trial
                shuffle(jitter_iti_1) # randomise its order
            
            current_jitter_1 = jitter_iti_1.pop() # extract one entry on each trial
            
            thisExp.addData('jitter_iti_1', current_jitter_1) # record in the data for this trial
            
            
            # keep track of which components have finished
            jitter_ITI_loop1Components = [iti_loop1]
            for thisComponent in jitter_ITI_loop1Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "jitter_ITI_loop1" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *iti_loop1* updates
                
                # if iti_loop1 is starting this frame...
                if iti_loop1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    iti_loop1.frameNStart = frameN  # exact frame index
                    iti_loop1.tStart = t  # local t and not account for scr refresh
                    iti_loop1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(iti_loop1, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'iti_loop1.started')
                    # update status
                    iti_loop1.status = STARTED
                    iti_loop1.setAutoDraw(True)
                
                # if iti_loop1 is active this frame...
                if iti_loop1.status == STARTED:
                    # update params
                    pass
                
                # if iti_loop1 is stopping this frame...
                if iti_loop1.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > iti_loop1.tStartRefresh + current_jitter_1-frameTolerance:
                        # keep track of stop time/frame for later
                        iti_loop1.tStop = t  # not accounting for scr refresh
                        iti_loop1.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'iti_loop1.stopped')
                        # update status
                        iti_loop1.status = FINISHED
                        iti_loop1.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in jitter_ITI_loop1Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "jitter_ITI_loop1" ---
            for thisComponent in jitter_ITI_loop1Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # the Routine "jitter_ITI_loop1" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed 1.0 repeats of 'loop1'
        
    # completed 1.0 repeats of 'loopL'
    
    
    # set up handler to look after randomisation of conditions etc
    loopA = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='loopA')
    thisExp.addLoop(loopA)  # add the loop to the experiment
    thisLoopA = loopA.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisLoopA.rgb)
    if thisLoopA != None:
        for paramName in thisLoopA:
            exec('{} = thisLoopA[paramName]'.format(paramName))
    
    for thisLoopA in loopA:
        currentLoop = loopA
        # abbreviate parameter names if possible (e.g. rgb = thisLoopA.rgb)
        if thisLoopA != None:
            for paramName in thisLoopA:
                exec('{} = thisLoopA[paramName]'.format(paramName))
        
        # # --- Prepare to start Routine "Block_A" ---
        # continueRoutine = True
        # # update component parameters for each repeat
        # Block_A_Resp.keys = []
        # Block_A_Resp.rt = []
        # _Block_A_Resp_allKeys = []
        # # keep track of which components have finished
        # Block_AComponents = [Block_A_ITI, Block_A_Context, Block_A_Confidence, Block_A_Resp]
        # for thisComponent in Block_AComponents:
        #     thisComponent.tStart = None
        #     thisComponent.tStop = None
        #     thisComponent.tStartRefresh = None
        #     thisComponent.tStopRefresh = None
        #     if hasattr(thisComponent, 'status'):
        #         thisComponent.status = NOT_STARTED
        # # reset timers
        # t = 0
        # _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        # frameN = -1
        
        # # --- Run Routine "Block_A" ---
        # routineForceEnded = not continueRoutine
        # while continueRoutine and routineTimer.getTime() < 10.5:
        #     # get current time
        #     t = routineTimer.getTime()
        #     tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        #     tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        #     frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        #     # update/draw components on each frame
            
        #     # *Block_A_ITI* updates
            
        #     # if Block_A_ITI is starting this frame...
        #     if Block_A_ITI.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        #         # keep track of start time/frame for later
        #         Block_A_ITI.frameNStart = frameN  # exact frame index
        #         Block_A_ITI.tStart = t  # local t and not account for scr refresh
        #         Block_A_ITI.tStartRefresh = tThisFlipGlobal  # on global time
        #         win.timeOnFlip(Block_A_ITI, 'tStartRefresh')  # time at next scr refresh
        #         # add timestamp to datafile
        #         thisExp.timestampOnFlip(win, 'Block_A_ITI.started')
        #         # update status
        #         Block_A_ITI.status = STARTED
        #         Block_A_ITI.setAutoDraw(True)
            
        #     # if Block_A_ITI is active this frame...
        #     if Block_A_ITI.status == STARTED:
        #         # update params
        #         pass
            
        #     # if Block_A_ITI is stopping this frame...
        #     if Block_A_ITI.status == STARTED:
        #         # is it time to stop? (based on global clock, using actual start)
        #         if tThisFlipGlobal > Block_A_ITI.tStartRefresh + .5-frameTolerance:
        #             # keep track of stop time/frame for later
        #             Block_A_ITI.tStop = t  # not accounting for scr refresh
        #             Block_A_ITI.frameNStop = frameN  # exact frame index
        #             # add timestamp to datafile
        #             thisExp.timestampOnFlip(win, 'Block_A_ITI.stopped')
        #             # update status
        #             Block_A_ITI.status = FINISHED
        #             Block_A_ITI.setAutoDraw(False)
            
        #     # *Block_A_Context* updates
            
        #     # if Block_A_Context is starting this frame...
        #     if Block_A_Context.status == NOT_STARTED and tThisFlip >= .5-frameTolerance:
        #         # keep track of start time/frame for later
        #         Block_A_Context.frameNStart = frameN  # exact frame index
        #         Block_A_Context.tStart = t  # local t and not account for scr refresh
        #         Block_A_Context.tStartRefresh = tThisFlipGlobal  # on global time
        #         win.timeOnFlip(Block_A_Context, 'tStartRefresh')  # time at next scr refresh
        #         # add timestamp to datafile
        #         thisExp.timestampOnFlip(win, 'Block_A_Context.started')
        #         # update status
        #         Block_A_Context.status = STARTED
        #         Block_A_Context.setAutoDraw(True)
            
        #     # if Block_A_Context is active this frame...
        #     if Block_A_Context.status == STARTED:
        #         # update params
        #         pass
            
        #     # if Block_A_Context is stopping this frame...
        #     if Block_A_Context.status == STARTED:
        #         # is it time to stop? (based on global clock, using actual start)
        #         if tThisFlipGlobal > Block_A_Context.tStartRefresh + 5.0-frameTolerance:
        #             # keep track of stop time/frame for later
        #             Block_A_Context.tStop = t  # not accounting for scr refresh
        #             Block_A_Context.frameNStop = frameN  # exact frame index
        #             # add timestamp to datafile
        #             thisExp.timestampOnFlip(win, 'Block_A_Context.stopped')
        #             # update status
        #             Block_A_Context.status = FINISHED
        #             Block_A_Context.setAutoDraw(False)
            
        #     # *Block_A_Confidence* updates
            
        #     # if Block_A_Confidence is starting this frame...
        #     if Block_A_Confidence.status == NOT_STARTED and tThisFlip >= 5.5-frameTolerance:
        #         # keep track of start time/frame for later
        #         Block_A_Confidence.frameNStart = frameN  # exact frame index
        #         Block_A_Confidence.tStart = t  # local t and not account for scr refresh
        #         Block_A_Confidence.tStartRefresh = tThisFlipGlobal  # on global time
        #         win.timeOnFlip(Block_A_Confidence, 'tStartRefresh')  # time at next scr refresh
        #         # add timestamp to datafile
        #         thisExp.timestampOnFlip(win, 'Block_A_Confidence.started')
        #         # update status
        #         Block_A_Confidence.status = STARTED
        #         Block_A_Confidence.setAutoDraw(True)
            
        #     # if Block_A_Confidence is active this frame...
        #     if Block_A_Confidence.status == STARTED:
        #         # update params
        #         pass
            
        #     # if Block_A_Confidence is stopping this frame...
        #     if Block_A_Confidence.status == STARTED:
        #         # is it time to stop? (based on global clock, using actual start)
        #         if tThisFlipGlobal > Block_A_Confidence.tStartRefresh + 5-frameTolerance:
        #             # keep track of stop time/frame for later
        #             Block_A_Confidence.tStop = t  # not accounting for scr refresh
        #             Block_A_Confidence.frameNStop = frameN  # exact frame index
        #             # add timestamp to datafile
        #             thisExp.timestampOnFlip(win, 'Block_A_Confidence.stopped')
        #             # update status
        #             Block_A_Confidence.status = FINISHED
        #             Block_A_Confidence.setAutoDraw(False)
            
        #     # *Block_A_Resp* updates
        #     waitOnFlip = False
            
        #     # if Block_A_Resp is starting this frame...
        #     if Block_A_Resp.status == NOT_STARTED and tThisFlip >= 5.5-frameTolerance:
        #         # keep track of start time/frame for later
        #         Block_A_Resp.frameNStart = frameN  # exact frame index
        #         Block_A_Resp.tStart = t  # local t and not account for scr refresh
        #         Block_A_Resp.tStartRefresh = tThisFlipGlobal  # on global time
        #         win.timeOnFlip(Block_A_Resp, 'tStartRefresh')  # time at next scr refresh
        #         # add timestamp to datafile
        #         thisExp.timestampOnFlip(win, 'Block_A_Resp.started')
        #         # update status
        #         Block_A_Resp.status = STARTED
        #         # keyboard checking is just starting
        #         waitOnFlip = True
        #         win.callOnFlip(Block_A_Resp.clock.reset)  # t=0 on next screen flip
        #         win.callOnFlip(Block_A_Resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            
        #     # if Block_A_Resp is stopping this frame...
        #     if Block_A_Resp.status == STARTED:
        #         # is it time to stop? (based on global clock, using actual start)
        #         if tThisFlipGlobal > Block_A_Resp.tStartRefresh + 5-frameTolerance:
        #             # keep track of stop time/frame for later
        #             Block_A_Resp.tStop = t  # not accounting for scr refresh
        #             Block_A_Resp.frameNStop = frameN  # exact frame index
        #             # add timestamp to datafile
        #             thisExp.timestampOnFlip(win, 'Block_A_Resp.stopped')
        #             # update status
        #             Block_A_Resp.status = FINISHED
        #             Block_A_Resp.status = FINISHED
        #     if Block_A_Resp.status == STARTED and not waitOnFlip:
        #         theseKeys = Block_A_Resp.getKeys(keyList=['a','b','c','d', 'A', 'B', 'C', 'D'], waitRelease=False)
        #         _Block_A_Resp_allKeys.extend(theseKeys)
        #         if len(_Block_A_Resp_allKeys):
        #             Block_A_Resp.keys = [key.name for key in _Block_A_Resp_allKeys]  # storing all keys
        #             Block_A_Resp.rt = [key.rt for key in _Block_A_Resp_allKeys]
        #             # a response ends the routine
        #             continueRoutine = False
            
        #     # check for quit (typically the Esc key)
        #     if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        #         core.quit()
            
        #     # check if all components have finished
        #     if not continueRoutine:  # a component has requested a forced-end of Routine
        #         routineForceEnded = True
        #         break
        #     continueRoutine = False  # will revert to True if at least one component still running
        #     for thisComponent in Block_AComponents:
        #         if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
        #             continueRoutine = True
        #             break  # at least one component has not yet finished
            
        #     # refresh the screen
        #     if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        #         win.flip()
        
        # # --- Ending Routine "Block_A" ---
        # for thisComponent in Block_AComponents:
        #     if hasattr(thisComponent, "setAutoDraw"):
        #         thisComponent.setAutoDraw(False)
        # # check responses
        # if Block_A_Resp.keys in ['', [], None]:  # No response was made
        #     Block_A_Resp.keys = None
        # loopA.addData('Block_A_Resp.keys',Block_A_Resp.keys)
        # if Block_A_Resp.keys != None:  # we had a response
        #     loopA.addData('Block_A_Resp.rt', Block_A_Resp.rt)
        # # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        # if routineForceEnded:
        #     routineTimer.reset()
        # else:
        #     routineTimer.addTime(-10.500000)
        
        # set up handler to look after randomisation of conditions etc
        loop2 = data.TrialHandler(nReps=1.0, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('Battles_Run1_A.xlsx'),
            seed=None, name='loop2')
        thisExp.addLoop(loop2)  # add the loop to the experiment
        thisLoop2 = loop2.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisLoop2.rgb)
        if thisLoop2 != None:
            for paramName in thisLoop2:
                exec('{} = thisLoop2[paramName]'.format(paramName))
        
        for thisLoop2 in loop2:
            currentLoop = loop2
            # abbreviate parameter names if possible (e.g. rgb = thisLoop2.rgb)
            if thisLoop2 != None:
                for paramName in thisLoop2:
                    exec('{} = thisLoop2[paramName]'.format(paramName))
            
            # --- Prepare to start Routine "firststim_loop2" ---
            continueRoutine = True
            # update component parameters for each repeat
            firststim_img_loop2.setImage(FirstStimA)
            # keep track of which components have finished
            firststim_loop2Components = [firststim_img_loop2]
            for thisComponent in firststim_loop2Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "firststim_loop2" ---
            routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 1.0:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *firststim_img_loop2* updates
                
                # if firststim_img_loop2 is starting this frame...
                if firststim_img_loop2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    firststim_img_loop2.frameNStart = frameN  # exact frame index
                    firststim_img_loop2.tStart = t  # local t and not account for scr refresh
                    firststim_img_loop2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(firststim_img_loop2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'firststim_img_loop2.started')
                    # update status
                    firststim_img_loop2.status = STARTED
                    firststim_img_loop2.setAutoDraw(True)
                
                # if firststim_img_loop2 is active this frame...
                if firststim_img_loop2.status == STARTED:
                    # update params
                    pass
                
                # if firststim_img_loop2 is stopping this frame...
                if firststim_img_loop2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > firststim_img_loop2.tStartRefresh + 1-frameTolerance:
                        # keep track of stop time/frame for later
                        firststim_img_loop2.tStop = t  # not accounting for scr refresh
                        firststim_img_loop2.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'firststim_img_loop2.stopped')
                        # update status
                        firststim_img_loop2.status = FINISHED
                        firststim_img_loop2.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in firststim_loop2Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "firststim_loop2" ---
            for thisComponent in firststim_loop2Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-1.000000)
            
            # --- Prepare to start Routine "ISI_conf_stim1_loop2" ---
            continueRoutine = True
            # update component parameters for each repeat
            # keep track of which components have finished
            ISI_conf_stim1_loop2Components = [isi_conf_stim1_loop2]
            for thisComponent in ISI_conf_stim1_loop2Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "ISI_conf_stim1_loop2" ---
            routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 0.25:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *isi_conf_stim1_loop2* updates
                
                # if isi_conf_stim1_loop2 is starting this frame...
                if isi_conf_stim1_loop2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    isi_conf_stim1_loop2.frameNStart = frameN  # exact frame index
                    isi_conf_stim1_loop2.tStart = t  # local t and not account for scr refresh
                    isi_conf_stim1_loop2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(isi_conf_stim1_loop2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'isi_conf_stim1_loop2.started')
                    # update status
                    isi_conf_stim1_loop2.status = STARTED
                    isi_conf_stim1_loop2.setAutoDraw(True)
                
                # if isi_conf_stim1_loop2 is active this frame...
                if isi_conf_stim1_loop2.status == STARTED:
                    # update params
                    pass
                
                # if isi_conf_stim1_loop2 is stopping this frame...
                if isi_conf_stim1_loop2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > isi_conf_stim1_loop2.tStartRefresh + .3-frameTolerance:
                        # keep track of stop time/frame for later
                        isi_conf_stim1_loop2.tStop = t  # not accounting for scr refresh
                        isi_conf_stim1_loop2.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'isi_conf_stim1_loop2.stopped')
                        # update status
                        isi_conf_stim1_loop2.status = FINISHED
                        isi_conf_stim1_loop2.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in ISI_conf_stim1_loop2Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "ISI_conf_stim1_loop2" ---
            for thisComponent in ISI_conf_stim1_loop2Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-0.250000)
            
            # --- Prepare to start Routine "conf_stim1_loop2" ---
            continueRoutine = True
            # update component parameters for each repeat
            conf_img_stim1_loop2.setImage(ConfidenceA)
            conf_resp_stim1_loop2.keys = []
            conf_resp_stim1_loop2.rt = []
            _conf_resp_stim1_loop2_allKeys = []
            # keep track of which components have finished
            conf_stim1_loop2Components = [conf_img_stim1_loop2, conf_resp_stim1_loop2]
            for thisComponent in conf_stim1_loop2Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "conf_stim1_loop2" ---
            routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 5.0:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *conf_img_stim1_loop2* updates
                
                # if conf_img_stim1_loop2 is starting this frame...
                if conf_img_stim1_loop2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    conf_img_stim1_loop2.frameNStart = frameN  # exact frame index
                    conf_img_stim1_loop2.tStart = t  # local t and not account for scr refresh
                    conf_img_stim1_loop2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(conf_img_stim1_loop2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'conf_img_stim1_loop2.started')
                    # update status
                    conf_img_stim1_loop2.status = STARTED
                    conf_img_stim1_loop2.setAutoDraw(True)
                
                # if conf_img_stim1_loop2 is active this frame...
                if conf_img_stim1_loop2.status == STARTED:
                    # update params
                    pass
                
                # if conf_img_stim1_loop2 is stopping this frame...
                if conf_img_stim1_loop2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > conf_img_stim1_loop2.tStartRefresh + 5-frameTolerance:
                        # keep track of stop time/frame for later
                        conf_img_stim1_loop2.tStop = t  # not accounting for scr refresh
                        conf_img_stim1_loop2.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'conf_img_stim1_loop2.stopped')
                        # update status
                        conf_img_stim1_loop2.status = FINISHED
                        conf_img_stim1_loop2.setAutoDraw(False)
                
                # *conf_resp_stim1_loop2* updates
                waitOnFlip = False
                
                # if conf_resp_stim1_loop2 is starting this frame...
                if conf_resp_stim1_loop2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    conf_resp_stim1_loop2.frameNStart = frameN  # exact frame index
                    conf_resp_stim1_loop2.tStart = t  # local t and not account for scr refresh
                    conf_resp_stim1_loop2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(conf_resp_stim1_loop2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'conf_resp_stim1_loop2.started')
                    # update status
                    conf_resp_stim1_loop2.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(conf_resp_stim1_loop2.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(conf_resp_stim1_loop2.clearEvents, eventType='keyboard')  # clear events on next screen flip
                
                # if conf_resp_stim1_loop2 is stopping this frame...
                if conf_resp_stim1_loop2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > conf_resp_stim1_loop2.tStartRefresh + 5-frameTolerance:
                        # keep track of stop time/frame for later
                        conf_resp_stim1_loop2.tStop = t  # not accounting for scr refresh
                        conf_resp_stim1_loop2.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'conf_resp_stim1_loop2.stopped')
                        # update status
                        conf_resp_stim1_loop2.status = FINISHED
                        conf_resp_stim1_loop2.status = FINISHED
                if conf_resp_stim1_loop2.status == STARTED and not waitOnFlip:
                    theseKeys = conf_resp_stim1_loop2.getKeys(keyList=['a', 'b', 'c', 'd', 'A', 'B', 'C', 'D'], waitRelease=False)
                    _conf_resp_stim1_loop2_allKeys.extend(theseKeys)
                    if len(_conf_resp_stim1_loop2_allKeys):
                        conf_resp_stim1_loop2.keys = [key.name for key in _conf_resp_stim1_loop2_allKeys]  # storing all keys
                        conf_resp_stim1_loop2.rt = [key.rt for key in _conf_resp_stim1_loop2_allKeys]
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in conf_stim1_loop2Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "conf_stim1_loop2" ---
            for thisComponent in conf_stim1_loop2Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # check responses
            if conf_resp_stim1_loop2.keys in ['', [], None]:  # No response was made
                conf_resp_stim1_loop2.keys = None
            loop2.addData('conf_resp_stim1_loop2.keys',conf_resp_stim1_loop2.keys)
            if conf_resp_stim1_loop2.keys != None:  # we had a response
                loop2.addData('conf_resp_stim1_loop2.rt', conf_resp_stim1_loop2.rt)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-5.000000)
            
            # --- Prepare to start Routine "ISI_stim_loop2" ---
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from isi_stim_code_loop2
            import random as rand
            
            jitter_isi_2 = rand.choices([0.5, 0.5, 0.5, 1.0, 1.0, 1.5, 2.0], k=54) # create the list
            
            if loop2.thisN == 0: # only on the first trial
                shuffle(jitter_isi_2) # randomise its order
            
            current_isi_2 = jitter_isi_2.pop() # extract one entry on each trial
            thisExp.addData('isi_stim_2', current_isi_2) # record in the data for this trial
            # keep track of which components have finished
            ISI_stim_loop2Components = [isi_stim_loop2]
            for thisComponent in ISI_stim_loop2Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "ISI_stim_loop2" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *isi_stim_loop2* updates
                
                # if isi_stim_loop2 is starting this frame...
                if isi_stim_loop2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    isi_stim_loop2.frameNStart = frameN  # exact frame index
                    isi_stim_loop2.tStart = t  # local t and not account for scr refresh
                    isi_stim_loop2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(isi_stim_loop2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'isi_stim_loop2.started')
                    # update status
                    isi_stim_loop2.status = STARTED
                    isi_stim_loop2.setAutoDraw(True)
                
                # if isi_stim_loop2 is active this frame...
                if isi_stim_loop2.status == STARTED:
                    # update params
                    pass
                
                # if isi_stim_loop2 is stopping this frame...
                if isi_stim_loop2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > isi_stim_loop2.tStartRefresh + current_isi_2-frameTolerance:
                        # keep track of stop time/frame for later
                        isi_stim_loop2.tStop = t  # not accounting for scr refresh
                        isi_stim_loop2.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'isi_stim_loop2.stopped')
                        # update status
                        isi_stim_loop2.status = FINISHED
                        isi_stim_loop2.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in ISI_stim_loop2Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "ISI_stim_loop2" ---
            for thisComponent in ISI_stim_loop2Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # the Routine "ISI_stim_loop2" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "secondstim_loop2" ---
            continueRoutine = True
            # update component parameters for each repeat
            secondstim_img_loop2.setImage(SecondStimA)
            # keep track of which components have finished
            secondstim_loop2Components = [secondstim_img_loop2]
            for thisComponent in secondstim_loop2Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "secondstim_loop2" ---
            routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 1.0:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *secondstim_img_loop2* updates
                
                # if secondstim_img_loop2 is starting this frame...
                if secondstim_img_loop2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    secondstim_img_loop2.frameNStart = frameN  # exact frame index
                    secondstim_img_loop2.tStart = t  # local t and not account for scr refresh
                    secondstim_img_loop2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(secondstim_img_loop2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'secondstim_img_loop2.started')
                    # update status
                    secondstim_img_loop2.status = STARTED
                    secondstim_img_loop2.setAutoDraw(True)
                
                # if secondstim_img_loop2 is active this frame...
                if secondstim_img_loop2.status == STARTED:
                    # update params
                    pass
                
                # if secondstim_img_loop2 is stopping this frame...
                if secondstim_img_loop2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > secondstim_img_loop2.tStartRefresh + 1-frameTolerance:
                        # keep track of stop time/frame for later
                        secondstim_img_loop2.tStop = t  # not accounting for scr refresh
                        secondstim_img_loop2.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'secondstim_img_loop2.stopped')
                        # update status
                        secondstim_img_loop2.status = FINISHED
                        secondstim_img_loop2.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in secondstim_loop2Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "secondstim_loop2" ---
            for thisComponent in secondstim_loop2Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-1.000000)
            
            # --- Prepare to start Routine "ISI_conf_stim2_loop2" ---
            continueRoutine = True
            # update component parameters for each repeat
            # keep track of which components have finished
            ISI_conf_stim2_loop2Components = [isi_conf_loop2]
            for thisComponent in ISI_conf_stim2_loop2Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "ISI_conf_stim2_loop2" ---
            routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 0.25:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *isi_conf_loop2* updates
                
                # if isi_conf_loop2 is starting this frame...
                if isi_conf_loop2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    isi_conf_loop2.frameNStart = frameN  # exact frame index
                    isi_conf_loop2.tStart = t  # local t and not account for scr refresh
                    isi_conf_loop2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(isi_conf_loop2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'isi_conf_loop2.started')
                    # update status
                    isi_conf_loop2.status = STARTED
                    isi_conf_loop2.setAutoDraw(True)
                
                # if isi_conf_loop2 is active this frame...
                if isi_conf_loop2.status == STARTED:
                    # update params
                    pass
                
                # if isi_conf_loop2 is stopping this frame...
                if isi_conf_loop2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > isi_conf_loop2.tStartRefresh + .3-frameTolerance:
                        # keep track of stop time/frame for later
                        isi_conf_loop2.tStop = t  # not accounting for scr refresh
                        isi_conf_loop2.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'isi_conf_loop2.stopped')
                        # update status
                        isi_conf_loop2.status = FINISHED
                        isi_conf_loop2.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in ISI_conf_stim2_loop2Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "ISI_conf_stim2_loop2" ---
            for thisComponent in ISI_conf_stim2_loop2Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-0.250000)
            
            # --- Prepare to start Routine "conf_stim2_loop2" ---
            continueRoutine = True
            # update component parameters for each repeat
            conf_img_stim2_loop2.setImage(ConfidenceA)
            conf_resp_stim2_loop2.keys = []
            conf_resp_stim2_loop2.rt = []
            _conf_resp_stim2_loop2_allKeys = []
            # keep track of which components have finished
            conf_stim2_loop2Components = [conf_img_stim2_loop2, conf_resp_stim2_loop2]
            for thisComponent in conf_stim2_loop2Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "conf_stim2_loop2" ---
            routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 5.0:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *conf_img_stim2_loop2* updates
                
                # if conf_img_stim2_loop2 is starting this frame...
                if conf_img_stim2_loop2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    conf_img_stim2_loop2.frameNStart = frameN  # exact frame index
                    conf_img_stim2_loop2.tStart = t  # local t and not account for scr refresh
                    conf_img_stim2_loop2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(conf_img_stim2_loop2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'conf_img_stim2_loop2.started')
                    # update status
                    conf_img_stim2_loop2.status = STARTED
                    conf_img_stim2_loop2.setAutoDraw(True)
                
                # if conf_img_stim2_loop2 is active this frame...
                if conf_img_stim2_loop2.status == STARTED:
                    # update params
                    pass
                
                # if conf_img_stim2_loop2 is stopping this frame...
                if conf_img_stim2_loop2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > conf_img_stim2_loop2.tStartRefresh + 5-frameTolerance:
                        # keep track of stop time/frame for later
                        conf_img_stim2_loop2.tStop = t  # not accounting for scr refresh
                        conf_img_stim2_loop2.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'conf_img_stim2_loop2.stopped')
                        # update status
                        conf_img_stim2_loop2.status = FINISHED
                        conf_img_stim2_loop2.setAutoDraw(False)
                
                # *conf_resp_stim2_loop2* updates
                waitOnFlip = False
                
                # if conf_resp_stim2_loop2 is starting this frame...
                if conf_resp_stim2_loop2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    conf_resp_stim2_loop2.frameNStart = frameN  # exact frame index
                    conf_resp_stim2_loop2.tStart = t  # local t and not account for scr refresh
                    conf_resp_stim2_loop2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(conf_resp_stim2_loop2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'conf_resp_stim2_loop2.started')
                    # update status
                    conf_resp_stim2_loop2.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(conf_resp_stim2_loop2.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(conf_resp_stim2_loop2.clearEvents, eventType='keyboard')  # clear events on next screen flip
                
                # if conf_resp_stim2_loop2 is stopping this frame...
                if conf_resp_stim2_loop2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > conf_resp_stim2_loop2.tStartRefresh + 5-frameTolerance:
                        # keep track of stop time/frame for later
                        conf_resp_stim2_loop2.tStop = t  # not accounting for scr refresh
                        conf_resp_stim2_loop2.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'conf_resp_stim2_loop2.stopped')
                        # update status
                        conf_resp_stim2_loop2.status = FINISHED
                        conf_resp_stim2_loop2.status = FINISHED
                if conf_resp_stim2_loop2.status == STARTED and not waitOnFlip:
                    theseKeys = conf_resp_stim2_loop2.getKeys(keyList=['a','b','c','d', 'A', 'B', 'C', 'D'], waitRelease=False)
                    _conf_resp_stim2_loop2_allKeys.extend(theseKeys)
                    if len(_conf_resp_stim2_loop2_allKeys):
                        conf_resp_stim2_loop2.keys = [key.name for key in _conf_resp_stim2_loop2_allKeys]  # storing all keys
                        conf_resp_stim2_loop2.rt = [key.rt for key in _conf_resp_stim2_loop2_allKeys]
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in conf_stim2_loop2Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "conf_stim2_loop2" ---
            for thisComponent in conf_stim2_loop2Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # check responses
            if conf_resp_stim2_loop2.keys in ['', [], None]:  # No response was made
                conf_resp_stim2_loop2.keys = None
            loop2.addData('conf_resp_stim2_loop2.keys',conf_resp_stim2_loop2.keys)
            if conf_resp_stim2_loop2.keys != None:  # we had a response
                loop2.addData('conf_resp_stim2_loop2.rt', conf_resp_stim2_loop2.rt)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-5.000000)
            
            # --- Prepare to start Routine "ISI_outcome" ---
            continueRoutine = True
            # update component parameters for each repeat
            # keep track of which components have finished
            ISI_outcomeComponents = [isi_outcome]
            for thisComponent in ISI_outcomeComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "ISI_outcome" ---
            routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 0.25:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *isi_outcome* updates
                
                # if isi_outcome is starting this frame...
                if isi_outcome.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    isi_outcome.frameNStart = frameN  # exact frame index
                    isi_outcome.tStart = t  # local t and not account for scr refresh
                    isi_outcome.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(isi_outcome, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'isi_outcome.started')
                    # update status
                    isi_outcome.status = STARTED
                    isi_outcome.setAutoDraw(True)
                
                # if isi_outcome is active this frame...
                if isi_outcome.status == STARTED:
                    # update params
                    pass
                
                # if isi_outcome is stopping this frame...
                if isi_outcome.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > isi_outcome.tStartRefresh + 0.5-frameTolerance:
                        # keep track of stop time/frame for later
                        isi_outcome.tStop = t  # not accounting for scr refresh
                        isi_outcome.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'isi_outcome.stopped')
                        # update status
                        isi_outcome.status = FINISHED
                        isi_outcome.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in ISI_outcomeComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "ISI_outcome" ---
            for thisComponent in ISI_outcomeComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-0.2500000)
            
            # --- Prepare to start Routine "outcome_loop2" ---
            continueRoutine = True
            # update component parameters for each repeat
            outcome_image_loop2.setImage(OutcomeA)
            Tone_loop2.setSound(ToneA, secs=1.3, hamming=True)
            Tone_loop2.setVolume(1.0, log=False)
            # keep track of which components have finished
            outcome_loop2Components = [outcome_image_loop2, Tone_loop2]
            for thisComponent in outcome_loop2Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "outcome_loop2" ---
            routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 1.5:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *outcome_image_loop2* updates
                
                # if outcome_image_loop2 is starting this frame...
                if outcome_image_loop2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    outcome_image_loop2.frameNStart = frameN  # exact frame index
                    outcome_image_loop2.tStart = t  # local t and not account for scr refresh
                    outcome_image_loop2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(outcome_image_loop2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'outcome_image_loop2.started')
                    # update status
                    outcome_image_loop2.status = STARTED
                    outcome_image_loop2.setAutoDraw(True)
                
                # if outcome_image_loop2 is active this frame...
                if outcome_image_loop2.status == STARTED:
                    # update params
                    pass
                
                # if outcome_image_loop2 is stopping this frame...
                if outcome_image_loop2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > outcome_image_loop2.tStartRefresh + 1.5-frameTolerance:
                        # keep track of stop time/frame for later
                        outcome_image_loop2.tStop = t  # not accounting for scr refresh
                        outcome_image_loop2.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'outcome_image_loop2.stopped')
                        # update status
                        outcome_image_loop2.status = FINISHED
                        outcome_image_loop2.setAutoDraw(False)
                # start/stop Tone_loop2
                
                # if Tone_loop2 is starting this frame...
                if Tone_loop2.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
                    # keep track of start time/frame for later
                    Tone_loop2.frameNStart = frameN  # exact frame index
                    Tone_loop2.tStart = t  # local t and not account for scr refresh
                    Tone_loop2.tStartRefresh = tThisFlipGlobal  # on global time
                    # add timestamp to datafile
                    thisExp.addData('Tone_loop2.started', tThisFlipGlobal)
                    # update status
                    Tone_loop2.status = STARTED
                    Tone_loop2.play(when=win)  # sync with win flip
                
                # if Tone_loop2 is stopping this frame...
                if Tone_loop2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Tone_loop2.tStartRefresh + 1.3-frameTolerance:
                        # keep track of stop time/frame for later
                        Tone_loop2.tStop = t  # not accounting for scr refresh
                        Tone_loop2.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'Tone_loop2.stopped')
                        # update status
                        Tone_loop2.status = FINISHED
                        Tone_loop2.stop()
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in outcome_loop2Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "outcome_loop2" ---
            for thisComponent in outcome_loop2Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            Tone_loop2.stop()  # ensure sound has stopped at end of routine
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-1.500000)
            
            # --- Prepare to start Routine "jitter_ITI_loop2" ---
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from iti_code_loop2
            import random as rand
            
            jitter_iti_2 = rand.choices([.5, 1.0, 1.5, 2.0], k=54) # create the list
            
            if loop2.thisN == 0: # only on the first trial
                shuffle(jitter_iti_2) # randomise its order
            
            current_jitter_2 = jitter_iti_2.pop() # extract one entry on each trial
            
            thisExp.addData('jitter_iti_2', current_jitter_2) # record in the data for this trial
            
            
            # keep track of which components have finished
            jitter_ITI_loop2Components = [iti_loop2]
            for thisComponent in jitter_ITI_loop2Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "jitter_ITI_loop2" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *iti_loop2* updates
                
                # if iti_loop2 is starting this frame...
                if iti_loop2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    iti_loop2.frameNStart = frameN  # exact frame index
                    iti_loop2.tStart = t  # local t and not account for scr refresh
                    iti_loop2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(iti_loop2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'iti_loop2.started')
                    # update status
                    iti_loop2.status = STARTED
                    iti_loop2.setAutoDraw(True)
                
                # if iti_loop2 is active this frame...
                if iti_loop2.status == STARTED:
                    # update params
                    pass
                
                # if iti_loop2 is stopping this frame...
                if iti_loop2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > iti_loop2.tStartRefresh + current_jitter_2-frameTolerance:
                        # keep track of stop time/frame for later
                        iti_loop2.tStop = t  # not accounting for scr refresh
                        iti_loop2.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'iti_loop2.stopped')
                        # update status
                        iti_loop2.status = FINISHED
                        iti_loop2.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in jitter_ITI_loop2Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "jitter_ITI_loop2" ---
            for thisComponent in jitter_ITI_loop2Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # the Routine "jitter_ITI_loop2" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed 1.0 repeats of 'loop2'
        
    # completed 1.0 repeats of 'loopA'
    
    
    # set up handler to look after randomisation of conditions etc
    loopH = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='loopH')
    thisExp.addLoop(loopH)  # add the loop to the experiment
    thisLoopH = loopH.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisLoopH.rgb)
    if thisLoopH != None:
        for paramName in thisLoopH:
            exec('{} = thisLoopH[paramName]'.format(paramName))
    
    for thisLoopH in loopH:
        currentLoop = loopH
        # abbreviate parameter names if possible (e.g. rgb = thisLoopH.rgb)
        if thisLoopH != None:
            for paramName in thisLoopH:
                exec('{} = thisLoopH[paramName]'.format(paramName))
        
        # # --- Prepare to start Routine "Block_H" ---
        # continueRoutine = True
        # # update component parameters for each repeat
        # Block_H_Resp.keys = []
        # Block_H_Resp.rt = []
        # _Block_H_Resp_allKeys = []
        # # keep track of which components have finished
        # Block_HComponents = [Block_H_ITI, Block_H_Context, Block_H_Confidence, Block_H_Resp]
        # for thisComponent in Block_HComponents:
        #     thisComponent.tStart = None
        #     thisComponent.tStop = None
        #     thisComponent.tStartRefresh = None
        #     thisComponent.tStopRefresh = None
        #     if hasattr(thisComponent, 'status'):
        #         thisComponent.status = NOT_STARTED
        # # reset timers
        # t = 0
        # _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        # frameN = -1
        
        # # --- Run Routine "Block_H" ---
        # routineForceEnded = not continueRoutine
        # while continueRoutine and routineTimer.getTime() < 10.5:
        #     # get current time
        #     t = routineTimer.getTime()
        #     tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        #     tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        #     frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        #     # update/draw components on each frame
            
        #     # *Block_H_ITI* updates
            
        #     # if Block_H_ITI is starting this frame...
        #     if Block_H_ITI.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        #         # keep track of start time/frame for later
        #         Block_H_ITI.frameNStart = frameN  # exact frame index
        #         Block_H_ITI.tStart = t  # local t and not account for scr refresh
        #         Block_H_ITI.tStartRefresh = tThisFlipGlobal  # on global time
        #         win.timeOnFlip(Block_H_ITI, 'tStartRefresh')  # time at next scr refresh
        #         # add timestamp to datafile
        #         thisExp.timestampOnFlip(win, 'Block_H_ITI.started')
        #         # update status
        #         Block_H_ITI.status = STARTED
        #         Block_H_ITI.setAutoDraw(True)
            
        #     # if Block_H_ITI is active this frame...
        #     if Block_H_ITI.status == STARTED:
        #         # update params
        #         pass
            
        #     # if Block_H_ITI is stopping this frame...
        #     if Block_H_ITI.status == STARTED:
        #         # is it time to stop? (based on global clock, using actual start)
        #         if tThisFlipGlobal > Block_H_ITI.tStartRefresh + .5-frameTolerance:
        #             # keep track of stop time/frame for later
        #             Block_H_ITI.tStop = t  # not accounting for scr refresh
        #             Block_H_ITI.frameNStop = frameN  # exact frame index
        #             # add timestamp to datafile
        #             thisExp.timestampOnFlip(win, 'Block_H_ITI.stopped')
        #             # update status
        #             Block_H_ITI.status = FINISHED
        #             Block_H_ITI.setAutoDraw(False)
            
        #     # *Block_H_Context* updates
            
        #     # if Block_H_Context is starting this frame...
        #     if Block_H_Context.status == NOT_STARTED and tThisFlip >= .5-frameTolerance:
        #         # keep track of start time/frame for later
        #         Block_H_Context.frameNStart = frameN  # exact frame index
        #         Block_H_Context.tStart = t  # local t and not account for scr refresh
        #         Block_H_Context.tStartRefresh = tThisFlipGlobal  # on global time
        #         win.timeOnFlip(Block_H_Context, 'tStartRefresh')  # time at next scr refresh
        #         # add timestamp to datafile
        #         thisExp.timestampOnFlip(win, 'Block_H_Context.started')
        #         # update status
        #         Block_H_Context.status = STARTED
        #         Block_H_Context.setAutoDraw(True)
            
        #     # if Block_H_Context is active this frame...
        #     if Block_H_Context.status == STARTED:
        #         # update params
        #         pass
            
        #     # if Block_H_Context is stopping this frame...
        #     if Block_H_Context.status == STARTED:
        #         # is it time to stop? (based on global clock, using actual start)
        #         if tThisFlipGlobal > Block_H_Context.tStartRefresh + 5.0-frameTolerance:
        #             # keep track of stop time/frame for later
        #             Block_H_Context.tStop = t  # not accounting for scr refresh
        #             Block_H_Context.frameNStop = frameN  # exact frame index
        #             # add timestamp to datafile
        #             thisExp.timestampOnFlip(win, 'Block_H_Context.stopped')
        #             # update status
        #             Block_H_Context.status = FINISHED
        #             Block_H_Context.setAutoDraw(False)
            
        #     # *Block_H_Confidence* updates
            
        #     # if Block_H_Confidence is starting this frame...
        #     if Block_H_Confidence.status == NOT_STARTED and tThisFlip >= 5.5-frameTolerance:
        #         # keep track of start time/frame for later
        #         Block_H_Confidence.frameNStart = frameN  # exact frame index
        #         Block_H_Confidence.tStart = t  # local t and not account for scr refresh
        #         Block_H_Confidence.tStartRefresh = tThisFlipGlobal  # on global time
        #         win.timeOnFlip(Block_H_Confidence, 'tStartRefresh')  # time at next scr refresh
        #         # add timestamp to datafile
        #         thisExp.timestampOnFlip(win, 'Block_H_Confidence.started')
        #         # update status
        #         Block_H_Confidence.status = STARTED
        #         Block_H_Confidence.setAutoDraw(True)
            
        #     # if Block_H_Confidence is active this frame...
        #     if Block_H_Confidence.status == STARTED:
        #         # update params
        #         pass
            
        #     # if Block_H_Confidence is stopping this frame...
        #     if Block_H_Confidence.status == STARTED:
        #         # is it time to stop? (based on global clock, using actual start)
        #         if tThisFlipGlobal > Block_H_Confidence.tStartRefresh + 5-frameTolerance:
        #             # keep track of stop time/frame for later
        #             Block_H_Confidence.tStop = t  # not accounting for scr refresh
        #             Block_H_Confidence.frameNStop = frameN  # exact frame index
        #             # add timestamp to datafile
        #             thisExp.timestampOnFlip(win, 'Block_H_Confidence.stopped')
        #             # update status
        #             Block_H_Confidence.status = FINISHED
        #             Block_H_Confidence.setAutoDraw(False)
            
        #     # *Block_H_Resp* updates
        #     waitOnFlip = False
            
        #     # if Block_H_Resp is starting this frame...
        #     if Block_H_Resp.status == NOT_STARTED and tThisFlip >= 5.5-frameTolerance:
        #         # keep track of start time/frame for later
        #         Block_H_Resp.frameNStart = frameN  # exact frame index
        #         Block_H_Resp.tStart = t  # local t and not account for scr refresh
        #         Block_H_Resp.tStartRefresh = tThisFlipGlobal  # on global time
        #         win.timeOnFlip(Block_H_Resp, 'tStartRefresh')  # time at next scr refresh
        #         # add timestamp to datafile
        #         thisExp.timestampOnFlip(win, 'Block_H_Resp.started')
        #         # update status
        #         Block_H_Resp.status = STARTED
        #         # keyboard checking is just starting
        #         waitOnFlip = True
        #         win.callOnFlip(Block_H_Resp.clock.reset)  # t=0 on next screen flip
        #         win.callOnFlip(Block_H_Resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            
        #     # if Block_H_Resp is stopping this frame...
        #     if Block_H_Resp.status == STARTED:
        #         # is it time to stop? (based on global clock, using actual start)
        #         if tThisFlipGlobal > Block_H_Resp.tStartRefresh + 5-frameTolerance:
        #             # keep track of stop time/frame for later
        #             Block_H_Resp.tStop = t  # not accounting for scr refresh
        #             Block_H_Resp.frameNStop = frameN  # exact frame index
        #             # add timestamp to datafile
        #             thisExp.timestampOnFlip(win, 'Block_H_Resp.stopped')
        #             # update status
        #             Block_H_Resp.status = FINISHED
        #             Block_H_Resp.status = FINISHED
        #     if Block_H_Resp.status == STARTED and not waitOnFlip:
        #         theseKeys = Block_H_Resp.getKeys(keyList=['a','b','c','d', 'A', 'B', 'C', 'D'], waitRelease=False)
        #         _Block_H_Resp_allKeys.extend(theseKeys)
        #         if len(_Block_H_Resp_allKeys):
        #             Block_H_Resp.keys = [key.name for key in _Block_H_Resp_allKeys]  # storing all keys
        #             Block_H_Resp.rt = [key.rt for key in _Block_H_Resp_allKeys]
        #             # a response ends the routine
        #             continueRoutine = False
            
        #     # check for quit (typically the Esc key)
        #     if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        #         core.quit()
            
        #     # check if all components have finished
        #     if not continueRoutine:  # a component has requested a forced-end of Routine
        #         routineForceEnded = True
        #         break
        #     continueRoutine = False  # will revert to True if at least one component still running
        #     for thisComponent in Block_HComponents:
        #         if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
        #             continueRoutine = True
        #             break  # at least one component has not yet finished
            
        #     # refresh the screen
        #     if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        #         win.flip()
        
        # # --- Ending Routine "Block_H" ---
        # for thisComponent in Block_HComponents:
        #     if hasattr(thisComponent, "setAutoDraw"):
        #         thisComponent.setAutoDraw(False)
        # # check responses
        # if Block_H_Resp.keys in ['', [], None]:  # No response was made
        #     Block_H_Resp.keys = None
        # loopH.addData('Block_H_Resp.keys',Block_H_Resp.keys)
        # if Block_H_Resp.keys != None:  # we had a response
        #     loopH.addData('Block_H_Resp.rt', Block_H_Resp.rt)
        # # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        # if routineForceEnded:
        #     routineTimer.reset()
        # else:
        #     routineTimer.addTime(-10.500000)
        
        # set up handler to look after randomisation of conditions etc
        loop3 = data.TrialHandler(nReps=1.0, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('Battles_Run1_H.xlsx'),
            seed=None, name='loop3')
        thisExp.addLoop(loop3)  # add the loop to the experiment
        thisLoop3 = loop3.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisLoop3.rgb)
        if thisLoop3 != None:
            for paramName in thisLoop3:
                exec('{} = thisLoop3[paramName]'.format(paramName))
        
        for thisLoop3 in loop3:
            currentLoop = loop3
            # abbreviate parameter names if possible (e.g. rgb = thisLoop3.rgb)
            if thisLoop3 != None:
                for paramName in thisLoop3:
                    exec('{} = thisLoop3[paramName]'.format(paramName))
            
            # --- Prepare to start Routine "firststim_loop3" ---
            continueRoutine = True
            # update component parameters for each repeat
            firststim_img_loop3.setImage(FirstStimH)
            # keep track of which components have finished
            firststim_loop3Components = [firststim_img_loop3]
            for thisComponent in firststim_loop3Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "firststim_loop3" ---
            routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 1.0:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *firststim_img_loop3* updates
                
                # if firststim_img_loop3 is starting this frame...
                if firststim_img_loop3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    firststim_img_loop3.frameNStart = frameN  # exact frame index
                    firststim_img_loop3.tStart = t  # local t and not account for scr refresh
                    firststim_img_loop3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(firststim_img_loop3, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'firststim_img_loop3.started')
                    # update status
                    firststim_img_loop3.status = STARTED
                    firststim_img_loop3.setAutoDraw(True)
                
                # if firststim_img_loop3 is active this frame...
                if firststim_img_loop3.status == STARTED:
                    # update params
                    pass
                
                # if firststim_img_loop3 is stopping this frame...
                if firststim_img_loop3.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > firststim_img_loop3.tStartRefresh + 1-frameTolerance:
                        # keep track of stop time/frame for later
                        firststim_img_loop3.tStop = t  # not accounting for scr refresh
                        firststim_img_loop3.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'firststim_img_loop3.stopped')
                        # update status
                        firststim_img_loop3.status = FINISHED
                        firststim_img_loop3.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in firststim_loop3Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "firststim_loop3" ---
            for thisComponent in firststim_loop3Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-1.000000)
            
            # --- Prepare to start Routine "ISI_conf_stim1_loop3" ---
            continueRoutine = True
            # update component parameters for each repeat
            # keep track of which components have finished
            ISI_conf_stim1_loop3Components = [isi_conf_stim1_loop3]
            for thisComponent in ISI_conf_stim1_loop3Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "ISI_conf_stim1_loop3" ---
            routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 0.25:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *isi_conf_stim1_loop3* updates
                
                # if isi_conf_stim1_loop3 is starting this frame...
                if isi_conf_stim1_loop3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    isi_conf_stim1_loop3.frameNStart = frameN  # exact frame index
                    isi_conf_stim1_loop3.tStart = t  # local t and not account for scr refresh
                    isi_conf_stim1_loop3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(isi_conf_stim1_loop3, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'isi_conf_stim1_loop3.started')
                    # update status
                    isi_conf_stim1_loop3.status = STARTED
                    isi_conf_stim1_loop3.setAutoDraw(True)
                
                # if isi_conf_stim1_loop3 is active this frame...
                if isi_conf_stim1_loop3.status == STARTED:
                    # update params
                    pass
                
                # if isi_conf_stim1_loop3 is stopping this frame...
                if isi_conf_stim1_loop3.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > isi_conf_stim1_loop3.tStartRefresh + .3-frameTolerance:
                        # keep track of stop time/frame for later
                        isi_conf_stim1_loop3.tStop = t  # not accounting for scr refresh
                        isi_conf_stim1_loop3.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'isi_conf_stim1_loop3.stopped')
                        # update status
                        isi_conf_stim1_loop3.status = FINISHED
                        isi_conf_stim1_loop3.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in ISI_conf_stim1_loop3Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "ISI_conf_stim1_loop3" ---
            for thisComponent in ISI_conf_stim1_loop3Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-0.250000)
            
            # --- Prepare to start Routine "conf_stim1_loop3" ---
            continueRoutine = True
            # update component parameters for each repeat
            conf_img_stim1_loop3.setImage(ConfidenceH)
            conf_resp_stim1_loop3.keys = []
            conf_resp_stim1_loop3.rt = []
            _conf_resp_stim1_loop3_allKeys = []
            # keep track of which components have finished
            conf_stim1_loop3Components = [conf_img_stim1_loop3, conf_resp_stim1_loop3]
            for thisComponent in conf_stim1_loop3Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "conf_stim1_loop3" ---
            routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 5.0:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *conf_img_stim1_loop3* updates
                
                # if conf_img_stim1_loop3 is starting this frame...
                if conf_img_stim1_loop3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    conf_img_stim1_loop3.frameNStart = frameN  # exact frame index
                    conf_img_stim1_loop3.tStart = t  # local t and not account for scr refresh
                    conf_img_stim1_loop3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(conf_img_stim1_loop3, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'conf_img_stim1_loop3.started')
                    # update status
                    conf_img_stim1_loop3.status = STARTED
                    conf_img_stim1_loop3.setAutoDraw(True)
                
                # if conf_img_stim1_loop3 is active this frame...
                if conf_img_stim1_loop3.status == STARTED:
                    # update params
                    pass
                
                # if conf_img_stim1_loop3 is stopping this frame...
                if conf_img_stim1_loop3.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > conf_img_stim1_loop3.tStartRefresh + 5-frameTolerance:
                        # keep track of stop time/frame for later
                        conf_img_stim1_loop3.tStop = t  # not accounting for scr refresh
                        conf_img_stim1_loop3.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'conf_img_stim1_loop3.stopped')
                        # update status
                        conf_img_stim1_loop3.status = FINISHED
                        conf_img_stim1_loop3.setAutoDraw(False)
                
                # *conf_resp_stim1_loop3* updates
                waitOnFlip = False
                
                # if conf_resp_stim1_loop3 is starting this frame...
                if conf_resp_stim1_loop3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    conf_resp_stim1_loop3.frameNStart = frameN  # exact frame index
                    conf_resp_stim1_loop3.tStart = t  # local t and not account for scr refresh
                    conf_resp_stim1_loop3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(conf_resp_stim1_loop3, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'conf_resp_stim1_loop3.started')
                    # update status
                    conf_resp_stim1_loop3.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(conf_resp_stim1_loop3.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(conf_resp_stim1_loop3.clearEvents, eventType='keyboard')  # clear events on next screen flip
                
                # if conf_resp_stim1_loop3 is stopping this frame...
                if conf_resp_stim1_loop3.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > conf_resp_stim1_loop3.tStartRefresh + 5-frameTolerance:
                        # keep track of stop time/frame for later
                        conf_resp_stim1_loop3.tStop = t  # not accounting for scr refresh
                        conf_resp_stim1_loop3.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'conf_resp_stim1_loop3.stopped')
                        # update status
                        conf_resp_stim1_loop3.status = FINISHED
                        conf_resp_stim1_loop3.status = FINISHED
                if conf_resp_stim1_loop3.status == STARTED and not waitOnFlip:
                    theseKeys = conf_resp_stim1_loop3.getKeys(keyList=['a','b','c','d', 'A', 'B', 'C', 'D'], waitRelease=False)
                    _conf_resp_stim1_loop3_allKeys.extend(theseKeys)
                    if len(_conf_resp_stim1_loop3_allKeys):
                        conf_resp_stim1_loop3.keys = [key.name for key in _conf_resp_stim1_loop3_allKeys]  # storing all keys
                        conf_resp_stim1_loop3.rt = [key.rt for key in _conf_resp_stim1_loop3_allKeys]
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in conf_stim1_loop3Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "conf_stim1_loop3" ---
            for thisComponent in conf_stim1_loop3Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # check responses
            if conf_resp_stim1_loop3.keys in ['', [], None]:  # No response was made
                conf_resp_stim1_loop3.keys = None
            loop3.addData('conf_resp_stim1_loop3.keys',conf_resp_stim1_loop3.keys)
            if conf_resp_stim1_loop3.keys != None:  # we had a response
                loop3.addData('conf_resp_stim1_loop3.rt', conf_resp_stim1_loop3.rt)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-5.000000)
            
            # --- Prepare to start Routine "ISI_stim_loop3" ---
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from isi_stim_code_loop3
            import random as rand
            
            jitter_isi_3 = rand.choices([0.5, 0.5, 0.5, 1.0, 1.0, 1.5, 2.0], k=54) # create the list
            
            
            if loop3.thisN == 0: # only on the first trial
                shuffle(jitter_isi_3) # randomise its order
            
            current_isi_3 = jitter_isi_3.pop() # extract one entry on each trial
            thisExp.addData('isi_stim_3', current_isi_3) # record in the data for this trial
            # keep track of which components have finished
            ISI_stim_loop3Components = [isi_stim_loop3]
            for thisComponent in ISI_stim_loop3Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "ISI_stim_loop3" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *isi_stim_loop3* updates
                
                # if isi_stim_loop3 is starting this frame...
                if isi_stim_loop3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    isi_stim_loop3.frameNStart = frameN  # exact frame index
                    isi_stim_loop3.tStart = t  # local t and not account for scr refresh
                    isi_stim_loop3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(isi_stim_loop3, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'isi_stim_loop3.started')
                    # update status
                    isi_stim_loop3.status = STARTED
                    isi_stim_loop3.setAutoDraw(True)
                
                # if isi_stim_loop3 is active this frame...
                if isi_stim_loop3.status == STARTED:
                    # update params
                    pass
                
                # if isi_stim_loop3 is stopping this frame...
                if isi_stim_loop3.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > isi_stim_loop3.tStartRefresh + current_isi_3-frameTolerance:
                        # keep track of stop time/frame for later
                        isi_stim_loop3.tStop = t  # not accounting for scr refresh
                        isi_stim_loop3.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'isi_stim_loop3.stopped')
                        # update status
                        isi_stim_loop3.status = FINISHED
                        isi_stim_loop3.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in ISI_stim_loop3Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "ISI_stim_loop3" ---
            for thisComponent in ISI_stim_loop3Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # the Routine "ISI_stim_loop3" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "secondstim_loop3" ---
            continueRoutine = True
            # update component parameters for each repeat
            secondstim_img_loop3.setImage(SecondStimH)
            # keep track of which components have finished
            secondstim_loop3Components = [secondstim_img_loop3]
            for thisComponent in secondstim_loop3Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "secondstim_loop3" ---
            routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 1.0:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *secondstim_img_loop3* updates
                
                # if secondstim_img_loop3 is starting this frame...
                if secondstim_img_loop3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    secondstim_img_loop3.frameNStart = frameN  # exact frame index
                    secondstim_img_loop3.tStart = t  # local t and not account for scr refresh
                    secondstim_img_loop3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(secondstim_img_loop3, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'secondstim_img_loop3.started')
                    # update status
                    secondstim_img_loop3.status = STARTED
                    secondstim_img_loop3.setAutoDraw(True)
                
                # if secondstim_img_loop3 is active this frame...
                if secondstim_img_loop3.status == STARTED:
                    # update params
                    pass
                
                # if secondstim_img_loop3 is stopping this frame...
                if secondstim_img_loop3.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > secondstim_img_loop3.tStartRefresh + 1-frameTolerance:
                        # keep track of stop time/frame for later
                        secondstim_img_loop3.tStop = t  # not accounting for scr refresh
                        secondstim_img_loop3.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'secondstim_img_loop3.stopped')
                        # update status
                        secondstim_img_loop3.status = FINISHED
                        secondstim_img_loop3.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in secondstim_loop3Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "secondstim_loop3" ---
            for thisComponent in secondstim_loop3Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-1.000000)
            
            # --- Prepare to start Routine "ISI_conf_stim2_loop3" ---
            continueRoutine = True
            # update component parameters for each repeat
            # keep track of which components have finished
            ISI_conf_stim2_loop3Components = [isi_conf_stim2_loop3]
            for thisComponent in ISI_conf_stim2_loop3Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "ISI_conf_stim2_loop3" ---
            routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 0.25:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *isi_conf_stim2_loop3* updates
                
                # if isi_conf_stim2_loop3 is starting this frame...
                if isi_conf_stim2_loop3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    isi_conf_stim2_loop3.frameNStart = frameN  # exact frame index
                    isi_conf_stim2_loop3.tStart = t  # local t and not account for scr refresh
                    isi_conf_stim2_loop3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(isi_conf_stim2_loop3, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'isi_conf_stim2_loop3.started')
                    # update status
                    isi_conf_stim2_loop3.status = STARTED
                    isi_conf_stim2_loop3.setAutoDraw(True)
                
                # if isi_conf_stim2_loop3 is active this frame...
                if isi_conf_stim2_loop3.status == STARTED:
                    # update params
                    pass
                
                # if isi_conf_stim2_loop3 is stopping this frame...
                if isi_conf_stim2_loop3.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > isi_conf_stim2_loop3.tStartRefresh + .3-frameTolerance:
                        # keep track of stop time/frame for later
                        isi_conf_stim2_loop3.tStop = t  # not accounting for scr refresh
                        isi_conf_stim2_loop3.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'isi_conf_stim2_loop3.stopped')
                        # update status
                        isi_conf_stim2_loop3.status = FINISHED
                        isi_conf_stim2_loop3.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in ISI_conf_stim2_loop3Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "ISI_conf_stim2_loop3" ---
            for thisComponent in ISI_conf_stim2_loop3Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-0.250000)
            
            # --- Prepare to start Routine "conf_stim2_loop3" ---
            continueRoutine = True
            # update component parameters for each repeat
            conf_img_stim2_loop3.setImage(ConfidenceH)
            conf_resp_stim2_loop3.keys = []
            conf_resp_stim2_loop3.rt = []
            _conf_resp_stim2_loop3_allKeys = []
            # keep track of which components have finished
            conf_stim2_loop3Components = [conf_img_stim2_loop3, conf_resp_stim2_loop3]
            for thisComponent in conf_stim2_loop3Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "conf_stim2_loop3" ---
            routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 5.0:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *conf_img_stim2_loop3* updates
                
                # if conf_img_stim2_loop3 is starting this frame...
                if conf_img_stim2_loop3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    conf_img_stim2_loop3.frameNStart = frameN  # exact frame index
                    conf_img_stim2_loop3.tStart = t  # local t and not account for scr refresh
                    conf_img_stim2_loop3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(conf_img_stim2_loop3, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'conf_img_stim2_loop3.started')
                    # update status
                    conf_img_stim2_loop3.status = STARTED
                    conf_img_stim2_loop3.setAutoDraw(True)
                
                # if conf_img_stim2_loop3 is active this frame...
                if conf_img_stim2_loop3.status == STARTED:
                    # update params
                    pass
                
                # if conf_img_stim2_loop3 is stopping this frame...
                if conf_img_stim2_loop3.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > conf_img_stim2_loop3.tStartRefresh + 5-frameTolerance:
                        # keep track of stop time/frame for later
                        conf_img_stim2_loop3.tStop = t  # not accounting for scr refresh
                        conf_img_stim2_loop3.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'conf_img_stim2_loop3.stopped')
                        # update status
                        conf_img_stim2_loop3.status = FINISHED
                        conf_img_stim2_loop3.setAutoDraw(False)
                
                # *conf_resp_stim2_loop3* updates
                waitOnFlip = False
                
                # if conf_resp_stim2_loop3 is starting this frame...
                if conf_resp_stim2_loop3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    conf_resp_stim2_loop3.frameNStart = frameN  # exact frame index
                    conf_resp_stim2_loop3.tStart = t  # local t and not account for scr refresh
                    conf_resp_stim2_loop3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(conf_resp_stim2_loop3, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'conf_resp_stim2_loop3.started')
                    # update status
                    conf_resp_stim2_loop3.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(conf_resp_stim2_loop3.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(conf_resp_stim2_loop3.clearEvents, eventType='keyboard')  # clear events on next screen flip
                
                # if conf_resp_stim2_loop3 is stopping this frame...
                if conf_resp_stim2_loop3.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > conf_resp_stim2_loop3.tStartRefresh + 5-frameTolerance:
                        # keep track of stop time/frame for later
                        conf_resp_stim2_loop3.tStop = t  # not accounting for scr refresh
                        conf_resp_stim2_loop3.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'conf_resp_stim2_loop3.stopped')
                        # update status
                        conf_resp_stim2_loop3.status = FINISHED
                        conf_resp_stim2_loop3.status = FINISHED
                if conf_resp_stim2_loop3.status == STARTED and not waitOnFlip:
                    theseKeys = conf_resp_stim2_loop3.getKeys(keyList=['a','b','c','d', 'A', 'B', 'C', 'D'], waitRelease=False)
                    _conf_resp_stim2_loop3_allKeys.extend(theseKeys)
                    if len(_conf_resp_stim2_loop3_allKeys):
                        conf_resp_stim2_loop3.keys = [key.name for key in _conf_resp_stim2_loop3_allKeys]  # storing all keys
                        conf_resp_stim2_loop3.rt = [key.rt for key in _conf_resp_stim2_loop3_allKeys]
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in conf_stim2_loop3Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "conf_stim2_loop3" ---
            for thisComponent in conf_stim2_loop3Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # check responses
            if conf_resp_stim2_loop3.keys in ['', [], None]:  # No response was made
                conf_resp_stim2_loop3.keys = None
            loop3.addData('conf_resp_stim2_loop3.keys',conf_resp_stim2_loop3.keys)
            if conf_resp_stim2_loop3.keys != None:  # we had a response
                loop3.addData('conf_resp_stim2_loop3.rt', conf_resp_stim2_loop3.rt)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-5.000000)
            
            # --- Prepare to start Routine "ISI_outcome" ---
            continueRoutine = True
            # update component parameters for each repeat
            # keep track of which components have finished
            ISI_outcomeComponents = [isi_outcome]
            for thisComponent in ISI_outcomeComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "ISI_outcome" ---
            routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 0.25:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *isi_outcome* updates
                
                # if isi_outcome is starting this frame...
                if isi_outcome.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    isi_outcome.frameNStart = frameN  # exact frame index
                    isi_outcome.tStart = t  # local t and not account for scr refresh
                    isi_outcome.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(isi_outcome, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'isi_outcome.started')
                    # update status
                    isi_outcome.status = STARTED
                    isi_outcome.setAutoDraw(True)
                
                # if isi_outcome is active this frame...
                if isi_outcome.status == STARTED:
                    # update params
                    pass
                
                # if isi_outcome is stopping this frame...
                if isi_outcome.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > isi_outcome.tStartRefresh + 0.5-frameTolerance:
                        # keep track of stop time/frame for later
                        isi_outcome.tStop = t  # not accounting for scr refresh
                        isi_outcome.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'isi_outcome.stopped')
                        # update status
                        isi_outcome.status = FINISHED
                        isi_outcome.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in ISI_outcomeComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "ISI_outcome" ---
            for thisComponent in ISI_outcomeComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-0.2500000)
            
            # --- Prepare to start Routine "outcome_loop3" ---
            continueRoutine = True
            # update component parameters for each repeat
            outcome_img_loop3.setImage(OutcomeH)
            Tone_loop3.setSound(ToneH, secs=1.3, hamming=True)
            Tone_loop3.setVolume(1.0, log=False)
            # keep track of which components have finished
            outcome_loop3Components = [outcome_img_loop3, Tone_loop3]
            for thisComponent in outcome_loop3Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "outcome_loop3" ---
            routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 1.5:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *outcome_img_loop3* updates
                
                # if outcome_img_loop3 is starting this frame...
                if outcome_img_loop3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    outcome_img_loop3.frameNStart = frameN  # exact frame index
                    outcome_img_loop3.tStart = t  # local t and not account for scr refresh
                    outcome_img_loop3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(outcome_img_loop3, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'outcome_img_loop3.started')
                    # update status
                    outcome_img_loop3.status = STARTED
                    outcome_img_loop3.setAutoDraw(True)
                
                # if outcome_img_loop3 is active this frame...
                if outcome_img_loop3.status == STARTED:
                    # update params
                    pass
                
                # if outcome_img_loop3 is stopping this frame...
                if outcome_img_loop3.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > outcome_img_loop3.tStartRefresh + 1.5-frameTolerance:
                        # keep track of stop time/frame for later
                        outcome_img_loop3.tStop = t  # not accounting for scr refresh
                        outcome_img_loop3.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'outcome_img_loop3.stopped')
                        # update status
                        outcome_img_loop3.status = FINISHED
                        outcome_img_loop3.setAutoDraw(False)
                # start/stop Tone_loop3
                
                # if Tone_loop3 is starting this frame...
                if Tone_loop3.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
                    # keep track of start time/frame for later
                    Tone_loop3.frameNStart = frameN  # exact frame index
                    Tone_loop3.tStart = t  # local t and not account for scr refresh
                    Tone_loop3.tStartRefresh = tThisFlipGlobal  # on global time
                    # add timestamp to datafile
                    thisExp.addData('Tone_loop3.started', tThisFlipGlobal)
                    # update status
                    Tone_loop3.status = STARTED
                    Tone_loop3.play(when=win)  # sync with win flip
                
                # if Tone_loop3 is stopping this frame...
                if Tone_loop3.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Tone_loop3.tStartRefresh + 1.3-frameTolerance:
                        # keep track of stop time/frame for later
                        Tone_loop3.tStop = t  # not accounting for scr refresh
                        Tone_loop3.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'Tone_loop3.stopped')
                        # update status
                        Tone_loop3.status = FINISHED
                        Tone_loop3.stop()
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in outcome_loop3Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "outcome_loop3" ---
            for thisComponent in outcome_loop3Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            Tone_loop3.stop()  # ensure sound has stopped at end of routine
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-1.500000)
            
            # --- Prepare to start Routine "jitter_ITI_loop3" ---
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from iti_code_loop3
            import random as rand
            
            jitter_iti_3 = rand.choices([.5, 1.0, 1.5, 2.0], k=54) # create the list
            
            if loop3.thisN == 0: # only on the first trial
                shuffle(jitter_iti_3) # randomise its order
            
            current_jitter_3 = jitter_iti_3.pop() # extract one entry on each trial
            
            thisExp.addData('jitter_iti_3', current_jitter_3) # record in the data for this trial
            
            
            # keep track of which components have finished
            jitter_ITI_loop3Components = [iti_loop3]
            for thisComponent in jitter_ITI_loop3Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "jitter_ITI_loop3" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *iti_loop3* updates
                
                # if iti_loop3 is starting this frame...
                if iti_loop3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    iti_loop3.frameNStart = frameN  # exact frame index
                    iti_loop3.tStart = t  # local t and not account for scr refresh
                    iti_loop3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(iti_loop3, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'iti_loop3.started')
                    # update status
                    iti_loop3.status = STARTED
                    iti_loop3.setAutoDraw(True)
                
                # if iti_loop3 is active this frame...
                if iti_loop3.status == STARTED:
                    # update params
                    pass
                
                # if iti_loop3 is stopping this frame...
                if iti_loop3.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > iti_loop3.tStartRefresh + current_jitter_3-frameTolerance:
                        # keep track of stop time/frame for later
                        iti_loop3.tStop = t  # not accounting for scr refresh
                        iti_loop3.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'iti_loop3.stopped')
                        # update status
                        iti_loop3.status = FINISHED
                        iti_loop3.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in jitter_ITI_loop3Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "jitter_ITI_loop3" ---
            for thisComponent in jitter_ITI_loop3Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # the Routine "jitter_ITI_loop3" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed 1.0 repeats of 'loop3'
        
    # completed 1.0 repeats of 'loopH'
    
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'FullLoop'


# --- Prepare to start Routine "Completion" ---
continueRoutine = True
# update component parameters for each repeat
completion_prompt_resp.keys = []
completion_prompt_resp.rt = []
_completion_prompt_resp_allKeys = []
# keep track of which components have finished
CompletionComponents = [completion_prompt, completion_prompt_resp]
for thisComponent in CompletionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Completion" ---
routineForceEnded = not continueRoutine
while continueRoutine and routineTimer.getTime() < 10.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *completion_prompt* updates
    
    # if completion_prompt is starting this frame...
    if completion_prompt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        completion_prompt.frameNStart = frameN  # exact frame index
        completion_prompt.tStart = t  # local t and not account for scr refresh
        completion_prompt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(completion_prompt, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'completion_prompt.started')
        # update status
        completion_prompt.status = STARTED
        completion_prompt.setAutoDraw(True)
    
    # if completion_prompt is active this frame...
    if completion_prompt.status == STARTED:
        # update params
        pass
    
    # if completion_prompt is stopping this frame...
    if completion_prompt.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > completion_prompt.tStartRefresh + 10-frameTolerance:
            # keep track of stop time/frame for later
            completion_prompt.tStop = t  # not accounting for scr refresh
            completion_prompt.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'completion_prompt.stopped')
            # update status
            completion_prompt.status = FINISHED
            completion_prompt.setAutoDraw(False)
    
    # *completion_prompt_resp* updates
    waitOnFlip = False
    
    # if completion_prompt_resp is starting this frame...
    if completion_prompt_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        completion_prompt_resp.frameNStart = frameN  # exact frame index
        completion_prompt_resp.tStart = t  # local t and not account for scr refresh
        completion_prompt_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(completion_prompt_resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'completion_prompt_resp.started')
        # update status
        completion_prompt_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(completion_prompt_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(completion_prompt_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    
    # if completion_prompt_resp is stopping this frame...
    if completion_prompt_resp.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > completion_prompt_resp.tStartRefresh + 10-frameTolerance:
            # keep track of stop time/frame for later
            completion_prompt_resp.tStop = t  # not accounting for scr refresh
            completion_prompt_resp.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'completion_prompt_resp.stopped')
            # update status
            completion_prompt_resp.status = FINISHED
            completion_prompt_resp.status = FINISHED
    if completion_prompt_resp.status == STARTED and not waitOnFlip:
        theseKeys = completion_prompt_resp.getKeys(keyList=['a'], waitRelease=False)
        _completion_prompt_resp_allKeys.extend(theseKeys)
        if len(_completion_prompt_resp_allKeys):
            completion_prompt_resp.keys = _completion_prompt_resp_allKeys[0].name  # just the first key pressed
            completion_prompt_resp.rt = _completion_prompt_resp_allKeys[0].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in CompletionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Completion" ---
for thisComponent in CompletionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if completion_prompt_resp.keys in ['', [], None]:  # No response was made
    completion_prompt_resp.keys = None
thisExp.addData('completion_prompt_resp.keys',completion_prompt_resp.keys)
if completion_prompt_resp.keys != None:  # we had a response
    thisExp.addData('completion_prompt_resp.rt', completion_prompt_resp.rt)
thisExp.nextEntry()
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-10.000000)

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
