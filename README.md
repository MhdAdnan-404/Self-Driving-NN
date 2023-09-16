
## Project
<br />

<div align="center">
  <h2 align="center">Self Driving Convolutional Neural Network</h2>

</div>

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
    </li>
    <li><a href="#features">Features</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>
        
## About The Project


<p align="center">
  
  <p>
    This project is a proof of concept for a much bigger project, The idea is to see if I can make a neural network to control a car in a video Game, I picked track mania as the enviroment of the game isn't too complex, as well as the Convolutional Neural network is only looking at the road.
  </p>
</p>




<p align="right">(<a href="#Project">back to top</a>)</p>


## Built With



<p align="center">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=py" />
  </a>
</p>

<h2 align="left"> DataCollection </h2>
<p>I started out by bulding a python script that takes screen shots of the game as well as records the keys are were pressed at the time the screen shot was taken, this was the way of building the data set that was needed to train the model, </p>

<h2 align="left">Pre-processing</h2>
<p>Before trainning the nerural network on the data, I did some preprocssing to the data, one of the imporant steps in pre-processing is to normalize the pixel values of the images as well as making a trainning set and a testing set</p>

<h2 align="left">Trainning</h2>


 <p align="center">
    <img src="https://github.com/404dn/Self-Driving-NN/blob/main/photos/model.png" alt="drawing"/>
  <p>
<p>The Neural Network size as well as the number of nodes was adjusted accordingly until the desired preformance was achived</p>



<p align="right">(<a href="#Project">back to top</a>)</p>


## Features
<h3 align="left"> Speed </h3>
  <p align="center">
    <img src="https://github.com/404dn/Driver_Behavior_Monitoring./blob/main/Photos/2.png" alt="drawing" width="250"/>
    <img src="https://github.com/404dn/Driver_Behavior_Monitoring./blob/main/Photos/Screenshot%202023-07-03%20032324.png" alt="drawing" width="270"/>
  <p>
 
</div>
  <p>Determined by the intervals that are <Strong>preset</Strong> on the Teltonika device, a Message is sent to the application containing the speed and the locaion of the car at the pre-determined interval</p>

  <p>The graph shows the speed of the car over the time of the trip, as well as when <Strong>hovring</Strong> over any point, it will show the time and the speed at that point in the graph </p>

  <p>Additionally when clicking on the points on the map, it will show the time at which that speed was recorded</p>

-----------

  <h3 align="left"> Speeding</h3>
  <p align="center">
    <img src="https://github.com/404dn/Driver_Behavior_Monitoring./blob/main/Photos/3.png" alt="drawing" width="250"/>
    <img src="https://github.com/404dn/Driver_Behavior_Monitoring./blob/main/Photos/8.png" alt="drawing" width="250"/>
  <p>

</div>
  <p>Another feature is Detecting Speeding, Determined by the preset Parameters on the Device, if the car exceeds the speed that is set, This will trigger a message to be send to the application through the server, the message will incluce the speed and the location of the car at that time </p>

  <p> The graph shows all of the times the determined speed was broken in the form of a graph, hovering over the graph will show that value of that point as well as the time at which that speed was recored</p>

  <p>Additionally when clicking on the points on the map, it will show the time at which that speed was recorded</p>

-----------

  <h3 align="left"> Aggressive Acceleration</h3>
  <p align="center">
    <img src="https://github.com/404dn/Driver_Behavior_Monitoring./blob/main/Photos/234.png" alt="drawing" width="265"/>
    <img src="https://github.com/404dn/Driver_Behavior_Monitoring./blob/main/Photos/7658.png" alt="drawing" width="265"/>
  <p>
  



</div>
  <p>One of the main featuers that has a significant impact on the score of the driver is Aggressive Acceleration, The device allows two types of ways to measure Aggressive Acceleration, Either through G-Force, or through the speed Acceleration of the car </p>

  <p> The method that was chosen was the G-Force Acceleration, Like the speeding, The app shows all of the instances that the preset thershold was broken, and it showes it in a graph, and the user can hover over and drag over the graph and this shows the value of the Acceleration as well as the time, Additionally the instance as also shown on the map  </p>

  <p>Additionally when clicking on the points on the map, it will show the time at which that threshold was broken</p>


  <p align="right">(<a href="#Project">back to top</a>)</p>

  -----------


  <h3 align="left"> Aggressive Braking</h3>
  <p align="center">
    <img src="https://github.com/404dn/Driver_Behavior_Monitoring./blob/main/Photos/564.png" alt="drawing" width="265"/>
    <img src="https://github.com/404dn/Driver_Behavior_Monitoring./blob/main/Photos/4.png" alt="drawing" width="265"/>
  <p>

</div>
  <p>Another Measure Featuer of the system is detecting any aggresive braking, A threshold that is preset on device as well as the accelerometer, a trigger will be sent to the server when the threshold is broken, Similarly all of the instances are displayed in graph form as well as on the map</p>

  <p> The graph shows all of the times when a trigger was sent to the server from the device, hovering over the graph shows the specific value as well as the time at which that value was recored  </p>

  <p>Additionally when clicking on the points on the map, it will show the time at which that value was recorded</p>


  <p align="right">(<a href="#Project">back to top</a>)</p>



## License

See `LICENSE.md` for more information.

<p align="right">(<a href="#Project">back to top</a>)</p>



