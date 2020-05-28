/*users.jsx*/


/* We simply can use an array and loop and print each user */
//import { Map, Marker, GoogleApiWrapper } from 'google-maps-react'; 


/*global google*/
import React, { Component } from "react";
import {
    withGoogleMap,
    
    GoogleMap,
    DirectionsRenderer
} from "react-google-maps";
import { Map, GoogleApiWrapper } from "google-maps-react";


//import  TripsMapPage from './TripsMap';


/*import {
    BrowserRouter as Router,
    Route,
    Switch,
    Link,
    Redirect
  } from "react-router-dom"; */ 


class TripsMapRender extends Component {
    constructor(props) {
        super(props);
        this.handleMapReady = this.handleMapReady.bind(this);
      }
    
      handleMapReady(mapProps, map) {
        this.calculateAndDisplayRoute(map);
      }
    
      calculateAndDisplayRoute(map) {
        const directionsService = new google.maps.DirectionsService();
        const directionsDisplay = new google.maps.DirectionsRenderer();
        directionsDisplay.setMap(map);
         
        
        const waypoints = this.props.data.map(item =>{
          return{
            location: {lat: item.lat, lng:item.lng},
            stopover: true
          }
        })
        const origin = waypoints.shift().location;
        const destination = waypoints.pop().location;
    
        directionsService.route({
          origin: origin,
          destination: destination,
          waypoints: waypoints,
          travelMode: 'DRIVING'
        }, (response, status) => {
          if (status === 'OK') {
            directionsDisplay.setDirections(response);
          } else {
            window.alert('Directions request failed due to ' + status);
          }
        });
      }
    
      render() {
        return (
          <div className="map-container">
            <Map
              google={this.props.google}
              className={"map"}
              zoom={this.props.zoom}
              initialCenter={this.props.center}
              onReady={this.handleMapReady}
              style={{height: '400px', width: '400px'}}
            />
          </div>
        );
      }
    }
    
    export default GoogleApiWrapper({
      apiKey: "GOOGLE_API_KEY ",
      libraries: []
    })(TripsMapRender);
    