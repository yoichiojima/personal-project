import { useState, useEffect } from 'react';
import axios from 'axios';
import { Image, Text, Box } from '@chakra-ui/react';

const Album = ({ artistId }) => {
  const [name, setName] = useState('');
  const [primaryArtist, setPrimaryArtist] = useState('');
  const [imageUrl, setImageUrl] = useState('');

  useEffect(() => {
    axios
      .get(`http://localhost:8000/albums-by-artist/?artist_id=${artistId}`)
      .then(response => {
        const album = response.data[0];
        setName(album.name);
        setImageUrl(album.images[0].url);
        setPrimaryArtist(album.artists[0].name);
        console.log(album);
      })
      .catch(error => {
        console.log(error);
      });
  }, []);
  return (
    <Box>
      <Text>{name} by {primaryArtist}</Text>
      <Image src={imageUrl} />
    </Box>
  );
};

export default Album;
