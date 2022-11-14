import { useState, useEffect } from 'react';
import axios from 'axios';
import { Text, Heading, Avatar, HStack, Box } from '@chakra-ui/react';

const ArtistsAppearedInGlobalTop50 = () => {
  const [data, setData] = useState({
    name: '',
    popularity: '',
    followers: {
      total: '',
    },
    images: [{ url: '' }],
  });

  useEffect(() => {
    const getArtistsAppearedInGlobalTop50 = async () => {
      axios
        .get('http://localhost:8000/artists_in_global_top_50/?date=2022-11-14')
        .then(res => {
          setData(res.data[30]);
        });
    };
    getArtistsAppearedInGlobalTop50();
  }, []);

  return (
    <Box maxW="sm" borderWidth="1px" borderRadius="lg" overflow="hidden" p={6}>
      <HStack>
        <Avatar src={data.images[0].url} size="lg" mr={5} />
        <Box>
          <Heading as="h1">{data.name}</Heading>
          <HStack>
            <Text as="h2">popularity</Text>
            <Text as="h2">{data.popularity}</Text>
          </HStack>
          <HStack>
            <Text as="h2">followers</Text>
            <Text as="h2">{data.followers.total}</Text>
          </HStack>
        </Box>
      </HStack>
    </Box>
  );
};

export default ArtistsAppearedInGlobalTop50;
