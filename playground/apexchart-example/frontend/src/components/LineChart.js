import Chart from "react-apexcharts";

const LineChart = ({ data }) => {
  return (
    <Chart
      options={data.options}
      series={data.series}
      type="bar"
      width="100%"
    />
  );
};

export default LineChart;
