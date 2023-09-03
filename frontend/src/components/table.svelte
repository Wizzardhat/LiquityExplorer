<script>
    export let tableHeaders;
    export let tableData;
</script>

<div class="overflow-x-auto">
    <table class="table">
        <!-- head -->
        <thead>
            <tr>
                <th>id</th>
                {#each tableHeaders as header (header)}
                    <th>{header}</th>
                {/each}
            </tr>
        </thead>
        <tbody>
            <!-- rows -->
            {#each tableData as row, index (row.id || index)}
                <tr>
                    <th>{index + 1}</th>
                    {#each tableHeaders as header (header)}
                        <td>{row[header]}</td>
                    {/each}
                </tr>
            {/each}
        </tbody>
    </table>
</div>
