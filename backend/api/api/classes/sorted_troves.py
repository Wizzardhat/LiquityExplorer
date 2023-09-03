from web3 import Web3
from api.contracts import get_trove_manager_contract_data, get_sorted_troves_contract_data
import api.utils as utils

class SortedTroves:
    def __init__(self):
        MAINNET_RPC_URL = utils.load_env()
        print('teeeeest', MAINNET_RPC_URL)
        self.web3 = Web3(Web3.HTTPProvider(MAINNET_RPC_URL))
        sorted_troves_address, sorted_troves_abi = get_sorted_troves_contract_data()
        self.sorted_troves = self.web3.eth.contract(address=sorted_troves_address, abi=sorted_troves_abi)
        
        trove_manager_address, trove_manager_abi = get_trove_manager_contract_data()
        self.trove_manager = self.web3.eth.contract(address=trove_manager_address, abi=trove_manager_abi)

    def get_trove_data_by_address(self, trove_address):
        return self.trove_manager.functions.Troves(trove_address).call()

    def get_sorted_troves_list_next_node(self, address):
        return self.sorted_troves.functions.getNext(address).call()

    def get_sorted_troves_list_prev_node(self, address):
        return self.sorted_troves.functions.getPrev(address).call()

    def get_best_troves_data(self, troves_number, head_address):
        best_troves_array = []
        current_address = head_address
            
        for _ in range(troves_number):
            debt, collateral, stake, status, array_index = self.get_trove_data_by_address(current_address)
            best_troves_array.append(
                {'address': current_address, 'debt': debt, 'collateral': collateral, 'stake': stake, 'status': status, 'array_index': array_index}
            )
            current_address = self.get_sorted_troves_list_next_node(current_address)
        return best_troves_array

    def get_troves_to_liquidation_data(self, troves_number, tail_address):
        troves_to_liquidation_data = []
        current_address = tail_address
            
        for _ in range(troves_number):
            debt, collateral, stake, status, array_index = self.get_trove_data_by_address(current_address)
            troves_to_liquidation_data.append(
                {'address': current_address, 'debt': debt, 'collateral': collateral, 'stake': stake, 'status': status, 'array_index': array_index}
            )
            current_address = self.get_sorted_troves_list_prev_node(current_address)
        return troves_to_liquidation_data

    def get_best_sorted_troves_list(self):
        sorted_troves_head, sorted_troves_tail, sorted_troves_max_size, sorted_troves_size = self.sorted_troves.functions.data().call()
        print('hehe')
        return self.get_best_troves_data(5, sorted_troves_head)

    def get_worst_sorted_troves_list(self):
        sorted_troves_head, sorted_troves_tail, sorted_troves_max_size, sorted_troves_size = self.sorted_troves.functions.data().call()
        return self.get_troves_to_liquidation_data(5, sorted_troves_tail)
