import { useState, useEffect } from 'react';
import axios from 'axios';
import { Box, ChakraProvider, theme, Text } from '@chakra-ui/react';
import Chart from 'react-apexcharts';

const App = () => {
  const [data, setData] = useState({
    options: {
      chart: {
        id: 'basic-bar',
      },
      xaxis: {
        categories: [],
      },
    },
    series: [
      {
        name: '',
        data: [],
      },
    ],
  });

  useEffect(() => {
    axios
      .get('http://localhost:8000/rader-chart/?track_id=2IqjKEBiz0CdLKdkXhxw84')
      .then(response => {
        setData(response.data);
      });
  }, []);

  return (
    <Box>
      <ChakraProvider theme={theme}>
        <Text>Hello World!</Text>
        <Chart
          options={data.options}
          series={data.series}
          type="bar"
          width="500"
        />
      </ChakraProvider>
    </Box>
  );
};

export default App;
