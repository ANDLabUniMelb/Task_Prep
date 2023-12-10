#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.1.0),
    on Wed Oct  4 12:51:56 2023
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

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2023.1.0'
expName = 'Safety_Run4_Tone'  # from the Builder filename that created this script
expInfo = {
    'participant': '',
    'run': '004',
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
    originPath='/Users/stashjian/Documents/Melbourne/Adolescent_Safety/SafetyTask_windows/AversiveTone/Run4/Safety_Run4_Tone.py',
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
    monitor='mri_monitor', color=[0,0,0], colorSpace='rgb',
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

defaultKeyboard = keyboard.Keyboard()

# --- Initialize components for Routine "Trigger" ---
trigger = visual.TextStim(win=win, name='trigger',
    text='Now you will play the last set of battles with animals and weapons…',
    font='Arial',
    pos=(0, 0), height=0.08, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
trigger_resp = keyboard.Keyboard()

# --- Initialize components for Routine "Wait" ---
wait = visual.TextStim(win=win, name='wait',
    text='The game will start in 5 seconds.\n\nRemember to hold still in the scanner...',
    font='Arial',
    pos=(0, 0), height=0.08, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "firststim" ---
firststim_image = visual.ImageStim(
    win=win,
    name='firststim_image', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.6, 0.6),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
firststim_resp = keyboard.Keyboard()

# Initialize components for Routine "firststim_feedback"
fdbk = visual.TextStim(win=win, name='fdbk',
    text='Do you think you will win?\nPress RIGHT for yes and LEFT for no.',
    font='Arial',
    pos=(0, -0.38), height=0.05, wrapWidth=None, ori=0.0,
    color='black', colorSpace='rgb', opacity=None,
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "ISI_stim" ---
isi_stim = visual.TextStim(win=win, name='isi_stim',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "secondstim" ---
secondstim_image = visual.ImageStim(
    win=win,
    name='secondstim_image', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.6, 0.6),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
secondstim_resp = keyboard.Keyboard()

# Initialize components for Routine "secondstim_feedback"
fdbk2 = visual.TextStim(win=win, name='fdbk2',
    text='Do you think you will win?\nPress RIGHT for yes and LEFT for no.',
    font='Arial',
    pos=(0, -0.38), height=0.05, wrapWidth=None, ori=0.0,
    color='black', colorSpace='rgb', opacity=None,
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "ISI_outcome" ---
isi_outcome = visual.TextStim(win=win, name='isi_outcome',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "outcome" ---
outcome_image = visual.ImageStim(
    win=win,
    name='outcome_image', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.6, 0.6),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
tone = sound.Sound('A', secs=1.3, stereo=True, hamming=True,
    name='tone')
tone.setVolume(1.0)

# --- Initialize components for Routine "jitter_ITI" ---
iti = visual.TextStim(win=win, name='iti',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.3, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "Completion" ---
completion_prompt = visual.TextStim(win=win, name='completion_prompt',
    text="You are finished!\n\nPlease press the LEFT key to end.",
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
TriggerComponents = [trigger, trigger_resp]
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
    
    # *trigger* updates
    
    # if trigger is starting this frame...
    if trigger.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        trigger.frameNStart = frameN  # exact frame index
        trigger.tStart = t  # local t and not account for scr refresh
        trigger.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(trigger, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'trigger.started')
        # update status
        trigger.status = STARTED
        trigger.setAutoDraw(True)
    
    # if trigger is active this frame...
    if trigger.status == STARTED:
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
Loop = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Battles_Run4_tone.xlsx'),
    seed=None, name='Loop')
thisExp.addLoop(Loop)  # add the loop to the experiment
thisLoop = Loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLoop.rgb)
if thisLoop != None:
    for paramName in thisLoop:
        exec('{} = thisLoop[paramName]'.format(paramName))

for thisLoop in Loop:
    currentLoop = Loop
    # abbreviate parameter names if possible (e.g. rgb = thisLoop.rgb)
    if thisLoop != None:
        for paramName in thisLoop:
            exec('{} = thisLoop[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "firststim" ---
    continueRoutine = True
    # update component parameters for each repeat
    firststim_image.setImage(FirstStim)
    firststim_resp.keys = []
    firststim_resp.rt = []
    _firststim_resp_allKeys = []
    # keep track of which components have finished
    firststimComponents = [firststim_image, firststim_resp]
    for thisComponent in firststimComponents:
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
    
    # --- Run Routine "firststim" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 8.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *firststim_image* updates
        
        # if firststim_image is starting this frame...
        if firststim_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            firststim_image.frameNStart = frameN  # exact frame index
            firststim_image.tStart = t  # local t and not account for scr refresh
            firststim_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(firststim_image, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'firststim_image.started')
            # update status
            firststim_image.status = STARTED
            firststim_image.setAutoDraw(True)
        
        # if firststim_image is active this frame...
        if firststim_image.status == STARTED:
            # update params
            pass
        
        # if firststim_image is stopping this frame...
        if firststim_image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > firststim_image.tStartRefresh + 8-frameTolerance:
                # keep track of stop time/frame for later
                firststim_image.tStop = t  # not accounting for scr refresh
                firststim_image.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'firststim_image.stopped')
                # update status
                firststim_image.status = FINISHED
                firststim_image.setAutoDraw(False)
        
        # *firststim_resp* updates
        waitOnFlip = False
        
        # if firststim_resp is starting this frame...
        if firststim_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            firststim_resp.frameNStart = frameN  # exact frame index
            firststim_resp.tStart = t  # local t and not account for scr refresh
            firststim_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(firststim_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'firststim_resp.started')
            # update status
            firststim_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(firststim_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(firststim_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        
        # if firststim_resp is stopping this frame...
        if firststim_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > firststim_resp.tStartRefresh + 8-frameTolerance:
                # keep track of stop time/frame for later
                firststim_resp.tStop = t  # not accounting for scr refresh
                firststim_resp.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'firststim_resp.stopped')
                # update status
                firststim_resp.status = FINISHED
                firststim_resp.status = FINISHED
        if firststim_resp.status == STARTED and not waitOnFlip:
            theseKeys = firststim_resp.getKeys(keyList=['c','a'], waitRelease=False)
            _firststim_resp_allKeys.extend(theseKeys)
            if len(_firststim_resp_allKeys):
                firststim_resp.keys = _firststim_resp_allKeys[-1].name  # just the last key pressed
                firststim_resp.rt = _firststim_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
            
        # fdbk
        if firststim_resp.keys in ['', [], None] and routineTimer.getTime() >= 5:
            firststim_resp.keys = None
            fdbk.draw()
            win.flip()

            # Start a 2-second loop to check for key responses
            feedback_timer = core.CountdownTimer(2)  # 2 seconds timer
            while feedback_timer.getTime() > 0:
                theseKeys = firststim_resp.getKeys(keyList=['c','a'], waitRelease=False)
                if len(theseKeys):
                    firststim_resp.keys = theseKeys[-1].name
                    firststim_resp.rt = theseKeys[-1].rt
                    continueRoutine = False
                    break
                    
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in firststimComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "firststim" ---
    for thisComponent in firststimComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if firststim_resp.keys in ['', [], None]:  # No response was made
        firststim_resp.keys = None
    Loop.addData('firststim_resp.keys',firststim_resp.keys)
    if firststim_resp.keys != None:  # we had a response
        Loop.addData('firststim_resp.rt', firststim_resp.rt)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-8.000000)
    
    # --- Prepare to start Routine "ISI_stim" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from isi_stim_code
    import random as rand
    
    jitter_isi = rand.choices([0.5, 0.5, 1.0, 1.0, 1.5, 2.0], k=161) # create the list
    
    
    if Loop.thisN == 0: # only on the first trial
        shuffle(jitter_isi) # randomise its order
    
    current_isi = jitter_isi.pop() # extract one entry on each trial
    thisExp.addData('isi_stim', current_isi) # record in the data for this trial
    # keep track of which components have finished
    ISI_stimComponents = [isi_stim]
    for thisComponent in ISI_stimComponents:
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
    
    # --- Run Routine "ISI_stim" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *isi_stim* updates
        
        # if isi_stim is starting this frame...
        if isi_stim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            isi_stim.frameNStart = frameN  # exact frame index
            isi_stim.tStart = t  # local t and not account for scr refresh
            isi_stim.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(isi_stim, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'isi_stim.started')
            # update status
            isi_stim.status = STARTED
            isi_stim.setAutoDraw(True)
        
        # if isi_stim is active this frame...
        if isi_stim.status == STARTED:
            # update params
            pass
        
        # if isi_stim is stopping this frame...
        if isi_stim.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > isi_stim.tStartRefresh + current_isi-frameTolerance:
                # keep track of stop time/frame for later
                isi_stim.tStop = t  # not accounting for scr refresh
                isi_stim.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'isi_stim.stopped')
                # update status
                isi_stim.status = FINISHED
                isi_stim.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ISI_stimComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ISI_stim" ---
    for thisComponent in ISI_stimComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "ISI_stim" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "secondstim" ---
    continueRoutine = True
    # update component parameters for each repeat
    secondstim_image.setImage(SecondStim)
    secondstim_resp.keys = []
    secondstim_resp.rt = []
    _secondstim_resp_allKeys = []
    # keep track of which components have finished
    secondstimComponents = [secondstim_image, secondstim_resp]
    for thisComponent in secondstimComponents:
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
    
    # --- Run Routine "secondstim" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 8.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *secondstim_image* updates
        
        # if secondstim_image is starting this frame...
        if secondstim_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            secondstim_image.frameNStart = frameN  # exact frame index
            secondstim_image.tStart = t  # local t and not account for scr refresh
            secondstim_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(secondstim_image, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'secondstim_image.started')
            # update status
            secondstim_image.status = STARTED
            secondstim_image.setAutoDraw(True)
        
        # if secondstim_image is active this frame...
        if secondstim_image.status == STARTED:
            # update params
            pass
        
        # if secondstim_image is stopping this frame...
        if secondstim_image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > secondstim_image.tStartRefresh + 8-frameTolerance:
                # keep track of stop time/frame for later
                secondstim_image.tStop = t  # not accounting for scr refresh
                secondstim_image.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'secondstim_image.stopped')
                # update status
                secondstim_image.status = FINISHED
                secondstim_image.setAutoDraw(False)
        
        # *secondstim_resp* updates
        waitOnFlip = False
        
        # if secondstim_resp is starting this frame...
        if secondstim_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            secondstim_resp.frameNStart = frameN  # exact frame index
            secondstim_resp.tStart = t  # local t and not account for scr refresh
            secondstim_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(secondstim_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'secondstim_resp.started')
            # update status
            secondstim_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(secondstim_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(secondstim_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        
        # if secondstim_resp is stopping this frame...
        if secondstim_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > secondstim_resp.tStartRefresh + 8-frameTolerance:
                # keep track of stop time/frame for later
                secondstim_resp.tStop = t  # not accounting for scr refresh
                secondstim_resp.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'secondstim_resp.stopped')
                # update status
                secondstim_resp.status = FINISHED
                secondstim_resp.status = FINISHED
        if secondstim_resp.status == STARTED and not waitOnFlip:
            theseKeys = secondstim_resp.getKeys(keyList=['c','a'], waitRelease=False)
            _secondstim_resp_allKeys.extend(theseKeys)
            if len(_secondstim_resp_allKeys):
                secondstim_resp.keys = _secondstim_resp_allKeys[-1].name  # just the last key pressed
                secondstim_resp.rt = _secondstim_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # fdbk2
        if secondstim_resp.keys in ['', [], None] and routineTimer.getTime() >= 5:
            secondstim_resp.keys = None
            fdbk.draw()
            win.flip()

            # Start a 2-second loop to check for key responses
            feedback_timer = core.CountdownTimer(2)  # 2 seconds timer
            while feedback_timer.getTime() > 0:
                theseKeys = secondstim_resp.getKeys(keyList=['c','a'], waitRelease=False)
                if len(theseKeys):
                    secondstim_resp.keys = theseKeys[-1].name
                    secondstim_resp.rt = theseKeys[-1].rt
                    continueRoutine = False
                    break
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in secondstimComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
            
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
            
    # --- Ending Routine "secondstim" ---
    for thisComponent in secondstimComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if secondstim_resp.keys in ['', [], None]:  # No response was made
        secondstim_resp.keys = None
    Loop.addData('secondstim_resp.keys',secondstim_resp.keys)
    if secondstim_resp.keys != None:  # we had a response
        Loop.addData('secondstim_resp.rt', secondstim_resp.rt)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-8.000000)
    
    # --- Prepare to start Routine "ISI_outcome" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from isi_outcome_code
    # import random as rand
    
    # jitter_isi_outcome = rand.choices([.5, 1.0, 1.5, 2.0], k=161) # create the list
    
    
    # if Loop.thisN == 0: # only on the first trial
    #     shuffle(jitter_isi_outcome) # randomise its order
    
    # current_isi_outcome = jitter_isi_outcome.pop() # extract one entry on each trial
    current_isi_outcome = .25
    thisExp.addData('isi_outcome', current_isi_outcome) # record in the data for this trial
    
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
    while continueRoutine:
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
            if tThisFlipGlobal > isi_outcome.tStartRefresh + current_isi_outcome-frameTolerance:
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
    # the Routine "ISI_outcome" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "outcome" ---
    continueRoutine = True
    # update component parameters for each repeat
    outcome_image.setImage(Outcome)
    tone.setSound(Tone, secs=1.3, hamming=True)
    tone.setVolume(1.0, log=False)
    # keep track of which components have finished
    outcomeComponents = [outcome_image, tone]
    for thisComponent in outcomeComponents:
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
    
    # --- Run Routine "outcome" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 1.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *outcome_image* updates
        
        # if outcome_image is starting this frame...
        if outcome_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            outcome_image.frameNStart = frameN  # exact frame index
            outcome_image.tStart = t  # local t and not account for scr refresh
            outcome_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(outcome_image, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'outcome_image.started')
            # update status
            outcome_image.status = STARTED
            outcome_image.setAutoDraw(True)
        
        # if outcome_image is active this frame...
        if outcome_image.status == STARTED:
            # update params
            pass
        
        # if outcome_image is stopping this frame...
        if outcome_image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > outcome_image.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                outcome_image.tStop = t  # not accounting for scr refresh
                outcome_image.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'outcome_image.stopped')
                # update status
                outcome_image.status = FINISHED
                outcome_image.setAutoDraw(False)
        # start/stop tone
        
        # if tone is starting this frame...
        if tone.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
            # keep track of start time/frame for later
            tone.frameNStart = frameN  # exact frame index
            tone.tStart = t  # local t and not account for scr refresh
            tone.tStartRefresh = tThisFlipGlobal  # on global time
            # add timestamp to datafile
            thisExp.addData('tone.started', tThisFlipGlobal)
            # update status
            tone.status = STARTED
            tone.play(when=win)  # sync with win flip
        
        # if tone is stopping this frame...
        if tone.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > tone.tStartRefresh + 1.3-frameTolerance:
                # keep track of stop time/frame for later
                tone.tStop = t  # not accounting for scr refresh
                tone.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'tone.stopped')
                # update status
                tone.status = FINISHED
                tone.stop()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in outcomeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "outcome" ---
    for thisComponent in outcomeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    tone.stop()  # ensure sound has stopped at end of routine
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.500000)
    
    # --- Prepare to start Routine "jitter_ITI" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from iti_code
    import random as rand
    
    jitter_iti = rand.choices([0.5, 1.0, 1.5, 2.0], k=161) # create the list
    
    if Loop.thisN == 0: # only on the first trial
        shuffle(jitter_iti) # randomise its order
    
    current_jitter = jitter_iti.pop() # extract one entry on each trial
    
    thisExp.addData('jitter_iti', current_jitter) # record in the data for this trial
    
    
    # keep track of which components have finished
    jitter_ITIComponents = [iti]
    for thisComponent in jitter_ITIComponents:
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
    
    # --- Run Routine "jitter_ITI" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *iti* updates
        
        # if iti is starting this frame...
        if iti.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            iti.frameNStart = frameN  # exact frame index
            iti.tStart = t  # local t and not account for scr refresh
            iti.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(iti, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'iti.started')
            # update status
            iti.status = STARTED
            iti.setAutoDraw(True)
        
        # if iti is active this frame...
        if iti.status == STARTED:
            # update params
            pass
        
        # if iti is stopping this frame...
        if iti.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > iti.tStartRefresh + current_jitter-frameTolerance:
                # keep track of stop time/frame for later
                iti.tStop = t  # not accounting for scr refresh
                iti.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'iti.stopped')
                # update status
                iti.status = FINISHED
                iti.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in jitter_ITIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "jitter_ITI" ---
    for thisComponent in jitter_ITIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "jitter_ITI" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'Loop'


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
while continueRoutine:
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
    if completion_prompt_resp.status == STARTED and not waitOnFlip:
        theseKeys = completion_prompt_resp.getKeys(keyList=['c'], waitRelease=False)
        _completion_prompt_resp_allKeys.extend(theseKeys)
        if len(_completion_prompt_resp_allKeys):
            completion_prompt_resp.keys = _completion_prompt_resp_allKeys[-1].name  # just the last key pressed
            completion_prompt_resp.rt = _completion_prompt_resp_allKeys[-1].rt
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
# the Routine "Completion" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

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
