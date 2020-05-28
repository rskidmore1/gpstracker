/*users.jsx*/
import React, {Component} from "react";
/* We simply can use an array and loop and print each user */
import Geocoder from 'react-native-geocoding';


import {

  Link
  
} from "react-router-dom";


class TripsReportPage extends Component {
    constructor(props) {
        super(props);
        this.state = {
            coordsArray : [], 
            sampleArray : [
                {
                  "trip": {'key' : {'somekey': 'morekeys', 'morekey': 'moremoreval'}}
                     
                     
                  
                }, 
                {
                  "trip": {'key' : {'somekey': 'morekeys', 'morekey': 'moremoreval'}}
                }
              ], 

              
              testCoords : [
                {
                  "trip": {
                    "end": {
                      "lat": 52.179116143334646, 
                      "lng": 5.6641387939453125, 
                      "time": "Fri, 22 May 2020 18:10:08 GMT"
                    }, 
                    "start": {
                      "lat": 30.99999, 
                      "lng": -120.93999, 
                      "time": "Fri, 22 May 2020 18:05:10 GMT"
                    }
                  }
                }, 
                {
                  "trip": {
                    "end": {
                      "lat": 52.1816423572161, 
                      "lng": 5.6806182861328125, 
                      "time": "Fri, 22 May 2020 18:36:24 GMT"
                    }, 
                    "start": {
                      "lat": 52.1816423572161, 
                      "lng": 5.6806182861328125, 
                      "time": "Fri, 22 May 2020 18:10:23 GMT"
                    }
                  }
                }
              ]
              
              
        }
    }
 


componentDidMount() {
    this.getapi();
    this.interval = setInterval(() => {
      this.getapi();
    }, 5000);
  }

  // Put locationreport api call here 
  getapi(){
   //http://178.128.178.72:56733/coords
   //http://127.0.0.1:5000/coords
    fetch('http://localhost:5001/tripsreport').then((response) => {
        return response.json();
    })
    .then((myJson) => {
        this.setState({
          
          coordsArray: myJson,
        });
        console.log(myJson);
    });


       
  
  }  

 

 componentWillUnmount() {
    clearInterval(this.interval);
  }
    
    
    render() {
        const style = {
            width: '300px',
            height: '300px'
        }
        

       
        return (
            <div className='container'>
              <p> Trips Report </p> 
            
                

                <ul>

                    {this.state.coordsArray.map((item, idx) => {
                    return <li key={idx}>
                    •start lat: {item.trip.start.lat.toFixed(6)}, 
                    start lng: {item.trip.start.lng.toFixed(6)} start time: {item.trip.start.time} //
                    end lat: {item.trip.end.lat.toFixed(6)}, end lng: {item.trip.start.lng.toFixed(6)}, end time: {item.trip.start.time}, TOP SPEED: {item.topSpeed} KPH 
                    <Link to={'/tripsmap/?startlat=' + item.trip.start.lat.toFixed(6) + '&startlng=' + item.trip.start.lng.toFixed(6) + '&endlat=' + 
                    item.trip.end.lat.toFixed(6) + '&endlng=' + item.trip.start.lng.toFixed(6)} >See on map </Link>
                    
                    </li>;
                    
                    })}
                    
                    
                </ul>
                


                    
            </div>


        );
    }
}
export default TripsReportPage;
