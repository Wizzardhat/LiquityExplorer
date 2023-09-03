<script>
    import { onMount } from "svelte";
    import LineChart from "./line-chart.svelte";
    import Loading from "./loading.svelte";
    import { fetchData } from "../utils/fetch-data";

    let eth = [];
    let LUSD = [];
    let blocks = [];
    let isLoading = true; // Used for loading animation

    onMount(async () => {
        let response_data = await fetchData("get-historical-number-of-eth-lusd/");
        isLoading = false;
        eth = response_data.eth;
        LUSD = response_data.LUSD;
        blocks = response_data.blocks;
    });
</script>

<main>
    {#if isLoading}
        <Loading />
    {:else}
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
    {/if}
</main>
