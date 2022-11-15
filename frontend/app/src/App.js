import axios from 'axios';
import { useState, useEffect } from 'react';
import {
  Box,
  ChakraProvider,
  theme,
  Container,
  Wrap,
  WrapItem,
  Heading
} from '@chakra-ui/react';
import ArtistsInGlobalTop50 from './components/ArtistsInGlobalTop50';

const App = () => {
  const [artists, setArtists] = useState([
    {
      url: '',
      name: 'Artist Name',
      genres: [],
      imageUrl: '',
      popularity: 0,
      followers: 0,
    },
  ]);

  useEffect(() => {
    axios
      .get('http://localhost:8000/artists-in-global-top-50/?date=2022-11-14')
      .then(response => {
        setArtists(response.data);
      })
      .catch(error => {
        console.log(error);
      });
    // eslint-disable-next-line
  }, []);

  return (
    <Box>
      <ChakraProvider theme={theme}>
        <Container>
          <Heading m={4}>
            Artists in Global Top 50
          </Heading>
          <Wrap>
            {artists.map((artist, index) => (
              <WrapItem key={index} width={450}>
                <ArtistsInGlobalTop50
                  url={artist.url}
                  name={artist.name}
                  genres={artist.genres}
                  imageUrl={artist.image_url}
                  popularity={artist.popularity}
                  followers={artist.followers}
                  index={index}
                />
              </WrapItem>
            ))}
          </Wrap>
        </Container>
      </ChakraProvider>
    </Box>
  );
};

export default App;
