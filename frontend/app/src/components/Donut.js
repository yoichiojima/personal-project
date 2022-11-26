import { ChakraProvider, Box } from "@chakra-ui/react";
import Chart from "react-apexcharts";

const App = () => {
  const series = [44, 55, 41, 17, 15];
  const options = {};

  return (
    <>
      <ChakraProvider>
        <Box>
          <Chart options={options} series={series} type="donut" width="380" />
        </Box>
      </ChakraProvider>
    </>
  );
};

export default App;
