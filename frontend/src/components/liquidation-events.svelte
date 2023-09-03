<script>
    import { onMount } from "svelte";
    import LineChart from "./line-chart.svelte";
    import Loading from "./loading.svelte";
    import { fetchData } from "../utils/fetch-data";
    
    let trove_counts = []
    let blocks = []
    let isLoading = true; // Used for loading animation


    onMount(async () => {
        let response_data = await fetchData("get-trove-liquidation-events/");
        isLoading = false;
    });
</script>

<main>
    {#if isLoading}
    <Loading/>
    {:else}
    <div></div>
    {/if}
</main>
