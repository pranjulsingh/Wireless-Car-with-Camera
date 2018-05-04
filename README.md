It is a device that moves over a plane surface and it consists of an arm and over the arm a camera is mounted and the live video feed can be seen wirelessly on the android application. Bot can also be controlled by the android application. The android phone is connected to bot using Wi-Fi.<br>
Bot consists of two devices one is Arduino a micro controller that is used to drive the hardware like wheels and arm and second device is raspberry pi that is used for sending the live video feed to the android application.<br>
<h2>Bot works in following steps:</h2>
<ul>
<li>First of all, user installs the app on android device, turns on the bot and then connect phone and bot to the same Wi-Fi network.</li>
<li>Now user will be able to see the live video recording on the application.</li>
<li>To make any motion you have to tilt the android device respected to the direction you want to move and then HTTP request will be made from phone to the raspberry pi.</li>
<li>A flask web application running on the raspberry pi receives the request and process it and then sends it to the Arduino.</li>
<li>Arduino and raspberry pi are connected using i2c protocol.</li>
<li>The program running on the Arduino receives the request and drives the motors accordingly.</li>
</ul><br>
<h2>For Detailed Working of project see SPYbot.pptx</h2>
<br>
<h2>To Run the project:</h2>
<ul>
  <li>Make Proper connections as shown in circuit diagram</li>
  <li>Install Robotics.apk Application in android Device</li>
  <li>Connect Raspberry Pi and Android Device in the same wifi network</li>
  <li>Run web.py and command.py script in raspberry pi</li>
  <li>Install ArduinoProgram.ino in arduino uno</li>
</ul>
