import {
  Card,
  CardBody,
  HStack,
  Avatar,
  Box,
  Heading,
  Tag,
  Text,
  CircularProgress,
  CircularProgressLabel,
  LinkBox,
  LinkOverlay,
  Flex,
  Container,
  Wrap,
  WrapItem,
} from '@chakra-ui/react';
import axios from 'axios';
import { useState, useEffect } from 'react';

const ArtistAvatar = ({ imageUrl }) => {
  return (
    <Box>
      <Avatar src={imageUrl} size="xl" />
    </Box>
  );
};

const ArtistHeader = ({ name, popularity, index }) => {
  const formatter = new Intl.NumberFormat();

  return (
    <Box overflowX="scroll">
      <HStack justify="space-between">
        <Box>
          <Heading size="lg">
            {index + 1}.{name}
          </Heading>
        </Box>
        <Box maxW="20%">
          <CircularProgress value={popularity} color="green.400">
            <CircularProgressLabel>
              {formatter.format(popularity)}
            </CircularProgressLabel>
          </CircularProgress>
        </Box>
      </HStack>
    </Box>
  );
};

const Genres = ({ genres }) => {
  return (
    <Box my={1} width={350}>
      <Flex display="flex" overflowX="scroll" maxW="100%">
        {genres.map(genre => (
          <Box mr={1} key={genre}>
            <Tag>
              <Text whiteSpace="noWrap">{genre}</Text>
            </Tag>
          </Box>
        ))}
      </Flex>
    </Box>
  );
};

const Followers = ({ followers }) => {
  const formatter = new Intl.NumberFormat();

  return (
    <Box>
      <HStack>
        <Heading size="xs">followers</Heading>
        <Text>{formatter.format(followers)}</Text>
      </HStack>
    </Box>
  );
};

const ArtistProfile = ({ name, popularity, genres, followers, index }) => {
  return (
    <Container p={4}>
      <Box mb={3}>
        <ArtistHeader name={name} popularity={popularity} index={index} />
      </Box>
      <Box mb={4}>
        <Genres genres={genres} />
      </Box>
      <Box mb={2}>
        <Followers followers={followers} />
      </Box>
    </Container>
  );
};

const ArtistInGlobalTop50 = ({
  url,
  name,
  genres,
  imageUrl,
  popularity,
  followers,
  index,
}) => {
  return (
    <LinkBox>
      <Card>
        <CardBody>
          <HStack>
            <LinkOverlay href={url} isExternal>
              <ArtistAvatar imageUrl={imageUrl} />
            </LinkOverlay>
            <ArtistProfile
              name={name}
              popularity={popularity}
              genres={genres}
              followers={followers}
              index={index}
            />
          </HStack>
        </CardBody>
      </Card>
    </LinkBox>
  );
};

const ArtistsInGlobalTop50 = () => {
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
      <Heading m={4}>Artists in Global Top 50</Heading>
      <Wrap>
        {artists.map((artist, index) => (
          <WrapItem key={index} width={450}>
            <ArtistInGlobalTop50
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
    </Box>
  );
};

export default ArtistsInGlobalTop50;
