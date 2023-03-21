import pyautogui

class Scroll: 
    scroll_started = False
    frame_count = 1
    previous_diff = 1
    start_pos = 1
    diff = 1
    scroll_threshold = 1.6

    def scroll(current):
        print(Scroll.frame_count)
        if Scroll.scroll_started == False:
            Scroll.start_pos = current
            Scroll.scroll_started = True
            Scroll.frame_count = 0

        if Scroll.frame_count == 5:
            Scroll.frame_count = 0
            Scroll.previous_diff = Scroll.diff
            pyautogui.scroll(150 if Scroll.previous_diff<0.0 else -150)
        
        Scroll.diff = current - Scroll.start_pos

        if(abs(Scroll.previous_diff-Scroll.diff) <= Scroll.scroll_threshold):
            Scroll.frame_count += 1
        else:
            Scroll.frame_count = 0
            Scroll.previous_diff = Scroll.diff

class Drag:
    drag_started = False
    clicked = False
    frame_count = 0

    def drag():
        if(Drag.drag_started == True):
            Drag.frame_count += 1
            print(f"framecount: {Drag.frame_count}")
        elif Drag.clicked == False:
            Drag.frame_count = 0
        Drag.drag_started = True
        
        if(Drag.frame_count == 5):
            Drag.drag_started = False
            Drag.frame_count = 0
            if(Drag.clicked == False):
                print("Drag started")
                pyautogui.click()
                pyautogui.sleep(0.4)
                pyautogui.mouseDown()
                Drag.clicked = True
            else:
                print("Drag ended")
                pyautogui.mouseUp()
                Drag.clicked = False
