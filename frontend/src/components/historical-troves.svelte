<script>
    import { onMount } from "svelte";
    import LineChart from "./line-chart.svelte";
    import Loading from "./loading.svelte";
    import { fetchData } from "../utils/fetch-data"
    let trove_counts = []
    let blocks = []
    let isLoading = true; // Used for loading animation

    onMount(async () => {
        let response_data = await fetchData("get_historical_number_of_troves/");
        isLoading = false;
        trove_counts = response_data.trove_counts
        blocks = response_data.blocks
    });
</script>

<main>
    {#if isLoading}
    <Loading/>
    {:else}
    <LineChart
        xSeries={trove_counts}
        xSeriesLabel={"Number of open troves"}
        ySeries={blocks}
    />
    {/if}
</main>
