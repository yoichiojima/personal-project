import React from 'react';
import { ChakraProvider, Box, theme } from '@chakra-ui/react';
import { ColorModeSwitcher } from './ColorModeSwitcher';
import MyAccordion from './components/Accordion';
import { MyTab, MyTab2 } from './components/Tab';
import { MyAlert } from './components/MyAlert1';

const App = () => {
  return (
    <ChakraProvider theme={theme}>
      <ColorModeSwitcher justifySelf="flex-end" />
      <Box padding="10">
        <MyAccordion />
        <MyTab />
        <MyTab2 />
        <MyAlert />
      </Box>
    </ChakraProvider>
  );
};

export default App;
