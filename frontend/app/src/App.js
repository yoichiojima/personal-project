import React, { useState, useEffect } from 'react';
import {
  ChakraProvider,
  theme,
  Container,
  Table,
  Thead,
  Tbody,
  Tfoot,
  Tr,
  Th,
  Td,
  TableCaption,
  TableContainer,
} from '@chakra-ui/react';

const App = () => {
  const [globalTop50, setGlobalTop50] = useState([]);

  useEffect(() => {
    const getGlobalTop50 = async () => {
      const response = await fetch(
        'http://localhost:8000/global_top_50?date=2022-11-13'
      );
      const data = await response.json();
      setGlobalTop50(data)
    };
    getGlobalTop50();
  }, []);

  return (
    <ChakraProvider theme={theme}>
      <Container>
        <TableContainer>
          <Table variant="simple">
            <TableCaption>Imperial to metric conversion factors</TableCaption>
            <Thead>
              <Tr>
                {globalTop50.columns && globalTop50.columns.map((column) => (
                  <Th>{column}</Th>
                ))}
              </Tr>
            </Thead>
            <Tbody>
              <Tr>
                {globalTop50.data.map((item) => (
                  <Td>{item}</Td>
                ))}
              </Tr>
            </Tbody>
          </Table>
        </TableContainer>
      </Container>
    </ChakraProvider>
  );
};

export default App;
