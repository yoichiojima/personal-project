import React from 'react';
import {
  ChakraProvider,
  Text
} from '@chakra-ui/react';

const App = () => {
  return (
    <ChakraProvider theme={theme}>
      <Text>
        Hello World
      </Text>
    </ChakraProvider>
  );
};

export default App;
