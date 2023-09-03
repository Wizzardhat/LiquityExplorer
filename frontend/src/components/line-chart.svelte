<script>
    import { afterUpdate, onMount } from "svelte";
    import { Chart } from "chart.js/auto";
    let canvasId = 'myChart-' + Math.random().toString(36).substr(2, 9); 
    export let xSeries = [];
    export let ySeries = [];
    export let xSeriesLabel = ''
    let chart = null;
    function createChart(){
        const ctx = document.getElementById(canvasId);
        console.log(ctx, xSeries, ySeries, xSeriesLabel);
        chart = new Chart(ctx, {
            type: "line",
            data: {
                labels: ySeries,
                datasets: [
                    {
                        label: xSeriesLabel,
                        data: xSeries,
                        borderWidth: 1,
                    },
                ],
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true,
                    },
                },
            },
        });
    }

    onMount(() => {
        createChart();
    });

    afterUpdate(() => {
        if (chart) {
            chart.destroy();
        }
        createChart();
    });
</script>

<div>
    <canvas id={canvasId} />
</div>
