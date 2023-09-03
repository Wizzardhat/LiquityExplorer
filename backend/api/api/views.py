import json
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from web3 import Web3
from .contracts import get_trove_manager_contract_data, get_lqty_staking_contract_data, get_acitve_pool_contract_data
from .classes.sorted_troves import SortedTroves
from . import utils

@api_view(['GET'])
def get_trove_stake(request):
    # Load alchemy API key from .env file
    MAINNET_RPC_URL = utils.load_env()
    trove_manager_address, trove_manager_abi = get_trove_manager_contract_data()
    if not trove_manager_abi or not trove_manager_address:
        return Response({'error': 'Contract address and ABI are required.'}, status=status.HTTP_400_BAD_REQUEST)
    try:
        # Initialize Web3 with your Ethereum node provider (e.g., Alchemy or Infura)
        ethereum_provider_url = MAINNET_RPC_URL
        web3 = Web3(Web3.HTTPProvider(ethereum_provider_url))

        # Create a contract instance using the address and ABI
        contract = web3.eth.contract(
            address=trove_manager_address, abi=trove_manager_abi)

        # Read the balance from the contract
        trove_manager_stake = contract.functions.totalStakes().call()

        # Prepare the response JSON
        response_data = {
            'stake': trove_manager_stake
        }

        return Response(response_data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def get_historical_number_of_troves(request):
    # Load alchemy API key from .env file
    MAINNET_RPC_URL = utils.load_env()
    trove_manager_address, trove_manager_abi = get_trove_manager_contract_data()
    if not trove_manager_abi or not trove_manager_address:
        return Response({'error': 'Contract address and ABI are required.'}, status=status.HTTP_400_BAD_REQUEST)
    try:
        # Initialize Web3 with your Ethereum node provider (e.g., Alchemy or Infura)
        ethereum_provider_url = MAINNET_RPC_URL
        web3 = Web3(Web3.HTTPProvider(ethereum_provider_url))

        # Create a contract instance using the address and ABI
        trove_manager = web3.eth.contract(
            address=trove_manager_address, abi=trove_manager_abi)

        # Pandas dataframe will be used to plot the trove count over time (block numbers)
        blocks = []
        trove_counts = []
        # Liquity protocol deployment block number: April 2021
        start_block = 12178557
        # The final block on the chart is the current block
        end_block = web3.eth.block_number

        while start_block <= end_block:
            trove_count_value = trove_manager.functions.getTroveOwnersCount().call(
                block_identifier=start_block)
            blocks.append(start_block)
            trove_counts.append(trove_count_value)
            start_block += 178560

        response_data = {
            'blocks': blocks,
            'trove_counts': trove_counts
        }

        return Response(response_data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def get_staked_lqty_token_amount(request):
    MAINNET_RPC_URL = utils.load_env()
    lqty_staking_address, lqty_staking_abi = get_lqty_staking_contract_data()
    if not lqty_staking_address or not lqty_staking_abi:
        return Response({'error': 'Contract address and ABI are required.'}, status=status.HTTP_400_BAD_REQUEST)
    try:
        ethereum_provider_url = MAINNET_RPC_URL
        web3 = Web3(Web3.HTTPProvider(ethereum_provider_url))
        lqty_staking = web3.eth.contract(
            address=lqty_staking_address, abi=lqty_staking_abi)
        lqty_staking_total_staked = lqty_staking.functions.totalLQTYStaked().call()

        response_data = {
            'total_staked': lqty_staking_total_staked
        }

        return Response(response_data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def get_best_troves(request):
    sorted_troves = SortedTroves()
    sorted_troves.get_best_sorted_troves_list()
    return Response({"troves": sorted_troves.get_best_sorted_troves_list()})


@api_view(['GET'])
def get_worst_troves(request):
    sorted_troves = SortedTroves()
    return Response({"troves":sorted_troves.get_worst_sorted_troves_list()})

@api_view(['GET'])
def get_historical_number_of_eth_lusd(request):
    MAINNET_RPC_URL = utils.load_env()
    web3 = Web3(Web3.HTTPProvider(MAINNET_RPC_URL))
    active_pool_address, active_pool_abi = get_acitve_pool_contract_data()
    active_pool_contract = web3.eth.contract(address=active_pool_address, abi=active_pool_abi)
    start_block = 12178558
    end_block = web3.eth.block_number
    interval = 178560
    eth = []
    LUSD = []
    blocks = []
    while start_block <= end_block:
        try:
            tmp_eth = active_pool_contract.functions.getETH().call(block_identifier=start_block)
            tmp_lusd = active_pool_contract.functions.getLUSDDebt().call(block_identifier=start_block)
            eth.append(tmp_eth)
            LUSD.append(tmp_lusd)
            blocks.append(start_block)
        except:
            print('not found')
        start_block += interval
    return Response({
        "eth": eth,
        "LUSD": LUSD,
        "blocks": blocks
    })

@api_view(['GET'])
def get_redemption_events(request):
    MAINNET_RPC_URL = utils.load_env()
    web3 = Web3(Web3.HTTPProvider(MAINNET_RPC_URL))
    trove_manager_address, trove_manager_abi = get_trove_manager_contract_data()
    trove_manager = web3.eth.contract(
    address=trove_manager_address, abi=trove_manager_abi)
    from_block = max(0, web3.eth.block_number - 100000)
    redemptions_event_filter = trove_manager.events.Redemption.create_filter(fromBlock=from_block, toBlock='latest')
    redemptions_events = redemptions_event_filter.get_all_entries()
    logs = []
    for log in redemptions_events:
        print("Block Number:", log.blockNumber)
        print("Transaction Hash:", log.transactionHash.hex())
        print("Event Name:", log.event)
        print("Event Data:", log.args)
        print("")
        log = {
                "block_number": log.blockNumber,
                "transaction_hash:": log.transactionHash.hex(),
                "event_name:": log.event,
                "event_data:": log.args,
            }
        logs.append(log)
        print(logs, 'test')
    return Response({"redemption_logs": logs})

@api_view(['GET'])
def get_trove_liquidation_events(request):
    MAINNET_RPC_URL = utils.load_env()
    web3 = Web3(Web3.HTTPProvider(MAINNET_RPC_URL))
    trove_manager_address, trove_manager_abi = get_trove_manager_contract_data()
    trove_manager = web3.eth.contract(
    address=trove_manager_address, abi=trove_manager_abi)
    from_block = max(0, web3.eth.block_number - 100000)
    trove_liquidation_event_filter = trove_manager.events.TroveLiquidated.create_filter(fromBlock=from_block, toBlock='latest')
    liquidation_events = trove_liquidation_event_filter.get_all_entries()
    logs = []
    for log in liquidation_events:
        print("Block Number:", log.blockNumber)
        print("Transaction Hash:", log.transactionHash.hex())
        print("Event Name:", log.event)
        print("Event Data:", log.args)
        print("")
        log = {
                "block_number": log.blockNumber,
                "transaction_hash:": log.transactionHash.hex(),
                "event_name:": log.event,
                "event_data:": log.args
            }
        logs.append(log)
    return Response({"liquidation_logs": logs})