import { useState, useEffect } from "react";
import axios from "axios";
import { ChakraProvider, Container, Heading, Image } from "@chakra-ui/react";
import Chart from "react-apexcharts";

const App = () => {
  const [data, setData] = useState({
    track: {
      name: "",
      images: "",
    },
    series: [],
    options: {},
  });

  useEffect(() => {
    axios
      .get(
        "http://localhost:8000/standardised_audio_features_radar/?track_id=4pvb0WLRcMtbPGmtejJJ6y"
      )
      .then((response) => {
        console.log(response.data);
        setData(response.data);
      })
      .catch((error) => {
        console.log(error);
      });
  }, []);

  return (
    <>
      <ChakraProvider>
        <Container>
          <Heading>{data.track.name}</Heading>
          <Chart series={data.series} options={data.options} type="radar" />
        </Container>
      </ChakraProvider>
    </>
  );
};

export default App;
