<script>
    import { onMount } from "svelte";
    import { Chart } from "chart.js/auto";
    import LineChart from "./line-chart.svelte";

    let eth = []
    let LUSD = []
    let blocks = []

    async function fetchEthLusdData() {
        const response = await fetch(
            'http://127.0.0.1:8000/get-historical-number-of-eth-lusd/',
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
        let response_data = await fetchEthLusdData();
        eth = response_data.eth;
        LUSD = response_data.LUSD
        blocks = response_data.blocks
    });
</script>
<div>
    <LineChart
        xSeries={eth}
        ySeries={blocks} 
        xSeriesLabel={"Total ETH in protocol"}
     />
    <LineChart 
        xSeries={LUSD} 
        ySeries={blocks} 
        xSeriesLabel={"Total LUSD in protocol"}
    />    
</div>
