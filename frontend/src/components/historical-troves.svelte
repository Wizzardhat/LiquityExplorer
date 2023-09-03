<script>
    import { onMount } from "svelte";
    import LineChart from "./line-chart.svelte";

    let trove_counts = []
    let blocks = []

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
        trove_counts = response_data.trove_counts
        blocks = response_data.blocks
    });
</script>

<LineChart
    xSeries={trove_counts}
    xSeriesLabel={"Number of open troves"}
    ySeries={blocks}
/>
