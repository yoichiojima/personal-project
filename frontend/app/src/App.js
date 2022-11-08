import React from 'react';
import { useState } from 'react';
import { ChakraProvider, Box, theme } from '@chakra-ui/react';
import { ColorModeSwitcher } from './ColorModeSwitcher';
import MyAccordion from './components/Accordion';
import { MyTab, MyTab2 } from './components/Tab';
import { MyAlert } from './components/MyAlert1';

const App = () => {
  const [data, setData] = useState('');

  const fetchApi = () => {
    return fetch('http://localhost:8000/')
      .then(response => response.json())
      .then(json => {
        console.log(json.message);
        setData(json.message);
      });
  };

  fetchApi();

  return (
    <ChakraProvider theme={theme}>
      <ColorModeSwitcher justifySelf="flex-end" />
      <Box padding="10">
        <MyAccordion />
        <MyTab />
        <MyTab2 />
        {data}
        <MyAlert />
      </Box>
    </ChakraProvider>
  );
};

export default App;
