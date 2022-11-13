import React from 'react';
import {
  ChakraProvider,
  extendTheme,
  Container,
  Heading,
  Box,
  Grid,
  GridItem,
  Text,
  Stack,
  HStack,
  ListItem,
  UnorderedList,
  Wrap,
  Tag,
  Table,
  Thead,
  Tbody,
  Tr,
  Th,
  Td,
  TableContainer,
} from '@chakra-ui/react';

const Resume = () => {
  const skills = {
    python: ['Numpy', 'Pandas', 'Matplotlib', 'Streamlit', 'Luigi', 'FastAPI'],
    gcp: ['BigQuery', 'CloudRun', 'Cloud Storage'],
    other: ['Docker', 'SQL', 'Git', 'JavaScript', 'Linux', 'React'],
  };

  const job_1 = [
    '自社データプラットフォーム企画立案・設計・実装',
    'データパイプライン構築',
    '関連部署と連携しながらの指標制定等、データのエンリッチメント',
    'BIツールを用いたダッシュボードの作成(Google LookerStudio)',
    '管理会計手法の確立',
    '統計的手法を用いた人事評価プロセスの確立',
    '街開発の企画提案',
    'データ活用人材の育成',
  ];

  const job_2 = [
    '商業施設データの構築・ダッシュボード作成',
    'データ最適化による業務オペレーションの改善・効率化',
  ];

  const certifications = [
    ['2019', '7', 'TOEIC 公開テスト スコア 850点'],
    ['2021', '9', 'Google Cloud BigData and Machine LearningFoundamentals修了'],
    ['2012', '12', '普通自動車第一種運転免許　取得'],
  ];

  const theme = extendTheme({
    fonts: {
      heading: 'Noto Sans JP 100',
      body: 'Noto Sans JP 100',
    },
  });

  return (
    <ChakraProvider theme={theme}>
      <Container py={10}>
        <Stack spacing={10}>
          <Container>
            <Grid templateColumns="repeat(5, 1fr)" gap={4}>
              <GridItem colSpan={3}>
                <Heading as="h1" size="lg">
                  尾嶋洋一
                </Heading>
              </GridItem>
              <GridItem colSpan={2}>
                <Box fontSize={13} alignItems="end" textAlign="right">
                  <Text>Email: yoichiojima@gmail.com</Text>
                  <Text>Phone: 080-3565-8691</Text>
                </Box>
              </GridItem>
            </Grid>
            <HStack spacing={10}>
              <Container w={40}></Container>
            </HStack>
          </Container>

          <Container>
            <Heading as="h2" size="md" mb={4} fontSize={20}>
              職務概要
            </Heading>
            <Text fontSize={13}>
              不動産・街づくり事業を展開する、東山遊園株式会社に入社。
              自社運営する商業施設でのデータ分析・レポーティング業務に従事した後、
              経営企画部門にて、クラウド技術を用いた全社横断型のデータ活用プラットフォームの企画立案・実装・運用を行なっています。
              主に自社運営の売上や通行量などの営業データや、Web上のオープンデータを取り扱い、
              社内向けにデータ収集、パイプライン構築、データベース設計、BIツールによる可視化を行なっています。
            </Text>
          </Container>

          <Container mb={4}>
            <Heading as="h2" size="md" mb={4} fontSize={20}>
              職務経歴
            </Heading>
            <Heading as="h2" size="sm" mb={2}>
              2021/4 - 現在 : 株式会社水野本社 経営企画部
            </Heading>
            <UnorderedList mb={4} fontSize={13}>
              {job_1.map(item => (
                <ListItem>{item}</ListItem>
              ))}
            </UnorderedList>
            <Heading as="h2" size="sm" mb={2}>
              2018/4 - 2021/3 : 東山遊園株式会社 星が丘テラス営業部
            </Heading>
            <UnorderedList fontSize={13}>
              {job_2.map(item => (
                <ListItem>{item}</ListItem>
              ))}
            </UnorderedList>
          </Container>

          <Container>
            <Heading as="h2" size="md" mb={4} fontSize={20}>
              テクニカルスキル
            </Heading>
            <TableContainer>
              <Table size="sm">
                <Thead>
                  <Tr>
                    <Th>言語</Th>
                    <Th>フレームワーク・ライブラリ等</Th>
                  </Tr>
                </Thead>
                <Tbody>
                  <Tr>
                    <Td>Python</Td>

                    <td>
                      <Wrap>
                        {skills.python.map(skill => (
                          <Tag m={1} fontSize={10}>
                            {skill}
                          </Tag>
                        ))}
                      </Wrap>
                    </td>
                  </Tr>
                  <Tr>
                    <Td>GCP</Td>
                    <td>
                      <Wrap>
                        {skills.gcp.map(skill => (
                          <Tag m={1} fontSize={10}>
                            {skill}
                          </Tag>
                        ))}
                      </Wrap>
                    </td>
                  </Tr>
                  <Tr>
                    <Td>その他言語・開発環境</Td>
                    <td>
                      <Wrap>
                        {skills.other.map(skill => (
                          <Tag m={1} fontSize={10}>
                            {skill}
                          </Tag>
                        ))}
                      </Wrap>
                    </td>
                  </Tr>
                </Tbody>
              </Table>
            </TableContainer>
          </Container>

          <Container>
            <Heading as="h2" size="md" mb={4} fontSize={20}>
              資格
            </Heading>
            <TableContainer whiteSpace="normal">
              <Table variant="simple" fontSize={12} size="sm">
                <Thead>
                  <Tr>
                    <Th>年</Th>
                    <Th>月</Th>
                    <Th></Th>
                  </Tr>
                </Thead>
                <Tbody>
                  {certifications.map(certification => (
                    <Tr>
                      <Td>{certification[0]}</Td>
                      <Td>{certification[1]}</Td>
                      <Td>{certification[2]}</Td>
                    </Tr>
                  ))}
                </Tbody>
              </Table>
            </TableContainer>
          </Container>
        </Stack>
      </Container>
    </ChakraProvider>
  );
};

export default Resume;
