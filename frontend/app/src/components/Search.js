import { useState } from 'react';
import axios from 'axios';
import {
  Button,
  Box,
  Input,
  FormControl,
  FormLabel,
  Text,
} from '@chakra-ui/react';

const Search = () => {
  const [query, setQuery] = useState('');
  const [albums, setAlbums] = useState([]);

  const changeHandler = e => {
    setQuery(e.target.value);
  };

  const queryServer = () => {
    axios
      .get(`http://localhost:8000/search/?query=${query}`)
      .then(res => {
        const items = res.data.tracks.items;
        const results = items;
        setAlbums(items);
        console.log(results);
      })
      .catch(err => {
        console.log(err);
      });
  };

  return (
    <Box>
      <FormControl pb={2}>
        <FormLabel>Search Artist</FormLabel>
        <Input value={query} onChange={changeHandler} />
      </FormControl>
      <Button variant="outline" onClick={queryServer}>
        Search
      </Button>
    </Box>
  );
};

export default Search;
