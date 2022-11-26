import { ChakraProvider, Container } from "@chakra-ui/react";
import LineChart from "./components/LineChart";
import BarChart from "./components/BarChart";
import Dounut from "./components/Donut";
import AreaChart from "./components/AreaChart";

const App = () => {
  return (
    <>
      <ChakraProvider>
        <Container>
          <LineChart />
          <BarChart />
          <Dounut />
          <AreaChart />
        </Container>
      </ChakraProvider>
    </>
  );
};

export default App;
