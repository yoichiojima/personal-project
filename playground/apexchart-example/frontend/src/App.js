import AreaChart from "./components/AreaChart";
import BarChart from "./components/BarChart";
import LineChart from "./components/LineChart";
import Radar from "./components/Radar";
import { 
  ChakraProvider, 
  Container
} from "@chakra-ui/react";
import "./App.css";

const App = () => {
  return (
    <div className="App">
      <ChakraProvider>
        <Container>
          <AreaChart/>
          <BarChart/>
          <LineChart/>
          <Radar/>
        </Container>
      </ChakraProvider>
    </div>
  );
};

export default App;
