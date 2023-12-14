#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.1.0),
    on Wed Oct  4 12:49:24 2023
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
expName = 'Localizer_Pre'  # from the Builder filename that created this script
expInfo = {
    'participant': '',
    'session (pre/post)': '',
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
    originPath='/Users/stashjian/Documents/Melbourne/Adolescent_Safety/SafetyTask_windows/AversiveTone/Localizer/Localizer.py',
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
trigger = visual.TextStim(win=win, name='trigger',
    text='Now you will see a series of pictures. Look carefully at the images.\n\nThis will take about 3 minutes.',
    font='Arial',
    pos=(0, 0), height=0.08, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
trigger_resp = keyboard.Keyboard()

# --- Initialize components for Routine "Wait" ---
wait = visual.TextStim(win=win, name='wait',
    text='The images will start in 5 seconds.\n\nRemember to hold still in the scanner...',
    font='Arial',
    pos=(0, 0), height=0.08, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "weapon" ---
weapon_img = visual.ImageStim(
    win=win,
    name='weapon_img', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.6, 0.6),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
ISI_weapon = visual.TextStim(win=win, name='ISI_weapon',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.3, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "ITI_weapon" ---
ITI_Weapon = visual.TextStim(win=win, name='ITI_Weapon',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "animal" ---
anima_img = visual.ImageStim(
    win=win,
    name='anima_img', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.6, 0.6),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
ISI_animal = visual.TextStim(win=win, name='ISI_animal',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.3, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "ITI_animal" ---
ITI_Animal = visual.TextStim(win=win, name='ITI_Animal',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "low_threat" ---
Low_Threat_img = visual.ImageStim(
    win=win,
    name='Low_Threat_img', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.6, 0.6),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
ISI_low_threat = visual.TextStim(win=win, name='ISI_low_threat',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.3, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "ITI_low_threat" ---
ITI_Low_Threat = visual.TextStim(win=win, name='ITI_Low_Threat',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "safe" ---
safe_img = visual.ImageStim(
    win=win,
    name='safe_img', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.6, 0.6),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
ISI_safe = visual.TextStim(win=win, name='ISI_safe',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.3, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "ITI_safe" ---
ITI_Safe = visual.TextStim(win=win, name='ITI_Safe',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.3, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "danger" ---
danger_img = visual.ImageStim(
    win=win,
    name='danger_img', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.6, 0.6),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
ISI_danger = visual.TextStim(win=win, name='ISI_danger',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.3, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "ITI_danger" ---
ITI_Danger = visual.TextStim(win=win, name='ITI_Danger',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.3, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "high_threat" ---
High_Threat_img = visual.ImageStim(
    win=win,
    name='High_Threat_img', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.6, 0.6),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
ISI_High_Threat = visual.TextStim(win=win, name='ISI_High_Threat',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.3, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "ITI_high_threat" ---
ITI_High_Threat = visual.TextStim(win=win, name='ITI_High_Threat',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.3, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "Completion" ---
completion = visual.TextStim(win=win, name='completion',
    text='You are finished!\n\nPlease press the LEFT key to end.',
    font='Arial',
    pos=(0, 0), height=0.08, wrapWidth=None, ori=0.0,
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
completion_resp = keyboard.Keyboard()

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
            trigger_resp.keys = [key.name for key in _trigger_resp_allKeys]  # storing all keys
            trigger_resp.rt = [key.rt for key in _trigger_resp_allKeys]
            # was this correct?
            if (trigger_resp.keys == str('5')) or (trigger_resp.keys == '5'):
                trigger_resp.corr = 1
            else:
                trigger_resp.corr = 0
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
    # was no response the correct answer?!
    if str('5').lower() == 'none':
       trigger_resp.corr = 1;  # correct non-response
    else:
       trigger_resp.corr = 0;  # failed to respond (incorrectly)
# store data for thisExp (ExperimentHandler)
thisExp.addData('trigger_resp.keys',trigger_resp.keys)
thisExp.addData('trigger_resp.corr', trigger_resp.corr)
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
Full_Loop = data.TrialHandler(nReps=2.0, method='random',
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='Full_Loop')
thisExp.addLoop(Full_Loop)  # add the loop to the experiment
thisFull_Loop = Full_Loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisFull_Loop.rgb)
if thisFull_Loop != None:
    for paramName in thisFull_Loop:
        exec('{} = thisFull_Loop[paramName]'.format(paramName))

for thisFull_Loop in Full_Loop:
    currentLoop = Full_Loop
    # abbreviate parameter names if possible (e.g. rgb = thisFull_Loop.rgb)
    if thisFull_Loop != None:
        for paramName in thisFull_Loop:
            exec('{} = thisFull_Loop[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    Weapon_loop = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='Weapon_loop')
    thisExp.addLoop(Weapon_loop)  # add the loop to the experiment
    thisWeapon_loop = Weapon_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisWeapon_loop.rgb)
    if thisWeapon_loop != None:
        for paramName in thisWeapon_loop:
            exec('{} = thisWeapon_loop[paramName]'.format(paramName))
    
    for thisWeapon_loop in Weapon_loop:
        currentLoop = Weapon_loop
        # abbreviate parameter names if possible (e.g. rgb = thisWeapon_loop.rgb)
        if thisWeapon_loop != None:
            for paramName in thisWeapon_loop:
                exec('{} = thisWeapon_loop[paramName]'.format(paramName))
        
        # set up handler to look after randomisation of conditions etc
        Weapon_img_loop = data.TrialHandler(nReps=2.0, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('Localizer.xlsx'),
            seed=None, name='Weapon_img_loop')
        thisExp.addLoop(Weapon_img_loop)  # add the loop to the experiment
        thisWeapon_img_loop = Weapon_img_loop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisWeapon_img_loop.rgb)
        if thisWeapon_img_loop != None:
            for paramName in thisWeapon_img_loop:
                exec('{} = thisWeapon_img_loop[paramName]'.format(paramName))
        
        for thisWeapon_img_loop in Weapon_img_loop:
            currentLoop = Weapon_img_loop
            # abbreviate parameter names if possible (e.g. rgb = thisWeapon_img_loop.rgb)
            if thisWeapon_img_loop != None:
                for paramName in thisWeapon_img_loop:
                    exec('{} = thisWeapon_img_loop[paramName]'.format(paramName))
            
            # --- Prepare to start Routine "weapon" ---
            continueRoutine = True
            # update component parameters for each repeat
            weapon_img.setImage(Weapon)
            # keep track of which components have finished
            weaponComponents = [weapon_img, ISI_weapon]
            for thisComponent in weaponComponents:
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
            
            # --- Run Routine "weapon" ---
            routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 0.4:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *weapon_img* updates
                
                # if weapon_img is starting this frame...
                if weapon_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    weapon_img.frameNStart = frameN  # exact frame index
                    weapon_img.tStart = t  # local t and not account for scr refresh
                    weapon_img.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(weapon_img, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'weapon_img.started')
                    # update status
                    weapon_img.status = STARTED
                    weapon_img.setAutoDraw(True)
                
                # if weapon_img is active this frame...
                if weapon_img.status == STARTED:
                    # update params
                    pass
                
                # if weapon_img is stopping this frame...
                if weapon_img.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > weapon_img.tStartRefresh + 0.3-frameTolerance:
                        # keep track of stop time/frame for later
                        weapon_img.tStop = t  # not accounting for scr refresh
                        weapon_img.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'weapon_img.stopped')
                        # update status
                        weapon_img.status = FINISHED
                        weapon_img.setAutoDraw(False)
                
                # *ISI_weapon* updates
                
                # if ISI_weapon is starting this frame...
                if ISI_weapon.status == NOT_STARTED and tThisFlip >= 0.3-frameTolerance:
                    # keep track of start time/frame for later
                    ISI_weapon.frameNStart = frameN  # exact frame index
                    ISI_weapon.tStart = t  # local t and not account for scr refresh
                    ISI_weapon.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ISI_weapon, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'ISI_weapon.started')
                    # update status
                    ISI_weapon.status = STARTED
                    ISI_weapon.setAutoDraw(True)
                
                # if ISI_weapon is active this frame...
                if ISI_weapon.status == STARTED:
                    # update params
                    pass
                
                # if ISI_weapon is stopping this frame...
                if ISI_weapon.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > ISI_weapon.tStartRefresh + 0.3-frameTolerance:
                        # keep track of stop time/frame for later
                        ISI_weapon.tStop = t  # not accounting for scr refresh
                        ISI_weapon.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'ISI_weapon.stopped')
                        # update status
                        ISI_weapon.status = FINISHED
                        ISI_weapon.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in weaponComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "weapon" ---
            for thisComponent in weaponComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-0.400000)
            thisExp.nextEntry()
            
        # completed 4.0 repeats of 'Weapon_img_loop'
        
        
        # --- Prepare to start Routine "ITI_weapon" ---
        continueRoutine = True
        # update component parameters for each repeat
        # keep track of which components have finished
        ITI_weaponComponents = [ITI_Weapon]
        for thisComponent in ITI_weaponComponents:
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
        
        # --- Run Routine "ITI_weapon" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 12.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *ITI_Weapon* updates
            
            # if ITI_Weapon is starting this frame...
            if ITI_Weapon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                ITI_Weapon.frameNStart = frameN  # exact frame index
                ITI_Weapon.tStart = t  # local t and not account for scr refresh
                ITI_Weapon.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ITI_Weapon, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ITI_Weapon.started')
                # update status
                ITI_Weapon.status = STARTED
                ITI_Weapon.setAutoDraw(True)
            
            # if ITI_Weapon is active this frame...
            if ITI_Weapon.status == STARTED:
                # update params
                pass
            
            # if ITI_Weapon is stopping this frame...
            if ITI_Weapon.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > ITI_Weapon.tStartRefresh + 12-frameTolerance:
                    # keep track of stop time/frame for later
                    ITI_Weapon.tStop = t  # not accounting for scr refresh
                    ITI_Weapon.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'ITI_Weapon.stopped')
                    # update status
                    ITI_Weapon.status = FINISHED
                    ITI_Weapon.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ITI_weaponComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "ITI_weapon" ---
        for thisComponent in ITI_weaponComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-12.000000)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'Weapon_loop'
    
    
    # set up handler to look after randomisation of conditions etc
    Animal_loop = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='Animal_loop')
    thisExp.addLoop(Animal_loop)  # add the loop to the experiment
    thisAnimal_loop = Animal_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisAnimal_loop.rgb)
    if thisAnimal_loop != None:
        for paramName in thisAnimal_loop:
            exec('{} = thisAnimal_loop[paramName]'.format(paramName))
    
    for thisAnimal_loop in Animal_loop:
        currentLoop = Animal_loop
        # abbreviate parameter names if possible (e.g. rgb = thisAnimal_loop.rgb)
        if thisAnimal_loop != None:
            for paramName in thisAnimal_loop:
                exec('{} = thisAnimal_loop[paramName]'.format(paramName))
        
        # set up handler to look after randomisation of conditions etc
        Animal_img_loop = data.TrialHandler(nReps=2.0, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('Localizer.xlsx'),
            seed=None, name='Animal_img_loop')
        thisExp.addLoop(Animal_img_loop)  # add the loop to the experiment
        thisAnimal_img_loop = Animal_img_loop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisAnimal_img_loop.rgb)
        if thisAnimal_img_loop != None:
            for paramName in thisAnimal_img_loop:
                exec('{} = thisAnimal_img_loop[paramName]'.format(paramName))
        
        for thisAnimal_img_loop in Animal_img_loop:
            currentLoop = Animal_img_loop
            # abbreviate parameter names if possible (e.g. rgb = thisAnimal_img_loop.rgb)
            if thisAnimal_img_loop != None:
                for paramName in thisAnimal_img_loop:
                    exec('{} = thisAnimal_img_loop[paramName]'.format(paramName))
            
            # --- Prepare to start Routine "animal" ---
            continueRoutine = True
            # update component parameters for each repeat
            anima_img.setImage(Animal)
            # keep track of which components have finished
            animalComponents = [anima_img, ISI_animal]
            for thisComponent in animalComponents:
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
            
            # --- Run Routine "animal" ---
            routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 0.4:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *anima_img* updates
                
                # if anima_img is starting this frame...
                if anima_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    anima_img.frameNStart = frameN  # exact frame index
                    anima_img.tStart = t  # local t and not account for scr refresh
                    anima_img.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(anima_img, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'anima_img.started')
                    # update status
                    anima_img.status = STARTED
                    anima_img.setAutoDraw(True)
                
                # if anima_img is active this frame...
                if anima_img.status == STARTED:
                    # update params
                    pass
                
                # if anima_img is stopping this frame...
                if anima_img.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > anima_img.tStartRefresh + 0.3-frameTolerance:
                        # keep track of stop time/frame for later
                        anima_img.tStop = t  # not accounting for scr refresh
                        anima_img.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'anima_img.stopped')
                        # update status
                        anima_img.status = FINISHED
                        anima_img.setAutoDraw(False)
                
                # *ISI_animal* updates
                
                # if ISI_animal is starting this frame...
                if ISI_animal.status == NOT_STARTED and tThisFlip >= 0.3-frameTolerance:
                    # keep track of start time/frame for later
                    ISI_animal.frameNStart = frameN  # exact frame index
                    ISI_animal.tStart = t  # local t and not account for scr refresh
                    ISI_animal.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ISI_animal, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'ISI_animal.started')
                    # update status
                    ISI_animal.status = STARTED
                    ISI_animal.setAutoDraw(True)
                
                # if ISI_animal is active this frame...
                if ISI_animal.status == STARTED:
                    # update params
                    pass
                
                # if ISI_animal is stopping this frame...
                if ISI_animal.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > ISI_animal.tStartRefresh + 0.3-frameTolerance:
                        # keep track of stop time/frame for later
                        ISI_animal.tStop = t  # not accounting for scr refresh
                        ISI_animal.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'ISI_animal.stopped')
                        # update status
                        ISI_animal.status = FINISHED
                        ISI_animal.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in animalComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "animal" ---
            for thisComponent in animalComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-0.400000)
            thisExp.nextEntry()
            
        # completed 4.0 repeats of 'Animal_img_loop'
        
        
        # --- Prepare to start Routine "ITI_animal" ---
        continueRoutine = True
        # update component parameters for each repeat
        # keep track of which components have finished
        ITI_animalComponents = [ITI_Animal]
        for thisComponent in ITI_animalComponents:
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
        
        # --- Run Routine "ITI_animal" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 12.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *ITI_Animal* updates
            
            # if ITI_Animal is starting this frame...
            if ITI_Animal.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                ITI_Animal.frameNStart = frameN  # exact frame index
                ITI_Animal.tStart = t  # local t and not account for scr refresh
                ITI_Animal.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ITI_Animal, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ITI_Animal.started')
                # update status
                ITI_Animal.status = STARTED
                ITI_Animal.setAutoDraw(True)
            
            # if ITI_Animal is active this frame...
            if ITI_Animal.status == STARTED:
                # update params
                pass
            
            # if ITI_Animal is stopping this frame...
            if ITI_Animal.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > ITI_Animal.tStartRefresh + 12-frameTolerance:
                    # keep track of stop time/frame for later
                    ITI_Animal.tStop = t  # not accounting for scr refresh
                    ITI_Animal.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'ITI_Animal.stopped')
                    # update status
                    ITI_Animal.status = FINISHED
                    ITI_Animal.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ITI_animalComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "ITI_animal" ---
        for thisComponent in ITI_animalComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-12.000000)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'Animal_loop'
    
    
    # set up handler to look after randomisation of conditions etc
    Low_Threat_loop = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='Low_Threat_loop')
    thisExp.addLoop(Low_Threat_loop)  # add the loop to the experiment
    thisLow_Threat_loop = Low_Threat_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisLow_Threat_loop.rgb)
    if thisLow_Threat_loop != None:
        for paramName in thisLow_Threat_loop:
            exec('{} = thisLow_Threat_loop[paramName]'.format(paramName))
    
    for thisLow_Threat_loop in Low_Threat_loop:
        currentLoop = Low_Threat_loop
        # abbreviate parameter names if possible (e.g. rgb = thisLow_Threat_loop.rgb)
        if thisLow_Threat_loop != None:
            for paramName in thisLow_Threat_loop:
                exec('{} = thisLow_Threat_loop[paramName]'.format(paramName))
        
        # set up handler to look after randomisation of conditions etc
        Low_Threat_img_loop = data.TrialHandler(nReps=2.0, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('Localizer.xlsx'),
            seed=None, name='Low_Threat_img_loop')
        thisExp.addLoop(Low_Threat_img_loop)  # add the loop to the experiment
        thisLow_Threat_img_loop = Low_Threat_img_loop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisLow_Threat_img_loop.rgb)
        if thisLow_Threat_img_loop != None:
            for paramName in thisLow_Threat_img_loop:
                exec('{} = thisLow_Threat_img_loop[paramName]'.format(paramName))
        
        for thisLow_Threat_img_loop in Low_Threat_img_loop:
            currentLoop = Low_Threat_img_loop
            # abbreviate parameter names if possible (e.g. rgb = thisLow_Threat_img_loop.rgb)
            if thisLow_Threat_img_loop != None:
                for paramName in thisLow_Threat_img_loop:
                    exec('{} = thisLow_Threat_img_loop[paramName]'.format(paramName))
            
            # --- Prepare to start Routine "low_threat" ---
            continueRoutine = True
            # update component parameters for each repeat
            Low_Threat_img.setImage(LowThreat)
            # keep track of which components have finished
            low_threatComponents = [Low_Threat_img, ISI_low_threat]
            for thisComponent in low_threatComponents:
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
            
            # --- Run Routine "low_threat" ---
            routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 0.4:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *Low_Threat_img* updates
                
                # if Low_Threat_img is starting this frame...
                if Low_Threat_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Low_Threat_img.frameNStart = frameN  # exact frame index
                    Low_Threat_img.tStart = t  # local t and not account for scr refresh
                    Low_Threat_img.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Low_Threat_img, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Low_Threat_img.started')
                    # update status
                    Low_Threat_img.status = STARTED
                    Low_Threat_img.setAutoDraw(True)
                
                # if Low_Threat_img is active this frame...
                if Low_Threat_img.status == STARTED:
                    # update params
                    pass
                
                # if Low_Threat_img is stopping this frame...
                if Low_Threat_img.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Low_Threat_img.tStartRefresh + 0.3-frameTolerance:
                        # keep track of stop time/frame for later
                        Low_Threat_img.tStop = t  # not accounting for scr refresh
                        Low_Threat_img.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'Low_Threat_img.stopped')
                        # update status
                        Low_Threat_img.status = FINISHED
                        Low_Threat_img.setAutoDraw(False)
                
                # *ISI_low_threat* updates
                
                # if ISI_low_threat is starting this frame...
                if ISI_low_threat.status == NOT_STARTED and tThisFlip >= 0.3-frameTolerance:
                    # keep track of start time/frame for later
                    ISI_low_threat.frameNStart = frameN  # exact frame index
                    ISI_low_threat.tStart = t  # local t and not account for scr refresh
                    ISI_low_threat.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ISI_low_threat, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'ISI_low_threat.started')
                    # update status
                    ISI_low_threat.status = STARTED
                    ISI_low_threat.setAutoDraw(True)
                
                # if ISI_low_threat is active this frame...
                if ISI_low_threat.status == STARTED:
                    # update params
                    pass
                
                # if ISI_low_threat is stopping this frame...
                if ISI_low_threat.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > ISI_low_threat.tStartRefresh + 0.3-frameTolerance:
                        # keep track of stop time/frame for later
                        ISI_low_threat.tStop = t  # not accounting for scr refresh
                        ISI_low_threat.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'ISI_low_threat.stopped')
                        # update status
                        ISI_low_threat.status = FINISHED
                        ISI_low_threat.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in low_threatComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "low_threat" ---
            for thisComponent in low_threatComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-0.400000)
            thisExp.nextEntry()
            
        # completed 2.0 repeats of 'Low_Threat_img_loop'
        
        
        # --- Prepare to start Routine "ITI_low_threat" ---
        continueRoutine = True
        # update component parameters for each repeat
        # keep track of which components have finished
        ITI_low_threatComponents = [ITI_Low_Threat]
        for thisComponent in ITI_low_threatComponents:
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
        
        # --- Run Routine "ITI_low_threat" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 12.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *ITI_Low_Threat* updates
            
            # if ITI_Low_Threat is starting this frame...
            if ITI_Low_Threat.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                ITI_Low_Threat.frameNStart = frameN  # exact frame index
                ITI_Low_Threat.tStart = t  # local t and not account for scr refresh
                ITI_Low_Threat.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ITI_Low_Threat, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ITI_Low_Threat.started')
                # update status
                ITI_Low_Threat.status = STARTED
                ITI_Low_Threat.setAutoDraw(True)
            
            # if ITI_Low_Threat is active this frame...
            if ITI_Low_Threat.status == STARTED:
                # update params
                pass
            
            # if ITI_Low_Threat is stopping this frame...
            if ITI_Low_Threat.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > ITI_Low_Threat.tStartRefresh + 12-frameTolerance:
                    # keep track of stop time/frame for later
                    ITI_Low_Threat.tStop = t  # not accounting for scr refresh
                    ITI_Low_Threat.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'ITI_Low_Threat.stopped')
                    # update status
                    ITI_Low_Threat.status = FINISHED
                    ITI_Low_Threat.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ITI_low_threatComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "ITI_low_threat" ---
        for thisComponent in ITI_low_threatComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-12.000000)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'Low_Threat_loop'
    
    
    # set up handler to look after randomisation of conditions etc
    Safe_loop = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='Safe_loop')
    thisExp.addLoop(Safe_loop)  # add the loop to the experiment
    thisSafe_loop = Safe_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisSafe_loop.rgb)
    if thisSafe_loop != None:
        for paramName in thisSafe_loop:
            exec('{} = thisSafe_loop[paramName]'.format(paramName))
    
    for thisSafe_loop in Safe_loop:
        currentLoop = Safe_loop
        # abbreviate parameter names if possible (e.g. rgb = thisSafe_loop.rgb)
        if thisSafe_loop != None:
            for paramName in thisSafe_loop:
                exec('{} = thisSafe_loop[paramName]'.format(paramName))
        
        # set up handler to look after randomisation of conditions etc
        Safe_img_loop = data.TrialHandler(nReps=2.0, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('Localizer.xlsx'),
            seed=None, name='Safe_img_loop')
        thisExp.addLoop(Safe_img_loop)  # add the loop to the experiment
        thisSafe_img_loop = Safe_img_loop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisSafe_img_loop.rgb)
        if thisSafe_img_loop != None:
            for paramName in thisSafe_img_loop:
                exec('{} = thisSafe_img_loop[paramName]'.format(paramName))
        
        for thisSafe_img_loop in Safe_img_loop:
            currentLoop = Safe_img_loop
            # abbreviate parameter names if possible (e.g. rgb = thisSafe_img_loop.rgb)
            if thisSafe_img_loop != None:
                for paramName in thisSafe_img_loop:
                    exec('{} = thisSafe_img_loop[paramName]'.format(paramName))
            
            # --- Prepare to start Routine "safe" ---
            continueRoutine = True
            # update component parameters for each repeat
            safe_img.setImage(Safe)
            # keep track of which components have finished
            safeComponents = [safe_img, ISI_safe]
            for thisComponent in safeComponents:
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
            
            # --- Run Routine "safe" ---
            routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 0.4:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *safe_img* updates
                
                # if safe_img is starting this frame...
                if safe_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    safe_img.frameNStart = frameN  # exact frame index
                    safe_img.tStart = t  # local t and not account for scr refresh
                    safe_img.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(safe_img, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'safe_img.started')
                    # update status
                    safe_img.status = STARTED
                    safe_img.setAutoDraw(True)
                
                # if safe_img is active this frame...
                if safe_img.status == STARTED:
                    # update params
                    pass
                
                # if safe_img is stopping this frame...
                if safe_img.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > safe_img.tStartRefresh + 0.3-frameTolerance:
                        # keep track of stop time/frame for later
                        safe_img.tStop = t  # not accounting for scr refresh
                        safe_img.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'safe_img.stopped')
                        # update status
                        safe_img.status = FINISHED
                        safe_img.setAutoDraw(False)
                
                # *ISI_safe* updates
                
                # if ISI_safe is starting this frame...
                if ISI_safe.status == NOT_STARTED and tThisFlip >= 0.3-frameTolerance:
                    # keep track of start time/frame for later
                    ISI_safe.frameNStart = frameN  # exact frame index
                    ISI_safe.tStart = t  # local t and not account for scr refresh
                    ISI_safe.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ISI_safe, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'ISI_safe.started')
                    # update status
                    ISI_safe.status = STARTED
                    ISI_safe.setAutoDraw(True)
                
                # if ISI_safe is active this frame...
                if ISI_safe.status == STARTED:
                    # update params
                    pass
                
                # if ISI_safe is stopping this frame...
                if ISI_safe.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > ISI_safe.tStartRefresh + 0.3-frameTolerance:
                        # keep track of stop time/frame for later
                        ISI_safe.tStop = t  # not accounting for scr refresh
                        ISI_safe.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'ISI_safe.stopped')
                        # update status
                        ISI_safe.status = FINISHED
                        ISI_safe.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in safeComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "safe" ---
            for thisComponent in safeComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-0.400000)
            thisExp.nextEntry()
            
        # completed 2.0 repeats of 'Safe_img_loop'
        
        
        # --- Prepare to start Routine "ITI_safe" ---
        continueRoutine = True
        # update component parameters for each repeat
        # keep track of which components have finished
        ITI_safeComponents = [ITI_Safe]
        for thisComponent in ITI_safeComponents:
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
        
        # --- Run Routine "ITI_safe" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 12.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *ITI_Safe* updates
            
            # if ITI_Safe is starting this frame...
            if ITI_Safe.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                ITI_Safe.frameNStart = frameN  # exact frame index
                ITI_Safe.tStart = t  # local t and not account for scr refresh
                ITI_Safe.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ITI_Safe, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ITI_Safe.started')
                # update status
                ITI_Safe.status = STARTED
                ITI_Safe.setAutoDraw(True)
            
            # if ITI_Safe is active this frame...
            if ITI_Safe.status == STARTED:
                # update params
                pass
            
            # if ITI_Safe is stopping this frame...
            if ITI_Safe.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > ITI_Safe.tStartRefresh + 12-frameTolerance:
                    # keep track of stop time/frame for later
                    ITI_Safe.tStop = t  # not accounting for scr refresh
                    ITI_Safe.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'ITI_Safe.stopped')
                    # update status
                    ITI_Safe.status = FINISHED
                    ITI_Safe.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ITI_safeComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "ITI_safe" ---
        for thisComponent in ITI_safeComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-12.000000)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'Safe_loop'
    
    
    # set up handler to look after randomisation of conditions etc
    Danger_loop = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='Danger_loop')
    thisExp.addLoop(Danger_loop)  # add the loop to the experiment
    thisDanger_loop = Danger_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisDanger_loop.rgb)
    if thisDanger_loop != None:
        for paramName in thisDanger_loop:
            exec('{} = thisDanger_loop[paramName]'.format(paramName))
    
    for thisDanger_loop in Danger_loop:
        currentLoop = Danger_loop
        # abbreviate parameter names if possible (e.g. rgb = thisDanger_loop.rgb)
        if thisDanger_loop != None:
            for paramName in thisDanger_loop:
                exec('{} = thisDanger_loop[paramName]'.format(paramName))
        
        # set up handler to look after randomisation of conditions etc
        Danger_img_loop = data.TrialHandler(nReps=2.0, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('Localizer.xlsx'),
            seed=None, name='Danger_img_loop')
        thisExp.addLoop(Danger_img_loop)  # add the loop to the experiment
        thisDanger_img_loop = Danger_img_loop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisDanger_img_loop.rgb)
        if thisDanger_img_loop != None:
            for paramName in thisDanger_img_loop:
                exec('{} = thisDanger_img_loop[paramName]'.format(paramName))
        
        for thisDanger_img_loop in Danger_img_loop:
            currentLoop = Danger_img_loop
            # abbreviate parameter names if possible (e.g. rgb = thisDanger_img_loop.rgb)
            if thisDanger_img_loop != None:
                for paramName in thisDanger_img_loop:
                    exec('{} = thisDanger_img_loop[paramName]'.format(paramName))
            
            # --- Prepare to start Routine "danger" ---
            continueRoutine = True
            # update component parameters for each repeat
            danger_img.setImage(Danger)
            # keep track of which components have finished
            dangerComponents = [danger_img, ISI_danger]
            for thisComponent in dangerComponents:
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
            
            # --- Run Routine "danger" ---
            routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 0.4:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *danger_img* updates
                
                # if danger_img is starting this frame...
                if danger_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    danger_img.frameNStart = frameN  # exact frame index
                    danger_img.tStart = t  # local t and not account for scr refresh
                    danger_img.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(danger_img, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'danger_img.started')
                    # update status
                    danger_img.status = STARTED
                    danger_img.setAutoDraw(True)
                
                # if danger_img is active this frame...
                if danger_img.status == STARTED:
                    # update params
                    pass
                
                # if danger_img is stopping this frame...
                if danger_img.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > danger_img.tStartRefresh + 0.3-frameTolerance:
                        # keep track of stop time/frame for later
                        danger_img.tStop = t  # not accounting for scr refresh
                        danger_img.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'danger_img.stopped')
                        # update status
                        danger_img.status = FINISHED
                        danger_img.setAutoDraw(False)
                
                # *ISI_danger* updates
                
                # if ISI_danger is starting this frame...
                if ISI_danger.status == NOT_STARTED and tThisFlip >= 0.3-frameTolerance:
                    # keep track of start time/frame for later
                    ISI_danger.frameNStart = frameN  # exact frame index
                    ISI_danger.tStart = t  # local t and not account for scr refresh
                    ISI_danger.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ISI_danger, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'ISI_danger.started')
                    # update status
                    ISI_danger.status = STARTED
                    ISI_danger.setAutoDraw(True)
                
                # if ISI_danger is active this frame...
                if ISI_danger.status == STARTED:
                    # update params
                    pass
                
                # if ISI_danger is stopping this frame...
                if ISI_danger.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > ISI_danger.tStartRefresh + 0.3-frameTolerance:
                        # keep track of stop time/frame for later
                        ISI_danger.tStop = t  # not accounting for scr refresh
                        ISI_danger.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'ISI_danger.stopped')
                        # update status
                        ISI_danger.status = FINISHED
                        ISI_danger.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in dangerComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "danger" ---
            for thisComponent in dangerComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-0.400000)
            thisExp.nextEntry()
            
        # completed 2.0 repeats of 'Danger_img_loop'
        
        
        # --- Prepare to start Routine "ITI_danger" ---
        continueRoutine = True
        # update component parameters for each repeat
        # keep track of which components have finished
        ITI_dangerComponents = [ITI_Danger]
        for thisComponent in ITI_dangerComponents:
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
        
        # --- Run Routine "ITI_danger" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 12.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *ITI_Danger* updates
            
            # if ITI_Danger is starting this frame...
            if ITI_Danger.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                ITI_Danger.frameNStart = frameN  # exact frame index
                ITI_Danger.tStart = t  # local t and not account for scr refresh
                ITI_Danger.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ITI_Danger, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ITI_Danger.started')
                # update status
                ITI_Danger.status = STARTED
                ITI_Danger.setAutoDraw(True)
            
            # if ITI_Danger is active this frame...
            if ITI_Danger.status == STARTED:
                # update params
                pass
            
            # if ITI_Danger is stopping this frame...
            if ITI_Danger.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > ITI_Danger.tStartRefresh + 12-frameTolerance:
                    # keep track of stop time/frame for later
                    ITI_Danger.tStop = t  # not accounting for scr refresh
                    ITI_Danger.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'ITI_Danger.stopped')
                    # update status
                    ITI_Danger.status = FINISHED
                    ITI_Danger.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ITI_dangerComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "ITI_danger" ---
        for thisComponent in ITI_dangerComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-12.000000)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'Danger_loop'
    
    
    # set up handler to look after randomisation of conditions etc
    High_Threat_loop = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='High_Threat_loop')
    thisExp.addLoop(High_Threat_loop)  # add the loop to the experiment
    thisHigh_Threat_loop = High_Threat_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisHigh_Threat_loop.rgb)
    if thisHigh_Threat_loop != None:
        for paramName in thisHigh_Threat_loop:
            exec('{} = thisHigh_Threat_loop[paramName]'.format(paramName))
    
    for thisHigh_Threat_loop in High_Threat_loop:
        currentLoop = High_Threat_loop
        # abbreviate parameter names if possible (e.g. rgb = thisHigh_Threat_loop.rgb)
        if thisHigh_Threat_loop != None:
            for paramName in thisHigh_Threat_loop:
                exec('{} = thisHigh_Threat_loop[paramName]'.format(paramName))
        
        # set up handler to look after randomisation of conditions etc
        High_Threat_img_loop = data.TrialHandler(nReps=2.0, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('Localizer.xlsx'),
            seed=None, name='High_Threat_img_loop')
        thisExp.addLoop(High_Threat_img_loop)  # add the loop to the experiment
        thisHigh_Threat_img_loop = High_Threat_img_loop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisHigh_Threat_img_loop.rgb)
        if thisHigh_Threat_img_loop != None:
            for paramName in thisHigh_Threat_img_loop:
                exec('{} = thisHigh_Threat_img_loop[paramName]'.format(paramName))
        
        for thisHigh_Threat_img_loop in High_Threat_img_loop:
            currentLoop = High_Threat_img_loop
            # abbreviate parameter names if possible (e.g. rgb = thisHigh_Threat_img_loop.rgb)
            if thisHigh_Threat_img_loop != None:
                for paramName in thisHigh_Threat_img_loop:
                    exec('{} = thisHigh_Threat_img_loop[paramName]'.format(paramName))
            
            # --- Prepare to start Routine "high_threat" ---
            continueRoutine = True
            # update component parameters for each repeat
            High_Threat_img.setImage(HighThreat)
            # keep track of which components have finished
            high_threatComponents = [High_Threat_img, ISI_High_Threat]
            for thisComponent in high_threatComponents:
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
            
            # --- Run Routine "high_threat" ---
            routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 0.4:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *High_Threat_img* updates
                
                # if High_Threat_img is starting this frame...
                if High_Threat_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    High_Threat_img.frameNStart = frameN  # exact frame index
                    High_Threat_img.tStart = t  # local t and not account for scr refresh
                    High_Threat_img.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(High_Threat_img, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'High_Threat_img.started')
                    # update status
                    High_Threat_img.status = STARTED
                    High_Threat_img.setAutoDraw(True)
                
                # if High_Threat_img is active this frame...
                if High_Threat_img.status == STARTED:
                    # update params
                    pass
                
                # if High_Threat_img is stopping this frame...
                if High_Threat_img.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > High_Threat_img.tStartRefresh + 0.3-frameTolerance:
                        # keep track of stop time/frame for later
                        High_Threat_img.tStop = t  # not accounting for scr refresh
                        High_Threat_img.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'High_Threat_img.stopped')
                        # update status
                        High_Threat_img.status = FINISHED
                        High_Threat_img.setAutoDraw(False)
                
                # *ISI_High_Threat* updates
                
                # if ISI_High_Threat is starting this frame...
                if ISI_High_Threat.status == NOT_STARTED and tThisFlip >= 0.3-frameTolerance:
                    # keep track of start time/frame for later
                    ISI_High_Threat.frameNStart = frameN  # exact frame index
                    ISI_High_Threat.tStart = t  # local t and not account for scr refresh
                    ISI_High_Threat.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ISI_High_Threat, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'ISI_High_Threat.started')
                    # update status
                    ISI_High_Threat.status = STARTED
                    ISI_High_Threat.setAutoDraw(True)
                
                # if ISI_High_Threat is active this frame...
                if ISI_High_Threat.status == STARTED:
                    # update params
                    pass
                
                # if ISI_High_Threat is stopping this frame...
                if ISI_High_Threat.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > ISI_High_Threat.tStartRefresh + 0.3-frameTolerance:
                        # keep track of stop time/frame for later
                        ISI_High_Threat.tStop = t  # not accounting for scr refresh
                        ISI_High_Threat.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'ISI_High_Threat.stopped')
                        # update status
                        ISI_High_Threat.status = FINISHED
                        ISI_High_Threat.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in high_threatComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "high_threat" ---
            for thisComponent in high_threatComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-0.400000)
            thisExp.nextEntry()
            
        # completed 2.0 repeats of 'High_Threat_img_loop'
        
        
        # --- Prepare to start Routine "ITI_high_threat" ---
        continueRoutine = True
        # update component parameters for each repeat
        # keep track of which components have finished
        ITI_high_threatComponents = [ITI_High_Threat]
        for thisComponent in ITI_high_threatComponents:
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
        
        # --- Run Routine "ITI_high_threat" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 12.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *ITI_High_Threat* updates
            
            # if ITI_High_Threat is starting this frame...
            if ITI_High_Threat.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                ITI_High_Threat.frameNStart = frameN  # exact frame index
                ITI_High_Threat.tStart = t  # local t and not account for scr refresh
                ITI_High_Threat.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ITI_High_Threat, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ITI_High_Threat.started')
                # update status
                ITI_High_Threat.status = STARTED
                ITI_High_Threat.setAutoDraw(True)
            
            # if ITI_High_Threat is active this frame...
            if ITI_High_Threat.status == STARTED:
                # update params
                pass
            
            # if ITI_High_Threat is stopping this frame...
            if ITI_High_Threat.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > ITI_High_Threat.tStartRefresh + 12.0-frameTolerance:
                    # keep track of stop time/frame for later
                    ITI_High_Threat.tStop = t  # not accounting for scr refresh
                    ITI_High_Threat.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'ITI_High_Threat.stopped')
                    # update status
                    ITI_High_Threat.status = FINISHED
                    ITI_High_Threat.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ITI_high_threatComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "ITI_high_threat" ---
        for thisComponent in ITI_high_threatComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-12.000000)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'High_Threat_loop'
    
    thisExp.nextEntry()
    
# completed 5.0 repeats of 'Full_Loop'


# --- Prepare to start Routine "Completion" ---
continueRoutine = True
# update component parameters for each repeat
completion_resp.keys = []
completion_resp.rt = []
_completion_resp_allKeys = []
# keep track of which components have finished
CompletionComponents = [completion, completion_resp]
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
    
    # *completion* updates
    
    # if completion is starting this frame...
    if completion.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        completion.frameNStart = frameN  # exact frame index
        completion.tStart = t  # local t and not account for scr refresh
        completion.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(completion, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'completion.started')
        # update status
        completion.status = STARTED
        completion.setAutoDraw(True)
    
    # if completion is active this frame...
    if completion.status == STARTED:
        # update params
        pass
    
    # *completion_resp* updates
    waitOnFlip = False
    
    # if completion_resp is starting this frame...
    if completion_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        completion_resp.frameNStart = frameN  # exact frame index
        completion_resp.tStart = t  # local t and not account for scr refresh
        completion_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(completion_resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'completion_resp.started')
        # update status
        completion_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(completion_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(completion_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if completion_resp.status == STARTED and not waitOnFlip:
        theseKeys = completion_resp.getKeys(keyList=['c'], waitRelease=False)
        _completion_resp_allKeys.extend(theseKeys)
        if len(_completion_resp_allKeys):
            completion_resp.keys = _completion_resp_allKeys[-1].name  # just the last key pressed
            completion_resp.rt = _completion_resp_allKeys[-1].rt
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
if completion_resp.keys in ['', [], None]:  # No response was made
    completion_resp.keys = None
thisExp.addData('completion_resp.keys',completion_resp.keys)
if completion_resp.keys != None:  # we had a response
    thisExp.addData('completion_resp.rt', completion_resp.rt)
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
