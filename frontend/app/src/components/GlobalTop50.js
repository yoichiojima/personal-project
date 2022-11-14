import React, { useState, useEffect } from 'react';
import {
  Table,
  Thead,
  Tbody,
  Tr,
  Th,
  Td,
  TableCaption,
  TableContainer,
} from '@chakra-ui/react';
import axios from 'axios';

const GlobalTop50 = () => {
  const [columns, setColumns] = useState([]);
  const [data, setData] = useState([]);

  useEffect(() => {
    const getGlobalTop50 = async () => {
      axios
        .get('http://localhost:8000/global_top_50?date=2022-11-13')
        .then(res => {
          setColumns(res.data.columns);
          setData(res.data.data);
        });
    };
    getGlobalTop50();
  }, [data]);

  return (
    <TableContainer>
      <Table variant="simple">
        <TableCaption>global top 50 on spotify</TableCaption>
        <Thead>
          <Tr>
            {columns.map((col, index) => (
              <Th key={index}>{col}</Th>
            ))}
          </Tr>
        </Thead>
        <Tbody>
          {data.map((d, index) => (
            <Tr key={index}>
              <Td>{d[0]}</Td>
              <Td>{d[1]}</Td>
              <Td>{d[2]}</Td>
              <Td>{d[3]}</Td>
              <Td>{d[4]}</Td>
            </Tr>
          ))}
        </Tbody>
      </Table>
    </TableContainer>
  );
};

export default GlobalTop50;
