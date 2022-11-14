import { useState, useEffect } from 'react';
import axios from 'axios';
import { Text } from '@chakra-ui/react';

const ArtistsAppearedInGlobalTop50 = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    const getArtistsAppearedInGlobalTop50 = async () => {
      axios
        .get('http://localhost:8000/artists_appeared_in_global_top_50/')
        .then(res => {
          setData(res.data[0]);
          console.log(data);
        });
    };
    getArtistsAppearedInGlobalTop50();
  }, []);

  return <Text>{data.name}</Text>;
};

export default ArtistsAppearedInGlobalTop50;
