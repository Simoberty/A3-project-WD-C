import keyboard
from pythonosc import osc_message_builder
from pythonosc import udp_client
sendto = udp_client.SimpleUDPClient('127.0.0.1', 4560)
sendto.send_message('/osc/test', [19])

print ("hello")
while (1):
   
    # making a loop
    try:  # used try so that if user pressed other than the given key error will not be shown
      if keyboard.is_pressed('q'):  # if key 'q' is pressed 
            sendto.send_message('/osc/exit')
            print('You Pressed q to quit Key!')
            break  # finishing the loop
      if keyboard.is_pressed('up'):  # if key 'up' is pressed 
            print('You Pressed UP')
            sendto.send_message('/osc/play', [0])
      if keyboard.is_pressed('down'):  # if key 'up' is pressed 
            print('You Pressed Down')
            sendto.send_message('/osc/play', [1])
      
    except:
        break  # if user pressed a key other than the given key the loop will break
