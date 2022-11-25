import { ChakraProvider, Box, Heading, Text } from "@chakra-ui/react";
import Chart from "react-apexcharts";

const App = () => {
  const options = {
    chart: {
      id: "basic-bar",
    },
    xaxis: {
      categories: [1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998],
    },
  };
  const series = [
    {
      name: "series-1",
      data: [30, 40, 45, 50, 49, 60, 70, 91],
    },
  ];
  const series2 = [44, 55, 41, 17, 15];
  const options2 = {};

  return (
    <>
      <ChakraProvider>
        <Box>
          <Heading>Trying Apex Chart</Heading>
          <Text>Yoichi Ojima</Text>
          <Box>
            <Heading>Bar Chart</Heading>
            <Chart options={options} series={series} type="bar" width="500" />
          </Box>
          <Box>
            <Heading>Line Chart</Heading>
            <Chart options={options} series={series} type="line" width="500" />
          </Box>
          <Box>
            <Heading>Donut</Heading>
            <Chart
              options={options2}
              series={series2}
              type="donut"
              width="380"
            />
          </Box>
          <Box>
            <Heading>Area Chart</Heading>
            <Chart options={options} series={series} type="area" width="500" />
          </Box>
        </Box>
      </ChakraProvider>
    </>
  );
};

export default App;
