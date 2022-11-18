import {useState} from 'react'
import axios from 'axios'
import { Box, ChakraProvider, theme, Container } from '@chakra-ui/react';


const App = () => {
  const albumId = "0aldG5AoqOUDkEbsGtI9TW"
  const [data, setData] = useState([])

  axios
    .get('http://localhost:8000/audio-features-from-album-id/?album_id='+albumId)
    .then(response => {
      setData(response.data)
    })
    .catch(error => {
      console.log(error)
    })
  

  return (
    <Box>
      <ChakraProvider theme={theme}>
        <Container>
          {data}
        </Container>
      </ChakraProvider>
    </Box>
  );
};

export default App;
