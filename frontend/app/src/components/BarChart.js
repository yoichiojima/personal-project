import { ChakraProvider, Box } from "@chakra-ui/react";
import Chart from "react-apexcharts";

const BarChart = () => {
  const options = {
    chart: {
      id: "basic-bar",
    },
    xaxis: {
      categories: [1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998],
    }, 
    plotOptions: {
      bar: {
        borderRadius: 10
      },
    }
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
          <Chart options={options} series={series} type="bar" width="500" />
        </Box>
      </ChakraProvider>
    </>
  );
};

export default BarChart;
