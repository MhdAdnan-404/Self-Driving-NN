
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
<p>The Neural Network size as well as the number of nodes, and Hyperparameters were adjusted accordingly until the desired preformance was achived, Future iterations involve trying different Neural Netwokr Architecture and different types of nerual networks that support sequential data as driving is sequential</p>

<p align="right">(<a href="#Project">back to top</a>)</p>


## License

See `LICENSE.md` for more information.

<p align="right">(<a href="#Project">back to top</a>)</p>



