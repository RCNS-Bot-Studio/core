"""모든 설정값은 이곳에서 수정되고 참조되어야합니다."""
from typing import List
import os

class Config:
    
    T = "token"
    mamager_list = [712838792595112006, 759911041659306024]

    def __init__(self):
        pass
        
    @property
    def token(self) -> str:
        """봇의 토큰을 반환합니다."""
        return self.T

    @property
    def test_guild(self) -> int:
        """테스트 서버의 아이디를 반환합니다."""
        return 919390564363931738

    @property
    def prefix(self) -> List['str']:
        """접두사를 반환합니다."""
        return ['!']

    @property
    def command_list(self) -> List['str']:
        """커맨드 리스트를 반환합니다."""
        commands = []
        
        cogs_path = 'command'
        abs_cogs_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), cogs_path)
        for ext in os.listdir(abs_cogs_path):
            if ext.endswith(".py"):
                commands.append(ext.replace('.py', ''))
        return commands
