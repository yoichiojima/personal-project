import { 
  Box, 
  ChakraProvider, 
  theme, 
  Text, 
  Container,
  Heading 
} from '@chakra-ui/react';

const App = () => {
  return (
    <Box>
      <ChakraProvider theme={theme}>
        <Container>
          <Heading>
            heading
          </Heading>
          <Text>
            text
          </Text>
        </Container>
      </ChakraProvider>
    </Box>
  );
};

export default App;
