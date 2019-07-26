# Authro     : ThreeDog
# Data       : 2019-06-12
# Function   : 共同包，存放一些公共的定义，主要是程序中用到文字转化的地方


# 消息类型，转化成对应的消息类型显示
type_dict = {
    'Map':'[定位]',
    'Card':'[名片推荐]',
    'Note':'[系统消息]',
    'Sharing':'[公众号链接]',
    'Picture':'[图片]',
    'Recording':'[语音]',
    'Attachment':'[文件]',
    'Video':'[视频]'
}

# linux常用命令，用于防止用户误输入被发送到聊天
cmd_list = ['pwd','ls','cd','grep','touch','rm','exit','bye','rm','vi',':wq',':q!',':Q!','cat','cp','mv','rmdir','mk','git','cls','clear','find']

# 英文翻译
language = {}

# 群聊还是个人
user_type_dict = {
    'r':'【群聊】',
    'f':'【好友】',
}

class History(object):
    '''
    输入历史，所有的输入历史都保存在这里。 类似一个队列 
    - 上--previous 获取上一个  
    - 下--next 获取下一个 
    '''
    def __init__(self):
        self.index = 0
        self.history = []
    
    def previous(self):
        '''
        获取下一条
        '''
        pass
    
    def next(self):
        '''
        获取上一条
        '''
        pass
    
    def append(self,cmd):
        '''
        添加新的
        '''
        self.history.append(cmd)

# 输入历史
history = History()
