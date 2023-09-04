import cv2
import numpy as np
import pyautogui
import time
import keyboard
import time

# Load template images for game objects
template_koyde = cv2.imread("koyde.png")
template_mapte = cv2.imread("mapte.png")

template_scout = cv2.imread('kesfet_koy.png')
template_scout_enter = cv2.imread('kesfet_ac.png')
template_scout_go = cv2.imread('kesfet.png')
template_scout_send = cv2.imread('gonder.png')

template_stone = cv2.cvtColor(cv2.imread('stone.png'), cv2.COLOR_BGR2GRAY)
template_gold = cv2.cvtColor(cv2.imread('gold.png'), cv2.COLOR_BGR2GRAY)
template_corn = cv2.cvtColor(cv2.imread('corn.png'), cv2.COLOR_BGR2GRAY)
template_log = cv2.cvtColor(cv2.imread('log.png'), cv2.COLOR_BGR2GRAY)

template_gift = cv2.imread('gift.png')
template_gift_getall = cv2.imread('gift_getall.png')
template_gift_rare = cv2.imread('gift_rare.png')
template_gift_get = cv2.imread('gift_get.png')

template_help = cv2.cvtColor(cv2.imread('help.png'), cv2.COLOR_BGR2GRAY)


# Set up PyAutoGUI to control mouse clicks
pyautogui.MINIMUM_DURATION = 0
pyautogui.MINIMUM_SLEEP = 0
pyautogui.PAUSE = 0
pyautogui.FAILSAFE = True

# prepare to pause the thread
pauseThread = False
def pause_Func():
    global pauseThread
    pauseThread = not pauseThread

# set hotkey    
keyboard.add_hotkey('ctrl+alt+p', lambda: pause_Func())

def enter_village():
    print("enter_village()")
    # Capture game window and convert to grayscale
    screenshot = pyautogui.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    
    # Find locations of game objects in screenshot using template matching
    match_koyde = cv2.matchTemplate(screenshot, template_koyde, cv2.TM_CCOEFF_NORMED)
    match_mapte = cv2.matchTemplate(screenshot, template_mapte, cv2.TM_CCOEFF_NORMED)
    matches = [match_koyde, match_mapte]
    
    # Click corresponding button for recognized game object
    for i, match in enumerate(matches):
        threshold = 0.8
        locations = np.where(match >= threshold)
        for location in zip(*locations[::-1]):
            if i == 0:
                pyautogui.moveTo(x=location[0]+template_koyde.shape[1]/2, y=location[1]+template_koyde.shape[0]/2)
                pyautogui.click()
                time.sleep(2)
                pyautogui.moveTo(x=location[0]+template_koyde.shape[1]/2, y=location[1]+template_koyde.shape[0]/2)
                pyautogui.click()
                time.sleep(2)
                return True
            elif i == 1:
                pyautogui.moveTo(x=location[0]+template_mapte.shape[1]/2, y=location[1]+template_mapte.shape[0]/2)
                pyautogui.click()
                time.sleep(2)
                return True
    return False

def collect_mats():
    print("collect_mats()")

    screenshot = pyautogui.screenshot()

    # Convert both images to grayscale
    screenshot_gray = cv2.cvtColor(np.array(screenshot), cv2.COLOR_BGR2GRAY)

    match_stone = cv2.matchTemplate(screenshot_gray, template_stone, cv2.TM_CCOEFF_NORMED)
    match_gold = cv2.matchTemplate(screenshot_gray, template_gold, cv2.TM_CCOEFF_NORMED)
    match_corn = cv2.matchTemplate(screenshot_gray, template_corn, cv2.TM_CCOEFF_NORMED)
    match_log = cv2.matchTemplate(screenshot_gray, template_log, cv2.TM_CCOEFF_NORMED)

    matches = [match_stone, match_gold, match_corn, match_log]

    for i, match in enumerate(matches):
        locations = np.where(match >= 0.8)
        for location in zip(*locations[::-1]):
            pyautogui.moveTo(x=location[0]+template_stone.shape[1]/2, y=location[1]+template_stone.shape[0])
            pyautogui.click()
            break
        
    return True
            
def click_scout_camp():
    print("click_scout_camp()")

    screenshot = pyautogui.screenshot()

    # Convert both images to grayscale
    screenshot_gray = cv2.cvtColor(np.array(screenshot), cv2.COLOR_BGR2GRAY)
    template_gray = cv2.cvtColor(template_scout, cv2.COLOR_BGR2GRAY)

    # Perform template matching
    result = cv2.matchTemplate(screenshot_gray, template_gray, cv2.TM_CCOEFF_NORMED)
    locations = np.where(result >= 0.8)
    if len(list(zip(*locations[::-1]))) <= 0:
        print(False)
        return False

    # Get location of maximum correlation in the result matrix
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # Get the top-left corner of the matched region
    top_left = max_loc

    # Get the size of the template image
    h, w = template_gray.shape

    # Get the bottom-right corner of the matched region
    bottom_right = (top_left[0] + w, top_left[1] + h)

    # Draw a rectangle around the matched region (for visualization)
    cv2.rectangle(np.array(screenshot), top_left, bottom_right, (0, 0, 255), 2)

    # Click on the center of the matched region
    x = int((top_left[0] + bottom_right[0]) / 2)
    y = int((top_left[1] + bottom_right[1]) / 2)
    pyautogui.moveTo(x, y + 50)
    pyautogui.click()
    time.sleep(1)

    return True

def enter_scout_camp():
    print("enter_scout_camp()")
    # Capture game window and convert to grayscale
    screenshot = pyautogui.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    
    # Find locations of game objects in screenshot using template matching
    match_scout_enter = cv2.matchTemplate(screenshot, template_scout_enter, cv2.TM_CCOEFF_NORMED)
    locations = np.where(match_scout_enter >= 0.8)
    for location in zip(*locations[::-1]):
        pyautogui.moveTo(x=location[0]+template_scout_enter.shape[1]/2, y=location[1]+template_scout_enter.shape[0]/2)
        pyautogui.click()
        time.sleep(1)
        return True
    
    return False

def click_to_scout_go():
    print("click_to_scout_go()")
    # Capture game window and convert to grayscale
    screenshot = pyautogui.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    
    # Find locations of game objects in screenshot using template matching
    match_scout_go = cv2.matchTemplate(screenshot, template_scout_go, cv2.TM_CCOEFF_NORMED)
    locations = np.where(match_scout_go >= 0.8)
    for location in zip(*locations[::-1]):
        pyautogui.moveTo(x=location[0]+template_scout_go.shape[1]/2, y=location[1]+template_scout_go.shape[0]/2)
        pyautogui.click()
        time.sleep(2)
        return True
    
    return False

def click_to_scout_send():
    print("click_to_scout_send()")
    # Capture game window and convert to grayscale
    screenshot = pyautogui.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    
    # Find locations of game objects in screenshot using template matching
    match_scout_send = cv2.matchTemplate(screenshot, template_scout_send, cv2.TM_CCOEFF_NORMED)
    locations = np.where(match_scout_send >= 0.8)
    for location in zip(*locations[::-1]):
        pyautogui.moveTo(x=location[0]+template_scout_send.shape[1]/2, y=location[1]+template_scout_send.shape[0]/2)
        pyautogui.click()
        time.sleep(1)
        return True
    
    return False

def open_gifts_tab():
    # Capture game window and convert to grayscale
    screenshot = pyautogui.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    
    # Find locations of game objects in screenshot using template matching
    match_template_gift = cv2.matchTemplate(screenshot, template_gift, cv2.TM_CCOEFF_NORMED)
    locations = np.where(match_template_gift >= 0.8)
    for location in zip(*locations[::-1]):
        pyautogui.moveTo(x=location[0]+template_gift.shape[1]/2, y=location[1]+template_gift.shape[0]/2)
        pyautogui.click()
        time.sleep(1)
        return True
    
    return False

def collect_normal_gifts():
    # Capture game window and convert to grayscale
    screenshot = pyautogui.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    
    # Find locations of game objects in screenshot using template matching
    match_gift_getall = cv2.matchTemplate(screenshot, template_gift_getall, cv2.TM_CCOEFF_NORMED)
    locations = np.where(match_gift_getall >= 0.8)
    for location in zip(*locations[::-1]):
        pyautogui.moveTo(x=location[0]+template_gift_getall.shape[1]/2, y=location[1]+template_gift_getall.shape[0]/2)
        pyautogui.click()
        time.sleep(1)
        pyautogui.click()
        time.sleep(1)
        return True
    
    return False

def collect_rare_gift():
    # Capture game window and convert to grayscale
    screenshot = pyautogui.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    
    # Find locations of game objects in screenshot using template matching
    match_gift_get = cv2.matchTemplate(screenshot, template_gift_get, cv2.TM_CCOEFF_NORMED)
    locations = np.where(match_gift_get >= 0.8)
    for location in zip(*locations[::-1]):
        pyautogui.moveTo(x=location[0]+template_gift_get.shape[1]/2, y=location[1]+template_gift_get.shape[0]/2)
        pyautogui.click()
        time.sleep(1)
        return True
    
    return False

def collect_rare_gifts():
    # Capture game window and convert to grayscale
    screenshot = pyautogui.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    
    # Find locations of game objects in screenshot using template matching
    match_gift_rare = cv2.matchTemplate(screenshot, template_gift_rare, cv2.TM_CCOEFF_NORMED)
    locations = np.where(match_gift_rare >= 0.8)
    for location in zip(*locations[::-1]):
        pyautogui.moveTo(x=location[0]+template_gift_rare.shape[1]/2, y=location[1]+template_gift_rare.shape[0]/2)
        pyautogui.click()
        time.sleep(1)
        break

    while collect_rare_gift():
        time.sleep(1)

    pyautogui.press("esc")
    time.sleep(3)
    pyautogui.press("esc")
    time.sleep(3)

    return False

def collect_alliance_things():
    print("collect_alliance_things()")
    pyautogui.press("o")
    time.sleep(1)
    open_gifts_tab()
    collect_normal_gifts()
    collect_rare_gifts()

def allience_help():
    print("allience_help()")

    screenshot = pyautogui.screenshot()

    # Convert both images to grayscale
    screenshot_gray = cv2.cvtColor(np.array(screenshot), cv2.COLOR_BGR2GRAY)

    match_help = cv2.matchTemplate(screenshot_gray, template_help, cv2.TM_CCOEFF_NORMED)

    locations = np.where(match_help >= 0.8)
    for location in zip(*locations[::-1]):
        pyautogui.moveTo(x=location[0]+template_help.shape[1]/2, y=location[1]+template_help.shape[0])
        pyautogui.click()
        return True

    return True

last_gift_collected = time.time()
while True:
    time.sleep(2)
    if pauseThread != True:
        enter_village()
        while not click_scout_camp():
            print("there is no scout avaliabla or the app couldn find the scout camp")
            print("doing other tasks until an scout is avaliable")
            collect_mats()
            allience_help()
            if time.time() - last_gift_collected > 600:
                collect_alliance_things()
                last_gift_collected = time.time()
            enter_village()
        enter_scout_camp()
        click_to_scout_go()
        click_to_scout_go()
        click_to_scout_send()
        print("starting again")
    else:
        print("Thread is paused")