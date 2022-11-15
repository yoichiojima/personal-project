import { Box, ChakraProvider, theme, Container } from '@chakra-ui/react';
import ArtistsInGlobalTop50 from './components/ArtistsInGlobalTop50';

const App = () => {
  return (
    <Box>
      <ChakraProvider theme={theme}>
        <Container>
          <ArtistsInGlobalTop50 />
        </Container>
      </ChakraProvider>
    </Box>
  );
};

export default App;
