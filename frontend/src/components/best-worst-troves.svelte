<script>
    import { onMount } from "svelte";
    import Loading from "./loading.svelte";
    import Table from "./table.svelte";

    let bestTroves = [];
    let worstTroves = [];

    let isLoading = true; // Used for loading animation

    async function fetchBestWorstTroves(url) {
        const response = await fetch("http://127.0.0.1:8000/" + url, {
            credentials: "include",
        }); // Replace with your API endpoint URL
        if (!response.ok) {
            throw new Error("Failed to fetch data from the API");
        }
        const data = await response.json();
        isLoading = false;
        return data.troves;
    }

    onMount(async () => {
        bestTroves = await fetchBestWorstTroves("get-best-troves/");
        worstTroves = await fetchBestWorstTroves("get-worst-troves/");
    });
</script>

<main>
    {#if isLoading}
        <Loading />
    {:else}
        <h3>Best Troves</h3>
        <Table
            tableHeaders={["address", "collateral", "debt", "stake"]}
            tableData={bestTroves}
        />
    {/if}
</main>

<main>
    {#if isLoading}
        <Loading />
    {:else}
        <h3>Worst Troves</h3>
        <Table
            tableHeaders={["address", "collateral", "debt", "stake"]}
            tableData={worstTroves}
        />
    {/if}
</main>
