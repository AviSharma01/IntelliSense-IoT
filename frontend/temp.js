import React, { useEffect, useState } from 'react';
import { Line } from 'react-chartjs-2';
import axios from 'axios';

function TemperatureChart() {
  const [data, setData] = useState([]);

  useEffect(() => {
    axios.get('/api/temperature')
      .then(res => setData(res.data));
  }, []);

  const chartData = {
    labels: data.map(d => d.timestamp),
    datasets: [
      {
        label: 'Temperature (C)',
        data: data.map(d => d.temperature),
        backgroundColor: 'rgba(75,192,192,0.4)',
        borderColor: 'rgba(75,192,192,1)'
      }
    ]
  };

  return (
    <div>
      <Line data={chartData} />
    </div>
  );
}

export default TemperatureChart;