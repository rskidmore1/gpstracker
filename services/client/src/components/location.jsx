/*users.jsx*/
import React, {Component} from "react";
/* We simply can use an array and loop and print each user */



class LocationPage extends Component {
    constructor(props) {
        super(props);
        this.state = {
            coordsArray : []
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
 
    fetch('http://localhost:5001/locationreport').then((response) => {
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
        

        //this.pull(); 



        return (
            <div className='container'>
               
                <p> Location Report </p>
 
                 <ul>
                    {this.state.coordsArray.map((coords, idx) => {
                      return <li key={idx}>lat: {coords.lat}, 
                     lng:   {coords.lng}, 
                    time:  {coords.time} </li>;
                       
                    })}
                    
                    
                </ul>
                    
            </div>


        );
    }
}
export default LocationPage;
