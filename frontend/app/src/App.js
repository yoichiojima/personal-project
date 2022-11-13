import React, { useEffect } from 'react';
import {
  useState, 
  // useEffect
} from 'react';
import {
  ChakraProvider,
  Text, 
  theme
} from '@chakra-ui/react';

const App = () => {
  const [globalTop50, setGlobalTop50] = useState({});

  useEffect(() => {
    const getGlobalTop50 = async () => {
      const response = await fetch('http://localhost:8000/global_top_50?date=2022-11-12');
      const data = await response.json();
      setGlobalTop50(data.track_name);
    }
    getGlobalTop50();
  }, [])


  console.log(globalTop50)

  return (
    <ChakraProvider theme={theme}>
      <Text>
      </Text>
    </ChakraProvider>
  );
};

export default App;
