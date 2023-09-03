<script>
    import { onMount } from "svelte";
    import Loading from "./loading.svelte";
    import { fetchData } from "../utils/fetch-data";

    let bestTroves = [];
    let worstTroves = [];

    let isLoading = true; // Used for loading animation

    onMount(async () => {
        bestTroves = (await fetchData("get-best-troves/")).troves;
        worstTroves = (await fetchData("get-worst-troves/")).troves;
        isLoading = false;
        console.log(bestTroves, worstTroves, isLoading);
    });
</script>

<main>
    {#if isLoading}
        <Loading />
    {:else}
        <h3>Best Troves</h3>
        <div>
            {#each bestTroves as bestTrove (bestTrove.array_index)}
                <div>
                    <span>Address: {bestTrove.address}</span>
                    <span>Collateral: {bestTrove.collateral}</span>
                    <span>Debt: {bestTrove.debt}</span>
                    <span>Stake: {bestTrove.stake}</span>
                    <br />
                </div>
            {/each}
        </div>
    {/if}
</main>

<main>
    {#if isLoading}
        <Loading />
    {:else}
        <h3>Worst Troves</h3>
        <div>
            {#each worstTroves as worstTrove (worstTrove.array_index)}
                <div>
                    <span>Address: {worstTrove.address}</span>
                    <span>Collateral: {worstTrove.collateral}</span>
                    <span>Debt: {worstTrove.debt}</span>
                    <span>Stake: {worstTrove.stake}</span>
                    <br />
                </div>
            {/each}
        </div>
    {/if}
</main>
