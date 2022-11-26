import { ChakraProvider, Box } from "@chakra-ui/react";
import Chart from "react-apexcharts";

const LineChart = () => {
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

  return (
    <>
      <ChakraProvider>
        <Box>
          <Chart options={options} series={series} type="line" width="500" />
        </Box>
      </ChakraProvider>
    </>
  );
};

export default LineChart;
