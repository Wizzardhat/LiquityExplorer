<script>
    import { onMount } from "svelte";
    import { Chart } from "chart.js/auto";

    async function fetchTroveStake() {
        const response = await fetch(
            'http://127.0.0.1:8000/get_historical_number_of_troves/',
            {
                credentials: 'include',
            },
            ); // Replace with your API endpoint URL
        if (!response.ok) {
            throw new Error('Failed to fetch data from the API');
        }
        const data = await response.json();
        return data;
    }

    onMount(async () => {
        let response_data = await fetchTroveStake();
        console.log(response_data);
        const ctx = document.getElementById("myChart");

        new Chart(ctx, {
            type: "line",
            data: {
                labels: response_data.blocks,
                datasets: [
                    {
                        label: "Number of open troves",
                        data: response_data.trove_counts,
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
    });
</script>

<div>
    <canvas id="myChart" />
</div>
