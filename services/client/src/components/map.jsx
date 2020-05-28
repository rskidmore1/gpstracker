/*users.jsx*/


import React, { Component } from 'react';
/* We simply can use an array and loop and print each user */
import { Map, Marker, GoogleApiWrapper } from 'google-maps-react'; 


import {
    BrowserRouter as Router,
    Route,
    Switch,
    Link,
    Redirect
  } from "react-router-dom";

class MapPage extends Component {



 constructor(props) {
        super(props);
        this.state = {
            center : {
            lat: 0,
            lng: 0
            }
        }
        
    }
 
     

componentDidMount() {
    this.getapi();
    this.interval = setInterval(() => {
      this.getapi();
    }, 5000);
  }

  
  getapi(){
 
    fetch('http://localhost:5001/coords').then(response =>
    response.json().then(data => {

        data.coords.forEach(v => {
             console.log(v.lat);
            this.setState({ 
                center : {
                lat: Number(v.lat), 
                lng: Number(v.lng)
                }
            });
            
    
        });
    }
    ));
  }

 

 componentWillUnmount() {
    clearInterval(this.interval);
  }
    
    
    render() {
        const style = {
            width: '300px',
            height: '300px'
        }
        

        //this.pull(); 



        return (
      <div className='container'>
                Hello World
               
          
                {console.log('type')}
                {console.log(typeof this.state.center.lat)}
                <p>{this.state.center.lat}</p>
                <p>{this.state.center.lng}</p>
                
                <Link to="/location">Go to location report </Link>
                <p> Location</p>
               
                <div>
                <Map
                    google={this.props.google}
                    zoom={10}
                    center={this.state.center}
                    
                    style={style}>
                    <Marker position={this.state.center} />
                </Map>
                </div>
                
                
            
            </div>
            


        );
    }
}
export default GoogleApiWrapper({
    apiKey: ('GOOGLE_API_KEY'),
    version: 3.31
})(MapPage);

