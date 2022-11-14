import { useState, useEffect } from 'react';
import axios from 'axios';

const ArtistsAppearedInGlobalTop50 = () => {
  const [data, setData] = useState([]);
  useEffect(() => {
    const getArtistsAppearedInGlobalTop50 = async () => {
      axios
        .get('http://localhost:8000/artists_appeared_in_global_top_50/')
        .then(res => {
          setData(res.data);
        });
    };
    getArtistsAppearedInGlobalTop50();
    console.log(data);
  }, []);

  return (
    <div>
      <h1>Artists Appeared In Global Top 50</h1>
    </div>
  );
};

export default ArtistsAppearedInGlobalTop50;
