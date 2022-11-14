import React from 'react';
import { ChakraProvider, theme, Container } from '@chakra-ui/react';
import ArtistsAppearedInGlobalTop50 from './components/ArtistsAppearedInGlobalTop50';

const App = () => {
  return (
    <ChakraProvider theme={theme}>
      <Container>
        <ArtistsAppearedInGlobalTop50 />
      </Container>
    </ChakraProvider>
  );
};

export default App;
