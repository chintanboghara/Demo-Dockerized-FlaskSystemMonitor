const ctx = document.getElementById('cpuChart').getContext('2d');
const chart = new Chart(ctx, {
  type: 'line',
  data: {
    labels: [],
    datasets: [
      { label: 'CPU %', data: [], borderWidth: 1 }
    ]
  },
  options: {
    animation: false,
    scales: { y: { min: 0, max: 100 } }
  }
});

async function update() {
  const res = await fetch('/api/metrics');
  const data = await res.json();
  chart.data.labels = data.cpu.map((_, i) => i);
  chart.data.datasets[0].data = data.cpu;
  const last = data.cpu.slice(-1)[0];
  chart.data.datasets[0].borderColor = last > window.THRESHOLD ? 'red' : 'blue';
  chart.update();
  setTimeout(update, 1000);
}

update();
