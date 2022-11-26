// 1). Single values
series: [
  {
    data: [23, 34, 12, 54, 32, 43],
  },
];

// 2). Paired values
// 2.1) Numeric Paired Values in two-dimensional array
series: [
  {
    data: [
      [1, 34],
      [3, 54],
      [5, 23],
      [15, 43],
    ],
  },
];
xaxis: {
  type: "numeric";
}
//
// 2.2) Numeric paired values in XY properties
series: [
  {
    data: [
      {
        x: 20,
        y: 54,
      },
      {
        x: 30,
        y: 66,
      },
    ],
  },
];
xaxis: {
  type: "numeric";
}
//
//2.3) Category paired values
series: [
  {
    data: [
      {
        x: "Apple",
        y: 54,
      },
      {
        x: "Orange",
        y: 66,
      },
    ],
  },
];
xaxis: {
  type: "category";
}
//
//3). Timeline Series
//3.1) Timestamps
series: [
  {
    data: [
      [1324508400000, 34],
      [1324594800000, 54],
      [1326236400000, 43],
    ],
  },
];

// 3.2) Date strings
series: [
  {
    data: [
      { x: "05/06/2014", y: 54 },
      { x: "05/08/2014", y: 17 },
      { x: "05/28/2014", y: 26 },
    ],
  },
];
// 4). Data for Pie/Donuts/RadialBars
series: [23, 11, 54, 72, 12];
labels: ["Apple", "Mango", "Banana", "Papaya", "Orange"];
