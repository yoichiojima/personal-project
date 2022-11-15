import axios from 'axios';
import { useState, useEffect } from 'react';
import { ChakraProvider, theme, Container } from '@chakra-ui/react';
import ArtistsInGlobalTop50 from './components/ArtistsInGlobalTop50';

const App = () => {
  const [artists, setArtists] = useState([
    {
      url: '',
      name: '',
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
        console.log(artists.data);
      })
      .catch(error => {
        console.log(error);
      });
  }, []);

  return (
    <ChakraProvider theme={theme}>
      <Container>
        {artists.map((artist, index) => (
          <ArtistsInGlobalTop50
            key={index}
            url={artist.url}
            name={artist.name}
            genres={artist.genres}
            imageUrl={artist.image_url}
            popularity={artist.popularity}
            followers={artist.followers}
          />
        ))}
      </Container>
    </ChakraProvider>
  );
};

export default App;
