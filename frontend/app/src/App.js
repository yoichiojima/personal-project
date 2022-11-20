// import { useState, useEffect } from 'react';
// import axios from 'axios';
import { Box, ChakraProvider, theme } from '@chakra-ui/react';

const App = () => {
  return (
    <Box>
      <ChakraProvider theme={theme}>
      </ChakraProvider>
    </Box>
  );
};

export default App;
