from ntgcalls import NTgCalls
from ntgcalls import StreamType


class Scaffold:
    _REQUIRED_PYROGRAM_VERSION = '1.2.20'
    _REQUIRED_TELETHON_VERSION = '1.24.0'

    def __init__(self):
        self._app = None
        self._async_core = None
        self._is_running = None
        self._my_id = None
        self._env_checker = None
        self._call_holder = None
        self._cache_user_peer = None
        self._wait_result = None
        self._cache_local_peer = None
        self._on_event_update = None
        self._binding: NTgCalls = None

    def _handle_mtproto(self):
        pass

    async def _init_mtproto(self):
        pass

    async def _stream_ended_handler(self, chat_id: int, stream: StreamType):
        pass

    async def start(self):
        pass
