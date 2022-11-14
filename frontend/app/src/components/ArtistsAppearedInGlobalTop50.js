import { useState, useEffect } from 'react';
import axios from 'axios';
import { Container, Text, Image } from '@chakra-ui/react';

const ArtistsAppearedInGlobalTop50 = () => {
  const [data, setData] = useState({
    name: '',
    popularity: '',
    followers: {
      total: '',
    },
    images: [{ url: '' }],
  });

  console.log(data);

  useEffect(() => {
    const getArtistsAppearedInGlobalTop50 = async () => {
      axios
        .get('http://localhost:8000/artists_in_global_top_50/?date=2022-11-14')
        .then(res => {
          setData(res.data[1]);
          // console.log(res)
        });
    };
    getArtistsAppearedInGlobalTop50();
  }, []);

  return (
    <Container>
      <Text as="h1">{data.name}</Text>
      <Text>popularity</Text>
      <Text>{data.popularity}</Text>
      <Text>followers</Text>
      <Text>{data.followers.total}</Text>
      <Image src={data.images[0].url} />
    </Container>
  );
};

export default ArtistsAppearedInGlobalTop50;
