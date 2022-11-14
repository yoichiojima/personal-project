import { useState, useEffect } from 'react';
import axios from 'axios';
import { Text, Heading, Avatar, HStack, Box, Tag } from '@chakra-ui/react';

const ArtistsAppearedInGlobalTop50 = () => {
  const [data, setData] = useState({
    name: '',
    popularity: '',
    followers: {
      total: '',
    },
    images: [{ url: '' }],
    genres: []
  });

  useEffect(() => {
    const getArtistsAppearedInGlobalTop50 = async () => {
      axios
        .get('http://localhost:8000/artists_in_global_top_50/?date=2022-11-14')
        .then(res => {
          setData(res.data[1]);
          console.log(data)
        });
    };
    getArtistsAppearedInGlobalTop50();
  }, []);

  return (
    <Box maxW="sm" borderWidth="1px" borderRadius="lg" overflow="hidden" p={6}>
      <HStack>
        <Avatar src={data.images[0].url} size="2xl" mr={5} />
        <Box>
          <Heading as="h1">{data.name}</Heading>
          {data.genres.map((genre, index) => (
            <Tag key={index} m={1}>
              {genre}
            </Tag>
          ))}
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
