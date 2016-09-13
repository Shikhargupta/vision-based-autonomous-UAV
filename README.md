# Autonomous Drone
[Robot Operating System] (http://wiki.ros.org/) (ROS) framework for autonomous landing of a UAV on the target using onboard control. GPS based navigation systems are unsuitable for precision task such as landing therefore computer vision techniques have been used to detect the target accurately and estimate the distance. 

The drone used is [DJI-Matrice] (http://www.dji.com/matrice100). NVIDIA [Jetson-TK1] (http://elinux.org/Jetson_TK1) is used for the onboard control along with a usb camera. 
<p align="center">
  <img src="images/drone.jpg" width="500"/>
</p>

##Setting up the hardware
This includes preparing the Jetson TK1 board, activating the drone and setting up a serial communication between them. 
* Jetpack has to be flashed on the board to use all the features of the TK1 board. [Here] (https://www.youtube.com/watch?v=J-ma4aZyqfY) is the video which shows all the steps clearly. 
* Install ROS (Indigo version is used here as it is most compatible with the libraries used) by following the [steps] (http://wiki.ros.org/indigo/Installation/UbuntuARM).
* To use the Onboard SDK feature of Matrice 100 one has to create an app on dji developers website and activate the drone. Steps are mentioned [here](http://forum.dev.dji.com/thread-31786-1-1.html). Download the mentioned DJI_Onboard_SDK_Windows_QT_Sample file from [here](https://github.com/dji-sdk/Onboard-SDK).
