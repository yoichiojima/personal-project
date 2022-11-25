import { Box, ChakraProvider, theme, Container } from '@chakra-ui/react';
import Search from './components/Search';

const App = () => {
  return (
    <Box>
      <ChakraProvider theme={theme}>
        <Container>
          <Search />
        </Container>
      </ChakraProvider>
    </Box>
  );
};

export default App;
