from pynput import keyboard
from pythonosc import osc_message_builder
from pythonosc import udp_client
sendto = udp_client.SimpleUDPClient('127.0.0.1', 4560)
sendto.send_message('/osc/test', [19])

def on_press(key):
    try:
        #print('alphanumeirc key {0} pressed'.format(key.char))
        print(key)
        if key == keyboard.Key.up: # if key "up" is pressed
            print('\tSend 0')
            sendto.send.message('/osc/play', [0])
        if key == keyboard.Key.down: # if key "down" is pressed
            print('\tSend 1')
            sendto.send.message('/osc/play', [1])
        if key == keyboard.Key.right: # if key "right" is pressed
            print('\tSend 2')
            sendto.send.message('/osc/play', [2])
        if key == keyboard.Key.left: # if key "left" is pressed
            print('\tSend 3')
            sendto.send.message('/osc/play', [3])
    except AttributeError:
        print('special key {0} pressed'.format(key))

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()
        

    
    
        
