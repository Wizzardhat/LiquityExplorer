<script>
    import { onMount } from "svelte";
    import { Chart } from "chart.js/auto";
    let bestTroves = [];
    let worstTroves = [];
    async function fetchBestWorstTroves(url) {
        const response = await fetch(
            'http://127.0.0.1:8000/'+url,
            {
                credentials: 'include',
            },
            ); // Replace with your API endpoint URL
        if (!response.ok) {
            throw new Error('Failed to fetch data from the API');
        }
        const data = await response.json();
        return data.troves;
    }

    onMount(async () => {
        bestTroves = await fetchBestWorstTroves('get-best-troves/');
        worstTroves = await fetchBestWorstTroves('get-worst-troves/');
    });
</script>

<h3>Best Troves</h3>
<div >
    {#each bestTroves as bestTrove (bestTrove.array_index)}
    <div>
        <span>Address: {bestTrove.address}</span>
        <span>Collateral: {bestTrove.collateral}</span>
        <span>Debt: {bestTrove.debt}</span>
        <span>Stake: {bestTrove.stake}</span>
        <br>
    </div>
  {/each}
</div>

<h3>Worst Troves</h3>
<div >
    {#each worstTroves as worstTrove (worstTrove.array_index)}
    <div>
        <span>Address: {worstTrove.address}</span>
        <span>Collateral: {worstTrove.collateral}</span>
        <span>Debt: {worstTrove.debt}</span>
        <span>Stake: {worstTrove.stake}</span>
        <br>
    </div>
  {/each}
</div>
