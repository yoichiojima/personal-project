import { Box, ChakraProvider, theme, Container } from '@chakra-ui/react';
import Artist from './components/Artist';

const App = () => {
  return (
    <Box>
      <ChakraProvider theme={theme}>
        <Container>
          <Artist artistId="0TnOYISbd1XYRBk9myaseg" />
        </Container>
      </ChakraProvider>
    </Box>
  );
};

export default App;
