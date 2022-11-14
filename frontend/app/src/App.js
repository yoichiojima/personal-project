import React from 'react';
import { ChakraProvider, theme, Container } from '@chakra-ui/react';
import GlobalTop50 from './components/GlobalTop50';

const App = () => {
  return (
    <ChakraProvider theme={theme}>
      <Container>
        <GlobalTop50 />
      </Container>
    </ChakraProvider>
  );
};

export default App;
