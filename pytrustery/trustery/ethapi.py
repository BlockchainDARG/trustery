import jsonrpc_requests
import rlp

# TODO: find a better way to do this than hardcoding it
TRUSTERY_ADDRESS = '0xd7f4a7b264ff1e5d25d12566c60ec726872a8a09'
TRUSTERY_ABI = '[{"constant":false,"inputs":[{"name":"signatureID","type":"uint256"}],"name":"revokeSignature","outputs":[{"name":"revocationID","type":"uint256"}],"type":"function"},{"constant":false,"inputs":[{"name":"attributeID","type":"uint256"},{"name":"expiry","type":"uint256"}],"name":"signAttribute","outputs":[{"name":"signatureID","type":"uint256"}],"type":"function"},{"constant":true,"inputs":[{"name":"","type":"uint256"}],"name":"signatures","outputs":[{"name":"signer","type":"address"},{"name":"attributeID","type":"uint256"},{"name":"expiry","type":"uint256"}],"type":"function"},{"constant":true,"inputs":[{"name":"","type":"uint256"}],"name":"attributes","outputs":[{"name":"owner","type":"address"},{"name":"attributeType","type":"string"},{"name":"has_proof","type":"bool"},{"name":"identifier","type":"string"},{"name":"data","type":"string"},{"name":"datahash","type":"string"}],"type":"function"},{"constant":false,"inputs":[{"name":"attributeType","type":"string"},{"name":"has_proof","type":"bool"},{"name":"identifier","type":"string"},{"name":"data","type":"string"},{"name":"datahash","type":"string"}],"name":"addAttribute","outputs":[{"name":"attributeID","type":"uint256"}],"type":"function"},{"constant":true,"inputs":[{"name":"","type":"uint256"}],"name":"revocations","outputs":[{"name":"signatureID","type":"uint256"}],"type":"function"},{"anonymous":false,"inputs":[{"indexed":true,"name":"attributeID","type":"uint256"},{"indexed":true,"name":"owner","type":"address"},{"indexed":false,"name":"attributeType","type":"string"},{"indexed":false,"name":"has_proof","type":"bool"},{"indexed":true,"name":"identifier","type":"string"},{"indexed":false,"name":"data","type":"string"},{"indexed":false,"name":"datahash","type":"string"}],"name":"AttributeAdded","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"signatureID","type":"uint256"},{"indexed":true,"name":"signer","type":"address"},{"indexed":true,"name":"attributeID","type":"uint256"},{"indexed":false,"name":"expiry","type":"uint256"}],"name":"AttributeSigned","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"revocationID","type":"uint256"},{"indexed":true,"name":"signatureID","type":"uint256"}],"name":"SignatureRevoked","type":"event"}]'

ethrpc = jsonrpc_requests.Server('http://127.0.0.1:8545')


def encode_api_data(data):
    if type(data) == bool:
        if data:
            return '0x1'
        else:
            return '0x0'
    else:
        return '0x' + rlp.utils.encode_hex(data)
