<script>
    import { onMount } from "svelte";
    import Loading from "./loading.svelte";
    import Table from "./table.svelte";
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
