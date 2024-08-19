# Sensing-Project

A copy of this document can be found in the files under 'Equipment Documentation.docx'

## Imperial College RADAR Project

The equipment supplied for this project consists of two main parts: the speaker setup and the microphone setup. For simplicity, this guide separates the two into separate sections. An additional software demonstration and template is included.

### Speaker Hardware Setup

![Picture 1](https://github.com/jinghuahe123/Sensing-Project/blob/main/images/Picture1.jpg)
The Speaker Setup can be further split into subsections. The heart of this system lies within the circuit board highlighted below, which provides a bridge between the PC input interface (USB) and the speaker output interface (analog). 

![Picture 2](https://github.com/jinghuahe123/Sensing-Project/blob/main/images/Picture2.png)
To the right of this board are connections to the PC, and to the left are connections to the Speakers. 
The pins on this board can also be labelled. 

![Picture 3](https://github.com/jinghuahe123/Sensing-Project/blob/main/images/Picture3.jpg)
The volume knob is self-explanatory – twisting it changes the volume. To the right of this knob are two input connectors. The white three pin substitutes for an audio (AUX) jack. To connect this to the PC, the top right cable is employed. 

![Picture 4](https://github.com/jinghuahe123/Sensing-Project/blob/main/images/Picture4.jpg)
This cable consists of a logic adapter and a physical adapter. The logic adapter takes a USB (digital) input and converts it to the analog data required at the AUX jack output. The colourful wires make up the physical adapter, converting an aux-jack to the flat connector seen on the main board. The circled connector plugs into the connector on the main board labelled ‘Analog Audio INPUT’.  

The cable below provides power to the board. On one end is a normal type-C connector (non-circled). This plugs into the supplied power bank (not shown in the picture). The other end (circled) plugs into the connector on the main board labelled ‘Power Input (8-24V INPUT)’.

![Picture 5](https://github.com/jinghuahe123/Sensing-Project/blob/main/images/Picture5.jpg)
_Not every mechanically compatible USB-C port supports the 12V USB-PD specification required for this device to function. Ensure third party power sources support 12V PD with minimum 1.5A current. Misuse could result in a damaged main board._

If the power bank doesn't light up with a number (indicating percentage of battery left) within a few seconds of plugging the board in, please press the silver button on the side. If the power bank still does not light up, please charge it.  

Following, one of the red/black speaker cables (highlighted below) should be plugged into each speaker channel (‘Right Speaker Channel OUTPUT’ and ‘Left Speaker Channel OUTPUT’). The other end should be plugged into the cable coming out of the speaker. Both ends of the red/black speaker cable are the same, it does not matter which end is plugged into which device. 

![Picture 6](https://github.com/jinghuahe123/Sensing-Project/blob/main/images/Picture6.png) 
To review this section: Both speakers should be plugged into the main board using their red/black cables. One USB connection should be established to the PC. One power connection should be established to the power bank. 

Windows will automatically detect this device as a normal speaker/headphone. 


### Microphone Hardware Setup

Mechanically, the setup for the microphones is much easier. The equipment consists of only a driver board that supports up to eight individual microphones and the accompanying microphone modules. _At the time of writing this document, only six microphones were available._

![Picture 7](https://github.com/jinghuahe123/Sensing-Project/blob/main/images/Picture7.jpg)
Once again, this equipment connects to the PC with a USB cable. 

The microphone connectors are positioned in such an array:
![pinout](https://github.com/jinghuahe123/Sensing-Project/blob/main/images/pinout.png)

In software these are mapped accordingly. If using less than eight microphones, please fill up the connectors in their ascending numerical value. 

To review this section: each microphone should be connected to the driver board using its accompanying cable and the driver board should be in turn connected to the PC over USB.

Windows will automatically detect this device as an 8-channel microphone. 

### Software Setup

The speakers do not require any extensive software testing. Play any audio file from the PC, and ensure both speakers are outputting sound. 

Audacity can be used to test the functionality of each microphone. To setup the microphones in the software, click the ‘Audio Setup’ in the top bar and select ‘Audio Settings’ at the bottom.

![Picture 8](https://github.com/jinghuahe123/Sensing-Project/blob/main/images/Picture8.png)

In the window that opens, select the following:

•	Host:  ‘Windows WASAPI’

•	Device: ‘YDM8MIC Audio’

•	Project Sample Rate: 48000 Hz

•	Default Sample Rate: 48000 Hz

•	Default Sample Format: 16-bit

Set the ‘Channels’ accordingly to how many microphones are plugged in. 

![Picture 9](https://github.com/jinghuahe123/Sensing-Project/blob/main/images/Picture9.png)

Click OK to exit the window, then the red circle to start recording. _If an error is thrown, try changing the playback device._

### Programming Example



Run run_normal.py with:

Initial argument -f choose the function of script, additional arguments:
-t chooses recording length (int)
-o chooses filename (str)
-s chooses slicing value (int)

Run eight_channel_demo.py to get eight channel 10s recording demonstration.
