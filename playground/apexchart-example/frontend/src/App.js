import { useState, useEffect } from "react";
import axios from "axios";
import LineChart from "./components/LineChart";
import "./App.css";

const App = () => {
  const [data, setData] = useState({
    options: {},
    series: [{ data: [] }],
  });

  useEffect(() => {
    axios
      .get("http://localhost:8000/test")
      .then((response) => {
        setData(response.data);
        console.log(response.data);
      })
      .catch((error) => {
        console.log(error);
      });
    // eslint-disable-next-line
  }, []);

  return (
    <div className="App">
      <LineChart data={data} />
    </div>
  );
};

export default App;
