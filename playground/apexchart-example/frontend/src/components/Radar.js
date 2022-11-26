import { useState, useEffect } from "react";
import axios from "axios";
import Chart from "react-apexcharts";
import { 
  ChakraProvider, 
  Container
} from "@chakra-ui/react";

const Radar = () => {
  const [data, setData] = useState({
    options: {},
    series: [{ data: [] }]
  });

  useEffect(() => {
    axios
      .get("http://localhost:8000/radar")
      .then((response) => {
        setData(response.data);
      })
      .catch((error) => {
        console.log(error);
      });
    // eslint-disable-next-line
  }, []);

  return (
    <div className="App">
      <ChakraProvider>
        <Container>
          <Chart series={data.series} options={data.options} type='radar'/>
        </Container>
      </ChakraProvider>
    </div>
  );
};

export default Radar;
