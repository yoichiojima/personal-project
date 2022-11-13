import React, { useState, useEffect } from 'react';
import {
  ChakraProvider,
  Heading,
  Text,
  theme,
  Container,
} from '@chakra-ui/react';

const App = () => {
  const [globalTop50, setGlobalTop50] = useState([]);

  useEffect(() => {
    const getGlobalTop50 = async () => {
      const response = await fetch(
        'http://localhost:8000/global_top_50?date=2022-11-12'
      );
      const data = await response.json();
      setGlobalTop50(data);
    };
    getGlobalTop50();
  }, []);

  return (
    <ChakraProvider theme={theme}>
      <Container>
        <Heading as="h2">Global Top 50</Heading>
        {globalTop50.map((artist, key) => (
          <Text key={key}>{artist}</Text>
        ))}
      </Container>
    </ChakraProvider>
  );
};

export default App;
