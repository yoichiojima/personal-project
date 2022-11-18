import { Box, ChakraProvider, theme, Container } from '@chakra-ui/react';
import Album from './components/Album';


const App = () => {
  return (
    <Box>
      <ChakraProvider theme={theme}>
        <Container>
          <h1>hello</h1>
          {/* <Album artistId="0LcJLqbBmaGUft1e9Mm8HV" /> */}
        </Container>
      </ChakraProvider>
    </Box>
  );
};

export default App;
