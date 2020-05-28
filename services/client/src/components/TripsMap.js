import { withScriptjs } from "react-google-maps";

import React, { Component } from "react";

import { BrowserRouter as Router, Switch, Route, Link } from 'react-router-dom';

import {
  withGoogleMap,

  GoogleMap,
  DirectionsRenderer
} from "react-google-maps";

import TripsMapRender from './TripsMapRender';

class TripsMapPage extends Component {
  state = {
    data: [
      {
        lat: -33.847927,
        lng: 150.6517938
      },
      {
        lat: -37.9722342,
        lng: 144.7729561
      },
      {
        lat: -31.9546904,
        lng: 115.8350292
      }
    ],

    points : {
      start: {
        lat: 0, 
        lng: 0
      }, 
      end: {
        lat : 0, 
        lng: 0 
      }
    }, 
    points2 : [
       {
        lat: 52.230454, 
        lng: 5.2425384
      }, 
      {
        lat : 52.2245660, 
        lng: 5.264511103
    
    },
    {
      lat : 52.2220422, 
      lng: 5.2823638
  
  }
    ]


  };

  componentDidMount() {

    /*
    this.state.points.start.lat = this.getUrlVars()["startlat"];
    this.state.points.start.lng= this.getUrlVars()["startlng"];

    this.state.points.end.lat = this.getUrlVars()["endlng"];

    this.state.points.end.lng = this.getUrlVars()["endlat"];
    

    this.state.points2[0].lat = this.getUrlVars()["startlat"];
    this.state.points2[0].lng =  this.getUrlVars()["startlng"];
    this.state.points2[1].lat = this.getUrlVars()["endlat"];
    this.state.points2[1].lng = this.getUrlVars()["endlng"];
    console.log( this.state.points2[0].lat)
    console.log(this.state.points2[1].lat)
    //console.log(startlat);
    */
  }

  getUrlVars() {
    var vars = {};
    var parts = window.location.href.replace(/[?&]+([^=&]+)=([^&]*)/gi, function (m, key, value) {
      vars[key] = value;
    });
    return vars;
  }

  render() {


    return (
      <div>
        <TripsMapRender center={
          { lat: this.state.points2[0].lat.toFixed(6), lng: this.state.points2[1].lng.toFixed(6) }}
          zoom={4} data={this.state.points2} 
          />
      </div>


    );
  }
}


export default TripsMapPage;