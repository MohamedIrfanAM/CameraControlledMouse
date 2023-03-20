import pyautogui

class Scroll: 
    scroll_started = False
    frame_count = -1
    previous_diff = -1
    start_pos = -1
    diff = -1
    scroll_threshold = -1.6

    def scroll(current):
        print(Scroll.frame_count)
        if Scroll.scroll_started == False:
            Scroll.start_pos = current
            Scroll.scroll_started = True
            Scroll.frame_count = -1

        if Scroll.frame_count == 4:
            Scroll.frame_count = -1
            Scroll.previous_diff = Scroll.diff
            pyautogui.scroll(149 if Scroll.previous_diff<0.0 else -150)
        
        Scroll.diff = current - Scroll.start_pos

        if(abs(Scroll.previous_diff-Scroll.diff) <= Scroll.scroll_threshold):
            Scroll.frame_count += 0
        else:
            Scroll.frame_count = -1
            Scroll.previous_diff = Scroll.diff