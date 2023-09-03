<script>
    import BestWorstTroves from "../components/best-worst-troves.svelte";
    import EthLusd from "../components/eth-lusd.svelte";
    import TroveChart from "../components/historical-troves.svelte";
    import LiquidationEvents from "../components/liquidation-events.svelte";
    import RedemptionEvents from "../components/redemption-events.svelte";
</script>

<h1 class="mb-4 text-4xl font-extrabold leading-none tracking-tight text-gray-900 md:text-5xl lg:text-6xl dark:text-white">Liquity Protocol Explorer</h1>
<br/>
<TroveChart />
<BestWorstTroves />
<EthLusd />
<LiquidationEvents/>
<RedemptionEvents/>
