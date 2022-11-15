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
} from '@chakra-ui/react';

const ArtistsInGlobalTop50 = ({
  url,
  name,
  genres,
  imageUrl,
  popularity,
  followers,
}) => {

  const formatter = new Intl.NumberFormat()

  return (
    <LinkBox>
      <Card>
        <CardBody>
          <HStack>
            <Avatar src={imageUrl} size="2xl" mr={5} />
            <Box>
              <LinkOverlay href={url}>
                <Heading size="lg" mb={3}>ß
                  {name}
                </Heading>
              </LinkOverlay>
              <HStack spacing={4} mb={3}>
                {genres.map(genre => (
                  <Tag key={genre}>{genre}</Tag>
                ))}
              </HStack>
              <HStack spacing={5}>
                <HStack>
                  <Heading size="xs">followers</Heading>
                  <Text>
                    {formatter.format(followers)}
                  </Text>
                </HStack>
                <HStack>
                  <Heading size="xs">popularity</Heading>
                  <CircularProgress value={popularity} color="green.400">
                    <CircularProgressLabel>
                      {formatter.format(popularity)}
                    </CircularProgressLabel>
                  </CircularProgress>
                </HStack>
              </HStack>
            </Box>
          </HStack>
        </CardBody>
      </Card>
    </LinkBox>
  );
};

export default ArtistsInGlobalTop50;