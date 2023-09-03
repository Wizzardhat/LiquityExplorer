<script>
    import { onMount } from "svelte";
    import LineChart from "./line-chart.svelte";
    import Loading from "./loading.svelte";
    import { fetchData } from "../utils/fetch-data";
    import Table from "./table.svelte";
    let liquidation_logs = []
    let isLoading = true; // Used for loading animation


    onMount(async () => {
        let response_data = await fetchData("get-trove-liquidation-events/");
        console.log(response_data);
        liquidation_logs = response_data.liquidation_logs
        console.log(liquidation_logs)
        isLoading = false;
    });
</script>

<main>
    {#if isLoading}
    <Loading/>
    {:else}
    <Table
        tableHeaders={["date", "event_name", "transaction_hash"]}
        tableData={liquidation_logs}
    />
    {/if}
</main>
