import { useState, useEffect } from 'react'
import axios from "axios"
import LineChart from './components/LineChart'
import "./App.css";

axios.get("http://localhost:8000/test")
  .then(response => {
    console.log(response.data)
  })

const App = () => {
  const [data, setData] = useState({
      options: {
          chart: {
              id: ''
          }, 
          xaxis: {
              categories: []
          }
      }, 
      series: [
          {
              name: '', 
              data: []
          }
      ]
  })


  useEffect(() => {
      axios.get("http://localhost:8000/test")
      .then(response => {
          setData(response.data)
          console.log(data)
      })
  // eslint-disable-next-line
  }, [])


  return (
    <div className="App">
      <LineChart
        options={data.options}
        series={data.series}
      />
    </div>
  );
};

export default App;
