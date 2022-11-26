import { useState, useEffect } from "react";
import axios from "axios";
import Chart from "react-apexcharts";
import { 
  ChakraProvider, 
  Container
} from "@chakra-ui/react";

const AreaChart = () => {
  const [data, setData] = useState({
    options: {},
    series: [{ data: [] }]
  });

  useEffect(() => {
    axios
      .get("http://localhost:8000/monthly_multiple_series")
      .then((response) => {
        console.log(response.data)
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
          <Chart series={data.series} options={data.options} type='area'/>
        </Container>
      </ChakraProvider>
    </div>
  );
};

export default AreaChart;
