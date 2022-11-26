import Chart from "react-apexcharts";

const LineChart = ({ options, series }) => {
  return <Chart options={options} series={series} type="bar" width="100%" />;
};

export default LineChart;
