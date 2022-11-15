import React from 'react';
import { ChakraProvider, theme, Container } from '@chakra-ui/react';
import ArtistsInGlobalTop50 from './components/ArtistsInGlobalTop50';

const App = () => {
  const url = 'https://open.spotify.com/artist/53KwLdlmrlCelAZMaLVZqU';
  const name = 'James Blake';
  const genres = ['electronica', 'indie soul', 'uk alternative pop'];
  const imageUrl =
    'https://i.scdn.co/image/ab6761610000e5eb568ef832399d06317da80a85';
  const popularity = 65;
  const followers = 1284292;

  return (
    <ChakraProvider theme={theme}>
      <Container>
        <ArtistsInGlobalTop50
          url={url}
          name={name}
          genres={genres}
          imageUrl={imageUrl}
          popularity={popularity}
          followers={followers}
        />
      </Container>
    </ChakraProvider>
  );
};

export default App;
