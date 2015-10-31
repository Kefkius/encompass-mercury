import cryptocur
from cryptocur import chainhook

class Currency(cryptocur.CryptoCur):
    p2pkh_version = 55
    p2sh_version = 28
    genesis_hash = '0000046309984501e5e724498cddb4aff41a126927355f64b44f1b8bba4f447e'

    coin_name = 'OKCash'
    code = 'OK'

    @chainhook
    def transaction_parse_fields(self, vds, is_coinbase, fields):
        timestamp = ('timestamp', vds.read_int32, True)
        fields.insert(1, timestamp)

    irc_nick_prefix = 'EL_'
    irc_channel = '#okcash'