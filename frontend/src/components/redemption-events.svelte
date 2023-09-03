<script>
    import { onMount } from "svelte";
    import LineChart from "./line-chart.svelte";
    import Loading from "./loading.svelte";
    import { fetchData } from "../utils/fetch-data";
    import Table from "./table.svelte";
    let isLoading = true; // Used for loading animation
    let redemption_logs = []
    onMount(async () => {
        let response_data = await fetchData("get-redemptions-events/");
        console.log(response_data);
        isLoading = false;
        redemption_logs = response_data.redemption_logs
        console.log(redemption_logs)

    });
</script>

<main>
    {#if isLoading}
    <Loading/>
    {:else}
    <Table
        tableHeaders={["date", "event_name", "transaction_hash"]}
        tableData={redemption_logs}
    />
    {/if}
</main>
