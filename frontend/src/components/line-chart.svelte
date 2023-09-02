<script>
    import { onMount } from "svelte";
    import { Chart } from "chart.js/auto";

    async function fetchTroveStake() {
        const response = await fetch(
            'http://127.0.0.1:8000/trove-stake/',
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
        let troveStake = await fetchTroveStake();
        console.log(troveStake);
        const ctx = document.getElementById("myChart");

        new Chart(ctx, {
            type: "line",
            data: {
                labels: ["Trove Stake"],
                datasets: [
                    {
                        label: "# of Votes",
                        data: [troveStake],
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
